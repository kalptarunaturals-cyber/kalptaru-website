# Dispatch Form on Google: one-time setup (about 10 minutes)

Sign in as **kalptarunaturals@gmail.com**. Dispatch emails will be sent from this account.

1. Open **script.google.com** and click **New project**. Rename it to **Kalptaru Dispatch Form**.
2. Delete everything in `Code.gs` and paste in the contents of **Code.gs**.
3. In the `CONFIG` block at the top, set:
   - `PASSCODE`: your team passcode (it can be the same one as on the old form)
   - `SALES_MANAGERS`: the real emails for the North, South and West sales managers
4. Click **+** next to Files, choose **HTML**, name it `Form` (exactly), and paste in **Form.html**.
5. Choose the function **setup** from the dropdown at the top and click **Run**. Allow the permissions when Google asks.
   If Google shows "Google hasn't verified this app", click Advanced, then Go to Kalptaru Dispatch Form.
   This creates the **Dispatch Log** sheet, the **Dispatch COAs** Drive folder, and the daily check that sends the report on the 25th.
6. Click **Deploy**, then **New deployment**, then the gear icon, then **Web app**.
   - Execute as: **Me**
   - Who has access: **Anyone**
   Click **Deploy** and copy the **Web app URL** (it ends in `/exec`).
7. Send that URL to Claude. kalptarunaturals.in/dispatch will then open the new form.

## Good to know
- Free Gmail accounts can send about 100 emails a day, which covers normal dispatch volume.
- The monthly report covers the 25th of last month up to the 24th of this month, and it goes out around 9 AM on the 25th.
- Every dispatch is saved in the **Dispatch Log** sheet, and every COA is saved in the **Dispatch COAs** folder.
