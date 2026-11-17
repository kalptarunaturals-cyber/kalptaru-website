/**
 * Kalptaru Naturals — Dispatch Form (Google Apps Script version)
 * Replaces the old GoDaddy PHP form at kalptarunaturals.in/dispatch
 *
 * What it does
 *  1. Shows the Dispatch Form (behind the team passcode).
 *  2. Emails every dispatch (with logo + COA attached) to the recipients the
 *     dispatcher types in, always CC finance@, chandrabdm@ and dispatch@.
 *  3. Logs every dispatch to the "Dispatch Log" Google Sheet.
 *  4. On the 25th of each month, emails each sales manager (North / South / West)
 *     an Excel file of the samples requested through them, CC chandrabdm only.
 *
 * Setup: see SETUP.md. Edit only the CONFIG block below.
 */

const CONFIG = {
  PASSCODE: '__PASSCODE__',                       // team passcode for the form
  ALWAYS_CC: ['finance@kalptarunaturals.in',
              'chandrabdm@kalptarunaturals.in',
              'dispatch@kalptarunaturals.in'],
  MONTHLY_CC: ['chandrabdm@kalptarunaturals.in'], // monthly report CC (only)
  SALES_MANAGERS: {                            // monthly sample report recipients
    North: '',   // TODO: North sales manager email
    South: '',   // TODO: South sales manager email
    West:  ''    // TODO: West sales manager email
  },
  LOGO_URL: 'https://raw.githubusercontent.com/kalptarunaturals-cyber/kalptaru-website/main/assets/img/logo-dark.png',
  SHEET_NAME: 'Dispatch Log',
  COA_FOLDER: 'Dispatch COAs'
};

const HEADERS = ['Timestamp', 'Dispatch type', 'Region', 'Sales manager email',
  'Customer company', 'Customer contact', 'Customer phone', 'Customer email', 'Customer address',
  'Dispatching company', 'Dispatcher name', 'Dispatcher phone', 'Dispatcher email',
  'Product', 'Batch no.', 'Quantity', 'Courier', 'Docket / AWB', 'Other recipients',
  'Notes', 'COA file'];

/* ---------- web app ---------- */

function doGet() {
  return HtmlService.createHtmlOutputFromFile('Form')
    .setTitle('Dispatch Form | Kalptaru Naturals')
    .addMetaTag('viewport', 'width=device-width, initial-scale=1')
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
}

function checkPasscode(code) {
  return String(code || '').trim() === CONFIG.PASSCODE;
}

function submitDispatch(d) {
  if (!checkPasscode(d.passcode)) throw new Error('Wrong passcode.');
  const need = ['type', 'region', 'smEmail', 'custCompany', 'custContact', 'product', 'batch', 'qty'];
  need.forEach(k => { if (!String(d[k] || '').trim()) throw new Error('Missing: ' + k); });

  // Save the COA to Drive and keep it for the email
  let coaBlob = null, coaUrl = '';
  if (d.coa && d.coa.data) {
    coaBlob = Utilities.newBlob(Utilities.base64Decode(d.coa.data), d.coa.mime, d.coa.name);
    const file = getFolder_().createFile(coaBlob);
    coaUrl = file.getUrl();
  }

  const now = new Date();
  getSheet_().appendRow([now, d.type, d.region, d.smEmail,
    d.custCompany, d.custContact, d.custPhone, d.custEmail, d.custAddress,
    d.dispCompany, d.dispName, d.dispPhone, d.dispEmail,
    d.product, d.batch, d.qty, d.courier, d.docket, d.others, d.notes, coaUrl]);

  // Recipients: requesting sales manager + customer + anyone typed in
  const to = uniq_([d.smEmail, d.custEmail].concat(splitEmails_(d.others)));
  const cc = CONFIG.ALWAYS_CC.filter(e => to.indexOf(e.toLowerCase()) === -1);

  const logo = UrlFetchApp.fetch(CONFIG.LOGO_URL).getBlob().setName('logo.png');
  const subject = `${d.type} dispatched: ${d.product} (Batch ${d.batch}) to ${d.custCompany}`;
  const row = (k, v) => v ? `<tr><td style="padding:6px 12px;color:#555">${k}</td><td style="padding:6px 12px"><b>${esc_(v)}</b></td></tr>` : '';
  const html = `
  <div style="font-family:Arial,sans-serif;max-width:620px">
    <img src="cid:logo" alt="Kalptaru Naturals" style="height:56px"><br>
    <h2 style="color:#1f4d2b;margin:16px 0 4px">${esc_(d.type)} dispatch</h2>
    <p>Dear all,<br>The following ${esc_(d.type.toLowerCase())} has been dispatched.</p>
    <table style="border-collapse:collapse;border:1px solid #ddd">
      ${row('Product', d.product)}${row('Batch no.', d.batch)}${row('Quantity', d.qty)}
      ${row('Courier', d.courier)}${row('Docket / AWB', d.docket)}
      ${row('Customer', d.custCompany)}${row('Contact', d.custContact)}${row('Phone', d.custPhone)}
      ${row('Email', d.custEmail)}${row('Address', d.custAddress)}
      ${row('Dispatched by', [d.dispName, d.dispCompany].filter(String).join(', '))}
      ${row('Dispatcher phone', d.dispPhone)}${row('Dispatcher email', d.dispEmail)}
      ${row('Sales manager', d.smEmail + ' (' + d.region + ')')}${row('Notes', d.notes)}
    </table>
    <p>${coaBlob ? 'The COA is attached.' : 'No COA was attached.'}</p>
    <p>Regards,<br>Dispatch Team<br>Kalptaru Naturals<br>
    <a href="https://kalptarunaturals.in">kalptarunaturals.in</a></p>
  </div>`;

  MailApp.sendEmail({
    to: to.join(','), cc: cc.join(','), subject: subject, htmlBody: html,
    name: 'Kalptaru Naturals Dispatch',
    replyTo: d.dispEmail || 'dispatch@kalptarunaturals.in',
    inlineImages: { logo: logo },
    attachments: coaBlob ? [coaBlob] : []
  });
  return 'Sent to ' + to.join(', ') + ' (CC ' + cc.join(', ') + ')';
}

/* ---------- monthly sample report (runs daily, acts on the 25th) ---------- */

function monthlySampleReport() {
  const today = new Date();
  if (today.getDate() !== 25) return;
  const tz = Session.getScriptTimeZone();
  // Period: 25th of last month (inclusive) to 25th of this month (exclusive)
  const end = new Date(today.getFullYear(), today.getMonth(), 25);
  const start = new Date(today.getFullYear(), today.getMonth() - 1, 25);
  const label = Utilities.formatDate(start, tz, 'd MMM') + ' – ' +
                Utilities.formatDate(new Date(end - 1), tz, 'd MMM yyyy');

  const rows = getSheet_().getDataRange().getValues().slice(1)
    .filter(r => r[1] === 'Sample' && r[0] >= start && r[0] < end);

  Object.keys(CONFIG.SALES_MANAGERS).forEach(region => {
    if (!CONFIG.SALES_MANAGERS[region]) return;   // no email set yet
    const mine = rows.filter(r => r[2] === region);
    const tmp = SpreadsheetApp.create(`Kalptaru samples ${region} ${label}`);
    const sh = tmp.getSheets()[0];
    sh.getRange(1, 1, 1, HEADERS.length).setValues([HEADERS]).setFontWeight('bold');
    if (mine.length) sh.getRange(2, 1, mine.length, HEADERS.length).setValues(mine);
    sh.autoResizeColumns(1, HEADERS.length);
    SpreadsheetApp.flush();
    const xlsx = UrlFetchApp.fetch(
      `https://docs.google.com/spreadsheets/d/${tmp.getId()}/export?format=xlsx`,
      { headers: { Authorization: 'Bearer ' + ScriptApp.getOAuthToken() } })
      .getBlob().setName(`Kalptaru-samples-${region}-${Utilities.formatDate(end, tz, 'yyyy-MM')}.xlsx`);
    MailApp.sendEmail({
      to: CONFIG.SALES_MANAGERS[region], cc: CONFIG.MONTHLY_CC.join(','),
      subject: `Samples requested – ${region} – ${label}`,
      htmlBody: `<p>Dear Sales Manager (${region}),</p><p>Attached is the list of samples requested ` +
        `through you for ${label}: <b>${mine.length}</b> sample dispatch(es).</p>` +
        `<p>Regards,<br>Kalptaru Naturals</p>`,
      name: 'Kalptaru Naturals', attachments: [xlsx]
    });
    DriveApp.getFileById(tmp.getId()).setTrashed(true);
  });
}

/** Run once from the editor: creates the log sheet and the daily trigger. */
function setup() {
  getSheet_(); getFolder_();
  ScriptApp.getProjectTriggers().forEach(t => ScriptApp.deleteTrigger(t));
  ScriptApp.newTrigger('monthlySampleReport').timeBased().everyDays(1).atHour(9).create();
  // Touch the services once so all permissions are granted now
  MailApp.getRemainingDailyQuota(); UrlFetchApp.fetch(CONFIG.LOGO_URL);
}

/* ---------- helpers ---------- */

function getSheet_() {
  const props = PropertiesService.getScriptProperties();
  let id = props.getProperty('SHEET_ID'), ss;
  if (id) { ss = SpreadsheetApp.openById(id); }
  else {
    ss = SpreadsheetApp.create(CONFIG.SHEET_NAME);
    props.setProperty('SHEET_ID', ss.getId());
    ss.getSheets()[0].appendRow(HEADERS);
    ss.getSheets()[0].setFrozenRows(1);
  }
  return ss.getSheets()[0];
}
function getFolder_() {
  const it = DriveApp.getFoldersByName(CONFIG.COA_FOLDER);
  return it.hasNext() ? it.next() : DriveApp.createFolder(CONFIG.COA_FOLDER);
}
function splitEmails_(s) { return String(s || '').split(/[,;\s]+/).filter(e => /@/.test(e)); }
function uniq_(a) { return [...new Set(a.filter(Boolean).map(e => e.trim().toLowerCase()))]; }
function esc_(s) { return String(s || '').replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c])); }
