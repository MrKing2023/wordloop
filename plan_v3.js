/* WordLoop v3: fixed day plan, day selection and redesigned navigation */

icons.plan = "▦";

function planEligibleCards(){
  return state.cards.filter(c => !c.isSuspended);
}

function shuffledCopy(items){
  const arr=[...items];
  for(let i=arr.length-1;i>0;i--){
    const j=Math.floor(Math.random()*(i+1));
    [arr[i],arr[j]]=[arr[j],arr[i]];
  }
  return arr;
}

function createPlanAssignments(wordsPerDay=20, orderMode="original", preserveName=true){
  const cards=planEligibleCards();
  const ordered=orderMode==="random"?shuffledCopy(cards):[...cards];
  const oldName=state.studyPlan?.name;
  const oldCreated=state.studyPlan?.createdAt;
  state.studyPlan={
    version:1,
    name:preserveName&&oldName?oldName:"核心英语 200 词",
    wordsPerDay:Math.max(1,Math.min(100,Number(wordsPerDay)||20)),
    orderMode,
    cardOrder:ordered.map(c=>c.id),
    currentDay:1,
    lastDay:1,
    createdAt:oldCreated||nowISO(),
    updatedAt:nowISO(),
    dayProgress:{}
  };
  save();
}

function ensureStudyPlan(){
  state.ui=state.ui||{};
  if(!state.studyPlan || !Array.isArray(state.studyPlan.cardOrder)){
    createPlanAssignments(state.settings.dailyGoal||20,"original",false);
  }
  state.studyPlan.dayProgress=state.studyPlan.dayProgress||{};
  const existing=new Set(state.cards.map(c=>c.id));
  state.studyPlan.cardOrder=state.studyPlan.cardOrder.filter(id=>existing.has(id));
  const assigned=new Set(state.studyPlan.cardOrder);
  planEligibleCards().forEach(c=>{if(!assigned.has(c.id))state.studyPlan.cardOrder.push(c.id);});
  state.studyPlan.wordsPerDay=Math.max(1,Number(state.studyPlan.wordsPerDay)||20);
  state.version=Math.max(3,Number(state.version||0));
  save();
}
ensureStudyPlan();

function totalPlanDays(){return Math.max(1,Math.ceil(state.studyPlan.cardOrder.length/state.studyPlan.wordsPerDay));}
function clampDay(day){return Math.max(1,Math.min(totalPlanDays(),Number(day)||1));}
function cardsForDay(day){
  day=clampDay(day);
  const start=(day-1)*state.studyPlan.wordsPerDay;
  return state.studyPlan.cardOrder.slice(start,start+state.studyPlan.wordsPerDay).map(id=>state.cards.find(c=>c.id===id)).filter(Boolean);
}
function progressForDay(day){
  const key=String(clampDay(day));
  if(!state.studyPlan.dayProgress[key]) state.studyPlan.dayProgress[key]={currentIndex:0,wrongCurrentIndex:0,studiedCardIds:[],correctCardIds:[],wrongCardIds:[],manualComplete:false,lastOpenedAt:null,updatedAt:null};
  const p=state.studyPlan.dayProgress[key];
  p.studiedCardIds=Array.isArray(p.studiedCardIds)?p.studiedCardIds:[];
  p.correctCardIds=Array.isArray(p.correctCardIds)?p.correctCardIds:[];
  p.wrongCardIds=Array.isArray(p.wrongCardIds)?p.wrongCardIds:[];
  p.currentIndex=Math.max(0,Number(p.currentIndex)||0);
  p.wrongCurrentIndex=Math.max(0,Number(p.wrongCurrentIndex)||0);
  return p;
}
function daySummary(day){
  const cards=cardsForDay(day), p=progressForDay(day), ids=new Set(cards.map(c=>c.id));
  const studied=p.studiedCardIds.filter(id=>ids.has(id)).length;
  const correct=p.correctCardIds.filter(id=>ids.has(id)).length;
  const wrong=p.wrongCardIds.filter(id=>ids.has(id)).length;
  const completed=Boolean(p.manualComplete || (cards.length>0&&studied>=cards.length));
  return {day:clampDay(day),total:cards.length,studied,correct,wrong,completed,status:completed?"completed":studied?"in_progress":"not_started",percent:cards.length?Math.round(studied/cards.length*100):0};
}
function dayStatusText(s){return s.status==="completed"?"已完成":s.status==="in_progress"?"学习中":"未开始";}
function dayStatusClass(s){return s.status==="completed"?"done":s.status==="in_progress"?"active":"";}
function nextSuggestedDay(){
  for(let d=1;d<=totalPlanDays();d++)if(!daySummary(d).completed)return d;
  return clampDay(state.studyPlan.lastDay||1);
}
function setCurrentPlanDay(day){
  day=clampDay(day);state.studyPlan.currentDay=day;state.studyPlan.lastDay=day;state.ui.lastPlanDay=day;
  const p=progressForDay(day);p.lastOpenedAt=nowISO();p.updatedAt=nowISO();save();
}
function addUnique(arr,id){if(!arr.includes(id))arr.push(id);}
function removeItem(arr,id){const i=arr.indexOf(id);if(i>=0)arr.splice(i,1);}
function recordDayOutcome(cardId,isCorrect){
  const mode=practiceSession?.mode||"";
  const match=mode.match(/^(day|daywrong)-(\d+)$/);if(!match)return;
  const day=clampDay(match[2]);const p=progressForDay(day);
  addUnique(p.studiedCardIds,cardId);
  if(isCorrect){
    addUnique(p.correctCardIds,cardId);
    // 在“只练错词”模式中答对，表示该错词已完成专项复习；
    // 在正常按天学习中，即使最终答对，也保留此前出现过的错误标记。
    if(match[1]==="daywrong") removeItem(p.wrongCardIds,cardId);
  }else{
    addUnique(p.wrongCardIds,cardId);
    removeItem(p.correctCardIds,cardId);
  }
  p.updatedAt=nowISO();state.studyPlan.lastDay=day;state.studyPlan.currentDay=day;save();
}
function updateDayIndex(mode,index){
  const match=String(mode||"").match(/^(day|daywrong)-(\d+)$/);if(!match)return;
  const p=progressForDay(match[2]);
  if(match[1]==="daywrong") p.wrongCurrentIndex=Math.max(0,Number(index)||0);
  else p.currentIndex=Math.max(0,Number(index)||0);
  p.updatedAt=nowISO();save();
}

function sidebarIsCollapsed(){return !!state.ui?.sidebarCollapsed;}
function toggleSidebar(){
  state.ui=state.ui||{};state.ui.sidebarCollapsed=!sidebarIsCollapsed();save();route();
}

const shellV2=shell;
shell=function(content,title,subtitle=""){
  const hash=location.hash||"#/dashboard";
  const nav=[
    ["dashboard","首页","#/dashboard"],["plan","学习计划","#/plan"],["practice","自由练习","#/practice"],["decks","单词本","#/decks"],["cards","卡片","#/cards"],["stats","统计","#/stats"],["settings","设置","#/settings"]
  ];
  document.body.classList.toggle("dark",state.settings.theme==="dark");
  const collapsed=sidebarIsCollapsed();
  const sidebarHead=collapsed
    ? `<div class="sidebar-head sidebar-head-collapsed"><button class="collapsed-brand-toggle" type="button" onclick="toggleSidebar()" aria-label="展开菜单栏" title="展开菜单栏"><span class="collapsed-logo-letter">W</span><span class="sidebar-panel-icon" aria-hidden="true"></span></button></div>`
    : `<div class="sidebar-head sidebar-head-expanded"><div class="brand"><div class="logo">W</div><div class="brand-copy"><h1>WordLoop</h1><p>AI 辅助语境记忆</p></div></div><button class="sidebar-toggle" type="button" onclick="toggleSidebar()" aria-label="收起菜单栏" title="收起菜单栏"><span class="sidebar-panel-icon" aria-hidden="true"></span></button></div>`;
  return `<div class="app-shell ${collapsed?"sidebar-collapsed":""}">
    <aside class="sidebar">
      ${sidebarHead}
      <nav class="nav">${nav.map(n=>`<a href="${n[2]}" title="${n[1]}" class="${hash.startsWith(n[2])?"active":""}"><span class="icon">${icons[n[0]]}</span><span class="nav-label">${n[1]}</span></a>`).join("")}
      <a href="#/import" title="导入导出" class="${hash.startsWith("#/import")?"active":""}"><span class="icon">${icons.import}</span><span class="nav-label">导入导出</span></a></nav>
      <div class="sidebar-footer"><strong>${escapeHtml(state.studyPlan.name)}</strong><br>${state.studyPlan.cardOrder.length} 个词 · 每天 ${state.studyPlan.wordsPerDay} 个 · 共 ${totalPlanDays()} 天<br><span>进度保存在当前浏览器，请定期导出备份。</span></div>
    </aside>
    <main class="main">
      <div class="topbar"><div class="page-title"><h2>${escapeHtml(title)}</h2><p>${escapeHtml(subtitle)}</p></div><div class="top-actions"><a class="btn btn-secondary" href="#/plan">▦ <span class="label-hide">选择学习日</span></a><button class="btn btn-secondary" onclick="toggleTheme()">◐ <span class="label-hide">切换主题</span></button></div></div>
      ${content}
    </main>
    <nav class="mobile-nav">${[["dashboard","首页","#/dashboard"],["plan","计划","#/plan"],["practice","练习","#/practice"],["cards","卡片","#/cards"],["stats","统计","#/stats"],["settings","设置","#/settings"]].map(n=>`<a href="${n[2]}" class="${hash.startsWith(n[2])?"active":""}"><span>${icons[n[0]]}</span>${n[1]}</a>`).join("")}</nav>
  </div>`;
};

function dayCardHTML(day,compact=false){
  const s=daySummary(day),p=progressForDay(day);const last=s.day===Number(state.studyPlan.lastDay||1);
  return `<article class="day-card ${dayStatusClass(s)} ${last?"last-day":""}">
    <div class="day-card-top"><div><span class="day-eyebrow">DAY</span><strong>${String(s.day).padStart(2,"0")}</strong></div><span class="day-status">${dayStatusText(s)}</span></div>
    <div class="day-progress"><span style="width:${s.percent}%"></span></div>
    <div class="day-numbers"><span>${s.studied}/${s.total} 已学</span><span>${s.correct} 对 · ${s.wrong} 错</span></div>
    ${compact?"":`<div class="day-card-actions"><a class="btn btn-small btn-primary" href="#/day/${s.day}">${s.status==="not_started"?"查看并开始":"继续学习"}</a></div>`}
  </article>`;
}

function planOverview(){
  const total=totalPlanDays(), completed=Array.from({length:total},(_,i)=>daySummary(i+1)).filter(s=>s.completed).length;
  const next=nextSuggestedDay();
  render(shell(`<section class="plan-hero card"><div><span class="hero-badge">固定学习计划</span><h3>${escapeHtml(state.studyPlan.name)}</h3><p>把 ${state.studyPlan.cardOrder.length} 个词固定分为 ${total} 天，每天 ${state.studyPlan.wordsPerDay} 个。你可以自由选择任意一天，关闭网页后仍会保留本机进度。</p><div class="hero-actions"><a class="btn btn-primary" href="#/day/${next}">继续第 ${next} 天</a><button class="btn btn-secondary" onclick="openPlanSettings()">调整计划</button></div></div><div class="plan-score"><strong>${completed}</strong><span>/ ${total} 天完成</span></div></section>
  <section class="section"><div class="section-head"><div><h3>选择学习日</h3><p class="meta">每组单词固定，不会因刷新或重新进入而变化。</p></div><div class="plan-legend"><span class="dot done"></span>完成 <span class="dot active"></span>学习中 <span class="dot"></span>未开始</div></div><div class="day-grid">${Array.from({length:total},(_,i)=>dayCardHTML(i+1)).join("")}</div></section>`,"学习计划",`共 ${total} 天，可手动进入任意一天`));
}

function planDashboard(){
  const todayLogs=state.reviewLogs.filter(x=>x.reviewedAt.startsWith(todayKey()));
  const correct=todayLogs.filter(x=>x.isCorrect).length;
  const due=state.reviewStates.filter(r=>r.status!=="new"&&new Date(r.dueAt)<=new Date()&&!state.cards.find(c=>c.id===r.cardId)?.isSuspended).length;
  const next=nextSuggestedDay(), nextS=daySummary(next), total=totalPlanDays();
  const completed=Array.from({length:total},(_,i)=>daySummary(i+1)).filter(s=>s.completed).length;
  const progress=Math.round(completed/total*100);
  const preview=Array.from({length:Math.min(6,total)},(_,i)=>dayCardHTML(i+1,true)).join("");
  render(shell(`<section class="welcome card"><div class="welcome-copy"><span class="hero-badge">AI 辅助背单词</span><h3>先主动回忆，再用发音、音标和详细解析逐层学习。</h3><p>今天可以从第 ${next} 天继续。按天划分让学习路线始终清晰，本地进度和错词复习则负责记录真实掌握情况。</p><div class="hero-actions"><a class="btn btn-primary btn-large" href="#/day/${next}">继续第 ${next} 天 · ${nextS.studied}/${nextS.total}</a><a class="btn btn-secondary" href="#/plan">查看全部 ${total} 天</a><a class="btn btn-ghost" href="#/practice?mode=review">复习到期错词</a></div></div><div class="plan-orbit"><div class="ring" style="--progress:${progress}%"><div class="ring-inner"><div><strong>${progress}%</strong><span>${completed}/${total} 天</span></div></div></div></div></section>
  <div class="grid grid-4 section"><div class="card stat"><div class="label">今日练习</div><div class="value">${todayLogs.length}</div><div class="hint">所有模式合计</div></div><div class="card stat"><div class="label">今日正确率</div><div class="value">${todayLogs.length?Math.round(correct/todayLogs.length*100):0}%</div><div class="hint">最终作答结果</div></div><div class="card stat"><div class="label">待间隔复习</div><div class="value">${due}</div><div class="hint">错词与到期卡片</div></div><div class="card stat"><div class="label">学习计划</div><div class="value">${completed}/${total}</div><div class="hint">已完成天数</div></div></div>
  <section class="section"><div class="section-head"><h3>学习日概览</h3><a class="btn btn-small btn-secondary" href="#/plan">全部日期</a></div><div class="day-grid compact">${preview}</div></section>`,"WordLoop",`本机学习计划：每天 ${state.studyPlan.wordsPerDay} 个，共 ${total} 天`));
}
dashboard=planDashboard;

function openPlanSettings(){
  modal(`<h3>调整学习计划</h3><p class="meta">重新生成计划会重新划分每一天，并清空“按天学习”的完成标记；原有卡片、间隔复习状态和答题记录不会删除。</p>
  <div class="field"><label>计划名称</label><input id="planName" class="input" value="${escapeHtml(state.studyPlan.name)}"></div>
  <div class="field" style="margin-top:14px"><label>每天新学单词数</label><input id="planWords" class="input" type="number" min="1" max="100" value="${state.studyPlan.wordsPerDay}"><small>${state.studyPlan.cardOrder.length} 个单词将自动计算总天数。</small></div>
  <div class="field" style="margin-top:14px"><label>排序方式</label><select id="planOrder" class="select"><option value="original" ${state.studyPlan.orderMode==="original"?"selected":""}>保持当前词库顺序</option><option value="random" ${state.studyPlan.orderMode==="random"?"selected":""}>随机固定分组</option></select></div>
  <div class="modal-actions"><button class="btn btn-secondary" onclick="closeModal()">取消</button><button class="btn btn-primary" onclick="applyPlanSettings()">重新生成计划</button></div>`);
}
function applyPlanSettings(){
  const name=document.getElementById("planName").value.trim()||"我的单词计划";
  const n=Math.max(1,Math.min(100,Number(document.getElementById("planWords").value)||20));
  const order=document.getElementById("planOrder").value;
  if(!confirm(`将按每天 ${n} 个重新划分学习日，并重置按天进度。继续吗？`))return;
  createPlanAssignments(n,order,false);state.studyPlan.name=name;state.settings.dailyGoal=n;save();closeModal();planOverview();toast(`已生成 ${totalPlanDays()} 天学习计划`);
}

function dayDetail(day){
  day=clampDay(day);setCurrentPlanDay(day);const cards=cardsForDay(day),s=daySummary(day),p=progressForDay(day);
  const status=s.completed?"本日已完成":s.studied?`已学习 ${s.studied}/${s.total}`:"尚未开始";
  const list=cards.map((c,i)=>{
    const studied=p.studiedCardIds.includes(c.id),wrong=p.wrongCardIds.includes(c.id),correct=p.correctCardIds.includes(c.id);
    return `<div class="day-word-row"><span class="word-order">${i+1}</span><div><strong>${escapeHtml(c.word||c.clozeAnswer||"短语")}</strong><span>${escapeHtml(c.pronunciation||"")}</span><p>${escapeHtml(c.meaningZh||c.sentenceZh||"")}</p></div><span class="word-state ${wrong?"wrong":correct?"correct":studied?"studied":""}">${wrong?"待复习":correct?"已掌握":studied?"已学习":"未学习"}</span></div>`;
  }).join("");
  render(shell(`<section class="day-detail-head card"><div><a class="back-link" href="#/plan">← 返回学习计划</a><div class="day-title"><span>DAY</span><strong>${String(day).padStart(2,"0")}</strong></div><h3>${status}</h3><p>本日共 ${s.total} 个词。你可以从上次位置继续，也可以重学全部或只练错词。</p></div><div class="day-detail-actions"><a class="btn btn-primary btn-large" href="#/practice?mode=day-${day}">${s.studied?"继续本日学习":"开始本日学习"}</a>${s.wrong?`<a class="btn btn-secondary" href="#/practice?mode=daywrong-${day}">只练错词 ${s.wrong}</a>`:""}<button class="btn btn-secondary" onclick="restartDay(${day})">从头重学</button></div></section>
  <div class="grid grid-4 section"><div class="card stat"><div class="label">本日总数</div><div class="value">${s.total}</div></div><div class="card stat"><div class="label">已经学习</div><div class="value">${s.studied}</div></div><div class="card stat"><div class="label">当前正确</div><div class="value">${s.correct}</div></div><div class="card stat"><div class="label">待复习</div><div class="value">${s.wrong}</div></div></div>
  <section class="section"><div class="section-head"><h3>第 ${day} 天单词</h3><div class="actions"><button class="btn btn-small btn-secondary" onclick="toggleDayComplete(${day})">${s.completed?"取消完成标记":"标记本日完成"}</button><button class="btn btn-small btn-ghost" onclick="resetDayProgress(${day})">重置本日进度</button></div></div><div class="card day-word-list">${list}</div></section>`,`第 ${day} 天`,`${s.total} 个单词 · ${s.percent}% 已学习`));
}
function restartDay(day){const p=progressForDay(day);p.currentIndex=0;p.wrongCurrentIndex=0;p.manualComplete=false;p.updatedAt=nowISO();save();practiceSession=null;location.hash=`#/practice?mode=day-${clampDay(day)}`;}
function resetDayProgress(day){if(!confirm("确定清空这一天的按天学习进度吗？原有间隔复习记录不会删除。"))return;state.studyPlan.dayProgress[String(clampDay(day))]={currentIndex:0,wrongCurrentIndex:0,studiedCardIds:[],correctCardIds:[],wrongCardIds:[],manualComplete:false,lastOpenedAt:nowISO(),updatedAt:nowISO()};save();dayDetail(day);toast("本日进度已重置");}
function toggleDayComplete(day){const p=progressForDay(day);p.manualComplete=!daySummary(day).completed;p.updatedAt=nowISO();save();dayDetail(day);}

const buildPracticeQueueV2=buildPracticeQueue;
buildPracticeQueue=function(mode){
  mode=String(mode||"");
  let m=mode.match(/^day-(\d+)$/);if(m)return cardsForDay(m[1]);
  m=mode.match(/^daywrong-(\d+)$/);if(m){const p=progressForDay(m[1]);return cardsForDay(m[1]).filter(c=>p.wrongCardIds.includes(c.id));}
  if(mode==="review"){
    return state.cards
      .filter(c=>!c.isSuspended)
      .filter(c=>{const r=getReview(c.id);return r.status!=="new"&&new Date(r.dueAt)<=new Date();})
      .sort((a,b)=>new Date(getReview(a.id).dueAt)-new Date(getReview(b.id).dueAt))
      .slice(0,Math.max(10,state.settings.dailyGoal));
  }
  return buildPracticeQueueV2(mode);
};

const practiceV2=practice;
practice=function(){
  const params=new URLSearchParams((location.hash.split("?")[1]||""));const mode=params.get("mode")||state.ui.lastPracticeMode||"review";
  const isNew=!practiceSession||practiceSession.mode!==mode;
  practiceV2();
  if(isNew&&practiceSession){
    const m=mode.match(/^(day|daywrong)-(\d+)$/);
    if(m){
      const day=clampDay(m[2]);setCurrentPlanDay(day);const p=progressForDay(day);
      const max=Math.max(0,practiceSession.queue.length-1);
      const savedIndex=m[1]==="daywrong"?p.wrongCurrentIndex:p.currentIndex;
      const restored=daySummary(day).completed&&m[1]==="day"?0:Math.min(max,savedIndex||0);
      if(restored>0){practiceSession.index=restored;practiceV2();}
    }
  }
  const m=mode.match(/^(?:day|daywrong)-(\d+)$/);
  if(m){
    const day=clampDay(m[1]);const kicker=document.querySelector(".practice-kicker");if(kicker)kicker.innerHTML=`<span class="practice-day-tag">第 ${day} 天</span>${kicker.innerHTML}`;
    const title=document.querySelector(".page-title h2");if(title)title.textContent=`第 ${day} 天学习`;
    const subtitle=document.querySelector(".page-title p");if(subtitle)subtitle.textContent=`本日 ${cardsForDay(day).length} 个词 · 进度自动保存在当前浏览器`;
  }
};

const submitPracticeV2=submitPractice;
submitPractice=function(){
  const card=currentCard(),mode=practiceSession?.mode;submitPracticeV2();
  if(!card||practiceSession?.mode!==mode)return;
  if(practiceSession?.feedback==="wrong")recordDayOutcome(card.id,false);
  else if(practiceSession?.feedback==="success")recordDayOutcome(card.id,true);
};
const useHintV2=useHint;
useHint=function(){const card=currentCard(),before=practiceSession?.hintStage||0;useHintV2();if(card&&before===0&&practiceSession?.hintStage>=1)recordDayOutcome(card.id,false);};
const revealAnswerV2=revealAnswer;
revealAnswer=function(){const card=currentCard();revealAnswerV2();if(card&&practiceSession?.feedback==="revealed")recordDayOutcome(card.id,false);};
const skipCardV2=skipCard;
skipCard=function(){const card=currentCard(),mode=practiceSession?.mode;if(card&&/^(?:day|daywrong)-\d+$/.test(mode||""))recordDayOutcome(card.id,false);skipCardV2();};
const nextCardV2=nextCard;
nextCard=function(){const mode=practiceSession?.mode;nextCardV2();if(practiceSession)updateDayIndex(mode,practiceSession.index);};
const finishPracticeV2=finishPractice;
finishPractice=function(done=false){
  const mode=practiceSession?.mode||"";const m=mode.match(/^(day|daywrong)-(\d+)$/);if(m){const day=clampDay(m[2]);const p=progressForDay(day);if(done&&m[1]==="day"&&daySummary(day).studied>=cardsForDay(day).length){p.manualComplete=true;p.currentIndex=cardsForDay(day).length;}p.updatedAt=nowISO();save();practiceSession=null;location.hash=`#/day/${day}`;return;}
  finishPracticeV2(done);
};

const settingsV2=settings;
settings=function(){
  settingsV2();
  const firstCard=document.querySelector(".main .card");
  if(firstCard){firstCard.insertAdjacentHTML("beforebegin",`<section class="card plan-settings-strip"><div><strong>当前学习计划</strong><span>${escapeHtml(state.studyPlan.name)} · 每天 ${state.studyPlan.wordsPerDay} 个 · 共 ${totalPlanDays()} 天</span></div><button class="btn btn-secondary" onclick="openPlanSettings()">调整按天计划</button></section>`);}
};

const routeV2=route;
route=function(){
  try{
    ensureStudyPlan();const path=(location.hash||"#/dashboard").slice(1).split("?")[0];
    if(path==="/plan")planOverview();
    else if(/^\/day\/\d+$/.test(path))dayDetail(path.split("/").pop());
    else routeV2();
  }catch(error){
    console.error("WordLoop route error",error);
    render(shell(`<div class="card empty"><h3>页面加载失败</h3><p>程序遇到异常，请返回首页重试。学习数据仍保存在浏览器中。</p><a class="btn btn-primary" href="#/dashboard">返回首页</a><pre class="code-note">${escapeHtml(error?.message||String(error))}</pre></div>`,"WordLoop","发生了一个可恢复的页面错误"));
  }
};

// app.js 在加载时绑定的是旧 route 函数对象。必须显式移除旧监听器，
// 否则点击 #/plan 或 #/day/... 时会被旧路由错误地送回首页。
window.removeEventListener("hashchange",routeV2);
window.addEventListener("hashchange",route);

// Re-render after v3 overrides are installed.
if(document.readyState!=="loading")route();
