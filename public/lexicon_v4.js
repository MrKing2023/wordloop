/* WordLoop v4.1: multi-library switching, CET-6 base lexicon and curated 100 cards */
(function(){
  "use strict";

  icons.libraries = "◫";

  const VERSION = "4.1.1";
  const LIBRARY_NAMES = {"core-200":"核心 200", cet6:"CET-6 精选 100"};
  const FALLBACK_LIBRARY_MANIFEST = {
    schemaVersion: 2,
    productVersion: VERSION,
    libraries: [
      {id:"core-200",name:"WordLoop 核心 200 词",shortName:"核心 200",status:"ready",baseEntryCount:200,cardCount:200,level:"基础—进阶",description:"原有 200 张学习卡，支持填空、整句翻译和详细解析。",source:"WordLoop 自建学习卡",licenseNote:"项目自建内容。",features:["句子填空","整句翻译","逐级提示","详细解析"],accent:"violet"},
      {id:"cet6",name:"CET-6 基础词库与精选学习卡",shortName:"CET-6",status:"ready",baseEntryCount:5407,cardCount:100,level:"大学英语六级",description:"已完成 ECDICT cet6 标签全量基础词库，并发布首批 100 张增强学习卡。",source:"ECDICT 基础字段 + WordLoop 原创学习内容",licenseNote:"ECDICT 使用 MIT License；本项目不宣称该集合是唯一或官方考试词表。",features:["5407 基础词条","100 张增强卡","音标与释义","搭配与例句"],accent:"blue"},
      {id:"kaoyan",name:"考研英语词库",shortName:"考研英语",status:"planned",baseEntryCount:null,cardCount:null,level:"考研英语",description:"突出熟词僻义、阅读搭配和长难句语境。",source:"考试标签词表 + 词典数据 + 原创学习内容",licenseNote:"来源与生成版本分别记录。",features:["熟词僻义","长难句语境","阅读搭配","整句输出"],accent:"amber"},
      {id:"ielts",name:"IELTS 主题词汇",shortName:"IELTS",status:"planned",baseEntryCount:null,cardCount:null,level:"IELTS",description:"按写作、听力、口语主题和同义改写拆分。",source:"开放词典 + 主题语料 + 原创学习内容",licenseNote:"不宣称官方完整词表。",features:["主题分类","常见搭配","同义改写","写作表达"],accent:"green"}
    ]
  };

  let libraryManifestCache = null;
  let libraryManifestPromise = null;
  let cet6CardsPromise = null;
  let cet6LexiconPromise = null;
  let lexiconView = {query:"", page:1, pageSize:50};

  function clone(value){ return JSON.parse(JSON.stringify(value)); }
  function cardLibraryId(card){ return card?.libraryId || (String(card?.id||"").startsWith("cet6-") ? "cet6" : "core-200"); }
  function activeLibraryId(){ return state.libraryCenter?.activeLibraryId || "core-200"; }
  function cardsInLibrary(id=activeLibraryId()){ return state.cards.filter(card => !card.isSuspended && cardLibraryId(card) === id); }
  function libraryPlanName(id){ return id === "cet6" ? "CET-6 精选 100" : "核心英语 200 词"; }

  function ensureLibraryState(){
    state.ui = state.ui || {};
    state.cards = state.cards || [];
    state.decks = state.decks || [];
    state.reviewStates = state.reviewStates || [];
    state.cards.forEach(card => { if(!card.libraryId) card.libraryId = cardLibraryId(card); });
    state.decks.forEach(deck => {
      if(!deck.libraryId){
        const deckCards=state.cards.filter(card=>card.deckId===deck.id);
        deck.libraryId=deckCards.some(card=>cardLibraryId(card)==="cet6")?"cet6":"core-200";
      }
    });
    state.libraryCenter = state.libraryCenter || {};
    state.libraryCenter.version = 2;
    state.libraryCenter.activeLibraryId = state.libraryCenter.activeLibraryId || "core-200";
    state.libraryCenter.lastViewedLibraryId = state.libraryCenter.lastViewedLibraryId || state.libraryCenter.activeLibraryId;
    state.libraryCenter.createdAt = state.libraryCenter.createdAt || nowISO();
    state.libraryCenter.updatedAt = nowISO();
    state.libraryPlans = state.libraryPlans || {};
    if(state.studyPlan && !state.libraryPlans[state.libraryCenter.activeLibraryId]){
      state.libraryPlans[state.libraryCenter.activeLibraryId] = state.studyPlan;
    }
    state.version = Math.max(4.1, Number(state.version || 0));
    save();
  }
  ensureLibraryState();

  async function loadJSON(path, label){
    const flatName=String(path||"").split("/").pop();
    const candidates=[path];
    if(flatName && flatName!==path)candidates.push(flatName);
    let lastError=null;
    for(const candidate of candidates){
      try{
        const url=new URL(candidate,document.baseURI).href;
        const response=await fetch(url,{cache:"no-store"});
        if(!response.ok){
          lastError=new Error(`${label}加载失败：${response.status}（${candidate}）`);
          continue;
        }
        return await response.json();
      }catch(error){
        lastError=error;
      }
    }
    throw lastError||new Error(`${label}加载失败`);
  }
  function loadLibraryManifest(){
    if(libraryManifestCache) return Promise.resolve(libraryManifestCache);
    if(libraryManifestPromise) return libraryManifestPromise;
    libraryManifestPromise=loadJSON("data/library_manifest.json","词库清单")
      .then(data=>{
        if(!data||!Array.isArray(data.libraries)) throw new Error("词库清单格式不正确");
        libraryManifestCache=data;return data;
      })
      .catch(error=>{console.warn("Using fallback library manifest",error);libraryManifestCache=FALLBACK_LIBRARY_MANIFEST;return FALLBACK_LIBRARY_MANIFEST;})
      .finally(()=>{libraryManifestPromise=null;});
    return libraryManifestPromise;
  }
  function loadCet6Cards(){
    if(!cet6CardsPromise)cet6CardsPromise=loadJSON("data/cet6/cet6_cards_100.json","CET-6 学习卡")
      .then(data=>{if(!Array.isArray(data.cards)||data.cards.length!==100)throw new Error("CET-6 学习卡数量或格式不正确");return data;})
      .catch(error=>{cet6CardsPromise=null;throw error;});
    return cet6CardsPromise;
  }
  function loadCet6Lexicon(){
    if(!cet6LexiconPromise)cet6LexiconPromise=loadJSON("data/cet6/cet6_lexicon.json","CET-6 基础词库")
      .then(data=>{if(!Array.isArray(data.entries)||!data.entries.length)throw new Error("CET-6 基础词库格式不正确");return data;})
      .catch(error=>{cet6LexiconPromise=null;throw error;});
    return cet6LexiconPromise;
  }

  function statusText(status){
    if(status === "ready") return "可学习";
    if(status === "building") return "建设中";
    return "规划中";
  }
  function statusClass(status){ return status === "ready" ? "green" : status === "building" ? "amber" : ""; }
  function countText(item){
    const base=Number.isFinite(item.baseEntryCount)?`${item.baseEntryCount} 基础词条`:"基础词条待整理";
    const cards=Number.isFinite(item.cardCount)?`${item.cardCount} 学习卡`:"学习卡待生成";
    return `${base} · ${cards}`;
  }
  function renderLibraryCard(item){
    const active=activeLibraryId()===item.id;
    const action=item.status==="ready"?`<a class="btn btn-primary" href="#/library/${escapeHtml(item.id)}">查看词库</a>`:`<a class="btn btn-secondary" href="#/library/${escapeHtml(item.id)}">查看计划</a>`;
    return `<article class="library-card card accent-${escapeHtml(item.accent||"violet")} ${active?"active-library":""}">
      <div class="library-card-head"><div><span class="library-kicker">${escapeHtml(item.level||"词库")}</span><h3>${escapeHtml(item.name)}</h3></div><span class="badge ${statusClass(item.status)}">${statusText(item.status)}</span></div>
      <p>${escapeHtml(item.description||"")}</p>
      <div class="library-meta"><span>${escapeHtml(countText(item))}</span>${active?`<strong>当前学习词库</strong>`:""}</div>
      <div class="library-tags">${(item.features||[]).map(x=>`<span>${escapeHtml(x)}</span>`).join("")}</div>
      <div class="library-card-actions">${action}</div>
    </article>`;
  }

  function librariesPage(){
    render(shell(`<section class="library-hero card"><div><span class="hero-badge">WORDLOOP v4.1</span><h3>完整基础词库已经接入，首批高质量学习卡可以直接练习。</h3><p>CET-6 基础层收录 ECDICT 中全部 5407 个 cet6 标签词条；学习层先发布 100 张经过结构化生成和自动校验的增强卡。两个层次分开维护，既能浏览完整词典，又不会把未经审核的内容直接变成练习题。</p><div class="hero-actions"><a class="btn btn-primary" href="#/library/cet6">进入 CET-6</a><a class="btn btn-secondary" href="#/library/core-200">核心 200</a></div></div><div class="library-pipeline-mini"><span>5407 基础词条</span><i>→</i><span>词义与音标</span><i>→</i><span>100 增强卡</span><i>→</i><span>规则质检</span></div></section>
      <section class="section"><div class="section-head"><div><h3>词库目录</h3><p class="meta">不同词库分别保存学习计划，切换后不会混入其他词库。</p></div></div><div id="libraryGrid" class="library-grid"><div class="card empty">正在加载词库清单……</div></div></section>
      <section class="section"><div class="card lexicon-note"><div><h3>“完整词库”与“学习卡”有什么区别？</h3><p>完整基础词库用于查词、筛选和后续生成；只有经过例句、翻译、搭配及填空校验的内容才进入学习计划。当前 CET-6 已有 100 张可直接学习的增强卡。</p></div><a class="btn btn-secondary" href="#/library/cet6/lexicon">浏览 5407 词条</a></div></section>`,"词库中心",`当前：${LIBRARY_NAMES[activeLibraryId()]||activeLibraryId()}`));
    loadLibraryManifest().then(manifest=>{
      if((location.hash||"").split("?")[0]!=="#/libraries")return;
      const grid=document.getElementById("libraryGrid");if(grid)grid.innerHTML=manifest.libraries.map(renderLibraryCard).join("");
    });
  }

  function activeLibraryStats(id){
    const cards=cardsInLibrary(id);
    const mastered=cards.filter(c=>getReview(c.id).status==="mastered").length;
    const due=cards.filter(c=>getReview(c.id).status!=="new"&&new Date(getReview(c.id).dueAt)<=new Date()).length;
    return {cards:cards.length,mastered,due};
  }

  function libraryDetail(id){
    render(shell(`<div class="card empty">正在加载词库信息……</div>`,"词库详情","来源、内容与学习入口"));
    loadLibraryManifest().then(manifest=>{
      const item=manifest.libraries.find(x=>x.id===id);
      if(!item){render(shell(`<div class="card empty"><h3>没有找到这个词库</h3><a class="btn btn-primary" href="#/libraries">返回词库中心</a></div>`,"词库详情","未知词库"));return;}
      state.libraryCenter.lastViewedLibraryId=item.id;state.libraryCenter.updatedAt=nowISO();save();
      const active=activeLibraryId()===item.id;
      const stats=activeLibraryStats(item.id);
      const ready=item.status==="ready";
      let actions="";
      if(ready){
        actions+=active?`<a class="btn btn-primary" href="#/plan">进入学习计划</a>`:`<button class="btn btn-primary" onclick="activateLibrary('${escapeHtml(item.id)}')">启用这个词库</button>`;
        if(item.id==="cet6")actions+=`<a class="btn btn-secondary" href="#/library/cet6/lexicon">浏览 5407 基础词条</a>`;
        actions+=`<a class="btn btn-secondary" href="#/cards">查看已加载卡片</a>`;
      }else actions=`<a class="btn btn-primary" href="#/libraries">返回词库目录</a>`;
      const baseCount=Number.isFinite(item.baseEntryCount)?item.baseEntryCount:"—";
      const cardCount=Number.isFinite(item.cardCount)?item.cardCount:"—";
      const statsHtml=ready?`<div class="grid grid-4 section"><div class="card stat"><div class="label">基础词条</div><div class="value">${baseCount}</div></div><div class="card stat"><div class="label">增强学习卡</div><div class="value">${cardCount}</div></div><div class="card stat"><div class="label">已加载到本机</div><div class="value">${stats.cards}</div></div><div class="card stat"><div class="label">当前状态</div><div class="value stat-word">${active?"正在学习":"可切换"}</div></div></div>`:"";
      const cet6Info=item.id==="cet6"?`<section class="section"><div class="card pipeline-card"><div class="section-head"><div><h3>CET-6 本次发布</h3><p class="meta">基础层与学习层分开，防止低质量例句直接进入练习。</p></div></div><div class="release-grid"><div><strong>5407</strong><span>ECDICT cet6 标签全量词条</span></div><div><strong>100</strong><span>原创增强学习卡</span></div><div><strong>100%</strong><span>答案位置与字段规则校验</span></div></div><ul class="release-list"><li>每张增强卡包含英文语境、准确中文翻译、用法提醒、常见搭配、相关表达、词族和扩展例句。</li><li>填空答案必须在英文句中恰好出现一次，并可完整还原原句。</li><li>5407 是 ECDICT 数据中带 <code>cet6</code> 标签的全量结果，不宣称为唯一或官方六级大纲词数。</li></ul></div></section>`:"";
      render(shell(`<a class="back-link" href="#/libraries">← 返回词库中心</a><section class="library-detail-hero card accent-${escapeHtml(item.accent||"violet")}"><div><div class="library-detail-title"><span class="badge ${statusClass(item.status)}">${statusText(item.status)}</span>${active?`<span class="badge">当前词库</span>`:""}</div><h3>${escapeHtml(item.name)}</h3><p>${escapeHtml(item.description||"")}</p><div class="hero-actions">${actions}</div></div><div class="library-detail-count"><strong>${cardCount}</strong><span>增强学习卡</span></div></section>${statsHtml}<section class="section grid grid-2"><div class="card form-card"><h3>数据来源</h3><p class="meta">${escapeHtml(item.source||"未填写")}</p><h3>许可与范围</h3><p class="meta">${escapeHtml(item.licenseNote||"")}</p></div><div class="card form-card"><h3>学习能力</h3><div class="library-feature-list">${(item.features||[]).map(x=>`<span>✓ ${escapeHtml(x)}</span>`).join("")}</div></div></section>${cet6Info}`,item.shortName||item.name,item.level||"词库详情"));
    });
  }

  function ensureDeckForLibrary(id,name){
    let deck=state.decks.find(d=>d.libraryId===id&&d.name===name);
    if(!deck){deck={id:uid(),libraryId:id,name,description:`${name} · WordLoop v4.1`,color:"#3b82f6",createdAt:nowISO(),updatedAt:nowISO()};state.decks.push(deck);}
    return deck;
  }
  function initialReview(cardId,index){return {cardId,status:"new",level:0,intervalDays:0,consecutiveCorrect:0,totalCorrect:0,totalWrong:0,lapses:0,dueAt:index<10?nowISO():addDays(new Date(),1+Math.floor(index/20)),lastReviewedAt:null,averageResponseTime:0};}
  async function importCet6Cards(){
    const payload=await loadCet6Cards();
    const deck=ensureDeckForLibrary("cet6",payload.name||"CET-6 精选 100");
    const existingById=new Map(state.cards.map(c=>[c.id,c]));
    payload.cards.forEach((source,index)=>{
      const existing=existingById.get(source.id);
      if(existing){
        const preserved={createdAt:existing.createdAt||nowISO(),updatedAt:nowISO(),isSuspended:!!existing.isSuspended};
        Object.assign(existing,clone(source),preserved,{deckId:deck.id,libraryId:"cet6"});
      }else{
        const card={...clone(source),deckId:deck.id,libraryId:"cet6",createdAt:nowISO(),updatedAt:nowISO()};
        state.cards.push(card);state.reviewStates.push(initialReview(card.id,index));
      }
    });
    save();
    return payload.cards.length;
  }

  window.activateLibrary=async function(id){
    const valid=["core-200","cet6"];
    if(!valid.includes(id)){toast("该词库还在规划中");return;}
    const button=document.activeElement;if(button?.tagName==="BUTTON"){button.disabled=true;button.textContent="正在准备词库……";}
    try{
      if(id==="cet6")await importCet6Cards();
      const current=activeLibraryId();
      if(state.studyPlan)state.libraryPlans[current]=state.studyPlan;
      state.libraryCenter.activeLibraryId=id;
      if(state.libraryPlans[id]){
        state.studyPlan=state.libraryPlans[id];
        ensureStudyPlan();
      }else{
        createPlanAssignments(state.settings.dailyGoal||20,"original",false);
        state.studyPlan.name=libraryPlanName(id);
        state.libraryPlans[id]=state.studyPlan;
      }
      state.libraryCenter.updatedAt=nowISO();
      practiceSession=null;save();toast(`已切换到${LIBRARY_NAMES[id]}`);location.hash="#/plan";
    }catch(error){console.error(error);alert(`词库启用失败：${error.message}\n请确认 data/cet6 文件已完整上传。`);if(button?.tagName==="BUTTON")button.disabled=false;}
  };

  const planEligibleCardsV4Base=planEligibleCards;
  planEligibleCards=function(){ return state.cards.filter(c=>!c.isSuspended&&cardLibraryId(c)===activeLibraryId()); };

  const buildPracticeQueueV4Base=buildPracticeQueue;
  buildPracticeQueue=function(mode){
    mode=String(mode||"");
    if(/^(?:day|daywrong)-\d+$/.test(mode))return buildPracticeQueueV4Base(mode);
    let cards=cardsInLibrary();
    if(mode==="new")cards=cards.filter(c=>getReview(c.id).status==="new");
    else if(mode==="review")cards=cards.filter(c=>getReview(c.id).status!=="new"&&new Date(getReview(c.id).dueAt)<=new Date());
    else cards=[...cards].sort(()=>Math.random()-.5);
    if(!cards.length&&mode==="review")cards=[...cardsInLibrary()].sort(()=>Math.random()-.5).slice(0,20);
    return [...cards].sort(()=>Math.random()-.5).slice(0,Math.max(10,state.settings.dailyGoal));
  };

  const createPlanAssignmentsV4Base=createPlanAssignments;
  createPlanAssignments=function(wordsPerDay=20,orderMode="original",preserveName=true){
    createPlanAssignmentsV4Base(wordsPerDay,orderMode,preserveName);
    state.studyPlan.libraryId=activeLibraryId();
    state.libraryPlans[activeLibraryId()]=state.studyPlan;
    save();
  };

  const ensureStudyPlanV4Base=ensureStudyPlan;
  ensureStudyPlan=function(){
    ensureStudyPlanV4Base();
    state.studyPlan.libraryId=activeLibraryId();
    state.libraryPlans[activeLibraryId()]=state.studyPlan;
    save();
  };

  function primaryMeaning(entry){
    const raw=(entry.meaningsZh||[]).join("；").replace(/\\n/g,"；").replace(/\s+/g," ").trim();
    return raw.length>145?raw.slice(0,145)+"…":raw;
  }
  function frequencyText(entry){
    const b=entry.frequency?.bnc,m=entry.frequency?.modern;
    if(b&&m)return `BNC ${b} · 当代 ${m}`;
    if(b)return `BNC ${b}`;if(m)return `当代 ${m}`;return "暂无词频";
  }
  function filterLexicon(entries){
    const q=lexiconView.query.trim().toLowerCase();
    if(!q)return entries;
    return entries.filter(e=>e.word.toLowerCase().includes(q)||primaryMeaning(e).toLowerCase().includes(q));
  }
  function renderLexiconRows(data){
    const host=document.getElementById("lexiconResults");if(!host)return;
    const filtered=filterLexicon(data.entries);
    const totalPages=Math.max(1,Math.ceil(filtered.length/lexiconView.pageSize));
    lexiconView.page=Math.max(1,Math.min(totalPages,lexiconView.page));
    const start=(lexiconView.page-1)*lexiconView.pageSize;
    const page=filtered.slice(start,start+lexiconView.pageSize);
    host.innerHTML=`<div class="lexicon-result-meta"><span>找到 ${filtered.length} 个词条 · 第 ${lexiconView.page}/${totalPages} 页</span><span>${escapeHtml(data.scopeNote||"")}</span></div><div class="card lexicon-table">${page.length?page.map(entry=>`<div class="lexicon-row"><div class="lexicon-word"><strong>${escapeHtml(entry.word)}</strong><span>${escapeHtml(entry.phonetic||"")}</span></div><div><span class="lexicon-pos">${escapeHtml((entry.partsOfSpeech||[]).join(" / ")||"词性未标注")}</span><p>${escapeHtml(primaryMeaning(entry)||"暂无中文释义")}</p></div><div class="lexicon-frequency">${escapeHtml(frequencyText(entry))}</div></div>`).join(""):`<div class="empty">没有匹配的词条。</div>`}</div><div class="lexicon-pagination"><button class="btn btn-secondary" ${lexiconView.page<=1?"disabled":""} onclick="changeLexiconPage(-1)">← 上一页</button><span>${lexiconView.page} / ${totalPages}</span><button class="btn btn-secondary" ${lexiconView.page>=totalPages?"disabled":""} onclick="changeLexiconPage(1)">下一页 →</button></div>`;
    host.dataset.totalPages=String(totalPages);
  }
  window.searchCet6Lexicon=function(value){lexiconView.query=value||"";lexiconView.page=1;loadCet6Lexicon().then(renderLexiconRows);};
  window.changeLexiconPage=function(delta){lexiconView.page+=Number(delta)||0;loadCet6Lexicon().then(data=>{renderLexiconRows(data);document.querySelector(".lexicon-browser")?.scrollIntoView({behavior:"smooth",block:"start"});});};

  function cet6LexiconPage(){
    render(shell(`<a class="back-link" href="#/library/cet6">← 返回 CET-6 词库</a><section class="card lexicon-browser"><div class="section-head"><div><span class="hero-badge">BASE LEXICON</span><h3>CET-6 基础词库浏览器</h3><p class="meta">ECDICT 中带 cet6 标签的 5407 个词条，包含音标、中英文释义、考试标签、词频和词形信息。</p></div><button class="btn btn-primary" onclick="activateLibrary('cet6')">启用精选 100 学习卡</button></div><div class="toolbar"><input class="input search" type="search" placeholder="搜索英文单词或中文释义" value="${escapeHtml(lexiconView.query)}" oninput="searchCet6Lexicon(this.value)"><select class="select lexicon-page-size" onchange="lexiconView.pageSize=Number(this.value);lexiconView.page=1;searchCet6Lexicon(document.querySelector('.lexicon-browser .search').value)"><option value="25">每页 25</option><option value="50" selected>每页 50</option><option value="100">每页 100</option></select></div><div id="lexiconResults"><div class="card empty">正在加载 5407 个基础词条……</div></div></section>`,"CET-6 基础词库","查词、筛选与后续学习卡生成的数据基础"));
    loadCet6Lexicon().then(data=>{if((location.hash||"").split("?")[0]==="#/library/cet6/lexicon")renderLexiconRows(data);}).catch(error=>{const host=document.getElementById("lexiconResults");if(host)host.innerHTML=`<div class="card empty"><h3>基础词库加载失败</h3><p>${escapeHtml(error.message)}</p><p>请确认 <code>public/data/cet6/cet6_lexicon.json</code> 已上传。</p></div>`;});
  }

  const shellV4Base=shell;
  shell=function(content,title,subtitle=""){
    let html=shellV4Base(content,title,subtitle);
    const hash=location.hash||"#/dashboard";
    const active=hash.startsWith("#/libraries")||hash.startsWith("#/library/");
    const link=`<a href="#/libraries" title="词库中心" class="${active?"active":""}"><span class="icon">${icons.libraries}</span><span class="nav-label">词库中心</span></a>`;
    if(!html.includes('href="#/libraries"'))html=html.replace('<a href="#/import"',link+'<a href="#/import"');
    const topLink=`<a class="btn btn-secondary library-top-link" href="#/libraries">${icons.libraries} <span class="label-hide">${escapeHtml(LIBRARY_NAMES[activeLibraryId()]||"词库中心")}</span></a>`;
    if(!html.includes("library-top-link"))html=html.replace('<div class="top-actions">','<div class="top-actions">'+topLink);
    return html;
  };

  const routeV4Base=route;
  route=function(){
    ensureLibraryState();
    const path=(location.hash||"#/dashboard").slice(1).split("?")[0];
    if(path==="/libraries")librariesPage();
    else if(path==="/library/cet6/lexicon")cet6LexiconPage();
    else if(/^\/library\/[a-z0-9-]+$/i.test(path))libraryDetail(path.split("/").pop());
    else routeV4Base();
  };

  const resetDataV4Base=resetData;
  resetData=function(){resetDataV4Base();ensureLibraryState();};

  window.lexiconView=lexiconView;
  window.removeEventListener("hashchange",routeV4Base);
  window.addEventListener("hashchange",route);
  if(document.readyState!=="loading")route();
})();
