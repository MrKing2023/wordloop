#!/usr/bin/env python3
"""Build WordLoop v4.2 postgraduate-exam core lexicon and 100 curated cards.

The base lexicon is the locally available ECDICT subset whose records carry both
``cet6`` and ``ky`` tags. This produces a broad 4,112-entry exam-core set without
copying data from GPL-licensed word-list projects. The learning-card text below is
original WordLoop content written for postgraduate entrance-exam reading contexts.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

CURATED_TSV = r'''address	v.	处理；应对（问题或需求）	The reform must address the unequal access to educational resources.	这项改革必须解决教育资源获取不平等的问题。	考研阅读中常见 address a problem/issue/need，表示“着手处理”，而不是“地址”。	address a problem|address an issue|address the needs of	deal with::最普通的“处理”，语体较中性|tackle::强调积极处理棘手问题	address n. 地址；演讲|addressee n. 收件人	The report addresses several weaknesses in the current system.::该报告处理了现行制度中的几个薄弱环节。	熟词僻义
approach	n.	方法；处理方式；研究路径	A purely technical approach may overlook the social causes of the problem.	纯技术性的处理方法可能会忽视该问题的社会成因。	常见 an approach to + 名词/动名词；注意介词用 to，不用 of。	an approach to|a systematic approach|adopt an approach	method::强调具体步骤或程序|perspective::强调看问题的角度	approach v. 接近；着手处理|approachable adj. 易接近的	Researchers adopted a different approach to measuring well-being.::研究人员采用了不同的方法衡量福祉。	熟词僻义
issue	n.	问题；议题；争议焦点	The article treats privacy as a political issue rather than a merely technical one.	这篇文章把隐私视为一个政治议题，而不只是技术问题。	issue 常指公共讨论中的议题；problem 更强调需要解决的困难。	a social issue|raise an issue|address the issue	problem::强调困难或故障|question::可指待讨论或待回答的问题	issue v. 发布；发行|issuance n. 发行	Climate change has become a central issue in economic policy.::气候变化已成为经济政策中的核心议题。	熟词僻义
charge	v.	指责；控告；声称（常接 that 从句）	Some critics charge that the policy favors large firms over small businesses.	一些批评者指责该政策偏袒大企业而非小企业。	charge that... 在评论文中表示“指责/声称”；另有 charge sb with sth“指控某人某事”。	charge that|charge someone with|take charge of	accuse::通常接 accuse sb of sth，明确指控某人|criticize::泛指批评，不一定包含正式指控	charge n. 费用；指控；负责|charged adj. 充满强烈情绪的	The company was charged with misleading consumers.::该公司被指控误导消费者。	熟词僻义
claim	v.	声称；主张；断言	The author does not claim that technology alone can eliminate inequality.	作者并未声称仅靠技术就能消除不平等。	claim that... 表示提出尚需证据支持的主张；阅读中要区分“作者观点”和“被引述者的声称”。	claim that|make a claim|support a claim	argue::强调给出论据进行论证|assert::语气更强，强调明确断言	claim n. 主张；权利要求|claimant n. 索赔人	The evidence is too limited to support such a broad claim.::这些证据太有限，无法支持如此宽泛的主张。	熟词僻义
interest	n.	利益；利害关系；权益	Policy makers must balance private interest against the public good.	政策制定者必须在私人利益与公共利益之间取得平衡。	in the interest(s) of 表示“为了……的利益”；vested interests 指既得利益集团。	public interest|vested interests|in the interests of	benefit::指获得的好处|stake::强调与结果有直接利害关系	interest v. 使感兴趣|interested adj. 感兴趣的|interesting adj. 有趣的	Researchers should disclose any financial interests.::研究人员应披露任何经济利益关系。	熟词僻义
object	v.	反对；提出异议	Several researchers object to treating test scores as the sole measure of ability.	几位研究人员反对把考试分数作为衡量能力的唯一标准。	作动词时常用 object to + 名词/动名词；to 是介词，后接 doing。	object to|strongly object|raise an objection	oppose::及物动词，可直接接名词或 doing|protest::可指公开抗议，也可指口头反对	object n. 物体；目标|objection n. 反对|objective adj. 客观的	Residents objected to the proposed expansion of the airport.::居民反对拟议中的机场扩建。	熟词僻义
apply	v.	适用；应用；申请	The same principle does not apply to every cultural context.	同一原则并不适用于所有文化背景。	apply to 表示“适用于”；apply for 表示“申请”；apply A to B 表示“把 A 应用于 B”。	apply to|apply for a position|apply a method to	use::泛指使用|implement::强调把计划、政策付诸实施	application n. 应用；申请|applicable adj. 适用的|applicant n. 申请人	These rules apply equally to public and private institutions.::这些规则同样适用于公立和私立机构。	熟词僻义
course	n.	过程；进程；发展方向	The course of social change is rarely smooth or predictable.	社会变革的进程很少是平稳或可预测的。	in the course of 表示“在……过程中”；course 不只表示“课程”。	the course of history|in the course of|change course	process::强调一系列步骤或变化|path::强调发展所走的路线	coursework n. 课程作业|course v. 流动；奔跑	The debate changed course after new evidence emerged.::新证据出现后，讨论改变了方向。	熟词僻义
deal	v.	处理；应对；论述	The policy fails to deal with the long-term effects of population ageing.	该政策未能处理人口老龄化的长期影响。	deal with 可表示“处理问题”“与人打交道”或“论述主题”，需结合宾语判断。	deal with a problem|deal with evidence|a great deal of	address::正式地处理某一问题|handle::强调实际操作或控制局面	deal n. 交易；协议|dealer n. 经销商	The final section deals with the ethical limits of the experiment.::最后一节讨论了该实验的伦理边界。	熟词僻义
feature	n.	特征；重要组成；特色	A notable feature of the argument is its emphasis on individual responsibility.	这一论点的一个显著特征是强调个人责任。	a feature of 表示“……的特征”；作动词 feature 可表示“以……为特色”或“重点介绍”。	a key feature|a distinctive feature|feature prominently	characteristic::可指典型特征，常含辨识作用|trait::常指人的性格或生物特性	feature v. 以……为特色|featured adj. 被重点介绍的	Flexibility is a central feature of the new framework.::灵活性是新框架的核心特征。	熟词僻义
reflect	v.	反映；体现；认真思考	These figures reflect changes in reporting practices as well as real behavior.	这些数字既反映了报告方式的变化，也反映了真实行为的变化。	reflect 可表示“反映事实”，也可用 reflect on/upon 表示“认真思考”。	reflect a change|reflect on experience|accurately reflect	indicate::表示数据或迹象“表明”|mirror::强调像镜子一样呈现相似模式	reflection n. 反映；思考|reflective adj. 深思的	The results may reflect differences in access rather than ability.::这些结果可能反映的是获取机会的差异，而非能力差异。	熟词僻义
term	n.	术语；时期；条件	The term is often used loosely, which can lead to misunderstanding.	这个术语常被宽泛地使用，因而可能导致误解。	in terms of 表示“就……而言”；terms 复数还可表示条件、关系。	technical term|in terms of|on equal terms	word::普通的“词”|concept::强调词背后的概念	terminology n. 术语体系|terminal adj. 末端的	The two theories describe the same process in different terms.::这两种理论用不同术语描述同一过程。	熟词僻义
maintain	v.	坚持认为；维持；维护	Some economists maintain that higher income does not automatically produce greater happiness.	一些经济学家坚持认为，更高收入不会自动带来更多幸福。	maintain that... 是考研阅读高频义，表示“坚持某观点”；另常见 maintain stability。	maintain that|maintain stability|maintain a balance	claim::声称，不一定强调持续坚持|preserve::强调使某物保持原状	maintenance n. 维护|maintainable adj. 可维持的	The researchers maintain that the correlation is not evidence of causation.::研究人员坚持认为，相关性并不能证明因果关系。	熟词僻义
assume	v.	假定；承担；呈现	The model assumes that individuals have access to complete information.	该模型假定个人能够获得完整信息。	assume that... 表示为推理暂作假设；assume responsibility 表示“承担责任”。	assume that|assume responsibility|assume a role	presume::根据一定可能性作推定|suppose::日常语体中更普通的“假设”	assumption n. 假设|assumed adj. 假定的	We should not assume that silence means agreement.::我们不应假定沉默就意味着同意。	学术论证
establish	v.	证实；确立；建立	The available evidence does not establish a causal link between the two trends.	现有证据并不能证实这两种趋势之间存在因果联系。	establish a fact/link 表示“证实”；establish a system/institution 表示“建立”。	establish a link|establish a principle|establish an institution	prove::强调以充分证据证明为真|found::专指创建组织、城市等	establishment n. 建立；机构|established adj. 公认的	The study establishes a clear relationship between sleep and memory.::该研究确立了睡眠与记忆之间的明确关系。	学术论证
constitute	v.	构成；组成；被视为	Small firms constitute the majority of employers in the region.	小企业构成该地区雇主的多数。	A constitutes B 表示“A 构成 B”；正式语体中也可表示“相当于、构成某种行为”。	constitute a majority|constitute evidence|constitute a threat	comprise::整体由若干部分组成，常用 the whole comprises parts|compose::部分组成整体，常用 parts compose the whole	constitution n. 构成；宪法|constituent n. 组成部分	Failure to disclose the data may constitute a breach of trust.::未披露数据可能构成对信任的破坏。	学术论证
derive	v.	源自；获得；推导	Much of the institution's authority derives from public trust.	该机构的大部分权威源自公众信任。	derive from 表示“源自”；derive A from B 表示“从 B 获得/推导 A”。	derive from|derive benefit from|derive a conclusion	originate::强调起源于某处或某时|deduce::强调依据逻辑推导结论	derivation n. 派生；推导|derivative adj. 派生的	Researchers derived the estimate from several independent data sets.::研究人员从多个独立数据集中推导出该估计值。	学术论证
interpret	v.	解释；理解；解读	The same evidence can be interpreted in several different ways.	同一证据可以有多种不同的解读方式。	interpret A as B 表示“把 A 理解为 B”；注意与 translate“翻译语言”区分。	interpret the results|interpret as|widely interpreted	explain::说明原因或含义|translate::在语言之间翻译	interpretation n. 解释|interpreter n. 口译员|interpretive adj. 解释性的	It would be a mistake to interpret correlation as causation.::把相关性理解为因果关系将是错误的。	学术论证
concern	v.	涉及；使担忧；与……有关	The final chapter concerns the ethical responsibilities of researchers.	最后一章涉及研究人员的伦理责任。	concern 作动词可表示“涉及”；be concerned with 表示“涉及/关注”，be concerned about 表示“担忧”。	concern the public|be concerned with|be concerned about	involve::表示包含或牵涉|worry::普通地表示使人担忧	concern n. 关切；担忧|concerning prep. 关于	This debate concerns how limited public resources should be allocated.::这场讨论涉及有限公共资源应如何分配。	熟词僻义
regard	v.	把……看作；认为；注视	Many readers regard the proposal as unrealistic but intellectually valuable.	许多读者认为该提议不切实际，但在思想上有价值。	regard A as B 是固定结构；with regard to 表示“关于”。	regard as|with regard to|in this regard	consider::可直接接宾语补足语，语体更宽泛|view::强调从某一角度看待	regard n. 尊重；方面|regardless adv. 不顾	The law regards access to basic education as a public right.::法律把接受基础教育视为一项公共权利。	熟词僻义
figure	v.	占重要地位；出现；计算	Economic factors figure prominently in the debate over migration.	经济因素在移民问题的讨论中占据重要地位。	figure prominently/large in 表示“在……中很重要”；figure out 表示“弄清楚”。	figure prominently|figure out|a key figure	appear::仅表示出现|calculate::专指计算数值	figure n. 数字；人物；图形|figurative adj. 比喻的	Questions of fairness figure heavily in the policy discussion.::公平问题在政策讨论中占有重要分量。	熟词僻义
observe	v.	指出；评论；观察；遵守	The author observes that efficiency and fairness do not always coincide.	作者指出，效率与公平并不总是一致。	学术写作中的 observe that 常表示“指出/评论”；另有 observe a rule“遵守规则”。	observe that|observe a pattern|observe the law	note::简洁地指出|notice::强调无意中注意到	observation n. 观察；评论|observer n. 观察者	Several scholars have observed a similar pattern in other countries.::几位学者在其他国家也观察到了类似模式。	熟词僻义
engage	v.	使参与；从事；吸引	Universities should engage students in evaluating competing arguments.	大学应让学生参与评估相互竞争的论点。	engage sb in sth 表示“使某人参与”；engage in 表示“从事”。	engage in debate|engage students in|actively engage	involve::强调让某人成为活动的一部分|attract::强调引起注意或兴趣	engagement n. 参与；约定|engaged adj. 忙于；投入的	Citizens are more likely to engage in public debate when information is accessible.::信息易于获取时，公民更可能参与公共讨论。	熟词僻义
conduct	v.	开展；实施；引导	The team will conduct a follow-up survey to test the initial findings.	该团队将开展后续调查，以检验最初的研究结果。	conduct research/survey/experiment 是正式搭配；名词 conduct 表示“行为”。	conduct research|conduct a survey|conduct an experiment	carry out::语义相近，较通用|perform::常用于任务、操作或表演	conduct n. 行为|conductor n. 指挥；导体	Independent researchers conducted the same experiment under stricter conditions.::独立研究人员在更严格条件下开展了同一实验。	学术方法
available	adj.	可获得的；可利用的；有空的	The conclusion should be based on the best evidence currently available.	结论应以目前可获得的最佳证据为基础。	available 常后置修饰名词，如 evidence available；be available to sb 表示“可供某人使用”。	readily available|available evidence|be available to	accessible::强调易于进入、理解或获得|obtainable::强调能够取得	availability n. 可获得性	Reliable data are not equally available in every region.::并非每个地区都能同等获得可靠数据。	学术方法
decline	v.	下降；衰退；婉拒	The journal declined to publish the paper without access to the underlying data.	由于无法获得底层数据，该期刊拒绝发表这篇论文。	decline to do 是较正式的“拒绝做”；decline by/to/from 用于数量下降。	decline to comment|decline sharply|a gradual decline	refuse::更直接、更强烈的拒绝|decrease::中性地表示数量减少	decline n. 下降|declining adj. 日益减少的	Participation declined after the financial support was withdrawn.::资金支持撤回后，参与度下降了。	熟词僻义
reserve	v.	保留；预留；预订	The author reserves judgment until more reliable evidence becomes available.	作者在获得更多可靠证据之前暂不作判断。	reserve judgment 表示“保留判断”；reserve A for B 表示“为 B 留出 A”。	reserve judgment|reserve the right|reserve resources for	retain::继续保有已有事物|preserve::保护某物不受损或改变	reserve n. 储备|reservation n. 保留意见；预订	Researchers reserved part of the sample for independent testing.::研究人员保留了部分样本用于独立检验。	熟词僻义
secure	v.	获得；确保；使安全	The research team failed to secure enough funding for a national survey.	研究团队未能获得足够资金开展全国性调查。	secure funding/support/access 表示“成功获得”；secure sth against 表示“使……免受”。	secure funding|secure access|secure support	obtain::中性地表示获得|ensure::强调确保某结果发生	secure adj. 安全的|security n. 安全；保障	The agreement secured wider access to public data.::该协议确保了更广泛的公共数据获取权。	熟词僻义
discipline	n.	学科；纪律；训练	Economics emerged as a distinct discipline in the modern university.	经济学在现代大学中发展成为一门独立学科。	discipline 在学术语境常指“学科”；academic discipline 是高频搭配。	academic discipline|professional discipline|maintain discipline	field::宽泛的研究领域|subject::学校课程或讨论主题	disciplinary adj. 学科的；纪律的|interdisciplinary adj. 跨学科的	The question requires knowledge from several different disciplines.::这个问题需要多个不同学科的知识。	熟词僻义
respect	n.	方面；尊重；重视	In this respect, the new theory differs sharply from the conventional view.	在这一方面，新理论与传统观点有明显差异。	in this respect 表示“在这方面”；with respect to 表示“关于”。	in this respect|with respect to|show respect for	aspect::事物的某个方面|regard::正式语境中的“关于/尊重”	respect v. 尊重|respective adj. 各自的|respectively adv. 分别地	The two methods are similar in some respects but not in others.::这两种方法在某些方面相似，在另一些方面则不同。	熟词僻义
appreciate	v.	理解并重视；欣赏；感激	To appreciate the argument, readers must first understand its historical background.	要充分理解这一论点，读者必须先了解其历史背景。	appreciate 可表示“充分理解某事的重要性”，不仅是“感激”。	appreciate the significance|fully appreciate|appreciate the difficulty	understand::一般理解|recognize::认识到某事实或价值	appreciation n. 理解；欣赏|appreciative adj. 感激的	It is difficult to appreciate the scale of the change from a single statistic.::仅凭一个统计数字很难理解变化的规模。	熟词僻义
accommodate	v.	容纳；适应；顾及	The framework must be flexible enough to accommodate regional differences.	该框架必须足够灵活，以顾及地区差异。	accommodate differences/needs 表示“容纳、顾及”；accommodate oneself to 表示“使自己适应”。	accommodate differences|accommodate demand|accommodate the needs of	adapt::主动改变以适应环境|adjust::作较小调整以适应	accommodation n. 住宿；调适|accommodating adj. 乐于通融的	The timetable was revised to accommodate students with part-time jobs.::时间表经过调整，以照顾兼职学生的需要。	学术与社会
advocate	v.	主张；提倡；拥护	The report advocates greater public investment in preventive health care.	该报告主张增加对预防性医疗的公共投入。	advocate 后直接接名词或 doing，不接 advocate to do；作名词表示“倡导者”。	advocate reform|advocate doing|a strong advocate of	promote::推动某事发展|recommend::提出建议，语气通常较弱	advocate n. 倡导者|advocacy n. 倡导	Many scholars advocate treating access to information as a basic right.::许多学者主张把信息获取视为一项基本权利。	观点态度
alternative	n.	替代方案；可供选择的事物	The proposal offers no realistic alternative to the existing system.	该提议没有为现行制度提供现实可行的替代方案。	an alternative to 是固定搭配；alternative choice 常显得重复。	an alternative to|a viable alternative|seek alternatives	option::可选择的一个项目|substitute::可替代原事物的人或物	alternative adj. 替代的|alternatively adv. 作为另一选择	Public transport provides an alternative to private car use.::公共交通为使用私家车提供了替代选择。	观点态度
arbitrary	adj.	任意的；武断的；缺乏合理依据的	The boundary between the two categories is largely arbitrary.	这两个类别之间的界线在很大程度上是人为任意划定的。	arbitrary 强调决定没有一致原则或充分理由，并非只是“随机”。	an arbitrary distinction|arbitrary rule|appear arbitrary	random::由随机过程产生|subjective::基于个人判断或感受	arbitrarily adv. 任意地|arbitrariness n. 任意性	An arbitrary deadline may encourage speed at the expense of quality.::一个武断设定的期限可能会以牺牲质量为代价鼓励速度。	批判性阅读
apparent	adj.	表面上的；明显的	The apparent contradiction disappears once the terms are defined more carefully.	一旦更仔细地界定术语，表面上的矛盾就会消失。	apparent 可表示“显而易见的”，也可表示“表面如此但未必真实”，需结合语境。	an apparent contradiction|become apparent|for no apparent reason	obvious::明确且很容易看出|seeming::强调看似如此但可能不真实	apparently adv. 显然；据说	The benefits are less apparent when long-term costs are included.::把长期成本考虑在内后，这些好处就不那么明显了。	批判性阅读
appropriate	adj.	合适的；恰当的	A single national standard may not be appropriate for every local community.	单一的全国标准未必适合每个地方社区。	be appropriate for/to；注意 appropriate 作动词时还可表示“拨款、挪用”。	an appropriate response|appropriate for the context|socially appropriate	suitable::适合某用途或情境|proper::符合规范、礼仪或正确做法	appropriately adv. 恰当地|appropriateness n. 适当性	Researchers must choose methods appropriate to the question being asked.::研究人员必须选择适合所提问题的方法。	学术方法
assess	v.	评估；判断；估量	The study assesses whether the program produces lasting changes in behavior.	该研究评估该项目是否会带来持久的行为变化。	assess risk/impact/effectiveness；通常强调依据证据作系统判断。	assess the impact|assess risk|critically assess	evaluate::按标准评价价值或效果|estimate::对数量或程度作近似估计	assessment n. 评估|assessor n. 评估者	It is too early to assess the long-term consequences of the policy.::现在评估该政策的长期后果还为时过早。	学术方法
attribute	v.	把……归因于；认为属于	It is misleading to attribute the entire decline to a single policy change.	把全部下降归因于一项政策变化是误导性的。	attribute A to B 表示“把 A 归因于 B”；名词 attribute 表示“属性”。	attribute success to|be attributed to|attribute a view to	ascribe::正式语体，表示归因或归属于|credit::常表示把功劳归于某人	attribute n. 属性|attribution n. 归因	The improvement was partly attributed to better teacher training.::这一改善部分归因于更好的教师培训。	因果关系
capacity	n.	能力；容量；身份	Institutions differ greatly in their capacity to respond to rapid change.	各机构应对快速变化的能力差异很大。	capacity to do 强调潜在或制度性能力；in one's capacity as 表示“以……身份”。	the capacity to|production capacity|in the capacity of	ability::个人做某事的一般能力|capability::具备完成特定任务的能力	capable adj. 有能力的|incapacity n. 无能力	The reform increased the local government's capacity to deliver services.::改革提升了地方政府提供服务的能力。	学术与社会
challenge	v.	质疑；挑战；对……提出异议	The findings challenge the assumption that economic growth benefits everyone equally.	这些研究结果质疑了“经济增长会让所有人同等受益”这一假设。	challenge an assumption/view 表示“质疑”；不只是“面临困难”。	challenge an assumption|challenge a decision|pose a challenge	question::提出疑问或怀疑|dispute::明确否认某主张的真实性或合法性	challenge n. 挑战|challenging adj. 有挑战性的	New evidence has challenged the conventional account of the event.::新证据对这一事件的传统解释提出了质疑。	批判性阅读
complex	adj.	复杂的；由多部分组成的	Human motivation is too complex to be explained by a single factor.	人的动机过于复杂，无法由单一因素解释。	complex 强调组成部分相互关联；complicated 更强调难以理解或操作。	a complex system|highly complex|complex relationship	complicated::繁复难懂或难处理|intricate::细节多且关系精密	complexity n. 复杂性	The relationship between income and health is complex and indirect.::收入与健康之间的关系复杂且并非直接。	学术论证
comprehensive	adj.	全面的；综合的	A comprehensive explanation must consider economic, cultural, and psychological factors.	全面的解释必须考虑经济、文化和心理因素。	comprehensive 强调覆盖范围广且较完整；常修饰 review、survey、policy。	a comprehensive review|comprehensive evidence|comprehensive reform	complete::强调没有遗漏|systematic::强调按系统步骤进行	comprehensively adv. 全面地|comprehensiveness n. 全面性	The report provides a comprehensive overview of recent research.::该报告对近期研究作了全面综述。	学术论证
conceive	v.	构想；设想；理解	It is difficult to conceive of progress without some willingness to accept risk.	很难设想在完全不愿承担风险的情况下还能取得进步。	conceive of A as B / conceive of doing；正式语体中表示“设想、理解”。	conceive of|conceive a plan|widely conceived	imagine::日常的想象|formulate::把想法明确形成方案或表述	conception n. 概念；构想|conceivable adj. 可想象的	Justice is often conceived as equal treatment under common rules.::正义常被理解为在共同规则下受到平等对待。	抽象论述
conclude	v.	得出结论；结束	The researchers conclude that the evidence is suggestive but not decisive.	研究人员得出结论：这些证据具有提示性，但并非决定性的。	conclude that 表示得出结论；conclude from 表示从……推断；不要与 include 混淆。	conclude that|conclude from evidence|conclude a discussion	infer::依据线索推断未明说的信息|finish::普通地表示结束	conclusion n. 结论|conclusive adj. 决定性的	We cannot conclude from correlation alone that one factor causes the other.::我们不能仅凭相关性就断定一个因素导致另一个因素。	学术论证
consistent	adj.	一致的；符合的；始终如一的	The observed pattern is consistent with the theory, but it does not prove the theory.	观察到的模式与该理论一致，但并不能证明该理论。	be consistent with 表示“与……一致/相符”；consistent in 表示在行为上始终一致。	consistent with|internally consistent|consistent pattern	compatible::能够共存、不冲突|uniform::在各处保持相同形式或水平	consistency n. 一致性|consistently adv. 一贯地	The results are broadly consistent across age groups.::不同年龄组的结果大体一致。	学术论证
constrain	v.	限制；约束；强迫	Limited funding can constrain the range of questions a study is able to examine.	有限资金会限制一项研究能够考察的问题范围。	constrain choice/growth/action；常用于说明资源、制度或条件造成的限制。	constrain growth|be constrained by|constrain choice	restrict::通过规则或边界限制|limit::最一般的“限制”	constraint n. 约束|constrained adj. 受限制的	Researchers were constrained by the lack of reliable historical data.::研究人员受到可靠历史数据不足的限制。	因果关系
context	n.	背景；语境；上下文	A statement that seems extreme in isolation may appear reasonable in context.	一句孤立看来极端的话，放在语境中可能显得合理。	in context / in the context of；考研阅读中词义和观点都需结合上下文判断。	in context|historical context|in the context of	background::提供理解所需的背景信息|setting::事件发生的具体环境	contextual adj. 语境的|contextualize v. 置于背景中理解	The policy can only be understood within its historical context.::只有放在历史背景中才能理解这项政策。	阅读方法
conventional	adj.	传统的；常规的；约定俗成的	The new findings call the conventional explanation into question.	新发现使传统解释受到质疑。	conventional wisdom 表示“传统看法/普遍观念”，常在转折中被质疑。	conventional wisdom|conventional method|conventional view	traditional::由长期传统传承|orthodox::被某一群体认可的正统观点	convention n. 惯例；大会|conventionally adv. 按惯例	The study uses a method that differs from conventional practice.::该研究采用了不同于常规做法的方法。	批判性阅读
critical	adj.	关键的；批判性的；危急的	Access to reliable data is critical to evaluating the success of the reform.	获得可靠数据对于评估改革成效至关重要。	be critical to 表示“对……至关重要”；critical of 表示“批评……”。	critical to success|critical analysis|be critical of	crucial::极其关键，语气较强|skeptical::持怀疑态度，不等于批判分析	criticism n. 批评|critically adv. 批判性地	Critical reading requires attention to both evidence and assumptions.::批判性阅读要求同时关注证据和假设。	熟词僻义
demonstrate	v.	证明；表明；展示	The experiment demonstrates that small changes in wording can influence judgment.	该实验证明，措辞的细微变化会影响判断。	demonstrate that 常用于证据“证明/表明”；show 语体更普通。	demonstrate a relationship|demonstrate that|clearly demonstrate	show::普通地显示|prove::要求更充分、决定性的证据	demonstration n. 证明；示范|demonstrable adj. 可证明的	The data demonstrate a steady decline in public trust.::数据显示公众信任持续下降。	学术论证
distinguish	v.	区分；辨别；使有别于	Good analysis must distinguish correlation from causation.	好的分析必须区分相关性与因果关系。	distinguish A from B / distinguish between A and B 是高频结构。	distinguish between|distinguish A from B|clearly distinguish	differentiate::较正式，强调识别差异|separate::强调把事物分开	distinction n. 区别|distinct adj. 明显不同的	The author distinguishes short-term effects from long-term consequences.::作者区分了短期影响与长期后果。	阅读方法
dominate	v.	支配；占主导地位	A small number of large firms dominate the digital advertising market.	少数大型公司支配着数字广告市场。	dominate a market/debate；也可用 be dominated by 表示“由……占主导”。	dominate the market|dominate the debate|be dominated by	control::直接控制行为或资源|prevail::某观点或状况最终占优势	dominant adj. 主导的|dominance n. 支配地位	Economic concerns dominated the discussion.::经济问题在讨论中占据主导地位。	社会经济
economy	n.	节约；简洁；经济体系	The theory achieves economy by explaining several patterns with one principle.	该理论用一个原理解释多种模式，因而具有简洁性。	economy 在正式语境可表示“节约、简洁”；economy of expression 指表达简练。	economy of expression|market economy|achieve economy	efficiency::以较少资源取得较好结果|frugality::个人生活中的节俭	economic adj. 经济的|economical adj. 节约的|economist n. 经济学家	The essay is admired for the economy and precision of its language.::这篇文章因语言简练而精确受到赞赏。	熟词僻义
emerge	v.	出现；显露；形成	A more complicated picture emerges when regional differences are considered.	把地区差异考虑在内后，会呈现出一幅更复杂的图景。	emerge from 表示“从……中出现”；常与 pattern、evidence、picture 搭配。	a pattern emerges|emerge from|newly emerging	appear::一般出现|arise::问题或情况产生，常无被动语态	emergence n. 出现|emerging adj. 新兴的	Several common themes emerged from the interviews.::访谈中呈现出几个共同主题。	学术论证
enable	v.	使能够；使成为可能	Digital archives enable researchers to compare sources from different periods.	数字档案使研究人员能够比较不同时期的资料。	enable sb to do 是固定结构；主语常为技术、制度或条件。	enable someone to|enable access|technology-enabled	allow::给予许可或提供可能|facilitate::使过程更容易、更顺畅	enablement n. 使能|enabled adj. 被启用的	The new method enables more precise measurement of small changes.::新方法使更精确地测量微小变化成为可能。	学术方法
encounter	v.	遇到；遭遇	Researchers often encounter difficulties when comparing data collected under different standards.	研究人员在比较按不同标准收集的数据时常会遇到困难。	encounter a problem/resistance；语体比 meet with 更正式。	encounter difficulty|encounter resistance|first encounter	meet::普通地遇见人或情况|face::强调必须应对困难	encounter n. 遭遇；相遇	The proposal encountered strong opposition from local residents.::该提议遭到当地居民的强烈反对。	学术方法
equivalent	adj.	等同的；相当的；等价的	Equal treatment is not always equivalent to fair treatment.	同等对待并不总是等同于公平对待。	be equivalent to 是固定搭配；不说 equivalent with。	be equivalent to|roughly equivalent|functional equivalent	equal::数量、程度或地位相同|comparable::足以进行比较，但不一定相等	equivalence n. 等价|equivalently adv. 等价地	One year of experience was treated as equivalent to formal training.::一年工作经验被视为等同于正式培训。	逻辑关系
evaluate	v.	评价；评估；判断价值	The review evaluates the evidence for and against the proposed explanation.	这篇综述评估了支持和反对所提解释的证据。	evaluate effectiveness/evidence；比 assess 更突出按标准判断价值或效果。	evaluate evidence|evaluate performance|critically evaluate	assess::系统估量状态、风险或影响|judge::泛指作判断	evaluation n. 评价|evaluative adj. 评价性的	The program should be evaluated against clearly stated objectives.::应根据明确陈述的目标评价该项目。	学术方法
evidence	n.	证据；根据；迹象	There is little evidence that the policy has improved long-term employment.	几乎没有证据表明该政策改善了长期就业。	evidence 通常不可数；说 a piece/body of evidence，不说 an evidence。	available evidence|a body of evidence|evidence suggests	proof::足以证明结论为真的证据|indication::提示某事可能为真的迹象	evident adj. 明显的|evidently adv. 显然	The claim is not supported by sufficient empirical evidence.::这一主张没有得到充分实证证据的支持。	学术论证
exclude	v.	排除；不包括；阻止进入	The analysis excludes cases for which essential information is missing.	该分析排除了缺少关键信息的案例。	exclude A from B；rule out 常用于排除可能性。	exclude from|exclude a possibility|mutually exclusive	omit::有意或无意省略|eliminate::完全去除或淘汰	exclusion n. 排除|exclusive adj. 排他的；独有的	The data do not exclude the possibility of an alternative explanation.::这些数据并未排除另一种解释的可能性。	学术方法
explicit	adj.	明确的；清楚陈述的；直白的	The author makes no explicit distinction between temporary and permanent change.	作者没有明确区分暂时变化与永久变化。	explicit 强调直接说出，不需推断；与 implicit“隐含的”相对。	explicit statement|make explicit|explicitly state	clear::泛指清楚|specific::强调具体而非笼统	explicitly adv. 明确地|explicitness n. 明确性	The assumptions should be made explicit before the model is tested.::在检验模型前，应明确说明其假设。	阅读方法
facilitate	v.	促进；使便利；使更容易	Shared standards facilitate comparison across different studies.	共同标准有助于比较不同研究。	facilitate 后直接接名词/doing，正式语体常表示“使过程更顺利”。	facilitate communication|facilitate access|facilitate comparison	enable::使某人能够做某事|promote::推动发展或提高	facilitation n. 促进|facilitator n. 促进者	Clear definitions facilitate more productive debate.::清晰定义有助于开展更有成效的讨论。	学术方法
fundamental	adj.	根本的；基础的；极重要的	The debate raises a fundamental question about the purpose of education.	这场讨论提出了一个关于教育目的的根本问题。	fundamental 强调构成基础、不能轻易忽略；常修饰 principle、change、difference。	fundamental principle|fundamental difference|fundamental change	basic::最基本、入门层面|essential::不可缺少的	fundamentally adv. 根本上|fundamentals n. 基本原理	The two approaches rest on fundamentally different assumptions.::这两种方法建立在根本不同的假设上。	抽象论述
generate	v.	产生；引起；生成	The new policy may generate unintended costs for small businesses.	新政策可能给小企业带来意料之外的成本。	generate income/data/interest；正式语体中常替代 produce。	generate evidence|generate income|generate interest	produce::最普通的“产生”|create::强调创造原先不存在的事物	generation n. 产生；一代|generator n. 发生器	The survey generated a large amount of useful data.::这项调查产生了大量有用数据。	因果关系
grant	v.	承认；准予；授予	Even critics grant that the reform has improved access to basic services.	即使批评者也承认，这项改革改善了基础服务的可及性。	grant that 在让步论证中表示“承认”；grant sb sth 表示“授予”。	grant that|grant permission|research grant	admit::不情愿地承认某事实|concede::在争论中承认对方某一点	grant n. 拨款|granted adv. 诚然	Granted, the sample is small, but the pattern is still worth examining.::诚然，样本很小，但这一模式仍值得研究。	观点态度
identify	v.	识别；确定；认定	The study identifies three factors that influence public trust.	该研究确定了影响公众信任的三个因素。	identify A as B 表示“认定 A 为 B”；identify with 表示“认同”。	identify a factor|identify as|identify with	recognize::识别已知事物或承认事实|detect::发现不易察觉的信号或问题	identification n. 识别|identity n. 身份	Researchers identified education as the strongest predictor of participation.::研究人员认定教育是参与度最强的预测因素。	学术方法
imply	v.	暗示；意味着	A rise in productivity does not necessarily imply an improvement in well-being.	生产率提高并不一定意味着福祉改善。	imply 是说话者/事实“暗示”；infer 是读者“推断”，两者方向相反。	imply that|strongly imply|implications for	suggest::较弱地表明或提出|mean::一般地表示意味着	implication n. 含义；影响|implicit adj. 隐含的	The wording implies that responsibility lies with individuals rather than institutions.::措辞暗示责任在个人而非机构。	逻辑关系
impose	v.	强加；征收；施加	Uniform rules may impose heavy costs on communities with limited resources.	统一规则可能给资源有限的社区带来沉重成本。	impose A on B；常搭配 tax、burden、restriction、standard。	impose a burden on|impose restrictions|impose a tax	force::迫使某人行动|enforce::执行已经存在的法律或规则	imposition n. 强加；征收	The law imposes strict limits on the use of personal data.::法律对个人数据的使用施加严格限制。	因果关系
indicate	v.	表明；指出；显示	The results indicate that the effect is smaller than previously assumed.	结果表明，该影响比先前假定的更小。	indicate that 常用于谨慎陈述证据；语气通常弱于 prove。	indicate a trend|indicate that|clearly indicate	show::语体更普通|demonstrate::强调证据较有力	indication n. 迹象|indicative adj. 表明……的	Several indicators suggest that public confidence is recovering.::多项指标表明公众信心正在恢复。	学术论证
inevitable	adj.	不可避免的；必然发生的	Technological change is not inevitable; it is shaped by social choices.	技术变革并非不可避免，而是受到社会选择的塑造。	inevitable 常在作者反驳“必然论”时出现；be inevitable that/inevitable consequence。	an inevitable consequence|seem inevitable|far from inevitable	unavoidable::因现实条件而无法避免|certain::确定会发生，但不强调无法阻止	inevitably adv. 不可避免地|inevitability n. 必然性	Conflict is not an inevitable result of cultural difference.::冲突并非文化差异的必然结果。	观点态度
infer	v.	推断；推论	We cannot infer individual attitudes from national averages alone.	我们不能仅凭全国平均值推断个人态度。	infer A from B；注意不要与 imply 混淆：证据 implies，读者 infers。	infer from|reasonably infer|draw an inference	deduce::依据规则或逻辑必然推导|conclude::综合证据后得出结论	inference n. 推断|inferential adj. 推论的	From the absence of complaints, one should not infer complete satisfaction.::不应从没有投诉推断出所有人都完全满意。	逻辑关系
inhibit	v.	抑制；阻碍；约束	Fear of failure can inhibit creative thinking and open discussion.	对失败的恐惧会抑制创造性思维和开放讨论。	inhibit growth/innovation/expression；比 prevent 更强调削弱或限制过程。	inhibit growth|inhibit innovation|inhibit expression	restrain::控制行为或冲动|prevent::完全阻止某事发生	inhibition n. 抑制；拘谨|inhibitory adj. 抑制性的	Excessive regulation may inhibit the development of small firms.::过度监管可能抑制小企业发展。	因果关系
initial	adj.	最初的；开始阶段的	The initial results were encouraging, but later studies were less conclusive.	最初结果令人鼓舞，但后续研究的结论没有那么确定。	initial 表示时间或顺序上的第一阶段；常与 preliminary“初步的”近义。	initial stage|initial findings|initial response	preliminary::为正式工作做准备的初步阶段|original::最初的或原创的	initially adv. 最初|initial n. 首字母	The initial hypothesis was revised after new data became available.::新数据出现后，最初假设被修订。	学术方法
institute	v.	建立；实行；启动	Governments may institute temporary controls during a public emergency.	政府可能在公共紧急状态期间实行临时管制。	institute a policy/inquiry/reform 是正式搭配；作名词表示学院或研究机构。	institute reforms|institute an inquiry|research institute	establish::建立长期组织或制度|implement::执行已制定的计划或政策	institution n. 机构；制度|institutional adj. 制度的	The university instituted a review of its admissions procedures.::该大学启动了对招生程序的审查。	熟词僻义
integrate	v.	整合；使融入；结合	The model integrates economic data with evidence from social psychology.	该模型把经济数据与社会心理学证据整合起来。	integrate A with/into B；强调形成协调的整体。	integrate into|integrate A with B|fully integrated	combine::把事物放在一起|incorporate::把某一部分纳入更大的整体	integration n. 整合|integrated adj. 综合的	Schools need to integrate digital tools into ordinary classroom practice.::学校需要把数字工具融入日常课堂实践。	学术方法
justify	v.	证明……合理；为……辩护	The potential benefits do not justify ignoring the risks to privacy.	潜在收益并不能证明忽视隐私风险是合理的。	justify doing / justify a decision；be justified in doing 表示“有正当理由做”。	justify a claim|justify doing|be justified by	defend::针对批评进行辩护|explain::说明原因，但不一定证明合理	justification n. 正当理由|justifiable adj. 可辩护的	The authors must justify their choice of sample and method.::作者必须说明其样本与方法选择的合理性。	批判性阅读
mechanism	n.	机制；机理；运作方式	The study proposes a mechanism through which inequality affects health.	该研究提出了一种不平等影响健康的机制。	mechanism through/by which 是解释因果过程的高频结构；不只是“机械装置”。	causal mechanism|market mechanism|underlying mechanism	process::一系列变化或步骤|system::由相互关联部分组成的整体	mechanical adj. 机械的|mechanistic adj. 机械论的	The precise mechanism linking stress to disease remains uncertain.::压力与疾病之间的确切作用机制仍不确定。	学术论证
objective	adj.	客观的；不受个人偏见影响的	An objective assessment requires transparent criteria and independent evidence.	客观评估需要透明标准和独立证据。	objective 作形容词与 subjective 相对；作名词表示目标。	objective evidence|objective assessment|research objective	impartial::不偏袒任何一方|factual::基于事实而非意见	objectivity n. 客观性|objectively adv. 客观地	No measurement is entirely objective if the categories are poorly defined.::如果类别界定不清，任何测量都不可能完全客观。	熟词僻义
perceive	v.	认为；察觉；理解	People may perceive the same risk differently depending on their experience.	人们可能因经历不同而对同一风险有不同看法。	perceive A as B 表示“把 A 看作 B”；也可表示通过感官察觉。	perceive as|widely perceived|perceive a difference	view::从某角度看待|detect::发现具体信号或变化	perception n. 看法；感知|perceptive adj. 有洞察力的	The policy was widely perceived as unfair.::这项政策被普遍认为不公平。	认知与观点
perspective	n.	视角；观点；观察问题的方法	From a historical perspective, the change was gradual rather than sudden.	从历史视角看，这一变化是渐进的而非突然的。	from the perspective of / put sth in perspective 是高频搭配。	from a ... perspective|broader perspective|put in perspective	viewpoint::个人或群体的具体观点|context::帮助理解事件的背景	perspective adj. 透视的	Comparative research helps place national experience in a broader perspective.::比较研究有助于从更广阔视角看待一国经验。	阅读方法
principle	n.	原则；原理；基本准则	The policy is attractive in principle but difficult to implement in practice.	这项政策原则上很有吸引力，但在实践中难以实施。	in principle 表示“原则上”；on principle 表示“基于原则”。	in principle|basic principle|guiding principle	rule::具体规定或操作规则|value::认为重要的信念或标准	principled adj. 有原则的	The principle of equal opportunity does not guarantee equal outcomes.::机会均等原则并不保证结果相同。	抽象论述
proceed	v.	继续进行；着手；前往	The analysis cannot proceed without a clear definition of the key terms.	没有对关键术语的清晰定义，分析就无法继续。	proceed with sth / proceed to do；正式语体常表示下一步行动。	proceed with|proceed to do|proceed cautiously	continue::最普通的继续|advance::向前推进或取得进展	procedure n. 程序|proceedings n. 会议记录；诉讼	After reviewing the evidence, the committee proceeded to a vote.::审查证据后，委员会进入投票阶段。	学术方法
proportion	n.	比例；部分；均衡	A growing proportion of research is now published through open-access platforms.	越来越高比例的研究如今通过开放获取平台发表。	a large proportion of + 复数名词，谓语常根据 of 后名词决定。	a large proportion of|in proportion to|direct proportion	percentage::用百分数表达的比例|ratio::两个数量之间的比率	proportional adj. 成比例的|disproportionate adj. 不成比例的	The proportion of older workers has increased steadily.::年长劳动者的比例持续上升。	数据表达
pursue	v.	追求；从事；继续探究	Researchers should pursue explanations that can be tested against evidence.	研究人员应探索能够用证据检验的解释。	pursue a goal/career/policy/line of inquiry；语体较正式。	pursue a goal|pursue research|pursue a policy	seek::努力寻找或获得|follow::沿着既定道路或观点继续	pursuit n. 追求；事业	The team decided to pursue a different line of investigation.::团队决定沿着另一条研究思路继续探索。	学术方法
range	n.	范围；一系列；幅度	The survey covers a wide range of social and economic backgrounds.	这项调查涵盖广泛的社会和经济背景。	a range of 后接复数名词；range from A to B 表示范围从 A 到 B。	a wide range of|range from A to B|within the range	scope::研究或活动所涵盖的界限|variety::不同种类的多样性	range v. 变化；排列	Responses ranged from cautious support to strong opposition.::回应从谨慎支持到强烈反对不等。	数据表达
relevant	adj.	相关的；切题的；适用的	Only evidence relevant to the research question should influence the conclusion.	只有与研究问题相关的证据才应影响结论。	be relevant to 是固定搭配；relevant information 指与当前目的直接相关的信息。	relevant to|directly relevant|relevant evidence	related::存在某种联系，不一定切题|pertinent::正式，强调与当前问题直接相关	relevance n. 相关性|irrelevant adj. 不相关的	Historical examples remain relevant to current policy debates.::历史案例对当前政策讨论仍有参考意义。	阅读方法
retain	v.	保留；保持；记住	The revised model retains the central insight of the earlier theory.	修订后的模型保留了早期理论的核心见解。	retain information/control/ownership；比 keep 更正式。	retain control|retain information|retain the right	keep::最普通的保持或保留|preserve::保护某物不被破坏或改变	retention n. 保留；记忆|retentive adj. 记忆力强的	The policy retains several features of the previous system.::该政策保留了原制度的若干特征。	学术论证
reveal	v.	揭示；显示；透露	The interviews reveal a gap between official policy and everyday practice.	访谈揭示了官方政策与日常实践之间的差距。	reveal a pattern/difference；强调把原本隐藏或未知的事物显现出来。	reveal a pattern|reveal that|newly revealed	disclose::正式披露信息，常涉及保密|show::普通地显示	revelation n. 揭示；启示|revealing adj. 发人深省的	The data reveal that the benefits were unevenly distributed.::数据显示，这些收益分配并不均衡。	学术论证
significant	adj.	重要的；显著的；有统计意义的	The reform produced a significant improvement in access, but not in quality.	改革显著改善了可及性，但没有改善质量。	significant 可表示“重要的”或“统计上显著的”；不能自动等同于“影响很大”。	significant difference|statistically significant|significant role	important::一般的重要|substantial::数量或程度相当大	significance n. 重要性|significantly adv. 显著地	A statistically significant result may still have little practical significance.::统计上显著的结果在实践中仍可能意义不大。	数据表达
sustain	v.	维持；支撑；承受	Short-term enthusiasm is not enough to sustain long-term institutional change.	短期热情不足以维持长期制度变革。	sustain growth/attention/argument；也可表示“遭受损失、受伤”。	sustain growth|sustain interest|sustain an argument	maintain::保持某状态|support::提供物质、逻辑或情感支撑	sustainable adj. 可持续的|sustainability n. 可持续性	The evidence is insufficient to sustain such a strong conclusion.::这些证据不足以支撑如此强的结论。	因果关系
tendency	n.	倾向；趋势；习性	There is a tendency to treat measurable outcomes as the only outcomes that matter.	人们往往把可测量的结果当作唯一重要的结果。	a tendency to do 是高频结构；可描述行为倾向或长期趋势。	a tendency to|general tendency|long-term tendency	trend::可观察到的总体变化方向|inclination::个人偏好或意愿	tend v. 倾向|tendentious adj. 有偏向性的	The media have a tendency to simplify complex scientific debates.::媒体往往会简化复杂的科学争论。	批判性阅读
theory	n.	理论；学说；解释框架	A useful theory should explain known facts and generate testable predictions.	有用的理论既应解释已知事实，也应产生可检验的预测。	in theory 表示“理论上”；theory 不等于毫无根据的猜测。	in theory|economic theory|test a theory	hypothesis::可被具体检验的假设|model::对现实过程的简化表示	theoretical adj. 理论的|theorize v. 建立理论	The theory is elegant, but the supporting evidence remains limited.::这一理论很精巧，但支持它的证据仍然有限。	学术论证
transform	v.	彻底改变；转化；改造	Digital communication has transformed how scientific knowledge is shared.	数字通信彻底改变了科学知识的共享方式。	transform A into B 强调性质或形式发生显著变化。	transform into|fundamentally transform|social transformation	change::一般变化|convert::从一种形式或用途转换为另一种	transformation n. 转变|transformative adj. 变革性的	The discovery transformed a local debate into an international one.::这一发现把地方性讨论转变为国际性讨论。	因果关系
valid	adj.	有效的；有根据的；合理的	The criticism is valid, although it does not undermine the entire study.	这一批评是有根据的，但并不会削弱整项研究。	valid argument/reason/measure；在研究中可指测量是否真正测到目标概念。	valid argument|valid evidence|remain valid	sound::论证合理、基础稳固|legitimate::合法或正当，也可指合理关切	validity n. 有效性|validate v. 验证|invalid adj. 无效的	The conclusion is valid only under the stated assumptions.::该结论只在所述假设下有效。	批判性阅读
virtue	n.	优点；美德；效力	The main virtue of the method is its simplicity rather than its precision.	这种方法的主要优点是简单，而不是精确。	by virtue of 表示“凭借、由于”；virtue 在评价方法时常指“优点”。	the virtue of|by virtue of|moral virtue	advantage::相对于其他选择的优势|merit::值得肯定的价值或优点	virtuous adj. 有美德的	The proposal has the virtue of being easy to implement.::该提议的优点是容易实施。	熟词僻义
whereas	conj.	然而；而；鉴于	The first model emphasizes individual choice, whereas the second stresses social structure.	第一个模型强调个人选择，而第二个模型强调社会结构。	whereas 连接对比鲜明的两个分句；正式法律文本中也可表示“鉴于”。	A whereas B|whereas in contrast|whereas the latter	while::也可表示对比，但还可表示时间|by contrast::句间副词短语，需配合标点	whereas 无常用词族	Some regions experienced growth, whereas others continued to decline.::一些地区实现增长，而另一些地区继续衰退。	逻辑关系
yield	v.	产生；带来；让步	A larger sample may yield more reliable estimates of the effect.	更大的样本可能产生更可靠的效果估计。	yield results/benefits；yield to 表示“向……让步”；名词 yield 表示产量或收益。	yield results|yield benefits|yield to pressure	produce::普通的产生|generate::常指产生数据、收入或反应	yield n. 产量；收益	The analysis yielded no clear evidence of a causal relationship.::分析没有得出因果关系的明确证据。	学术方法
involve	v.	涉及；包含；使参与	The proposed reform would involve major changes to teacher training.	拟议改革将涉及教师培训的重大变化。	involve doing 表示“涉及做某事”；involve sb in 表示“使某人参与”。	involve doing|involve someone in|be closely involved	include::把某部分列入整体|entail::必然带来某种结果或要求	involvement n. 参与；牵涉|involved adj. 参与的；复杂的	Effective evaluation involves comparing outcomes with clearly defined goals.::有效评估涉及把结果与明确界定的目标进行比较。	学术方法'''


def parse_curated() -> list[dict]:
    rows = []
    for lineno, raw in enumerate(CURATED_TSV.splitlines(), 1):
        if not raw.strip():
            continue
        cols = raw.split("\t")
        if len(cols) != 11:
            raise ValueError(f"Line {lineno}: expected 11 fields, got {len(cols)}")
        word, pos, meaning, sentence, zh, usage, collocs, related, family, extra, topic = cols

        def pairs(text: str, left: str, right: str) -> list[dict]:
            output = []
            for part in text.split("|"):
                a, b = part.split("::", 1)
                output.append({left: a.strip(), right: b.strip()})
            return output

        rows.append(
            {
                "word": word.strip(),
                "partOfSpeech": pos.strip(),
                "meaningZh": meaning.strip(),
                "sentenceEn": sentence.strip(),
                "sentenceZh": zh.strip(),
                "usageNotes": usage.strip(),
                "collocations": [x.strip() for x in collocs.split("|") if x.strip()],
                "relatedExpressions": pairs(related, "expression", "note"),
                "wordFamily": [x.strip() for x in family.split("|") if x.strip()],
                "extraExamples": pairs(extra, "en", "zh"),
                "topic": topic.strip(),
            }
        )
    return rows


def clean_phonetic(value: str) -> str:
    value = (value or "").strip().strip("/")
    return f"/{value}/" if value else ""


def word_forms(base: dict) -> list[str]:
    candidates = [base.get("word", "")]
    candidates.extend((base.get("forms") or {}).values())
    return sorted({str(x).strip() for x in candidates if str(x).strip()}, key=lambda x: (-len(x), x))


def split_cloze(sentence: str, base: dict) -> tuple[str, str, str]:
    found = []
    for candidate in word_forms(base):
        matches = list(re.finditer(rf"(?<![A-Za-z]){re.escape(candidate)}(?![A-Za-z])", sentence, flags=re.I))
        found.extend((candidate, match) for match in matches)
    # Multiple forms may be identical in the source; deduplicate by span.
    by_span = {(m.start(), m.end()): m for _, m in found}
    if len(by_span) != 1:
        raise ValueError(
            f"Expected exactly one lemma/form for {base.get('word')!r}; "
            f"found {len(by_span)} spans in: {sentence}"
        )
    match = next(iter(by_span.values()))
    answer = sentence[match.start() : match.end()]
    return sentence[: match.start()], answer, sentence[match.end() :]


def build(cet6_lexicon_path: Path, out_lexicon: Path, out_cards: Path) -> None:
    source = json.loads(cet6_lexicon_path.read_text(encoding="utf-8"))
    all_entries = source.get("entries", [])
    entries = [entry for entry in all_entries if "ky" in entry.get("examTags", [])]
    entries.sort(
        key=lambda e: (
            e.get("frequency", {}).get("modern") or 10**9,
            e.get("frequency", {}).get("bnc") or 10**9,
            e.get("word", "").lower(),
        )
    )
    by_word = {entry["word"].lower(): entry for entry in entries}
    curated = parse_curated()
    if len(curated) != 100 or len({item["word"] for item in curated}) != 100:
        raise ValueError(f"Curated set must contain 100 unique words; got {len(curated)}")

    compact_entries = [
        {
            "id": entry["id"],
            "word": entry["word"],
            "phonetic": clean_phonetic(entry.get("phonetic", "")),
            "partsOfSpeech": entry.get("partsOfSpeech", []),
            "definitionsEn": entry.get("definitionsEn", []),
            "meaningsZh": entry.get("meaningsZh", []),
            "examTags": entry.get("examTags", []),
            "frequency": entry.get("frequency", {}),
            "forms": entry.get("forms", {}),
        }
        for entry in entries
    ]
    lexicon = {
        "schemaVersion": 2,
        "id": "kaoyan-ecdict-core-4112",
        "name": "考研英语核心基础词库（ECDICT ky∩cet6 标签）",
        "version": "4.2.0",
        "generatedAt": "2026-07-12",
        "entryCount": len(compact_entries),
        "scopeNote": "本文件收录当前 WordLoop ECDICT 数据中同时带 ky 与 cet6 标签的 4112 个核心词条，适合作为考研核心学习与检索集合；不宣称为教育部官方或唯一完整词表。",
        "source": {
            "dataset": "ECDICT",
            "repository": "skywind3000/ECDICT",
            "license": "MIT",
            "filter": "examTags contains ky and cet6",
        },
        "entries": compact_entries,
    }

    cards = []
    for index, item in enumerate(curated, 1):
        base = by_word.get(item["word"].lower())
        if not base:
            raise ValueError(f"Missing from kaoyan core lexicon: {item['word']}")
        prefix, answer, suffix = split_cloze(item["sentenceEn"], base)
        card = {
            "id": f"kaoyan-{index:04d}-{item['word']}",
            "libraryId": "kaoyan",
            "deck": "考研英语精选 100",
            "type": "cloze",
            "word": item["word"],
            "pronunciation": clean_phonetic(base.get("phonetic", "")),
            "answerPronunciation": clean_phonetic(base.get("phonetic", "")),
            "partOfSpeech": item["partOfSpeech"],
            "meaningZh": item["meaningZh"],
            "sentenceEn": item["sentenceEn"],
            "sentenceZh": item["sentenceZh"],
            "clozePrefix": prefix,
            "clozeAnswer": answer,
            "clozeSuffix": suffix,
            "targetEnglish": "",
            "acceptedAnswers": [answer],
            "tags": ["考研英语", item["topic"]],
            "definitionZh": item["meaningZh"],
            "usageNotes": item["usageNotes"],
            "collocations": item["collocations"],
            "relatedExpressions": item["relatedExpressions"],
            "wordFamily": item["wordFamily"],
            "extraExamples": item["extraExamples"],
            "difficulty": 4,
            "source": "ECDICT 基础字段 + WordLoop 原创考研学习内容",
            "isSuspended": False,
            "lexiconRef": base["id"],
            "quality": {
                "senseAccuracy": 5,
                "translationAccuracy": 5,
                "contextStrength": 5,
                "reviewStatus": "curated",
            },
            "generation": {
                "contentVersion": "kaoyan-curated-100-v1",
                "generatedAt": "2026-07-12",
                "method": "manual curation + structural validation",
            },
        }
        cards.append(card)

    payload = {
        "schemaVersion": 2,
        "id": "kaoyan-curated-100",
        "name": "考研英语精选 100",
        "version": "4.2.0",
        "generatedAt": "2026-07-12",
        "cardCount": len(cards),
        "description": "首批 100 张考研增强学习卡，重点覆盖熟词僻义、学术论证、逻辑关系、因果表达与阅读方法。",
        "source": {
            "baseLexicon": "ECDICT ky∩cet6 tags",
            "learningContent": "WordLoop original",
        },
        "cards": cards,
    }

    out_lexicon.parent.mkdir(parents=True, exist_ok=True)
    out_cards.parent.mkdir(parents=True, exist_ok=True)
    out_lexicon.write_text(json.dumps(lexicon, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    out_cards.write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"Wrote {len(compact_entries)} kaoyan core entries -> {out_lexicon}")
    print(f"Wrote {len(cards)} curated cards -> {out_cards}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cet6-lexicon", type=Path, required=True)
    parser.add_argument("--lexicon-output", type=Path, required=True)
    parser.add_argument("--cards-output", type=Path, required=True)
    args = parser.parse_args()
    build(args.cet6_lexicon, args.lexicon_output, args.cards_output)


if __name__ == "__main__":
    main()
