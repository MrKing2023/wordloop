#!/usr/bin/env python3
"""Build WordLoop v4.1 CET-6 base lexicon and curated 100-card release.

Input is the ECDICT-derived cet6_lexicon_full.json produced by extract_exam_words.py.
The curated card content below is original WordLoop learning content.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

CURATED_TSV = r'''environmental	adj.	环境的；与环境有关的	The company introduced stricter environmental standards for all new projects.	公司为所有新项目引入了更严格的环保标准。	常作定语修饰 policy、impact、protection 等名词，强调与自然环境有关。	environmental protection|environmental impact|environmental standards	ecological::更强调生态系统及其相互关系|green::常指环保、低碳的做法	environment n. 环境|environmentally adv. 在环境方面	The report examines the environmental impact of urban expansion.::该报告研究城市扩张对环境的影响。	环境
participant	n.	参与者；参加者	Each participant was asked to complete a short questionnaire after the experiment.	实验结束后，每位参与者都被要求填写一份简短问卷。	常用于研究、会议和活动语境，通常与 in 搭配表示参加某项活动。	study participant|active participant|participant in the survey	attendee::强调出席会议或活动的人|respondent::强调回答调查问卷的人	participate v. 参加|participation n. 参与	More than two hundred participants joined the online workshop.::两百多名参与者参加了线上研讨会。	研究
context	n.	背景；语境；上下文	The meaning of the phrase becomes clear when it is read in context.	把这个短语放在上下文中阅读时，它的含义就清楚了。	常见结构为 in context、in the context of；学习词汇时应结合上下文理解词义。	in context|historical context|in the context of	background::泛指背景资料或情况|setting::强调故事或事件发生的环境	contextual adj. 上下文的|contextualize v. 置于背景中理解	The decision must be understood within its social context.::必须在其社会背景下理解这项决定。	语言
category	n.	类别；范畴	These products fall into a separate category because they require special handling.	这些产品属于单独一类，因为它们需要特殊处理。	常与 fall into、belong to、divide into 搭配，表示分类。	product category|broad category|fall into a category	type::日常用语中更宽泛的“类型”|classification::强调分类体系或分类过程	categorize v. 分类|categorization n. 分类	The survey divides responses into three main categories.::该调查把回答分为三个主要类别。	分类
assessment	n.	评估；评价	A careful assessment of the risks is required before construction begins.	施工开始前需要对风险进行仔细评估。	常指系统、正式的评价过程，可搭配 risk、performance、impact。	risk assessment|performance assessment|make an assessment	evaluation::强调依据标准判断价值或效果|appraisal::常用于工作表现、资产价值等正式评估	assess v. 评估|assessor n. 评估人员	The teacher used several methods to assess student progress.::老师采用了多种方法评估学生的进步。	评估
corporate	adj.	公司的；企业的	The firm revised its corporate strategy to focus on renewable energy.	这家公司调整了企业战略，把重点放在可再生能源上。	通常作定语，修饰 strategy、culture、responsibility、governance 等商业名词。	corporate strategy|corporate culture|corporate responsibility	commercial::强调商业或营利性质|business::更普通，可作名词或定语	corporation n. 公司|corporately adv. 以公司方式	The company is trying to improve its corporate image.::该公司正努力改善其企业形象。	商业
analyst	n.	分析师；分析人员	The analyst warned that the recent growth might not be sustainable.	分析师警告说，近期的增长可能无法持续。	常见于金融、政策、数据和市场分析语境。	financial analyst|data analyst|market analyst	researcher::强调开展研究的人|consultant::强调向客户提供专业建议的人	analyse v. 分析|analysis n. 分析|analytical adj. 分析的	Several analysts expect interest rates to remain unchanged.::几位分析师预计利率将保持不变。	职业
ethnic	adj.	民族的；族群的	The city is known for its rich ethnic diversity and cultural traditions.	这座城市以丰富的族群多样性和文化传统而闻名。	常修饰 group、minority、community、diversity，描述族群身份或文化。	ethnic group|ethnic minority|ethnic diversity	racial::更多涉及种族分类|cultural::范围更广，涉及文化特征	ethnicity n. 族群身份	The region is home to several ethnic communities.::该地区居住着多个族群社区。	社会
landscape	n.	景观；形势；格局	Digital technology has transformed the competitive landscape of the industry.	数字技术改变了该行业的竞争格局。	既可指自然景观，也可比喻某一领域的整体形势或格局。	urban landscape|political landscape|competitive landscape	scenery::主要指可观赏的自然风景|terrain::强调地形特征	landscaping n. 景观设计	The mountain landscape attracts visitors throughout the year.::山地景观全年吸引游客。	社会
perception	n.	看法；感知；认知	Public perception of the policy changed after more evidence was released.	更多证据公布后，公众对这项政策的看法发生了变化。	常与 public、consumer、visual 等搭配，表示人们形成的印象或感知。	public perception|consumer perception|change the perception	view::较普通的观点|impression::强调初步或总体印象	perceive v. 察觉；认为|perceptive adj. 有洞察力的	Our perception of risk is influenced by past experience.::我们对风险的认知会受到过去经历的影响。	认知
intervention	n.	干预；介入	Early intervention can prevent a minor problem from becoming more serious.	及早干预可以防止小问题变得更加严重。	常用于医疗、教育、政策和冲突语境，强调主动介入以改变结果。	early intervention|government intervention|medical intervention	involvement::泛指参与其中|interference::常含不受欢迎的干涉意味	intervene v. 干预	The program provides targeted intervention for struggling students.::该项目为学习困难的学生提供有针对性的干预。	政策
specifically	adv.	具体地；专门地；明确地	The new fund was created specifically to support small rural businesses.	设立这项新基金是专门为了支持农村小企业。	可用于强调精确对象或目的，常见 specifically designed for、specifically aimed at。	specifically designed|specifically intended|more specifically	particularly::尤其，强调程度或重要性|explicitly::明确地，强调清楚表达	specific adj. 具体的|specify v. 明确说明	The report deals specifically with air pollution in large cities.::这份报告专门讨论大城市的空气污染。	表达
sector	n.	部门；行业；领域	The renewable energy sector has created thousands of new jobs.	可再生能源行业创造了数千个新工作岗位。	常修饰经济中的某一行业或公共服务部门。	private sector|public sector|energy sector	industry::强调生产或商业行业|field::更宽泛的活动或研究领域	sectoral adj. 部门的	Investment in the technology sector continued to rise.::科技行业的投资持续增长。	经济
curriculum	n.	课程体系；课程设置	The school revised its curriculum to include more practical science lessons.	学校修订了课程设置，加入更多实践科学课。	指学校或项目中完整的课程体系；复数可用 curricula 或 curriculums。	school curriculum|core curriculum|curriculum design	syllabus::通常指一门具体课程的教学大纲|course::指单门课程	curricular adj. 课程的	Digital literacy is now part of the national curriculum.::数字素养如今已成为国家课程的一部分。	教育
asset	n.	资产；有价值的人或事物	Her ability to explain complex ideas is a valuable asset to the research team.	她解释复杂概念的能力是研究团队的一项宝贵优势。	既可指财务资产，也可指能带来价值的能力、资源或人员。	financial asset|valuable asset|company assets	resource::强调可供使用的资源|advantage::强调有利条件	assets n. 资产总额	Strong communication skills are an asset in almost any job.::良好的沟通能力在几乎任何工作中都是一种优势。	商业
transition	n.	过渡；转变	The transition from university to full-time employment can be challenging.	从大学生活过渡到全职工作可能具有挑战性。	常用结构 transition from A to B，强调状态或阶段的逐步改变。	smooth transition|energy transition|transition from A to B	change::最普通的变化|transformation::通常指更深刻、彻底的转变	transition v. 过渡|transitional adj. 过渡的	The country is making a gradual transition to cleaner energy.::该国正逐步向更清洁的能源过渡。	变化
symptom	n.	症状；征兆	Persistent tiredness may be a symptom of an underlying health problem.	持续疲劳可能是某种潜在健康问题的症状。	医学中指疾病表现；也可比喻某个更深层问题的外在征兆。	common symptom|show symptoms|symptom of disease	sign::更宽泛的迹象，也可为客观体征|indication::表示某事可能存在的迹象	symptomatic adj. 有症状的	A sudden loss of smell can be an early symptom.::嗅觉突然丧失可能是一种早期症状。	健康
negotiation	n.	谈判；协商	After weeks of negotiation, the two sides finally reached an agreement.	经过数周谈判，双方终于达成协议。	常用复数 negotiations 指一系列正式谈判；搭配 enter into、conduct、resume。	peace negotiation|contract negotiation|enter into negotiations	discussion::更一般的讨论|bargaining::强调讨价还价过程	negotiate v. 谈判|negotiator n. 谈判者	Salary negotiation requires preparation and clear priorities.::薪资谈判需要准备和明确的优先事项。	沟通
evaluation	n.	评价；评估	The final evaluation showed that the training program had improved productivity.	最终评估显示，该培训项目提高了生产率。	强调依据证据或标准判断效果、价值或质量。	program evaluation|critical evaluation|evaluation criteria	assessment::可指测量或判断过程，教育和风险语境常见|review::可较非正式地回顾检查	evaluate v. 评价|evaluative adj. 评价性的	The committee will evaluate each proposal independently.::委员会将独立评估每一份提案。	评估
deficit	n.	赤字；不足；缺口	The government introduced spending cuts to reduce the budget deficit.	政府实施削减开支措施，以减少预算赤字。	常见于财政、贸易和能力不足语境，如 budget deficit、attention deficit。	budget deficit|trade deficit|reduce the deficit	shortfall::强调实际数量低于所需数量|debt::指欠款总额，不等同于年度赤字	deficient adj. 缺乏的|deficiency n. 缺乏	The region faces a serious water deficit during the dry season.::该地区在旱季面临严重缺水。	经济
confront	v.	面对；正视；对抗	The organization must confront the causes of inequality rather than ignore them.	该组织必须正视不平等的根源，而不是忽视它们。	可表示勇敢面对问题，也可表示与某人对峙；常接 problem、challenge、reality。	confront a problem|confront the reality|be confronted with	face::较中性、常用的“面对”|challenge::可表示质疑或挑战	confrontation n. 对抗|confrontational adj. 对抗性的	Many cities are confronting a shortage of affordable housing.::许多城市正面临经济适用住房短缺问题。	行动
peer	n.	同龄人；同辈；同行	Young people are often strongly influenced by their peers.	年轻人经常受到同龄人的强烈影响。	常见 peer pressure、peer review、peer group；作动词时也可表示凝视。	peer pressure|peer group|peer review	colleague::同事，强调工作关系|contemporary::同一时代的人	peer-reviewed adj. 同行评审的	The article was checked through a formal peer-review process.::这篇文章经过了正式的同行评审过程。	社会
immigration	n.	移民入境；移居	The debate focused on how immigration affects the labor market.	这场辩论集中讨论移民入境如何影响劳动力市场。	指进入另一个国家定居；与 emigration“移出本国”相对。	immigration policy|illegal immigration|immigration control	migration::泛指人口或动物迁移|emigration::从本国迁往国外	immigrate v. 移入|immigrant n. 移民	Changes in immigration law affected thousands of families.::移民法的变化影响了数千个家庭。	社会
literally	adv.	按字面地；确实地	The phrase should not be interpreted literally in this context.	在这个语境中，不应按字面理解这个短语。	正式表达中表示“按字面”；口语中也常作强调语，但应避免过度使用。	take literally|translate literally|literally true	exactly::表示完全准确|figuratively::比喻地，与 literally 相对	literal adj. 字面的|literacy n. 读写能力	The temperature literally fell below zero overnight.::气温一夜之间确实降到了零度以下。	语言
consultant	n.	顾问；会诊专家	The company hired an independent consultant to review its safety procedures.	公司聘请了一名独立顾问审查其安全程序。	通常指为机构或个人提供专业建议的人。	management consultant|independent consultant|consultant on strategy	adviser::广义的建议者|specialist::强调某一领域的专门知识	consult v. 咨询|consultancy n. 咨询业	A financial consultant helped them prepare a long-term plan.::一位财务顾问帮助他们制定了长期计划。	职业
enterprise	n.	企业；事业；进取心	The policy is intended to encourage small enterprise in rural areas.	这项政策旨在鼓励农村地区发展小企业。	可指企业组织，也可指需要投入和主动性的事业。	private enterprise|small enterprise|enterprise development	company::普通的公司|venture::常指带风险的新项目或企业	enterprising adj. 有进取心的	The project is a joint enterprise between two universities.::该项目是两所大学的合作事业。	商业
negotiate	v.	谈判；协商；设法通过	The union will negotiate with management over pay and working conditions.	工会将就薪资和工作条件与管理层谈判。	常用 negotiate with someone over/about something；也可接 contract、deal。	negotiate a contract|negotiate with management|negotiate a settlement	bargain::强调讨价还价|mediate::作为第三方调解双方	negotiation n. 谈判|negotiator n. 谈判者	They negotiated a lower price with the supplier.::他们与供应商谈成了更低的价格。	沟通
criteria	n.	标准；准则（criterion 的复数）	All applications will be judged according to the same criteria.	所有申请都将按照相同的标准进行评判。	criteria 是复数，单数为 criterion；常与 meet、selection、evaluation 搭配。	selection criteria|meet the criteria|evaluation criteria	standards::通用的标准或规范|requirements::必须满足的具体要求	criterion n. 单项标准	Cost is only one criterion for choosing a supplier.::成本只是选择供应商的一项标准。	评估
clinical	adj.	临床的；冷静客观的	The treatment is still being tested in a large clinical trial.	这种治疗方法仍在一项大型临床试验中接受测试。	医学语境常修饰 trial、evidence、practice、symptom。	clinical trial|clinical evidence|clinical practice	medical::更宽泛地指医学或医疗|therapeutic::强调治疗用途	clinic n. 诊所|clinician n. 临床医师	Doctors need more clinical evidence before recommending the drug.::医生在推荐这种药物之前需要更多临床证据。	健康
refugee	n.	难民	The country agreed to provide temporary shelter for thousands of refugees.	该国同意为数千名难民提供临时住所。	指因战争、迫害或灾难被迫离开本国的人；注意与一般 migrant 区分。	refugee camp|refugee crisis|accept refugees	migrant::因多种原因迁移的人|asylum seeker::正在申请庇护、身份尚未确定的人	refuge n. 避难所	Many refugees were separated from their families during the conflict.::许多难民在冲突期间与家人失散。	社会
incorporate	v.	包含；把……纳入；合并	The revised plan incorporates feedback from local residents.	修订后的方案纳入了当地居民的反馈。	常用 incorporate A into B，表示把某要素纳入整体。	incorporate feedback|incorporate into the design|incorporate features	include::普通的“包括”|integrate::强调使不同部分协调成为整体	incorporation n. 纳入；公司注册	The course incorporates both theory and practical training.::这门课程同时包含理论和实践训练。	行动
mechanism	n.	机制；机械装置	Researchers are trying to identify the mechanism behind the disease.	研究人员正试图找出这种疾病背后的机制。	既可指机器部件，也常指产生某种结果的过程或制度。	underlying mechanism|market mechanism|defense mechanism	process::泛指过程|system::强调相互关联的整体	mechanical adj. 机械的|mechanism-based adj. 基于机制的	The body has a natural mechanism for regulating temperature.::人体具有调节体温的自然机制。	科学
penalty	n.	处罚；罚金；不利后果	Companies that break the rule may face a heavy financial penalty.	违反规定的公司可能面临高额经济处罚。	常与 impose、pay、face 搭配；体育中也可指罚球。	financial penalty|death penalty|impose a penalty	fine::特指金钱罚款|punishment::更宽泛的惩罚	penalize v. 处罚|penal adj. 刑罚的	Late payment may result in an additional penalty.::逾期付款可能导致额外罚金。	法律
incentive	n.	激励；刺激；动机	Tax reductions give businesses an incentive to invest in clean technology.	减税为企业投资清洁技术提供了激励。	常用 give/provide an incentive to do something；可指金钱或非金钱激励。	financial incentive|strong incentive|provide an incentive	motivation::内在或外在动机|reward::完成行为后给予的回报	incentivize v. 激励	The bonus scheme creates an incentive for employees to improve performance.::奖金制度激励员工提高绩效。	经济
violation	n.	违反；侵犯	The factory was fined for a serious violation of environmental regulations.	这家工厂因严重违反环保法规而被罚款。	常用 violation of law/rules/rights；指违反规定或侵犯权利。	traffic violation|human-rights violation|violation of the law	breach::常指违反合同、义务或安全规定|offense::可指违法行为或冒犯	violate v. 违反；侵犯	Sharing the data without permission would be a privacy violation.::未经允许共享这些数据将构成隐私侵犯。	法律
controversy	n.	争议；争论	The proposal caused considerable controversy among local residents.	这项提议在当地居民中引起了相当大的争议。	通常指持续、公开且意见对立的争论；常与 spark、cause、surround 搭配。	public controversy|cause controversy|surrounded by controversy	debate::可为有组织、理性的讨论|dispute::常指具体分歧或争端	controversial adj. 有争议的	The decision remains a subject of intense controversy.::这项决定仍是激烈争议的焦点。	社会
constitute	v.	构成；组成；被视为	Women constitute nearly half of the organization's senior staff.	女性构成该组织高级员工的近一半。	表示“构成某整体”时主语为组成部分；也可表示“构成某种行为或情况”。	constitute a threat|constitute the majority|be constituted by	form::普通的“形成”|comprise::整体由若干部分组成时常用	constitution n. 构成；宪法|constituent n. 组成部分	Such behavior may constitute a breach of contract.::这种行为可能构成违约。	学术
emission	n.	排放；排放物	The new engine produces significantly lower carbon emissions.	这种新发动机产生的碳排放显著更低。	环境语境中常用复数 emissions，搭配 carbon、gas、reduce。	carbon emissions|vehicle emissions|reduce emissions	discharge::强调释放液体、气体或废物|pollution::污染现象或污染物总称	emit v. 排放	Several countries have promised to cut greenhouse-gas emissions.::多个国家承诺削减温室气体排放。	环境
vulnerable	adj.	易受伤害的；脆弱的	Older people are particularly vulnerable to extreme heat.	老年人特别容易受到极端高温的伤害。	常用 vulnerable to，说明容易受某种风险、攻击或影响。	vulnerable groups|vulnerable to attack|economically vulnerable	susceptible::强调容易受疾病或影响|fragile::强调容易破碎或失去稳定	vulnerability n. 脆弱性	Small coastal communities are vulnerable to rising sea levels.::小型沿海社区容易受到海平面上升的影响。	社会
capability	n.	能力；性能	The new system has the capability to process large amounts of data in real time.	新系统具备实时处理大量数据的能力。	常用 capability to do 或 capability for doing；也可表示设备性能。	technical capability|military capability|develop capability	ability::最普通的能力|capacity::强调可容纳量或潜在能力	capable adj. 有能力的	The laboratory lacks the capability to conduct this type of test.::该实验室不具备开展这类测试的能力。	技术
psychology	n.	心理学；心理状态	The course introduces students to the basic principles of human psychology.	这门课程向学生介绍人类心理学的基本原理。	既指学科，也可指个人或群体的心理过程和思维方式。	social psychology|child psychology|consumer psychology	mindset::个人较稳定的思维模式|mentality::某人或群体的心态	psychological adj. 心理的|psychologist n. 心理学家	Consumer psychology plays an important role in advertising.::消费者心理在广告中起着重要作用。	学科
privacy	n.	隐私；独处	The application collects personal data, raising concerns about user privacy.	该应用收集个人数据，引发了对用户隐私的担忧。	不可数名词，常见 protect privacy、privacy concerns、right to privacy。	data privacy|protect privacy|privacy policy	confidentiality::强调信息保密义务|secrecy::强调有意隐藏信息	private adj. 私人的	Employees have a right to privacy in certain circumstances.::在某些情况下，员工享有隐私权。	技术
conviction	n.	坚定信念；定罪	She spoke with conviction about the need for equal access to education.	她坚定地谈到平等获得教育的必要性。	可表示强烈信念，也可指法院定罪；需根据语境区分。	deep conviction|criminal conviction|speak with conviction	belief::普通的信念或看法|confidence::对自己或结果的信心	convince v. 说服|convicted adj. 被判有罪的	The evidence led to his conviction for fraud.::这些证据导致他因欺诈被定罪。	社会
controversial	adj.	有争议的	The government postponed the controversial reform after widespread protests.	在广泛抗议之后，政府推迟了这项有争议的改革。	修饰引发强烈分歧的议题、决定、人物或观点。	controversial issue|highly controversial|controversial decision	disputed::强调真实性或合法性受到质疑|contentious::正式，指容易引发争论	controversy n. 争议	The article makes a controversial claim about social media.::这篇文章对社交媒体提出了一个有争议的主张。	社会
narrative	n.	叙事；叙述；故事	The documentary challenges the traditional narrative of economic progress.	这部纪录片质疑了关于经济进步的传统叙事。	既指故事叙述，也可指社会中被广泛传播的一套解释框架。	personal narrative|dominant narrative|construct a narrative	story::普通的故事|account::对事件的陈述或记录	narrate v. 叙述|narrator n. 叙述者	Different groups offered competing narratives of the event.::不同群体对该事件提出了相互竞争的叙事。	媒体
assert	v.	断言；坚持主张；维护	The report asserts that the current policy has failed to reduce inequality.	报告断言，现行政策未能减少不平等。	常接 that 从句；assert oneself 表示坚定表达自己或维护权利。	assert that|assert control|assert one's rights	claim::可表示声称，但未必有证据|declare::公开、正式宣布	assertion n. 断言|assertive adj. 坚定自信的	The company continues to assert its independence.::该公司继续坚持其独立性。	表达
dominant	adj.	占主导地位的；显著的	Online platforms have become a dominant source of news for many young adults.	网络平台已成为许多年轻人的主要新闻来源。	可描述力量、地位、特征或基因占优势。	dominant position|dominant culture|dominant role	leading::领先或主要的|prevailing::某时期普遍存在的	dominate v. 支配|dominance n. 主导地位	One firm holds a dominant position in the local market.::一家公司在当地市场占据主导地位。	社会
heritage	n.	遗产；传统	The museum works to preserve the region's cultural heritage.	该博物馆致力于保护该地区的文化遗产。	常指从过去继承的文化、历史、自然或家族传统。	cultural heritage|world heritage site|preserve heritage	legacy::强调前人留下、持续产生影响的事物|tradition::代代传承的习俗或做法	heritage conservation n. 遗产保护	Traditional crafts are an important part of the nation's heritage.::传统手工艺是该国遗产的重要组成部分。	文化
legacy	n.	遗产；后续影响	The scientist's greatest legacy is the network of young researchers she trained.	这位科学家最大的遗产是她培养的青年研究人员网络。	既可指遗赠财产，也常指一个人、制度或事件留下的长期影响。	lasting legacy|leave a legacy|historical legacy	heritage::强调继承的文化或传统|inheritance::法律或家庭财产继承	legatee n. 遗产受赠人	The conflict left a painful legacy for later generations.::这场冲突给后代留下了痛苦的影响。	文化
legitimate	adj.	合法的；合理的；正当的	Residents have legitimate concerns about the safety of the proposed facility.	居民对拟建设施的安全性有合理的担忧。	既表示法律上合法，也表示理由、要求或关切合理正当。	legitimate concern|legitimate business|legitimate authority	legal::严格指符合法律|valid::强调有充分依据、有效	legitimacy n. 合法性|legitimately adv. 合法地	The court must decide whether the claim is legitimate.::法院必须判断这项诉求是否正当。	法律
orientation	n.	方向；取向；入职培训	New employees attend an orientation program during their first week.	新员工在第一周参加入职培训项目。	可表示方向、价值取向，也常指帮助新人熟悉环境的培训。	career orientation|market orientation|orientation program	direction::普通的方向|induction::英式英语中常指入职介绍和培训	orient v. 使适应；确定方向	The course provides an orientation to basic research methods.::这门课程对基本研究方法作入门介绍。	教育
inflation	n.	通货膨胀；膨胀	High inflation has reduced the purchasing power of many households.	高通胀降低了许多家庭的购买力。	经济语境中为不可数名词，常与 rate、control、rising 搭配。	inflation rate|rising inflation|control inflation	price rise::某种价格上涨|deflation::通货紧缩，与 inflation 相反	inflate v. 使膨胀|inflationary adj. 引发通胀的	The central bank raised interest rates to curb inflation.::中央银行提高利率以遏制通货膨胀。	经济
cluster	n.	群；簇；集群	A cluster of technology companies has developed around the university.	大学周边形成了一个科技企业集群。	可指相互靠近的一组事物；作动词表示聚集在一起。	a cluster of|industrial cluster|cluster around	group::最普通的一组|concentration::强调大量集中于某处	cluster v. 聚集|clustered adj. 成群的	The cases were concentrated in a small geographic cluster.::这些病例集中在一个很小的地理区域内。	科学
depict	v.	描绘；描述	The painting depicts daily life in the city during the nineteenth century.	这幅画描绘了十九世纪这座城市的日常生活。	可用于图画、电影、文字对人物或情景的呈现。	depict a scene|accurately depict|depict as	portray::常强调对人物或形象的刻画|illustrate::用例子或图示说明	depiction n. 描绘	The chart depicts how energy use changed over time.::该图表展示了能源使用随时间的变化。	媒体
instructor	n.	教师；教练；指导员	The instructor demonstrated the procedure before allowing students to try it.	指导教师在让学生尝试之前演示了操作流程。	常指教授某项技能或课程的人，尤其在大学、培训或运动中。	course instructor|driving instructor|fitness instructor	teacher::最普通的教师|trainer::强调职业或技能训练	instruct v. 指导|instruction n. 指示；教学	Ask the instructor for help if the equipment does not work.::如果设备无法工作，请向指导教师求助。	教育
mortgage	n.	抵押贷款；按揭	They took out a mortgage to buy their first apartment.	他们办理了抵押贷款，购买第一套公寓。	常见 take out/pay off a mortgage；也可作动词表示以房产抵押。	mortgage payment|take out a mortgage|pay off a mortgage	loan::普通贷款|rent::租金，不产生房屋所有权	mortgage v. 抵押	Rising interest rates have increased monthly mortgage payments.::利率上升增加了每月按揭还款额。	经济
sanction	n.	制裁；批准	The international sanctions restricted the country's access to financial markets.	国际制裁限制了该国进入金融市场的渠道。	作名词可表示惩罚性制裁，也可表示正式批准；语境决定含义。	economic sanctions|impose sanctions|official sanction	penalty::对违规行为的处罚|approval::一般的批准	sanction v. 批准；制裁	The organization threatened to impose further sanctions.::该组织威胁要实施进一步制裁。	国际
ethics	n.	伦理；道德规范	The course examines the ethics of using artificial intelligence in healthcare.	这门课程探讨在医疗中使用人工智能的伦理问题。	通常作复数形式但可视为一门学科；常见 professional、research、business ethics。	business ethics|research ethics|code of ethics	morality::个人或社会的是非观|principles::指导行为的基本原则	ethical adj. 合乎伦理的|ethically adv. 合乎伦理地	All researchers must follow strict rules of professional ethics.::所有研究人员都必须遵守严格的职业伦理规范。	伦理
discourse	n.	话语；论述；讨论	The study analyzes how gender is represented in public discourse.	这项研究分析性别在公共话语中是如何被呈现的。	正式学术词，可指语言表达体系、公共讨论或较长的论述。	public discourse|political discourse|academic discourse	discussion::普通的讨论|narrative::一套叙事或解释框架	discursive adj. 论述的	Social media has changed the tone of political discourse.::社交媒体改变了政治话语的语调。	学术
competitor	n.	竞争者；竞争对手	The company lowered its prices after a major competitor entered the market.	一家主要竞争对手进入市场后，该公司降低了价格。	可指商业对手，也可指比赛参赛者。	main competitor|direct competitor|outperform competitors	rival::强调长期或强烈竞争关系|opponent::比赛、争论或选举中的对手	compete v. 竞争|competition n. 竞争|competitive adj. 有竞争力的	Small firms often struggle to compete with larger competitors.::小企业常常难以与更大的竞争对手竞争。	商业
portray	v.	描绘；刻画；扮演	The film portrays the main character as both ambitious and deeply insecure.	这部电影把主人公刻画成既有抱负又极度缺乏安全感的人。	常用 portray someone as，描述媒体或艺术作品如何呈现人物或事件。	portray a character|portray as|accurately portray	depict::可用于图像或文字客观呈现|represent::范围更广，可表示代表或象征	portrayal n. 描绘	The news report portrayed the protest as largely peaceful.::新闻报道把这场抗议描述为总体和平。	媒体
script	n.	剧本；脚本	The actor read the script several times before the first rehearsal.	这位演员在第一次排练前把剧本读了好几遍。	可指影视剧本、演讲稿，也可指计算机脚本。	film script|write a script|computer script	screenplay::专指电影剧本|code::泛指计算机代码	scripted adj. 按稿的|scriptwriter n. 编剧	A short script automates the most repetitive part of the task.::一个简短脚本自动完成了任务中最重复的部分。	媒体
nonetheless	adv.	尽管如此；然而	The evidence is limited; nonetheless, the findings deserve careful attention.	证据有限；尽管如此，这些发现仍值得认真关注。	正式连接副词，表示前后转折；常置于句首或分号之后。	but nonetheless|nonetheless important|nonetheless remain	nevertheless::意义几乎相同，正式|however::最常用的转折连接副词	none the less phr. 仍然	The journey was difficult, but it was nonetheless rewarding.::旅程很艰难，但仍然很有收获。	表达
prescription	n.	处方；规定；对策	The medicine is available only with a doctor's prescription.	这种药只有凭医生处方才能获得。	医疗中指处方；正式语境也可指解决问题的方案或指示。	prescription drug|write a prescription|on prescription	recipe::烹饪配方，也可比喻方法|recommendation::建议，不具有处方的正式性	prescribe v. 开处方；规定	The doctor changed the prescription after reviewing the test results.::医生查看检测结果后更改了处方。	健康
consensus	n.	共识；一致意见	The committee reached a consensus after several hours of discussion.	委员会经过数小时讨论后达成了共识。	不可数名词，常用 reach/build/achieve a consensus；通常不说 a general consensus 之外的普通复数。	reach a consensus|broad consensus|scientific consensus	agreement::普通的同意或协议|unanimity::所有人完全一致	consensual adj. 一致同意的	There is growing consensus that the system needs reform.::越来越多的人形成共识，认为该制度需要改革。	沟通
colonial	adj.	殖民的；殖民时期的	The museum contains documents from the country's colonial period.	博物馆收藏了该国殖民时期的文件。	常修饰 rule、history、period、power，涉及殖民统治或历史。	colonial rule|colonial history|colonial power	imperial::与帝国及其扩张有关|postcolonial::殖民统治结束后的	colony n. 殖民地|colonialism n. 殖民主义	Many present-day borders were drawn during the colonial era.::许多今天的边界是在殖民时代划定的。	历史
cognitive	adj.	认知的；思维的	Regular sleep is essential for memory and other cognitive functions.	规律睡眠对记忆及其他认知功能至关重要。	心理学和教育中常修饰 ability、process、development、function。	cognitive ability|cognitive development|cognitive process	mental::更宽泛的心理或精神方面|intellectual::强调智力和思考能力	cognition n. 认知	The task places a heavy cognitive demand on young children.::这项任务对幼儿提出了很高的认知要求。	心理
defendant	n.	被告	The defendant denied all the charges during the trial.	被告在审判中否认了所有指控。	法律术语，指刑事或民事案件中被起诉的一方。	criminal defendant|the defendant's lawyer|find the defendant guilty	accused::被指控者，身份表达较一般|plaintiff::民事诉讼中的原告	defend v. 辩护|defense n. 辩护	The court allowed the defendant to present new evidence.::法院允许被告提交新证据。	法律
fitness	n.	健康；适合度；适任性	Regular exercise can improve physical fitness and reduce stress.	规律锻炼可以改善身体素质并减轻压力。	可指身体健康，也可表示某人或某物对特定目的的适合程度。	physical fitness|fitness level|fitness for purpose	health::更宽泛的健康状态|suitability::对特定用途的适合性	fit adj. 健康的；适合的	The test measures the candidates' fitness for demanding work.::该测试衡量候选人是否适合高强度工作。	健康
alliance	n.	联盟；同盟；合作关系	The two organizations formed an alliance to promote digital education.	这两个组织结成联盟，以推动数字教育。	常见 form/enter an alliance；可指国家、政党或机构间合作。	strategic alliance|military alliance|form an alliance	partnership::通常指合作伙伴关系|coalition::为特定政治目标组成的联盟	ally n. 盟友	The parties entered an electoral alliance before the election.::这些政党在选举前组成了选举联盟。	国际
hypothesis	n.	假设；假说	The experiment was designed to test the hypothesis that sleep improves memory.	该实验旨在检验“睡眠能改善记忆”这一假设。	学术研究中指可通过证据检验的解释或预测；复数 hypotheses。	test a hypothesis|research hypothesis|support the hypothesis	theory::经过较广泛证据支持的解释体系|assumption::暂时接受为真的前提	hypotheses n. 假设（复数）|hypothesize v. 提出假设	The data did not provide enough evidence to reject the hypothesis.::数据没有提供足够证据来否定该假设。	学术
adolescent	n.	青少年	The program provides mental-health support for adolescents and their families.	该项目为青少年及其家庭提供心理健康支持。	通常指青春期到成年早期的人；也可作形容词。	adolescent development|adolescent health|adolescent behavior	teenager::日常用语，通常指十三至十九岁的人|youth::可指青年群体，范围更宽	adolescence n. 青春期	Adolescents often become more sensitive to peer opinion.::青少年往往会变得更在意同龄人的看法。	社会
norm	n.	规范；常态；标准	Working from home has become the norm in some industries.	在一些行业，居家办公已成为常态。	常用 the norm 表示通常情况；social norms 表示社会行为规范。	social norm|cultural norm|become the norm	standard::正式标准或水平|convention::社会习惯或惯例	normal adj. 正常的|normalize v. 使正常化	The study explores how social norms influence consumer behavior.::该研究探讨社会规范如何影响消费者行为。	社会
subtle	adj.	细微的；微妙的；不易察觉的	There is a subtle difference between the two expressions.	这两个表达之间存在细微差别。	可描述难以察觉的变化、含义、影响或技巧；注意发音中 b 不发音。	subtle difference|subtle change|subtle effect	slight::程度很小，但不一定难以察觉|delicate::精细、脆弱或需谨慎处理	subtlety n. 微妙之处|subtly adv. 微妙地	The advertisement uses subtle emotional cues.::这则广告使用了细微的情感暗示。	表达
integrity	n.	正直；完整性	Researchers must protect the integrity of the data they collect.	研究人员必须保护所收集数据的完整性。	可指诚实正直，也可指系统、结构或数据保持完整可靠。	academic integrity|data integrity|personal integrity	honesty::强调诚实不欺骗|wholeness::强调完整无缺	integral adj. 不可缺少的|integrate v. 使结合	She is widely respected for her professional integrity.::她因职业操守而广受尊敬。	伦理
essence	n.	本质；精髓	The essence of the proposal is to give local communities more control.	这项提案的核心是给予当地社区更多控制权。	常用 the essence of、in essence，表示最重要的本质或概括。	the essence of|in essence|capture the essence	core::核心部分|nature::某事物固有的性质	essential adj. 必要的；本质的|essentially adv. 本质上	The photograph captures the essence of life in the old town.::这张照片捕捉到了老城生活的精髓。	表达
unemployment	n.	失业；失业率	Youth unemployment remains a serious problem in many regions.	青年失业在许多地区仍是一个严重问题。	不可数名词；常搭配 rate、benefit、rise、reduce。	unemployment rate|youth unemployment|unemployment benefits	joblessness::失业状态，较少用于正式指标|redundancy::因职位取消而失业	unemployed adj. 失业的|employment n. 就业	The policy aims to reduce long-term unemployment.::这项政策旨在减少长期失业。	经济
humanity	n.	人类；人性；人道	Climate change presents a long-term challenge to humanity.	气候变化给全人类带来了长期挑战。	可表示人类整体，也可指同情、仁慈等人性品质。	crime against humanity|benefit humanity|common humanity	humankind::中性地指全人类|compassion::强调同情心	human adj. 人类的|humanitarian adj. 人道主义的	The discovery could bring great benefits to humanity.::这项发现可能给人类带来巨大益处。	社会
correlation	n.	相关性；相互关系	The study found a strong correlation between sleep quality and academic performance.	研究发现睡眠质量与学习表现之间存在很强的相关性。	常用 correlation between A and B；相关不等于因果。	strong correlation|positive correlation|correlation between	connection::普通的联系|causation::因果关系，不应与 correlation 混淆	correlate v. 相关	A correlation does not necessarily prove that one factor causes the other.::相关性并不一定证明一个因素导致另一个因素。	学术
allegation	n.	指控；未经证实的说法	The company launched an investigation into allegations of financial misconduct.	该公司对财务不当行为的指控展开调查。	强调尚未被证实的指控，常用 allegation of/that。	serious allegation|deny an allegation|allegation of misconduct	accusation::一般指责或控告|charge::正式的刑事指控	allege v. 声称；指控|alleged adj. 所谓的	The minister strongly denied the allegation.::部长坚决否认了这项指控。	法律
initiate	v.	发起；开始；使了解	The university initiated a review of its admissions policy.	大学启动了对招生政策的审查。	正式词，常接 process、investigation、discussion、program。	initiate a process|initiate an investigation|initiate contact	start::最普通的“开始”|launch::常用于正式推出项目、产品或活动	initiative n. 倡议；主动性|initiation n. 开始	The two sides initiated talks to resolve the dispute.::双方开始谈判以解决争端。	行动
plead	v.	恳求；作出有罪或无罪答辩	The defendant pleaded not guilty to all charges.	被告对所有指控作了无罪答辩。	法律中常用 plead guilty/not guilty；一般语境中 plead with someone to do。	plead guilty|plead not guilty|plead with someone	beg::更直接、强烈地请求|appeal::公开呼吁或提出上诉	plea n. 请求；答辩	She pleaded with the council to reconsider its decision.::她恳求委员会重新考虑决定。	法律
combat	v.	打击；与……斗争	The city introduced new measures to combat air pollution.	该市推出了新措施来治理空气污染。	正式动词，常接 disease、crime、poverty、pollution；也可作名词表示战斗。	combat climate change|combat crime|combat disease	fight::更普通，可用于具体或抽象斗争|tackle::强调着手处理问题	combatant n. 战斗人员	Education can play a major role in combating poverty.::教育可以在消除贫困方面发挥重要作用。	行动
sculpture	n.	雕塑；雕塑艺术	A large metal sculpture stands at the entrance to the museum.	博物馆入口处矗立着一座大型金属雕塑。	既可数指一件雕塑，也可不可数指雕塑艺术。	modern sculpture|bronze sculpture|sculpture garden	statue::通常指人物或动物塑像|artwork::泛指艺术作品	sculpt v. 雕刻|sculptor n. 雕塑家	The artist created the sculpture from recycled materials.::艺术家用回收材料创作了这件雕塑。	文化
ethical	adj.	道德的；合乎伦理的	Researchers must consider the ethical consequences of collecting personal data.	研究人员必须考虑收集个人数据的伦理后果。	常修饰 issue、standard、principle、concern；也可表示符合道德规范。	ethical issue|ethical standards|ethical responsibility	moral::更广泛涉及个人和社会的是非判断|legal::符合法律，但不一定合乎伦理	ethics n. 伦理|ethically adv. 合乎伦理地	The company promised to use only ethically sourced materials.::该公司承诺只使用以合乎伦理方式采购的材料。	伦理
innovation	n.	创新；创新成果	Continuous innovation is essential for firms operating in a competitive market.	持续创新对于在竞争市场中经营的企业至关重要。	既可指创新过程，也可指新方法、产品或理念。	technological innovation|product innovation|encourage innovation	invention::具体的新发明|creativity::产生新想法的能力	innovate v. 创新|innovative adj. 创新的	The award recognizes innovation in sustainable design.::该奖项表彰可持续设计方面的创新。	技术
undermine	v.	削弱；损害	Repeated delays have undermined public confidence in the project.	一再延期削弱了公众对该项目的信心。	常接 confidence、authority、stability、effort，表示逐渐削弱基础。	undermine confidence|undermine authority|seriously undermine	weaken::普通的削弱|damage::造成损害，范围更宽	undermining n. 削弱	False information can undermine trust in public institutions.::虚假信息会削弱公众对公共机构的信任。	行动
manipulate	v.	操纵；熟练操作	The images had been digitally manipulated to create a misleading impression.	这些图像经过数字处理，造成了误导性印象。	可表示熟练操作物体或数据，也可指不正当地影响他人。	manipulate data|manipulate public opinion|manipulate an object	influence::中性地影响|distort::扭曲信息或事实	manipulation n. 操纵|manipulative adj. 善于操纵人的	The device allows users to manipulate the model in three dimensions.::该设备允许用户在三维空间中操作模型。	技术
allocate	v.	分配；拨给	The council allocated additional funds to improve public transport.	市政委员会拨出额外资金改善公共交通。	常用 allocate something to/for，表示按计划分配资源。	allocate resources|allocate funds|allocate time to	assign::分配任务或职责|distribute::把事物分发给多方	allocation n. 分配	Managers must allocate limited resources carefully.::管理者必须谨慎分配有限资源。	管理
coherent	adj.	连贯的；一致的；有条理的	The report presents a coherent argument supported by clear evidence.	这份报告提出了一个由清晰证据支持的连贯论点。	可描述语言、论证、政策或系统内部逻辑一致。	coherent argument|coherent strategy|clear and coherent	consistent::强调前后一致|logical::强调符合逻辑推理	coherence n. 连贯性|coherently adv. 连贯地	The separate proposals need to be combined into a coherent plan.::这些分散的提议需要整合成一项连贯的计划。	学术
deteriorate	v.	恶化；变坏	Air quality began to deteriorate as traffic increased during the holiday.	假日期间交通量增加，空气质量开始恶化。	不及物用法常见；也可作及物动词，表示使某物变坏。	deteriorate rapidly|conditions deteriorate|health deteriorates	worsen::最直接的“变得更糟”|decline::下降或逐渐衰退	deterioration n. 恶化	The patient's condition deteriorated overnight.::病人的状况一夜之间恶化了。	变化
facilitate	v.	促进；使便利	The new platform facilitates communication between teachers and parents.	新平台促进了教师与家长之间的沟通。	正式词，表示使过程更容易或更顺利；常接 communication、learning、access。	facilitate learning|facilitate communication|facilitate access	enable::使某人能够做某事|promote::推动某事发展	facilitation n. 促进|facilitator n. 促进者	Clear guidelines can facilitate effective cooperation.::清晰的指南可以促进有效合作。	行动
infrastructure	n.	基础设施	Reliable digital infrastructure is essential for remote education.	可靠的数字基础设施对远程教育至关重要。	不可数名词，指交通、能源、通信等支撑社会运行的系统。	transport infrastructure|digital infrastructure|infrastructure investment	facilities::具体设施或场所|utilities::水、电、燃气等公用服务	infrastructural adj. 基础设施的	The city needs major investment in public infrastructure.::这座城市需要对公共基础设施进行大规模投资。	城市
momentum	n.	势头；动力；动量	The campaign gained momentum after several well-known scientists expressed support.	几位知名科学家表示支持后，这项运动获得了势头。	比喻用法常见 gain/maintain/lose momentum；物理中指动量。	gain momentum|maintain momentum|lose momentum	impetus::促使某事开始或加速的推动力|drive::持续的动力或干劲	momentous adj. 重大的	The economy continued to build momentum in the second quarter.::经济在第二季度继续积聚增长势头。	变化
simultaneous	adj.	同时发生的	The system can handle several simultaneous requests without slowing down.	该系统可以同时处理多个请求而不减速。	强调两件或多件事在同一时间发生。	simultaneous translation|simultaneous events|simultaneous access	concurrent::正式，指同时并行发生|synchronous::强调时间同步	simultaneously adv. 同时地	The two teams announced their results in simultaneous press conferences.::两个团队在同时举行的新闻发布会上公布了结果。	时间
trigger	v.	引发；触发	A sudden rise in food prices could trigger widespread public concern.	食品价格突然上涨可能引发广泛的公众担忧。	常接 reaction、crisis、alarm、response；也可作名词表示诱因或扳机。	trigger a response|trigger an alarm|trigger a crisis	cause::最普通的“导致”|provoke::引起强烈反应，常含负面意味	trigger n. 诱因；扳机	The announcement triggered a sharp fall in share prices.::这项公告引发股价大幅下跌。	行动
ambiguous	adj.	含糊的；有歧义的	The wording of the contract is ambiguous and may lead to different interpretations.	合同措辞含糊，可能导致不同解释。	描述词语、陈述或情况有两种以上解释，缺乏明确性。	ambiguous language|ambiguous statement|remain ambiguous	unclear::普通的“不清楚”|vague::缺乏细节或精确性	ambiguity n. 歧义	The question was deliberately ambiguous.::这个问题被故意表述得模棱两可。	语言
authentic	adj.	真实的；正宗的；可信的	The museum confirmed that the document was authentic.	博物馆确认这份文件是真迹。	可指物品真实非伪造，也可指体验、风格或表达真诚可信。	authentic document|authentic experience|authentic cuisine	genuine::真实、非伪造，常可互换|original::原始的或最初创作的	authenticity n. 真实性	Visitors can try authentic regional dishes at the market.::游客可以在市场品尝正宗的地方菜肴。	文化
compensate	v.	补偿；弥补	The company agreed to compensate residents for the damage caused by the accident.	公司同意赔偿居民因事故造成的损失。	常用 compensate someone for something；也可指弥补不足。	compensate for loss|compensate employees|fully compensate	reimburse::报销已支付的费用|offset::以相反效果抵消影响	compensation n. 补偿；薪酬	Extra training can compensate for a lack of experience.::额外培训可以弥补经验不足。	经济
consecutive	adj.	连续的；连贯的	The team has won five consecutive matches this season.	这支球队本赛季已经连续赢得五场比赛。	强调事件一个接一个、没有中断；常修饰 days、years、victories。	consecutive days|consecutive years|consecutive victories	continuous::持续不断，强调过程没有停顿|successive::一个接一个，语义相近	consecutively adv. 连续地	Sales increased for the third consecutive month.::销售额连续第三个月增长。	时间'''


def parse_curated() -> list[dict]:
    rows=[]
    for lineno, raw in enumerate(CURATED_TSV.splitlines(), 1):
        if not raw.strip():
            continue
        cols=raw.split("\t")
        if len(cols)!=11:
            raise ValueError(f"Line {lineno}: expected 11 fields, got {len(cols)}")
        (word,pos,meaning,sentence,zh,usage,collocs,related,family,extra,topic)=cols
        def pairs(text, left, right):
            out=[]
            for part in text.split("|"):
                a,b=part.split("::",1)
                out.append({left:a.strip(),right:b.strip()})
            return out
        rows.append({
            "word":word.strip(),"partOfSpeech":pos.strip(),"meaningZh":meaning.strip(),
            "sentenceEn":sentence.strip(),"sentenceZh":zh.strip(),"usageNotes":usage.strip(),
            "collocations":[x.strip() for x in collocs.split("|") if x.strip()],
            "relatedExpressions":pairs(related,"expression","note"),
            "wordFamily":[x.strip() for x in family.split("|") if x.strip()],
            "extraExamples":pairs(extra,"en","zh"),"topic":topic.strip(),
        })
    return rows


def clean_phonetic(value: str) -> str:
    value=(value or "").strip().strip("/")
    return f"/{value}/" if value else ""


def split_cloze(sentence: str, base: dict) -> tuple[str,str,str]:
    candidates=[base.get("word","")]
    candidates.extend((base.get("forms") or {}).values())
    # Prefer longer candidates and keep order stable.
    candidates=sorted({str(x).strip() for x in candidates if str(x).strip()}, key=lambda x:(-len(x),x))
    found=[]
    for candidate in candidates:
        matches=list(re.finditer(rf"(?<![A-Za-z]){re.escape(candidate)}(?![A-Za-z])", sentence, flags=re.I))
        found.extend((candidate,m) for m in matches)
    if len(found)!=1:
        raise ValueError(f"Expected exactly one lemma/form for {base.get('word')!r}; found {[x[0] for x in found]} in: {sentence}")
    _,match=found[0]
    answer=sentence[match.start():match.end()]
    return sentence[:match.start()], answer, sentence[match.end():]


def build(input_path: Path, out_lexicon: Path, out_cards: Path) -> None:
    source=json.loads(input_path.read_text(encoding="utf-8"))
    entries=source.get("entries",[])
    by_word={e["word"].lower():e for e in entries}
    curated=parse_curated()
    if len(curated)!=100 or len({x["word"] for x in curated})!=100:
        raise ValueError(f"Curated set must contain 100 unique words; got {len(curated)}")

    compact_entries=[]
    for e in entries:
        compact_entries.append({
            "id":e["id"],"word":e["word"],"phonetic":clean_phonetic(e.get("phonetic","")),
            "partsOfSpeech":e.get("partsOfSpeech",[]),"definitionsEn":e.get("definitionsEn",[]),
            "meaningsZh":e.get("meaningsZh",[]),"examTags":e.get("examTags",[]),
            "frequency":e.get("frequency",{}),"forms":e.get("forms",{}),
        })
    lexicon={
        "schemaVersion":2,"id":"cet6-ecdict-full","name":"CET-6 基础词库（ECDICT cet6 标签全量）",
        "version":"4.1.0","generatedAt":"2026-07-12","entryCount":len(compact_entries),
        "scopeNote":"本文件是 ECDICT 中带 cet6 标签词条的全量提取，不宣称为唯一或官方考试词表。",
        "source":{"dataset":"ECDICT","repository":"skywind3000/ECDICT","license":"MIT"},
        "entries":compact_entries,
    }

    cards=[]
    for i,c in enumerate(curated,1):
        base=by_word.get(c["word"].lower())
        if not base:
            raise ValueError(f"Missing from base lexicon: {c['word']}")
        if "cet6" not in base.get("examTags",[]):
            raise ValueError(f"Not tagged cet6 in ECDICT: {c['word']}")
        prefix,answer,suffix=split_cloze(c["sentenceEn"],base)
        card={
            "id":f"cet6-{i:04d}-{c['word']}","libraryId":"cet6","deck":"CET-6 精选 100",
            "type":"cloze","word":c["word"],"pronunciation":clean_phonetic(base.get("phonetic","")),
            "answerPronunciation":clean_phonetic(base.get("phonetic","")),"partOfSpeech":c["partOfSpeech"],
            "meaningZh":c["meaningZh"],"sentenceEn":c["sentenceEn"],"sentenceZh":c["sentenceZh"],
            "clozePrefix":prefix,"clozeAnswer":answer,"clozeSuffix":suffix,"targetEnglish":"",
            "acceptedAnswers":[answer],"tags":["CET-6",c["topic"]],
            "definitionZh":c["meaningZh"],"usageNotes":c["usageNotes"],
            "collocations":c["collocations"],"relatedExpressions":c["relatedExpressions"],
            "wordFamily":c["wordFamily"],"extraExamples":c["extraExamples"],
            "difficulty":3,"source":"ECDICT 基础字段 + WordLoop 原创学习内容","isSuspended":False,
            "lexiconRef":base["id"],
            "quality":{"senseAccuracy":5,"translationAccuracy":5,"contextStrength":4,"reviewStatus":"curated"},
            "generation":{"contentVersion":"cet6-curated-100-v1","generatedAt":"2026-07-12","method":"structured generation + rule validation"},
        }
        cards.append(card)
    payload={
        "schemaVersion":2,"id":"cet6-curated-100","name":"CET-6 精选 100","version":"4.1.0",
        "generatedAt":"2026-07-12","cardCount":len(cards),
        "description":"首批 100 张增强学习卡，含语境填空、中文翻译、用法、搭配、词族与扩展例句。",
        "source":{"baseLexicon":"ECDICT cet6 tag","learningContent":"WordLoop original"},
        "cards":cards,
    }
    out_lexicon.parent.mkdir(parents=True,exist_ok=True)
    out_cards.parent.mkdir(parents=True,exist_ok=True)
    out_lexicon.write_text(json.dumps(lexicon,ensure_ascii=False,separators=(",",":")),encoding="utf-8")
    out_cards.write_text(json.dumps(payload,ensure_ascii=False,separators=(",",":")),encoding="utf-8")
    print(f"Wrote {len(compact_entries)} lexicon entries -> {out_lexicon}")
    print(f"Wrote {len(cards)} curated cards -> {out_cards}")


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--input",type=Path,required=True)
    p.add_argument("--lexicon-output",type=Path,required=True)
    p.add_argument("--cards-output",type=Path,required=True)
    a=p.parse_args()
    build(a.input,a.lexicon_output,a.cards_output)

if __name__=="__main__":
    main()
