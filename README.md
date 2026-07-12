# WordLoop v4.1.1：CET-6 基础词库与精选学习卡

WordLoop 是一个以主动输入、语境记忆、逐级提示和间隔复习为核心的纯静态英语学习网站。可部署到 CloudBase、Cloudflare Workers Static Assets、GitHub Pages 或其他静态托管平台。

v4.1.1 为部署兼容修复版：CET-6 数据优先从 `data/cet6/` 读取，并在平台未保留子目录时尝试根目录同名备用文件；静态资源增加版本参数以避免旧缓存。

## v4.1 已完成

- 接入 **CET-6 基础词库 5407 条**：这是 ECDICT 中带 `cet6` 标签词条的全量提取；
- 发布 **CET-6 精选 100 张增强学习卡**；
- 每张增强卡包含英文语境、中文翻译、音标、词性、释义、用法提醒、搭配、相关表达、词族和扩展例句；
- 新增 CET-6 基础词库浏览器，支持英文或中文释义搜索和分页；
- 支持在“核心 200”和“CET-6 精选 100”之间切换；
- 不同词库分别保存按天学习计划，不会把两个词库混在同一计划中；
- 保留原有 200 张卡片、错词复习、发音、逐级提示、详细解析和上一题/下一题功能；
- 加入数据来源、范围说明和第三方许可文件。

> 5407 指 ECDICT 数据中带 `cet6` 标签的全部词条，不代表唯一或官方六级考试大纲词数。

## 运行

```bash
python -m http.server 8000 --directory public
```

浏览器访问：

```text
http://localhost:8000
```

## 使用 CET-6 词库

1. 打开“词库中心”；
2. 进入“CET-6”；
3. 点击“启用这个词库”；
4. 网站加载 100 张增强学习卡，并自动建立 5 天计划（默认每天 20 个）；
5. “浏览 5407 基础词条”仅用于查词和后续内容生成，不会把全部基础词条直接变成未经审核的练习题。

## 主要数据文件

```text
public/data/cet6/cet6_lexicon.json
public/data/cet6/cet6_cards_100.json
public/data/library_manifest.json
```

- `cet6_lexicon.json`：5407 条基础词典数据；
- `cet6_cards_100.json`：100 张可直接学习的增强卡；
- `library_manifest.json`：词库目录、状态、来源和数量。

## 词库生成工具

```text
tools/lexicon_builder/
```

其中 `build_cet6_v4_1.py` 可以从提取后的 ECDICT CET-6 数据重新构建本次发布文件。原始 ECDICT CSV 不提交到仓库。

## 本地数据

当前学习进度仍保存在当前域名下的浏览器 `localStorage`：

- 同一域名、设备和浏览器可以继续学习；
- Cloudflare 与 CloudBase 地址的数据彼此独立；
- 清理浏览器数据会导致记录丢失；
- 建议定期从“导入导出”页面备份 JSON。

大型词库原始数据采用静态 JSON 按需读取，只有启用的学习卡写入本地学习状态。后续将迁移到 IndexedDB，并增加 CloudBase 云同步。

## 部署

### CloudBase

把 `public/` 内所有文件和子目录作为静态网站根目录上传，必须保留：

```text
data/cet6/cet6_lexicon.json
data/cet6/cet6_cards_100.json
```

### Cloudflare Workers Static Assets

仓库根目录的 `wrangler.jsonc` 已指向：

```json
{"assets":{"directory":"./public"}}
```

GitHub `main` 分支更新后，已连接的 Cloudflare 项目会自动重新部署。

## 文档

- `ROADMAP.md`：后续产品计划；
- `CHANGELOG_v4.1.md`：版本变更；
- `TEST_REPORT_v4.1.md`：数据与功能检查；
- `THIRD_PARTY_NOTICES.md`：ECDICT 来源与许可；
- `docs/AI_CONTENT_PIPELINE.md`：后续大规模高质量内容生成流程。
