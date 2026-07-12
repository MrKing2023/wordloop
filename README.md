# WordLoop v4.2.1：CET-6 与考研英语词库

WordLoop 是一个以主动输入、语境记忆、逐级提示和间隔复习为核心的纯静态英语学习网站，可部署到 CloudBase、Cloudflare Workers Static Assets、GitHub Pages 或其他静态托管平台。

## v4.2 已完成

- 保留 CET-6 的 **5407 条基础词条 + 100 张增强学习卡**；
- 新增考研英语 **4112 条核心基础词条 + 100 张原创增强学习卡**；
- 考研卡重点覆盖熟词僻义、学术论证、逻辑关系、因果表达、数据描述和阅读方法；
- 每张考研卡包含英文语境、中文翻译、音标、词性、考点用法、3 个常见搭配、近义表达区别、词族和扩展例句；
- 支持在“核心 200”“CET-6 精选 100”“考研英语精选 100”之间切换；
- 每个词库独立保存按天学习计划与进度；
- CET-6 与考研英语都提供基础词库浏览器，可按英文单词或中文释义搜索；
- 延续 v4.1.1 的 CloudBase 路径兼容：先读取 `data/...`，失败时自动尝试根目录备用 JSON。

> 考研 4112 条指当前 WordLoop 本地 ECDICT 数据中同时带 `ky` 与 `cet6` 标签的核心交集。它适合作为考研核心检索与学习集合，但不宣称为教育部官方或唯一完整词表。完整 ECDICT `ky` 标签词表可通过生成工具在获得原始 CSV 后重新提取。

## 本地运行

Windows 推荐直接双击仓库根目录的 `start_wordloop.bat`。它使用独立端口 `8042`，避免仍在运行的旧版 `8000` 服务把浏览器带回旧目录。

也可以在仓库根目录运行：

```bash
python -m http.server 8042 --directory public
```

浏览器访问 `http://127.0.0.1:8042/`。

不要直接双击 `public/index.html`。`file://` 页面受浏览器安全策略限制，无法通过 `fetch()` 读取 `data/cet6/` 和 `data/kaoyan/` 下的 JSON，表现就是“词库启用失败：Failed to fetch”。

## 使用考研英语词库

1. 打开“词库中心”；
2. 进入“考研英语”；
3. 点击“启用这个词库”；
4. 网站加载 100 张增强卡，默认按每天 20 个生成 5 天计划；
5. “浏览 4112 基础词条”用于查词与后续选词，不会把未经整理的词典条目直接变成练习题。

## 主要数据文件

```text
public/data/cet6/cet6_lexicon.json
public/data/cet6/cet6_cards_100.json
public/data/kaoyan/kaoyan_lexicon.json
public/data/kaoyan/kaoyan_cards_100.json
public/data/library_manifest.json
```

CloudBase 部署包还在 `public/` 根目录保留同名备用文件，以兼容部分部署时子目录缺失的问题。

## 词库生成与验证

```text
tools/lexicon_builder/
```

主要程序：

- `extract_exam_words.py`：从 ECDICT CSV 按 `cet6`、`ky`、`ielts` 标签提取基础词库；
- `build_cet6_v4_1.py`：重建 CET-6 发布数据；
- `build_kaoyan_v4_2.py`：重建考研 4112 核心词条和 100 张增强卡；
- `validate_release_v4_2.py`：检查两个考试词库的数量、ID、填空还原、字段完整性与备用文件一致性。

运行考研构建：

```bash
python tools/lexicon_builder/build_kaoyan_v4_2.py \
  --cet6-lexicon public/data/cet6/cet6_lexicon.json \
  --lexicon-output public/data/kaoyan/kaoyan_lexicon.json \
  --cards-output public/data/kaoyan/kaoyan_cards_100.json
```

## 数据保存

学习进度仍保存在当前域名下的浏览器 `localStorage`。同一域名更新网站通常不会删除进度；更换域名、浏览器或设备不会自动同步。建议定期从“导入导出”页面备份 JSON。

## 部署

### CloudBase

上传 CloudBase 专用 ZIP。部署后检查以下地址能返回 JSON：

```text
data/kaoyan/kaoyan_lexicon.json
data/kaoyan/kaoyan_cards_100.json
```

### Cloudflare

仓库根目录 `wrangler.jsonc` 已将 `public/` 设置为静态资源目录。推送到 GitHub `main` 后，已连接的 Cloudflare 项目会自动部署。
