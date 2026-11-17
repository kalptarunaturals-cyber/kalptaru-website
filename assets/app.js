(function(){
"use strict";
var K=window.KN, R=document.body.getAttribute("data-root")||"";
var $=function(s,el){return (el||document).querySelector(s)}, $$=function(s,el){return Array.prototype.slice.call((el||document).querySelectorAll(s))};
var esc=function(s){return String(s).replace(/[&<>"']/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]})};
var byId={}; K.items.forEach(function(i){byId[i.id]=i});

/* toast */
var tt; function toast(m){var t=$(".toast");t.textContent=m;t.classList.add("on");clearTimeout(tt);tt=setTimeout(function(){t.classList.remove("on")},2400)}
function openWA(text){var a=document.createElement("a");a.href="https://wa.me/"+K.wa+"?text="+encodeURIComponent(text);a.target="_blank";a.rel="noopener";document.body.appendChild(a);a.click();a.remove()}

/* menu */
var mb=$(".menu"); if(mb) mb.addEventListener("click",function(){var n=$("header nav");n.classList.toggle("open");mb.setAttribute("aria-expanded",n.classList.contains("open"))});

/* basket */
var basket=[]; try{basket=JSON.parse(localStorage.getItem("kn-basket")||"[]").filter(function(x){return byId[x]})}catch(e){}
function save(){try{localStorage.setItem("kn-basket",JSON.stringify(basket))}catch(e){}}
function renderBasket(){
  $$(".bcount").forEach(function(b){b.textContent=basket.length});
  $(".bitems").innerHTML=basket.length?basket.map(function(id){var i=byId[id];return '<div class="bitem"><div><b>'+esc(i.name)+'</b><small>'+esc(i.inci)+' · '+esc(K.principals[i.p].short)+'</small></div><button type="button" data-del="'+id+'" aria-label="Remove">✕</button></div>'}).join(""):'<p class="muted">No ingredients yet. Tap “+ Enquire” on any ingredient to build a list for samples, TDS or prices.</p>';
  $$("[data-add]").forEach(function(b){var on=basket.indexOf(b.getAttribute("data-add"))>-1;b.classList.toggle("in",on);
    b.textContent=b.classList.contains("btn")?(on?"✓ In enquiry list":"+ Add to enquiry"):(on?"✓ Added":"+ Enquire")});
}
function drawer(o){$(".drawer").classList.toggle("open",o);$(".drawer").setAttribute("aria-hidden",!o);$(".drawer-bg").hidden=!o}
function basketText(f){return "Hello Kalptaru Naturals,\n\nRequest: "+f.need.value+"\nFrom: "+f.who.value+"\n\nIngredients:\n"+basket.map(function(id,n){var i=byId[id];return (n+1)+". "+i.name+" ("+i.inci+") — "+K.principals[i.p].short}).join("\n")+(f.note.value?"\n\nNotes: "+f.note.value:"")}
document.addEventListener("click",function(ev){
  var t=ev.target, a=t.closest("[data-add]");
  if(a){ev.preventDefault();var id=a.getAttribute("data-add");var k=basket.indexOf(id);
    if(k>-1){basket.splice(k,1);toast("Removed from enquiry list")}else{basket.push(id);toast(byId[id].name+" added to enquiry list")}
    save();renderBasket();return}
  var d=t.closest("[data-del]"); if(d){basket.splice(basket.indexOf(d.getAttribute("data-del")),1);save();renderBasket();return}
  if(t.closest(".basket-btn")){drawer(true);return}
  if(t.closest(".dclose")||t.classList.contains("drawer-bg")){drawer(false);return}
});
$(".bform").addEventListener("submit",function(ev){ev.preventDefault();if(!basket.length){toast("Add at least one ingredient first");return}openWA(basketText(this))});
$(".bcopy").addEventListener("click",function(){var f=$(".bform");if(!basket.length){toast("Add at least one ingredient first");return}
  try{navigator.clipboard.writeText(basketText(f)).then(function(){toast("Copied — paste into an email to "+K.email)},function(){toast("Copy not allowed here — please use WhatsApp")})}catch(e){toast("Copy not allowed here — please use WhatsApp")}});
var bm=$(".bmail"); if(bm) bm.addEventListener("click",function(){var f=$(".bform");if(!basket.length){toast("Add at least one ingredient first");return}
  location.href="mailto:"+K.email+"?subject="+encodeURIComponent("Enquiry: "+f.need.value+" — "+(f.who.value||"website"))+"&body="+encodeURIComponent(basketText(f))});
var cf=$(".cform"); if(cf) cf.addEventListener("submit",function(ev){ev.preventDefault();openWA("Hello Kalptaru Naturals,\n\nName: "+this.name.value+"\nCompany: "+this.co.value+"\n\n"+this.msg.value)});
var ef=$(".encform"); if(ef) ef.addEventListener("submit",function(ev){ev.preventDefault();openWA("Hello Kalptaru Naturals,\n\nCustom encapsulation enquiry\nActive: "+this.active.value+"\nBase: "+this.base.value+"\nGoal: "+this.goal.value+"\nFrom: "+this.who.value)});
/* email route for the contact and encapsulation forms */
$$(".fmail").forEach(function(b){b.addEventListener("click",function(){var f=b.closest("form"),lines=[];
  $$("input,select,textarea",f).forEach(function(x){if(x.value){var l=x.closest("label");lines.push((l?l.firstChild.textContent.trim():x.name)+": "+x.value)}});
  location.href="mailto:"+K.email+"?subject="+encodeURIComponent(f.classList.contains("encform")?"Custom encapsulation enquiry":"Website enquiry")+"&body="+encodeURIComponent("Hello Kalptaru Naturals,\n\n"+lines.join("\n"))})});
var hs=$(".hsearch"); if(hs) hs.addEventListener("submit",function(ev){ev.preventDefault();var q=$("#hq").value.trim().toLowerCase().replace(/[^a-z0-9]+/g,"-").replace(/^-|-$/g,"");location.href=R+"ingredients.html"+(q?"#q-"+q:"")});
renderBasket();

/* ---------- catalogue ---------- */
var fg=$("#fgroups");
if(fg){
  var S={q:"",p:[],a:[],c:[],k:[],g:"none"};
  var hay={}; K.items.forEach(function(i){hay[i.id]=[i.name,i.inci,K.principals[i.p].name,K.cats[i.cat],i.ben.join(" "),i.tags.map(function(t){return K.tags[t]}).join(" "),i.apps.map(function(a){return K.apps[a]}).join(" ")].join(" ").toLowerCase()});
  var val={p:function(i){return [i.p]},a:function(i){return i.apps},c:function(i){return i.tags},k:function(i){return [i.cat]}};
  function match(i,skip){
    if(S.q){var ws=S.q.toLowerCase().split(/\s+/);for(var n=0;n<ws.length;n++) if(hay[i.id].indexOf(ws[n])<0) return false}
    for(var key in val){if(key===skip||!S[key].length) continue; var v=val[key](i); if(!v.some(function(x){return S[key].indexOf(x)>-1})) return false}
    return true}
  var groups=[["p","Principal",K.pOrder,function(k){return K.principals[k].short}],
              ["a","Application",K.appOrder,function(k){return K.apps[k]}],
              ["c","Concern / claim",K.tagOrder,function(k){return K.tags[k]}],
              ["k","Category",K.catOrder,function(k){return K.cats[k]}]];
  function cnt(key,v){return K.items.filter(function(i){return match(i,key)&&val[key](i).indexOf(v)>-1}).length}
  function buildFilters(){
    fg.innerHTML=groups.map(function(g){return '<details class="fgroup"'+(g[0]!=="k"?" open":"")+'><summary>'+g[1]+'</summary>'+g[2].map(function(v){
      return '<label><input type="checkbox" data-f="'+g[0]+'" value="'+v+'"'+(S[g[0]].indexOf(v)>-1?" checked":"")+'> <span>'+esc(g[3](v))+'</span> <em data-n="'+g[0]+'|'+v+'"></em></label>'}).join("")+'</details>'}).join("");
    counts()}
  function counts(){$$("[data-n]",fg).forEach(function(el){var p=el.getAttribute("data-n").split("|");var n=cnt(p[0],p[1]);el.textContent=n;el.parentNode.classList.toggle("zero",n===0)})}
  function card(i){var p=K.principals[i.p];return '<article class="card"><div class="ctop"><span class="pname">'+esc(p.short)+'</span>'+(i.new?'<span class="new">New</span>':'')+'</div><h3><a href="ingredient/'+i.id+'.html">'+esc(i.name)+'</a></h3><p class="inci">'+esc(i.key)+'</p><p class="ben">'+esc(i.ben[0]||"")+'</p><div class="tags">'+i.tags.slice(0,3).map(function(t){return '<span class="tag">'+K.tags[t]+'</span>'}).join("")+'</div><div class="cfoot"><span>'+(i.dose?"Dosage "+esc(i.dose):esc(K.cats[i.cat]))+'</span><button class="add" type="button" data-add="'+i.id+'">+ Enquire</button></div></article>'}
  function render(){
    var list=K.items.filter(function(i){return match(i)});
    $("#count").textContent=list.length+" ingredient"+(list.length===1?"":"s");
    var chips=[];groups.forEach(function(g){S[g[0]].forEach(function(v){chips.push('<button type="button" class="chip" data-rm="'+g[0]+'|'+v+'">'+esc(g[3](v))+' ✕</button>')})});
    if(S.q) chips.push('<button type="button" class="chip q" data-rm="q|">“'+esc(S.q)+'” ✕</button>');
    $("#chips").innerHTML=chips.join("");
    $$(".seg button").forEach(function(b){b.classList.toggle("on",b.getAttribute("data-g")===S.g)});
    var out;
    if(!list.length) out='<div class="empty"><h2>No ingredients match</h2><p class="muted">Remove a filter, or ask us — we can source it.</p><a class="btn" href="contact.html">Ask Kalptaru</a></div>';
    else if(S.g==="none") out='<div class="grid">'+list.map(card).join("")+'</div>';
    else{var g=groups.filter(function(x){return x[0]===S.g})[0];
      out=g[2].map(function(v){var l=list.filter(function(i){return val[S.g](i).indexOf(v)>-1});return l.length?'<h2 class="gh">'+esc(g[3](v))+' <span>'+l.length+'</span></h2><div class="grid">'+l.map(card).join("")+'</div>':""}).join("")}
    $("#results").innerHTML=out;renderBasket();
  }
  function fromHash(){var h=decodeURIComponent(location.hash.slice(1));if(!h) return;
    var m=h.match(/^([pacqk])-(.+)$/);if(!m) return;["p","a","c","k"].forEach(function(k){S[k]=[]});S.q="";
    if(m[1]==="q"){S.q=m[2].replace(/-/g," ")} else S[m[1]]=[m[2]];
    if(m[1]==="p") S.g="k"; else S.g="none";
    $("#q").value=S.q}
  fromHash();
  try{var qs=new URLSearchParams(location.search).get("q");if(qs){S.q=qs;$("#q").value=qs}}catch(e){}
  buildFilters();render();
  window.addEventListener("hashchange",function(){fromHash();buildFilters();render();window.scrollTo(0,0)});
  fg.addEventListener("change",function(ev){var i=ev.target;if(!i.getAttribute("data-f")) return;var k=i.getAttribute("data-f");
    if(i.checked) S[k].push(i.value); else S[k].splice(S[k].indexOf(i.value),1); counts();render()});
  $("#q").addEventListener("input",function(){S.q=this.value.trim();counts();render()});
  $("#clear").addEventListener("click",function(){["p","a","c","k"].forEach(function(k){S[k]=[]});S.q="";$("#q").value="";buildFilters();render()});
  $(".seg").addEventListener("click",function(ev){var b=ev.target.closest("button");if(b){S.g=b.getAttribute("data-g");render()}});
  $("#chips").addEventListener("click",function(ev){var b=ev.target.closest("[data-rm]");if(!b) return;var p=b.getAttribute("data-rm").split("|");
    if(p[0]==="q"){S.q="";$("#q").value=""}else S[p[0]].splice(S[p[0]].indexOf(p[1]),1);buildFilters();render()});
  $(".ftoggle").addEventListener("click",function(){$(".filters").classList.toggle("open")});
}

/* ---------- research table filter ---------- */
var rq=$("#rq"); if(rq) rq.addEventListener("input",function(){var q=this.value.toLowerCase();$$(".rt tbody tr").forEach(function(tr){tr.hidden=q&&tr.textContent.toLowerCase().indexOf(q)<0})});

/* ---------- live PubMed on ingredient pages ---------- */
var rp=$(".research");
if(rp){
  var term=rp.getAttribute("data-term"), q=rp.getAttribute("data-q")||term, box=$(".pubs",rp);
  box.innerHTML='<p class="muted">Loading the most relevant papers from PubMed…</p>';
  var base="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/";
  fetch(base+"esearch.fcgi?db=pubmed&retmode=json&sort=relevance&retmax=5&term="+encodeURIComponent(q)).then(function(r){return r.json()}).then(function(s){
    var ids=s.esearchresult.idlist,total=s.esearchresult.count; if(!ids.length) throw 0;
    return fetch(base+"esummary.fcgi?db=pubmed&retmode=json&id="+ids.join(",")).then(function(r){return r.json()}).then(function(d){
      box.innerHTML='<p class="muted">'+Number(total).toLocaleString("en-IN")+' papers indexed for “'+esc(term)+'”. Most relevant:</p>'+ids.map(function(id){var a=d.result[id];if(!a) return "";
        var au=(a.authors||[]).slice(0,3).map(function(x){return x.name}).join(", ")+((a.authors||[]).length>3?" et al.":"");
        return '<div class="paper"><a href="https://pubmed.ncbi.nlm.nih.gov/'+id+'/" target="_blank" rel="noopener">'+esc(a.title)+'</a><small>'+esc(au)+' · <i>'+esc(a.source)+'</i> '+esc((a.pubdate||"").slice(0,4))+' · PMID '+id+'</small></div>'}).join("")})
  }).catch(function(){box.innerHTML='<p class="muted">Open the live PubMed results for “'+esc(term)+'” below.</p>'});
}
// ---- blog links on ingredient pages (posts.json maintained by blog_tool.py) ----
var br=$(".blogrel"); if(br&&window.fetch){
  fetch(R+"blog/posts.json",{cache:"no-cache"}).then(function(r){return r.ok?r.json():[]}).then(function(ps){
    var id=br.getAttribute("data-ing"), m=(ps||[]).filter(function(p){return (p.ingredients||[]).indexOf(id)>-1});
    if(!m.length) return;
    $(".bloglist",br).innerHTML=m.map(function(p){return '<li><a href="'+R+'blog/'+esc(p.slug)+'.html">'+esc(p.title)+'</a><small>'+esc(p.date)+' · '+esc(p.read_min||5)+' min read</small></li>'}).join("");
    br.hidden=false;
  }).catch(function(){});
}
})();
