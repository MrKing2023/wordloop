
const APP_KEY = "wordloop_local_v1";

const icons = {
  dashboard:"⌂", practice:"✎", decks:"▣", cards:"☰", stats:"▥", settings:"⚙", import:"⇅"
};

const seedCards = [{"deck": "四级核心词汇", "type": "cloze", "word": "commute", "pronunciation": "/kəˈmjuːt/", "partOfSpeech": "v.", "meaningZh": "通勤", "sentenceEn": "I usually commute to work by subway.", "sentenceZh": "我通常乘地铁通勤上班。", "clozePrefix": "I usually ", "clozeAnswer": "commute", "clozeSuffix": " to work by subway.", "acceptedAnswers": ["commute"], "tags": ["日常", "交通"]}, {"deck": "四级核心词汇", "type": "cloze", "word": "maintain", "pronunciation": "/meɪnˈteɪn/", "partOfSpeech": "v.", "meaningZh": "维持；维护", "sentenceEn": "Regular exercise helps maintain good health.", "sentenceZh": "规律锻炼有助于保持健康。", "clozePrefix": "Regular exercise helps ", "clozeAnswer": "maintain", "clozeSuffix": " good health.", "acceptedAnswers": ["maintain"], "tags": ["健康"]}, {"deck": "四级核心词汇", "type": "cloze", "word": "efficient", "pronunciation": "/ɪˈfɪʃənt/", "partOfSpeech": "adj.", "meaningZh": "高效的", "sentenceEn": "This is a more efficient way to solve the problem.", "sentenceZh": "这是解决这个问题更高效的方法。", "clozePrefix": "This is a more ", "clozeAnswer": "efficient", "clozeSuffix": " way to solve the problem.", "acceptedAnswers": ["efficient"], "tags": ["学习", "工作"]}, {"deck": "四级核心词汇", "type": "cloze", "word": "available", "pronunciation": "/əˈveɪləbl/", "partOfSpeech": "adj.", "meaningZh": "可获得的；有空的", "sentenceEn": "The report is available online.", "sentenceZh": "这份报告可以在网上获取。", "clozePrefix": "The report is ", "clozeAnswer": "available", "clozeSuffix": " online.", "acceptedAnswers": ["available"], "tags": ["学术"]}, {"deck": "四级核心词汇", "type": "cloze", "word": "respond", "pronunciation": "/rɪˈspɒnd/", "partOfSpeech": "v.", "meaningZh": "回应", "sentenceEn": "Please respond to the email before Friday.", "sentenceZh": "请在周五之前回复这封邮件。", "clozePrefix": "Please ", "clozeAnswer": "respond", "clozeSuffix": " to the email before Friday.", "acceptedAnswers": ["respond", "reply"], "tags": ["工作", "邮件"]}, {"deck": "四级核心词汇", "type": "cloze", "word": "improve", "pronunciation": "/ɪmˈpruːv/", "partOfSpeech": "v.", "meaningZh": "改善；提高", "sentenceEn": "Reading every day can improve your vocabulary.", "sentenceZh": "每天阅读可以提高你的词汇量。", "clozePrefix": "Reading every day can ", "clozeAnswer": "improve", "clozeSuffix": " your vocabulary.", "acceptedAnswers": ["improve"], "tags": ["学习"]}, {"deck": "四级核心词汇", "type": "cloze", "word": "require", "pronunciation": "/rɪˈkwaɪə/", "partOfSpeech": "v.", "meaningZh": "需要", "sentenceEn": "This task requires careful planning.", "sentenceZh": "这项任务需要仔细规划。", "clozePrefix": "This task ", "clozeAnswer": "requires", "clozeSuffix": " careful planning.", "acceptedAnswers": ["requires"], "tags": ["工作"]}, {"deck": "四级核心词汇", "type": "cloze", "word": "benefit", "pronunciation": "/ˈbenɪfɪt/", "partOfSpeech": "n./v.", "meaningZh": "益处；受益", "sentenceEn": "Students can benefit from regular review.", "sentenceZh": "学生可以从定期复习中受益。", "clozePrefix": "Students can ", "clozeAnswer": "benefit", "clozeSuffix": " from regular review.", "acceptedAnswers": ["benefit"], "tags": ["学习"]}, {"deck": "四级核心词汇", "type": "cloze", "word": "challenge", "pronunciation": "/ˈtʃælɪndʒ/", "partOfSpeech": "n.", "meaningZh": "挑战", "sentenceEn": "Learning a new language is a rewarding challenge.", "sentenceZh": "学习一门新语言是一项有回报的挑战。", "clozePrefix": "Learning a new language is a rewarding ", "clozeAnswer": "challenge", "clozeSuffix": ".", "acceptedAnswers": ["challenge"], "tags": ["学习"]}, {"deck": "四级核心词汇", "type": "cloze", "word": "environment", "pronunciation": "/ɪnˈvaɪrənmənt/", "partOfSpeech": "n.", "meaningZh": "环境", "sentenceEn": "We should protect the natural environment.", "sentenceZh": "我们应该保护自然环境。", "clozePrefix": "We should protect the natural ", "clozeAnswer": "environment", "clozeSuffix": ".", "acceptedAnswers": ["environment"], "tags": ["环境"]}, {"deck": "学术英语", "type": "cloze", "word": "significant", "pronunciation": "/sɪɡˈnɪfɪkənt/", "partOfSpeech": "adj.", "meaningZh": "显著的；重要的", "sentenceEn": "The experiment showed a significant improvement.", "sentenceZh": "实验显示出显著改善。", "clozePrefix": "The experiment showed a ", "clozeAnswer": "significant", "clozeSuffix": " improvement.", "acceptedAnswers": ["significant"], "tags": ["论文", "结果"]}, {"deck": "学术英语", "type": "cloze", "word": "indicate", "pronunciation": "/ˈɪndɪkeɪt/", "partOfSpeech": "v.", "meaningZh": "表明", "sentenceEn": "The results indicate that the method is reliable.", "sentenceZh": "结果表明该方法是可靠的。", "clozePrefix": "The results ", "clozeAnswer": "indicate", "clozeSuffix": " that the method is reliable.", "acceptedAnswers": ["indicate", "show"], "tags": ["论文", "结果"]}, {"deck": "学术英语", "type": "cloze", "word": "approach", "pronunciation": "/əˈprəʊtʃ/", "partOfSpeech": "n.", "meaningZh": "方法", "sentenceEn": "We propose a new approach to data analysis.", "sentenceZh": "我们提出了一种新的数据分析方法。", "clozePrefix": "We propose a new ", "clozeAnswer": "approach", "clozeSuffix": " to data analysis.", "acceptedAnswers": ["approach", "method"], "tags": ["论文", "方法"]}, {"deck": "学术英语", "type": "cloze", "word": "assume", "pronunciation": "/əˈsjuːm/", "partOfSpeech": "v.", "meaningZh": "假设", "sentenceEn": "We assume that the flow is incompressible.", "sentenceZh": "我们假设流动是不可压缩的。", "clozePrefix": "We ", "clozeAnswer": "assume", "clozeSuffix": " that the flow is incompressible.", "acceptedAnswers": ["assume"], "tags": ["论文", "理论"]}, {"deck": "学术英语", "type": "cloze", "word": "consistent", "pronunciation": "/kənˈsɪstənt/", "partOfSpeech": "adj.", "meaningZh": "一致的", "sentenceEn": "The numerical results are consistent with the experiment.", "sentenceZh": "数值结果与实验一致。", "clozePrefix": "The numerical results are ", "clozeAnswer": "consistent", "clozeSuffix": " with the experiment.", "acceptedAnswers": ["consistent"], "tags": ["论文", "结果"]}, {"deck": "学术英语", "type": "cloze", "word": "derive", "pronunciation": "/dɪˈraɪv/", "partOfSpeech": "v.", "meaningZh": "推导；得到", "sentenceEn": "The governing equation can be derived from conservation laws.", "sentenceZh": "控制方程可以由守恒定律推导得到。", "clozePrefix": "The governing equation can be ", "clozeAnswer": "derived", "clozeSuffix": " from conservation laws.", "acceptedAnswers": ["derived"], "tags": ["论文", "理论"]}, {"deck": "学术英语", "type": "cloze", "word": "approximately", "pronunciation": "/əˈprɒksɪmətli/", "partOfSpeech": "adv.", "meaningZh": "大约", "sentenceEn": "The simulation took approximately three hours.", "sentenceZh": "这次模拟大约花了三个小时。", "clozePrefix": "The simulation took ", "clozeAnswer": "approximately", "clozeSuffix": " three hours.", "acceptedAnswers": ["approximately", "about"], "tags": ["论文", "计算"]}, {"deck": "学术英语", "type": "cloze", "word": "evaluate", "pronunciation": "/ɪˈvæljueɪt/", "partOfSpeech": "v.", "meaningZh": "评估", "sentenceEn": "The model was used to evaluate structural performance.", "sentenceZh": "该模型用于评估结构性能。", "clozePrefix": "The model was used to ", "clozeAnswer": "evaluate", "clozeSuffix": " structural performance.", "acceptedAnswers": ["evaluate", "assess"], "tags": ["论文", "方法"]}, {"deck": "学术英语", "type": "cloze", "word": "parameter", "pronunciation": "/pəˈræmɪtə/", "partOfSpeech": "n.", "meaningZh": "参数", "sentenceEn": "Each parameter was carefully calibrated.", "sentenceZh": "每个参数都经过了仔细校准。", "clozePrefix": "Each ", "clozeAnswer": "parameter", "clozeSuffix": " was carefully calibrated.", "acceptedAnswers": ["parameter"], "tags": ["论文", "计算"]}, {"deck": "日常表达", "type": "cloze", "word": "appointment", "pronunciation": "/əˈpɔɪntmənt/", "partOfSpeech": "n.", "meaningZh": "预约", "sentenceEn": "I have a doctor's appointment tomorrow morning.", "sentenceZh": "我明天上午预约了医生。", "clozePrefix": "I have a doctor's ", "clozeAnswer": "appointment", "clozeSuffix": " tomorrow morning.", "acceptedAnswers": ["appointment"], "tags": ["日常"]}, {"deck": "日常表达", "type": "translation", "word": "on time", "pronunciation": "", "partOfSpeech": "phrase", "meaningZh": "准时", "sentenceEn": "Please arrive on time.", "sentenceZh": "请准时到达。", "targetEnglish": "Please arrive on time.", "acceptedAnswers": ["Please arrive on time.", "Please be on time."], "tags": ["日常"]}, {"deck": "日常表达", "type": "translation", "word": "look forward to", "pronunciation": "", "partOfSpeech": "phrase", "meaningZh": "期待", "sentenceEn": "I look forward to hearing from you.", "sentenceZh": "我期待收到你的回复。", "targetEnglish": "I look forward to hearing from you.", "acceptedAnswers": ["I look forward to hearing from you.", "I'm looking forward to hearing from you."], "tags": ["邮件", "日常"]}, {"deck": "日常表达", "type": "translation", "word": "take a break", "pronunciation": "", "partOfSpeech": "phrase", "meaningZh": "休息一下", "sentenceEn": "Let's take a short break.", "sentenceZh": "我们休息一会儿吧。", "targetEnglish": "Let's take a short break.", "acceptedAnswers": ["Let's take a short break.", "Let's take a break."], "tags": ["日常"]}, {"deck": "日常表达", "type": "translation", "word": "make progress", "pronunciation": "", "partOfSpeech": "phrase", "meaningZh": "取得进展", "sentenceEn": "You are making steady progress.", "sentenceZh": "你正在稳步取得进展。", "targetEnglish": "You are making steady progress.", "acceptedAnswers": ["You are making steady progress.", "You're making steady progress."], "tags": ["学习"]}, {"deck": "日常表达", "type": "translation", "word": "as soon as possible", "pronunciation": "", "partOfSpeech": "phrase", "meaningZh": "尽快", "sentenceEn": "Please send me the file as soon as possible.", "sentenceZh": "请尽快把文件发给我。", "targetEnglish": "Please send me the file as soon as possible.", "acceptedAnswers": ["Please send me the file as soon as possible.", "Please send the file to me as soon as possible."], "tags": ["工作", "邮件"]}, {"deck": "学术英语", "type": "translation", "word": "in good agreement with", "pronunciation": "", "partOfSpeech": "phrase", "meaningZh": "与……吻合良好", "sentenceEn": "The predictions are in good agreement with the measurements.", "sentenceZh": "预测结果与测量结果吻合良好。", "targetEnglish": "The predictions are in good agreement with the measurements.", "acceptedAnswers": ["The predictions are in good agreement with the measurements.", "The predicted results agree well with the measurements."], "tags": ["论文", "结果"]}, {"deck": "学术英语", "type": "translation", "word": "be attributed to", "pronunciation": "", "partOfSpeech": "phrase", "meaningZh": "归因于", "sentenceEn": "The difference may be attributed to numerical errors.", "sentenceZh": "这种差异可能归因于数值误差。", "targetEnglish": "The difference may be attributed to numerical errors.", "acceptedAnswers": ["The difference may be attributed to numerical errors.", "This difference may be attributed to numerical errors."], "tags": ["论文", "讨论"]}, {"deck": "学术英语", "type": "translation", "word": "it should be noted that", "pronunciation": "", "partOfSpeech": "phrase", "meaningZh": "需要指出的是", "sentenceEn": "It should be noted that the model has several limitations.", "sentenceZh": "需要指出的是，该模型存在若干局限性。", "targetEnglish": "It should be noted that the model has several limitations.", "acceptedAnswers": ["It should be noted that the model has several limitations.", "It is worth noting that the model has several limitations."], "tags": ["论文", "讨论"]}, {"deck": "学术英语", "type": "translation", "word": "compared with", "pronunciation": "", "partOfSpeech": "phrase", "meaningZh": "与……相比", "sentenceEn": "Compared with the baseline case, the wave load was reduced.", "sentenceZh": "与基准工况相比，波浪荷载有所降低。", "targetEnglish": "Compared with the baseline case, the wave load was reduced.", "acceptedAnswers": ["Compared with the baseline case, the wave load was reduced.", "The wave load was reduced compared with the baseline case."], "tags": ["论文", "结果"]}, {"deck": "日常表达", "type": "translation", "word": "It depends", "pronunciation": "", "partOfSpeech": "phrase", "meaningZh": "视情况而定", "sentenceEn": "It depends on the weather.", "sentenceZh": "这取决于天气。", "targetEnglish": "It depends on the weather.", "acceptedAnswers": ["It depends on the weather."], "tags": ["日常"]}];

function uid(){ return crypto?.randomUUID?.() || ("id-"+Date.now()+"-"+Math.random().toString(16).slice(2)); }
function nowISO(){ return new Date().toISOString(); }
function todayKey(d=new Date()){ return d.toISOString().slice(0,10); }
function addDays(date, days){ const d=new Date(date); d.setDate(d.getDate()+days); return d.toISOString(); }
function addMinutes(date, mins){ const d=new Date(date); d.setMinutes(d.getMinutes()+mins); return d.toISOString(); }
function escapeHtml(s=""){ return String(s).replace(/[&<>"']/g,m=>({"&":"&amp;","<":"&lt;",">":"&gt;","\"":"&quot;","'":"&#039;"}[m])); }
function formatDate(iso){ if(!iso) return "—"; return new Date(iso).toLocaleString("zh-CN",{month:"2-digit",day:"2-digit",hour:"2-digit",minute:"2-digit"}); }
function download(filename, text, type="application/json"){
  const blob=new Blob([text],{type}); const url=URL.createObjectURL(blob); const a=document.createElement("a");
  a.href=url;a.download=filename;a.click();URL.revokeObjectURL(url);
}
function toast(msg){ const el=document.getElementById("toast"); el.textContent=msg; el.classList.add("show"); clearTimeout(toast.t); toast.t=setTimeout(()=>el.classList.remove("show"),2200); }

function initialState(){
  const decksMap={}; seedCards.forEach(c=>decksMap[c.deck]=decksMap[c.deck]||{id:uid(),name:c.deck,description:"内置示例词库",color:"#6d5dfc",createdAt:nowISO(),updatedAt:nowISO()});
  const decks=Object.values(decksMap);
  const cards=seedCards.map((c,i)=>({
    id:uid(), deckId:decksMap[c.deck].id, type:c.type, word:c.word||"", pronunciation:c.pronunciation||"", partOfSpeech:c.partOfSpeech||"",
    meaningZh:c.meaningZh||"", sentenceEn:c.sentenceEn||"", sentenceZh:c.sentenceZh||"", clozePrefix:c.clozePrefix||"", clozeAnswer:c.clozeAnswer||"",
    clozeSuffix:c.clozeSuffix||"", targetEnglish:c.targetEnglish||"", acceptedAnswers:c.acceptedAnswers||[], tags:c.tags||[], difficulty:1,
    source:"内置示例", isSuspended:false, createdAt:nowISO(), updatedAt:nowISO()
  }));
  const reviewStates=cards.map((c,i)=>({cardId:c.id,status:"new",level:0,intervalDays:0,consecutiveCorrect:0,totalCorrect:0,totalWrong:0,lapses:0,dueAt:i<8?nowISO():addDays(new Date(),Math.ceil(i/8)),lastReviewedAt:null,averageResponseTime:0}));
  return {
    version:1,decks,cards,reviewStates,reviewLogs:[],
    settings:{dailyGoal:20,defaultPracticeMode:"mixed",autoAdvance:true,autoAdvanceDelay:700,autoPlayAudio:false,ignoreCase:true,ignoreEndingPunctuation:true,collapseWhitespace:true,showChineseHint:true,theme:"light"},
    ui:{lastPracticeMode:"review"}
  };
}
function loadState(){
  try{
    const raw=localStorage.getItem(APP_KEY);
    if(!raw) return initialState();
    const s=JSON.parse(raw);
    if(!s.settings) return initialState();
    return s;
  }catch(e){ console.error(e); return initialState(); }
}
let state=loadState();
function save(){ localStorage.setItem(APP_KEY,JSON.stringify(state)); }
function resetData(){ state=initialState(); save(); route(); toast("已恢复示例数据"); }
function getDeck(id){ return state.decks.find(d=>d.id===id); }
function getReview(cardId){
  let r=state.reviewStates.find(x=>x.cardId===cardId);
  if(!r){ r={cardId,status:"new",level:0,intervalDays:0,consecutiveCorrect:0,totalCorrect:0,totalWrong:0,lapses:0,dueAt:nowISO(),lastReviewedAt:null,averageResponseTime:0}; state.reviewStates.push(r); }
  return r;
}
function normalizeAnswer(text){
  let s=(text??"").normalize("NFKC").trim().replace(/[’‘]/g,"'");
  if(state.settings.collapseWhitespace) s=s.replace(/\s+/g," ");
  if(state.settings.ignoreEndingPunctuation) s=s.replace(/[.!?。！？]+$/g,"").trim();
  if(state.settings.ignoreCase) s=s.toLowerCase();
  return s;
}
function levenshtein(a,b){
  const dp=Array.from({length:a.length+1},()=>Array(b.length+1).fill(0));
  for(let i=0;i<=a.length;i++)dp[i][0]=i; for(let j=0;j<=b.length;j++)dp[0][j]=j;
  for(let i=1;i<=a.length;i++)for(let j=1;j<=b.length;j++)dp[i][j]=Math.min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+(a[i-1]===b[j-1]?0:1));
  return dp[a.length][b.length];
}
function evaluate(card, answer){
  const n=normalizeAnswer(answer);
  const options=[...(card.acceptedAnswers||[])];
  if(card.type==="cloze"&&card.clozeAnswer) options.unshift(card.clozeAnswer);
  if(card.type==="translation"&&card.targetEnglish) options.unshift(card.targetEnglish);
  const normalized=[...new Set(options.map(normalizeAnswer).filter(Boolean))];
  const correct=normalized.includes(n);
  const dist=Math.min(...normalized.map(x=>levenshtein(n,x)));
  return {correct,close:!correct&&n.length>2&&dist<=1,target:options[0]||""};
}
function reviewResult({correct,attempts,hintUsed,revealed,responseTime}){
  if(!correct||revealed) return "again";
  if(attempts===1&&!hintUsed&&responseTime<8000) return "easy";
  if(attempts===1&&!hintUsed) return "good";
  if(attempts===2&&!hintUsed) return "good";
  return "hard";
}
function schedule(cardId,result,responseTime){
  const r=getReview(cardId); const prevAvg=r.averageResponseTime||0; r.averageResponseTime=prevAvg?Math.round(prevAvg*.7+responseTime*.3):responseTime; r.lastReviewedAt=nowISO();
  if(result==="again"){
    r.totalWrong++; r.lapses++; r.consecutiveCorrect=0; r.level=Math.max(0,r.level-1); r.status="learning"; r.intervalDays=0; r.dueAt=addMinutes(new Date(),10);
  }else{
    r.totalCorrect++; r.consecutiveCorrect++; r.level++;
    const ladder=[1,3,7,14,30]; let days=ladder[Math.min(r.level-1,ladder.length-1)] || Math.round(30*Math.pow(1.7,r.level-5));
    if(result==="hard") days=Math.max(1,Math.round(days*.55)); if(result==="easy") days=Math.max(1,Math.round(days*1.35));
    r.intervalDays=days; r.dueAt=addDays(new Date(),days); r.status=r.level>=5?"mastered":"review";
  }
  save();
}
function speak(text){
  if(!("speechSynthesis" in window)){toast("当前浏览器不支持语音朗读");return;}
  speechSynthesis.cancel(); const u=new SpeechSynthesisUtterance(text); u.lang="en-US"; u.rate=.92; speechSynthesis.speak(u);
}

function shell(content,title,subtitle=""){
  const hash=location.hash||"#/dashboard";
  const nav=[
    ["dashboard","首页","#/dashboard"],["practice","练习","#/practice"],["decks","单词本","#/decks"],["cards","卡片","#/cards"],["stats","统计","#/stats"],["settings","设置","#/settings"]
  ];
  document.body.classList.toggle("dark",state.settings.theme==="dark");
  return `<div class="app-shell">
    <aside class="sidebar">
      <div class="brand"><div class="logo">W</div><div><h1>WordLoop</h1><p>语境填词记忆</p></div></div>
      <nav class="nav">${nav.map(n=>`<a href="${n[2]}" class="${hash.startsWith(n[2])?"active":""}"><span class="icon">${icons[n[0]]}</span>${n[1]}</a>`).join("")}
      <a href="#/import" class="${hash.startsWith("#/import")?"active":""}"><span class="icon">${icons.import}</span>导入导出</a></nav>
      <div class="sidebar-footer">数据保存在当前浏览器中。建议定期导出 JSON 备份。</div>
    </aside>
    <main class="main">
      <div class="topbar"><div class="page-title"><h2>${escapeHtml(title)}</h2><p>${escapeHtml(subtitle)}</p></div><div class="top-actions"><button class="btn btn-secondary" onclick="toggleTheme()">◐ <span class="label-hide">切换主题</span></button></div></div>
      ${content}
    </main>
    <nav class="mobile-nav">${nav.map(n=>`<a href="${n[2]}" class="${hash.startsWith(n[2])?"active":""}"><span>${icons[n[0]]}</span>${n[1]}</a>`).join("")}</nav>
  </div>`;
}
function render(html){ document.getElementById("app").innerHTML=html; window.scrollTo(0,0); }
function toggleTheme(){ state.settings.theme=state.settings.theme==="dark"?"light":"dark"; save(); route(); }

function dashboard(){
  const today=state.reviewLogs.filter(x=>x.reviewedAt.startsWith(todayKey()));
  const correct=today.filter(x=>x.isCorrect).length;
  const due=state.reviewStates.filter(r=>new Date(r.dueAt)<=new Date()&&!state.cards.find(c=>c.id===r.cardId)?.isSuspended).length;
  const pct=today.length?Math.round(correct/today.length*100):0;
  const goal=state.settings.dailyGoal; const progress=Math.min(100,Math.round(today.length/goal*100));
  const recent=[...state.reviewLogs].slice(-5).reverse();
  render(shell(`
    <div class="grid grid-4">
      <div class="card stat"><div class="label">今日待复习</div><div class="value">${due}</div><div class="hint">到期卡片</div></div>
      <div class="card stat"><div class="label">今日已完成</div><div class="value">${today.length}</div><div class="hint">目标 ${goal} 张</div></div>
      <div class="card stat"><div class="label">今日正确率</div><div class="value">${pct}%</div><div class="hint">按最终结果统计</div></div>
      <div class="card stat"><div class="label">词库总量</div><div class="value">${state.cards.length}</div><div class="hint">${state.decks.length} 个单词本</div></div>
    </div>
    <section class="card hero section"><div><h3>${due?"今天有 "+due+" 张卡片等待复习":"今天的复习已经清空"}</h3><p>一次只专注一道题。输入答案、立即反馈，再由系统自动安排下一次复习。</p><div class="hero-actions"><a class="btn btn-primary" href="#/practice?mode=review">开始复习</a><a class="btn btn-secondary" href="#/practice?mode=new">学习新词</a><a class="btn btn-ghost" href="#/cards">管理卡片</a></div></div><div class="hero-visual"><div class="ring" style="--progress:${progress}%"><div class="ring-inner"><div><strong>${progress}%</strong><span>今日目标</span></div></div></div></div></section>
    <section class="section"><div class="section-head"><h3>最近练习</h3><a class="btn btn-small btn-secondary" href="#/stats">查看统计</a></div>
      <div class="card list">${recent.length?recent.map(l=>{const c=state.cards.find(x=>x.id===l.cardId);return `<div class="list-row"><div><div class="title">${escapeHtml(c?.word||c?.targetEnglish||"已删除卡片")}</div><div class="meta">${escapeHtml(c?.sentenceZh||"")}</div></div><div><span class="badge ${l.isCorrect?"green":"red"}">${l.isCorrect?"正确":"错误"}</span></div><div class="meta">${Math.round(l.responseTimeMs/1000)} 秒</div><div class="meta">${formatDate(l.reviewedAt)}</div></div>`}).join(""):`<div class="empty">还没有练习记录，开始第一轮学习吧。</div>`}</div>
    </section>
  `,"学习首页","今日任务、学习进度与快速入口"));
}

let practiceSession=null;
function buildPracticeQueue(mode){
  let cards=state.cards.filter(c=>!c.isSuspended);
  if(mode==="new") cards=cards.filter(c=>getReview(c.id).status==="new");
  else if(mode==="review") cards=cards.filter(c=>new Date(getReview(c.id).dueAt)<=new Date());
  else cards=cards.sort(()=>Math.random()-.5);
  if(!cards.length && mode==="review") cards=state.cards.filter(c=>!c.isSuspended).sort(()=>Math.random()-.5).slice(0,20);
  return cards.sort(()=>Math.random()-.5).slice(0,Math.max(10,state.settings.dailyGoal));
}
function practice(){
  const params=new URLSearchParams((location.hash.split("?")[1]||"")); const mode=params.get("mode")||state.ui.lastPracticeMode||"review";
  if(!practiceSession||practiceSession.mode!==mode){
    practiceSession={mode,queue:buildPracticeQueue(mode),index:0,attempts:0,hintUsed:false,revealed:false,start:Date.now(),feedback:"",done:false,history:[]};
    state.ui.lastPracticeMode=mode; save();
  }
  const s=practiceSession; const card=s.queue[s.index];
  if(!card){ render(shell(`<div class="card empty"><h3>当前没有可练习的卡片</h3><p>可以先添加新卡片，或切换到混合练习。</p><a class="btn btn-primary" href="#/cards/new">添加卡片</a></div>`,"练习","主动回忆与即时反馈")); return; }
  const sentence=card.type==="cloze"?`${escapeHtml(card.clozePrefix)}<span class="blank">${s.revealed?escapeHtml(card.clozeAnswer):"________"}</span>${escapeHtml(card.clozeSuffix)}`:escapeHtml(card.sentenceZh);
  const kicker=card.type==="cloze"?"英语句子填词":"中文翻译成英文";
  const hint=s.hintUsed ? (card.type==="cloze"?`提示：${escapeHtml(card.clozeAnswer.slice(0,Math.max(1,Math.ceil(card.clozeAnswer.length/3))))}${"•".repeat(Math.max(0,card.clozeAnswer.length-Math.ceil(card.clozeAnswer.length/3)))}`:`提示：${escapeHtml((card.targetEnglish||"").split(" ").slice(0,3).join(" "))} …`) : "";
  const progress=Math.round((s.index)/s.queue.length*100);
  render(shell(`<div class="practice-wrap">
    <div class="practice-top"><span class="meta">${s.index+1} / ${s.queue.length}</span><div class="progress"><span style="width:${progress}%"></span></div><button class="btn btn-small btn-secondary" onclick="finishPractice()">结束</button></div>
    <div class="card practice-card">
      <div class="practice-kicker">${kicker}</div>
      ${card.type==="cloze"&&state.settings.showChineseHint?`<div class="prompt-cn">${escapeHtml(card.sentenceZh)}</div>`:""}
      <div class="sentence">${sentence}</div>
      <div class="answer-box"><input id="answerInput" class="input answer-input ${s.feedback==="success"?"correct":s.feedback==="wrong"?"wrong":""}" autocomplete="off" placeholder="${card.type==="cloze"?"输入缺失单词":"输入完整英文句子"}" value="${escapeHtml(s.currentInput||"")}" ${(s.revealed||s.feedback==="success")?"disabled":""}/></div>
      <div class="feedback ${s.feedback==="success"?"success":s.feedback==="wrong"?"error":""}">
        ${s.feedback==="success"?`<div class="full-sentence">${escapeHtml(card.sentenceEn||card.targetEnglish)}</div><div class="details">${escapeHtml(card.word||"")} ${escapeHtml(card.pronunciation||"")} · ${escapeHtml(card.partOfSpeech||"")} ${escapeHtml(card.meaningZh||"")}<br>${escapeHtml(card.sentenceZh||"")}</div>`:s.feedback==="wrong"?`<div>${escapeHtml(s.message||"答案不正确，请再试一次。")}</div>`:hint?`<div class="details">${hint}</div>`:""}
      </div>
      <div class="practice-actions">
        <button class="btn btn-primary" onclick="submitPractice()">提交答案</button>
        <button class="btn btn-secondary" onclick="useHint()">显示提示</button>
        <button class="btn btn-secondary" onclick="revealAnswer()">显示答案</button>
        <button class="btn btn-ghost" onclick="skipCard()">跳过</button>
        <button class="btn btn-ghost" onclick="speakCurrent()">🔊 发音</button>
      </div>
      <div class="shortcut">Enter 提交 · Tab 提示 · Ctrl + Enter 显示答案 · Esc 结束</div>
    </div>
  </div>`,"练习","一次只专注一道题"));
  const input=document.getElementById("answerInput"); if(input){ setTimeout(()=>input.focus(),30); input.addEventListener("keydown",e=>{ if(e.key==="Enter"&&!e.ctrlKey){e.preventDefault();submitPractice();} if(e.key==="Tab"){e.preventDefault();useHint();} if(e.key==="Enter"&&e.ctrlKey){e.preventDefault();revealAnswer();} if(e.key==="Escape"){finishPractice();} }); }
}
function currentCard(){ return practiceSession?.queue?.[practiceSession.index]; }
function submitPractice(){
  const s=practiceSession,c=currentCard(),input=document.getElementById("answerInput"); if(!c||!input||!input.value.trim()) return;
  s.attempts++; const response=Date.now()-s.start; const ev=evaluate(c,input.value);
  if(ev.correct){
    s.feedback="success"; const result=reviewResult({correct:true,attempts:s.attempts,hintUsed:s.hintUsed,revealed:s.revealed,responseTime:response});
    schedule(c.id,result,response); state.reviewLogs.push({id:uid(),cardId:c.id,mode:c.type,userAnswer:input.value,normalizedAnswer:normalizeAnswer(input.value),result,isCorrect:true,attemptCount:s.attempts,hintUsed:s.hintUsed,answerRevealed:s.revealed,responseTimeMs:response,reviewedAt:nowISO()}); save();
    practice();
    if(state.settings.autoPlayAudio) speak(c.sentenceEn||c.targetEnglish);
    if(state.settings.autoAdvance) setTimeout(nextCard,state.settings.autoAdvanceDelay);
  }else{
    s.currentInput=input.value; s.feedback="wrong"; s.message=ev.close?"非常接近，只差一个字符。请再检查一次。":"答案不正确，请再试一次。"; practice();
  }
}
function useHint(){ if(!practiceSession)return; const input=document.getElementById("answerInput"); if(input)practiceSession.currentInput=input.value; practiceSession.hintUsed=true; practice(); }
function revealAnswer(){
  const s=practiceSession,c=currentCard(); if(!s||!c||s.revealed)return; s.revealed=true; s.feedback="wrong"; s.message=`正确答案：${c.type==="cloze"?c.clozeAnswer:c.targetEnglish}`; const response=Date.now()-s.start;
  schedule(c.id,"again",response); state.reviewLogs.push({id:uid(),cardId:c.id,mode:c.type,userAnswer:"",normalizedAnswer:"",result:"again",isCorrect:false,attemptCount:s.attempts,hintUsed:s.hintUsed,answerRevealed:true,responseTimeMs:response,reviewedAt:nowISO()}); save(); practice();
}
function skipCard(){
  const s=practiceSession,c=currentCard(); if(!s||!c)return; if(s.revealed){ nextCard(); return; } const response=Date.now()-s.start; schedule(c.id,"again",response);
  state.reviewLogs.push({id:uid(),cardId:c.id,mode:c.type,userAnswer:"",normalizedAnswer:"",result:"again",isCorrect:false,attemptCount:s.attempts,hintUsed:s.hintUsed,answerRevealed:false,responseTimeMs:response,reviewedAt:nowISO()}); save(); nextCard();
}
function nextCard(){ const s=practiceSession;if(!s)return; s.index++;s.attempts=0;s.hintUsed=false;s.revealed=false;s.feedback="";s.message="";s.currentInput="";s.start=Date.now(); if(s.index>=s.queue.length){finishPractice(true);} else practice(); }
function finishPractice(done=false){ practiceSession=null; location.hash=done?"#/stats":"#/dashboard"; }
function speakCurrent(){ const c=currentCard(); if(c)speak(c.sentenceEn||c.targetEnglish||c.clozeAnswer); }

function decks(){
  const rows=state.decks.map(d=>{const cards=state.cards.filter(c=>c.deckId===d.id);const mastered=cards.filter(c=>getReview(c.id).status==="mastered").length;return `<div class="list-row"><div><div class="title">${escapeHtml(d.name)}</div><div class="meta">${escapeHtml(d.description||"")}</div></div><div class="meta">${cards.length} 张卡片</div><div class="meta">已掌握 ${mastered}</div><div class="actions"><button class="btn btn-small btn-secondary" onclick="editDeck('${d.id}')">编辑</button><button class="btn btn-small btn-ghost" onclick="deleteDeck('${d.id}')">删除</button></div></div>`}).join("");
  render(shell(`<div class="section-head"><h3>全部单词本</h3><button class="btn btn-primary" onclick="editDeck()">＋ 新建单词本</button></div><div class="card list">${rows||`<div class="empty">还没有单词本。</div>`}</div>`,"单词本","按主题管理你的学习内容"));
}
function editDeck(id){
  const d=id?state.decks.find(x=>x.id===id):{name:"",description:""}; modal(`<h3>${id?"编辑":"新建"}单词本</h3><div class="field"><label>名称</label><input id="deckName" class="input" value="${escapeHtml(d.name)}"></div><div class="field" style="margin-top:14px"><label>说明</label><textarea id="deckDesc" class="textarea">${escapeHtml(d.description||"")}</textarea></div><div class="modal-actions"><button class="btn btn-secondary" onclick="closeModal()">取消</button><button class="btn btn-primary" onclick="saveDeck('${id||""}')">保存</button></div>`);
}
function saveDeck(id){ const name=document.getElementById("deckName").value.trim(); if(!name)return toast("请输入单词本名称"); const desc=document.getElementById("deckDesc").value.trim(); if(id){const d=getDeck(id);d.name=name;d.description=desc;d.updatedAt=nowISO();}else state.decks.push({id:uid(),name,description:desc,color:"#6d5dfc",createdAt:nowISO(),updatedAt:nowISO()}); save();closeModal();decks(); }
function deleteDeck(id){ const count=state.cards.filter(c=>c.deckId===id).length; if(count)return toast("该单词本仍有卡片，请先移动或删除卡片"); if(confirm("确定删除这个单词本吗？")){state.decks=state.decks.filter(d=>d.id!==id);save();decks();} }

function cards(){
  const q=(window.cardSearch||"").toLowerCase(), deckFilter=window.cardDeck||"", typeFilter=window.cardType||"";
  let rows=state.cards.filter(c=>(!q||[c.word,c.sentenceEn,c.sentenceZh,c.meaningZh].join(" ").toLowerCase().includes(q))&&(!deckFilter||c.deckId===deckFilter)&&(!typeFilter||c.type===typeFilter));
  render(shell(`<div class="toolbar"><input class="input search" placeholder="搜索单词、句子或释义" value="${escapeHtml(window.cardSearch||"")}" oninput="window.cardSearch=this.value;cards()"><select class="select" style="width:auto" onchange="window.cardDeck=this.value;cards()"><option value="">全部单词本</option>${state.decks.map(d=>`<option value="${d.id}" ${deckFilter===d.id?"selected":""}>${escapeHtml(d.name)}</option>`).join("")}</select><select class="select" style="width:auto" onchange="window.cardType=this.value;cards()"><option value="">全部类型</option><option value="cloze" ${typeFilter==="cloze"?"selected":""}>填词</option><option value="translation" ${typeFilter==="translation"?"selected":""}>翻译</option></select><a class="btn btn-primary" href="#/cards/new">＋ 添加卡片</a></div>
    <div class="card table-wrap"><table class="table"><thead><tr><th>单词 / 表达</th><th>例句</th><th>单词本</th><th>状态</th><th>操作</th></tr></thead><tbody>${rows.map(c=>`<tr><td><strong>${escapeHtml(c.word||c.clozeAnswer||"翻译卡")}</strong><div class="meta">${escapeHtml(c.meaningZh||"")}</div></td><td>${escapeHtml(c.sentenceEn||c.targetEnglish||"")}<div class="meta">${escapeHtml(c.sentenceZh||"")}</div></td><td>${escapeHtml(getDeck(c.deckId)?.name||"")}</td><td><span class="badge ${c.isSuspended?"red":getReview(c.id).status==="mastered"?"green":""}">${c.isSuspended?"已暂停":getReview(c.id).status}</span></td><td><div class="actions"><a class="btn btn-small btn-secondary" href="#/cards/edit/${c.id}">编辑</a><button class="btn btn-small btn-ghost" onclick="toggleSuspend('${c.id}')">${c.isSuspended?"恢复":"暂停"}</button><button class="btn btn-small btn-ghost" onclick="deleteCard('${c.id}')">删除</button></div></td></tr>`).join("")}</tbody></table>${rows.length?"":`<div class="empty">没有匹配的卡片。</div>`}</div>`,"卡片管理","搜索、编辑、暂停或删除学习卡片"));
}
function toggleSuspend(id){const c=state.cards.find(x=>x.id===id);c.isSuspended=!c.isSuspended;c.updatedAt=nowISO();save();cards();}
function deleteCard(id){if(confirm("确定删除这张卡片吗？")){state.cards=state.cards.filter(c=>c.id!==id);state.reviewStates=state.reviewStates.filter(r=>r.cardId!==id);state.reviewLogs=state.reviewLogs.filter(l=>l.cardId!==id);save();cards();}}

function cardForm(id){
  const c=id?state.cards.find(x=>x.id===id):{type:"cloze",deckId:state.decks[0]?.id||"",word:"",pronunciation:"",partOfSpeech:"",meaningZh:"",sentenceEn:"",sentenceZh:"",clozePrefix:"",clozeAnswer:"",clozeSuffix:"",targetEnglish:"",acceptedAnswers:[],tags:[],source:"",difficulty:1,isSuspended:false};
  if(!c){location.hash="#/cards";return;}
  render(shell(`<div class="card form-card"><form onsubmit="saveCard(event,'${id||""}')"><div class="form-grid">
    <div class="field"><label>卡片类型</label><select id="type" class="select" ><option value="cloze" ${c.type==="cloze"?"selected":""}>英语句子填词</option><option value="translation" ${c.type==="translation"?"selected":""}>中文翻译成英文</option></select></div>
    <div class="field"><label>所属单词本</label><select id="deckId" class="select">${state.decks.map(d=>`<option value="${d.id}" ${c.deckId===d.id?"selected":""}>${escapeHtml(d.name)}</option>`).join("")}</select></div>
    <div class="field"><label>单词 / 表达</label><input id="word" class="input" value="${escapeHtml(c.word||"")}"></div>
    <div class="field"><label>中文释义</label><input id="meaningZh" class="input" value="${escapeHtml(c.meaningZh||"")}"></div>
    <div class="field"><label>音标</label><input id="pronunciation" class="input" value="${escapeHtml(c.pronunciation||"")}"></div>
    <div class="field"><label>词性</label><input id="partOfSpeech" class="input" value="${escapeHtml(c.partOfSpeech||"")}"></div>
    <div class="field full"><label>英文完整句子</label><textarea id="sentenceEn" class="textarea" rows="3">${escapeHtml(c.sentenceEn||c.targetEnglish||"")}</textarea></div>
    <div class="field full"><label>中文翻译 / 中文题目</label><textarea id="sentenceZh" class="textarea" rows="2">${escapeHtml(c.sentenceZh||"")}</textarea></div>
    <div class="field full"><label>填空前部分</label><input id="clozePrefix" class="input" value="${escapeHtml(c.clozePrefix||"")}"><small>填词卡使用；例如 “I usually ”</small></div>
    <div class="field"><label>正确填词答案</label><input id="clozeAnswer" class="input" value="${escapeHtml(c.clozeAnswer||"")}"></div>
    <div class="field"><label>填空后部分</label><input id="clozeSuffix" class="input" value="${escapeHtml(c.clozeSuffix||"")}"></div>
    <div class="field full"><label>标准英文答案</label><textarea id="targetEnglish" class="textarea" rows="2">${escapeHtml(c.targetEnglish||"")}</textarea><small>翻译卡使用</small></div>
    <div class="field full"><label>可接受答案</label><textarea id="acceptedAnswers" class="textarea" rows="3">${escapeHtml((c.acceptedAnswers||[]).join("\n"))}</textarea><small>每行一个答案</small></div>
    <div class="field"><label>标签</label><input id="tags" class="input" value="${escapeHtml((c.tags||[]).join(", "))}"><small>使用逗号分隔</small></div>
    <div class="field"><label>来源</label><input id="source" class="input" value="${escapeHtml(c.source||"")}"></div>
    <div class="field full"><div class="actions"><button class="btn btn-primary" type="submit">保存卡片</button><a class="btn btn-secondary" href="#/cards">取消</a></div></div>
  </div></form></div>`, id ? "编辑卡片" : "添加卡片", "创建填词卡片或中译英卡片"));
}
function saveCard(e,id){e.preventDefault(); const val=x=>document.getElementById(x).value.trim(); const type=val("type");
  const obj={id:id||uid(),deckId:val("deckId"),type,word:val("word"),pronunciation:val("pronunciation"),partOfSpeech:val("partOfSpeech"),meaningZh:val("meaningZh"),sentenceEn:val("sentenceEn"),sentenceZh:val("sentenceZh"),clozePrefix:val("clozePrefix"),clozeAnswer:val("clozeAnswer"),clozeSuffix:val("clozeSuffix"),targetEnglish:val("targetEnglish"),acceptedAnswers:val("acceptedAnswers").split("\n").map(x=>x.trim()).filter(Boolean),tags:val("tags").split(/[,，]/).map(x=>x.trim()).filter(Boolean),difficulty:1,source:val("source"),isSuspended:false,createdAt:id?state.cards.find(x=>x.id===id).createdAt:nowISO(),updatedAt:nowISO()};
  if(type==="cloze"&&!obj.clozeAnswer)return toast("填词卡必须填写正确答案"); if(type==="translation"&&!obj.targetEnglish)return toast("翻译卡必须填写标准英文答案");
  if(!obj.acceptedAnswers.length)obj.acceptedAnswers=[type==="cloze"?obj.clozeAnswer:obj.targetEnglish];
  if(id){const i=state.cards.findIndex(x=>x.id===id);obj.isSuspended=state.cards[i].isSuspended;state.cards[i]=obj;}else{state.cards.push(obj);getReview(obj.id);}
  save();location.hash="#/cards";toast("卡片已保存");
}

function stats(){
  const last7=Array.from({length:7},(_,i)=>{const d=new Date();d.setDate(d.getDate()-(6-i));return todayKey(d)});
  const daily=last7.map(k=>{const logs=state.reviewLogs.filter(l=>l.reviewedAt.startsWith(k));return {k,count:logs.length,acc:logs.length?Math.round(logs.filter(l=>l.isCorrect).length/logs.length*100):0};});
  const max=Math.max(1,...daily.map(x=>x.count));
  const groups=["new","learning","review","mastered"].map(s=>({s,n:state.reviewStates.filter(r=>r.status===s).length}));
  const errorMap={}; state.reviewLogs.filter(l=>!l.isCorrect).forEach(l=>errorMap[l.cardId]=(errorMap[l.cardId]||0)+1);
  const errors=Object.entries(errorMap).sort((a,b)=>b[1]-a[1]).slice(0,10);
  const avg=state.reviewLogs.length?Math.round(state.reviewLogs.reduce((a,b)=>a+b.responseTimeMs,0)/state.reviewLogs.length/1000):0;
  render(shell(`<div class="grid grid-4">${groups.map(g=>`<div class="card stat"><div class="label">${g.s}</div><div class="value">${g.n}</div><div class="hint">卡片状态</div></div>`).join("")}</div>
    <div class="grid grid-2 section"><div class="card chart"><div class="section-head"><h3>最近 7 天学习量</h3><span class="meta">平均回答 ${avg} 秒</span></div><div class="bars">${daily.map(d=>`<div class="bar-col"><div class="bar" style="height:${Math.max(4,d.count/max*140)}px" title="${d.count} 张"></div><div class="bar-label">${d.k.slice(5)}<br>${d.count}</div></div>`).join("")}</div></div>
    <div class="card chart"><div class="section-head"><h3>最近 7 天正确率</h3></div><div class="bars">${daily.map(d=>`<div class="bar-col"><div class="bar" style="height:${Math.max(4,d.acc/100*140)}px" title="${d.acc}%"></div><div class="bar-label">${d.k.slice(5)}<br>${d.acc}%</div></div>`).join("")}</div></div></div>
    <section class="section"><div class="section-head"><h3>最常出错的卡片</h3></div><div class="card list">${errors.length?errors.map(([id,n])=>{const c=state.cards.find(x=>x.id===id);return `<div class="list-row"><div><div class="title">${escapeHtml(c?.word||c?.targetEnglish||"已删除卡片")}</div><div class="meta">${escapeHtml(c?.sentenceEn||"")}</div></div><div><span class="badge red">${n} 次</span></div><div class="meta">${escapeHtml(getDeck(c?.deckId)?.name||"")}</div><div></div></div>`}).join(""):`<div class="empty">暂无错题记录。</div>`}</div></section>`,"学习统计","基于真实练习记录生成"));
}

function importExport(){
  render(shell(`<div class="grid grid-2">
    <div class="card form-card"><h3>备份与恢复</h3><p class="meta">导出全部单词本、卡片、复习状态、设置和练习记录。</p><div class="actions"><button class="btn btn-primary" onclick="exportJSON()">导出 JSON</button><button class="btn btn-secondary" onclick="chooseFile('json')">导入 JSON</button></div></div>
    <div class="card form-card"><h3>CSV 批量导入</h3><p class="meta">适合从 Excel 批量整理词库。</p><div class="actions"><button class="btn btn-primary" onclick="chooseFile('csv')">导入 CSV</button><button class="btn btn-secondary" onclick="downloadCSVTemplate()">下载模板</button></div></div>
  </div>
  <section class="section"><div class="card form-card"><h3>CSV 字段说明</h3><div class="code-note">deck,type,word,pronunciation,partOfSpeech,meaningZh,sentenceEn,sentenceZh,clozePrefix,clozeAnswer,clozeSuffix,targetEnglish,acceptedAnswers,tags,source</div><p class="meta">acceptedAnswers 和 tags 使用 | 分隔；type 只能填写 cloze 或 translation。</p></div></section>
  <section class="section"><div class="card form-card"><h3>本地数据安全</h3><p class="meta">当前数据保存在浏览器 localStorage 中。清理浏览器数据或更换浏览器后，本地记录可能丢失，请定期导出 JSON。</p></div></section>`,"导入导出","备份、恢复和批量导入词库"));
}
function exportJSON(){download(`wordloop-backup-${todayKey()}.json`,JSON.stringify(state,null,2));toast("备份已导出");}
function chooseFile(type){const input=document.getElementById("fileInput");input.accept=type==="json"?".json":".csv";input.value="";input.onchange=e=>handleFile(e.target.files[0],type);input.click();}
function handleFile(file,type){if(!file)return;const reader=new FileReader();reader.onload=()=>{try{if(type==="json"){const data=JSON.parse(reader.result);if(!data.cards||!data.decks)throw new Error("文件结构不正确");state=data;save();route();toast("JSON 数据已恢复");}else importCSV(reader.result);}catch(e){alert("导入失败："+e.message)}};reader.readAsText(file,"UTF-8");}
function csvParse(text){
  const rows=[];let row=[],cell="",quote=false;
  for(let i=0;i<text.length;i++){const ch=text[i];if(ch==='"'){if(quote&&text[i+1]==='"'){cell+='"';i++;}else quote=!quote;}else if(ch===","&&!quote){row.push(cell);cell="";}else if((ch==="\n"||ch==="\r")&&!quote){if(ch==="\r"&&text[i+1]==="\n")i++;row.push(cell);if(row.some(x=>x.trim()!==""))rows.push(row);row=[];cell="";}else cell+=ch;}
  row.push(cell);if(row.some(x=>x.trim()!==""))rows.push(row);return rows;
}
function importCSV(text){
  const rows=csvParse(text);if(rows.length<2)throw new Error("CSV 没有数据");
  const headers=rows[0].map(x=>x.trim());let imported=0,errors=[];
  rows.slice(1).forEach((r,idx)=>{const o={};headers.forEach((h,i)=>o[h]=(r[i]||"").trim());if(!["cloze","translation"].includes(o.type)){errors.push(`第 ${idx+2} 行 type 错误`);return;}
    let deck=state.decks.find(d=>d.name===o.deck);if(!deck){deck={id:uid(),name:o.deck||"导入词库",description:"CSV 导入",color:"#6d5dfc",createdAt:nowISO(),updatedAt:nowISO()};state.decks.push(deck);}
    const c={id:uid(),deckId:deck.id,type:o.type,word:o.word||"",pronunciation:o.pronunciation||"",partOfSpeech:o.partOfSpeech||"",meaningZh:o.meaningZh||"",sentenceEn:o.sentenceEn||o.targetEnglish||"",sentenceZh:o.sentenceZh||"",clozePrefix:o.clozePrefix||"",clozeAnswer:o.clozeAnswer||"",clozeSuffix:o.clozeSuffix||"",targetEnglish:o.targetEnglish||"",acceptedAnswers:(o.acceptedAnswers||"").split("|").map(x=>x.trim()).filter(Boolean),tags:(o.tags||"").split("|").map(x=>x.trim()).filter(Boolean),difficulty:1,source:o.source||"CSV 导入",isSuspended:false,createdAt:nowISO(),updatedAt:nowISO()};
    if(c.type==="cloze"&&!c.clozeAnswer){errors.push(`第 ${idx+2} 行缺少 clozeAnswer`);return;}if(c.type==="translation"&&!c.targetEnglish){errors.push(`第 ${idx+2} 行缺少 targetEnglish`);return;}if(!c.acceptedAnswers.length)c.acceptedAnswers=[c.type==="cloze"?c.clozeAnswer:c.targetEnglish];state.cards.push(c);getReview(c.id);imported++;
  });
  save();route();toast(`已导入 ${imported} 张卡片${errors.length?`，${errors.length} 行有错误`:""}`);if(errors.length)alert(errors.slice(0,20).join("\n"));
}
function downloadCSVTemplate(){
  const h="deck,type,word,pronunciation,partOfSpeech,meaningZh,sentenceEn,sentenceZh,clozePrefix,clozeAnswer,clozeSuffix,targetEnglish,acceptedAnswers,tags,source\n";
  const r='示例词库,cloze,commute,/kəˈmjuːt/,v.,通勤,I usually commute to work by subway.,我通常乘地铁通勤上班。,I usually ,commute, to work by subway.,,commute,日常|交通,手工整理\n';
  download("wordloop-import-template.csv","\ufeff"+h+r,"text/csv;charset=utf-8");toast("CSV 模板已下载");
}

function settings(){
  const s=state.settings;
  render(shell(`<div class="card">
    <div class="setting-row"><div><strong>每日目标</strong><div class="desc">每天计划完成的卡片数量</div></div><input class="input" style="width:100px" type="number" min="1" max="500" value="${s.dailyGoal}" onchange="setSetting('dailyGoal',Number(this.value))"></div>
    <div class="setting-row"><div><strong>自动进入下一题</strong><div class="desc">回答正确后自动切换</div></div><label class="switch"><input type="checkbox" ${s.autoAdvance?"checked":""} onchange="setSetting('autoAdvance',this.checked)"><span class="slider"></span></label></div>
    <div class="setting-row"><div><strong>自动切题延迟</strong><div class="desc">单位：毫秒</div></div><input class="input" style="width:120px" type="number" min="0" max="5000" step="100" value="${s.autoAdvanceDelay}" onchange="setSetting('autoAdvanceDelay',Number(this.value))"></div>
    <div class="setting-row"><div><strong>显示中文提示</strong><div class="desc">填词模式显示中文句意</div></div><label class="switch"><input type="checkbox" ${s.showChineseHint?"checked":""} onchange="setSetting('showChineseHint',this.checked)"><span class="slider"></span></label></div>
    <div class="setting-row"><div><strong>忽略大小写</strong><div class="desc">Hello 与 hello 视为相同</div></div><label class="switch"><input type="checkbox" ${s.ignoreCase?"checked":""} onchange="setSetting('ignoreCase',this.checked)"><span class="slider"></span></label></div>
    <div class="setting-row"><div><strong>忽略句末标点</strong><div class="desc">句号、问号和感叹号不影响判定</div></div><label class="switch"><input type="checkbox" ${s.ignoreEndingPunctuation?"checked":""} onchange="setSetting('ignoreEndingPunctuation',this.checked)"><span class="slider"></span></label></div>
    <div class="setting-row"><div><strong>合并连续空格</strong><div class="desc">多个空格按一个空格处理</div></div><label class="switch"><input type="checkbox" ${s.collapseWhitespace?"checked":""} onchange="setSetting('collapseWhitespace',this.checked)"><span class="slider"></span></label></div>
    <div class="setting-row"><div><strong>正确后自动朗读</strong><div class="desc">使用浏览器原生语音功能</div></div><label class="switch"><input type="checkbox" ${s.autoPlayAudio?"checked":""} onchange="setSetting('autoPlayAudio',this.checked)"><span class="slider"></span></label></div>
  </div>
  <section class="section"><div class="card form-card"><h3>危险操作</h3><p class="meta">将删除当前浏览器中的全部学习记录，并恢复示例词库。</p><button class="btn btn-danger" onclick="if(confirm('确定清空全部数据吗？'))resetData()">清空并恢复示例数据</button></div></section>`,"设置","调整练习判定、节奏和界面"));
}
function setSetting(k,v){state.settings[k]=v;save();toast("设置已保存");}

function modal(html){const el=document.createElement("div");el.id="modal";el.className="modal-backdrop";el.innerHTML=`<div class="modal">${html}</div>`;el.addEventListener("click",e=>{if(e.target===el)closeModal()});document.body.appendChild(el);}
function closeModal(){document.getElementById("modal")?.remove();}

function route(){
  const path=(location.hash||"#/dashboard").slice(1).split("?")[0];
  if(path==="/dashboard"||path==="/") dashboard();
  else if(path==="/practice") practice();
  else if(path==="/decks") decks();
  else if(path==="/cards") cards();
  else if(path==="/cards/new") cardForm();
  else if(path.startsWith("/cards/edit/")) cardForm(path.split("/").pop());
  else if(path==="/stats") stats();
  else if(path==="/settings") settings();
  else if(path==="/import") importExport();
  else dashboard();
}
window.addEventListener("hashchange",route);
window.addEventListener("DOMContentLoaded",()=>{save();route();});
