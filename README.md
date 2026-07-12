# WordLoop v3.4：AI 辅助语境背单词

一个纯静态、可部署到 GitHub + Cloudflare Workers Static Assets 的本地英语学习网站。

## v3 新功能

- 将全部词库固定划分为 M 天，每天 N 个词；
- 默认 200 个词、每天 20 个，共 10 天；
- 可调整每天词数，自动重新计算总天数；
- 可以自由选择任意一天学习；
- 每天独立记录已学数量、正确、错词和继续位置；
- 支持继续本日学习、从头重学、只练本日错词；
- 支持手动标记本日完成、取消完成、重置本日进度；
- 按天学习与原有间隔复习并存；
- 中文题目与英文填空句采用接近的字号和视觉权重；
- 首页、学习计划、日期详情和练习页重新设计；
- 逐级提示：发音 → 音标 → 答案；
- 答题后显示详细释义、用法、搭配、相近表达和更多例句；
- 内置 200 张卡片。

## 本地运行

### 直接打开

双击 `public/index.html`。部分手机浏览器对本地 HTML 的存储和发音支持有限。

### 推荐：本地服务器

Windows 双击：

```text
start_wordloop.bat
```

或在当前目录运行：

```bash
python -m http.server 8000 --directory public
```

浏览器访问：

```text
http://localhost:8000
```

## 数据保存

数据保存在当前网站域名下的浏览器 localStorage 中：

- 关闭并重新打开网页后仍会保留；
- 同一网址、同一设备、同一浏览器可继续学习；
- 换设备或换浏览器不会自动同步；
- 清除浏览器数据可能导致记录丢失；
- 建议定期在“导入导出”页面导出 JSON。

## 部署

项目不需要前端构建。Cloudflare Workers Static Assets 只会发布 `public/` 中的网站文件：

- Build command：`exit 0`
- Deploy command：`npx wrangler deploy`
- Root directory：`/`

更详细步骤见 `DEPLOY_GITHUB_CLOUDFLARE.md`。

## 主要文件

- `public/index.html`：入口页面
- `public/styles.css`：基础样式和 v3 响应式设计
- `public/app.js`：基础功能
- `public/enhancements.js`：200 词库、逐级提示和详细解析
- `public/plan_v3.js`：按天学习计划、日期进度与 v3 页面
- `public/word_bank_200.json`：独立的 200 词库数据
- `WordLoop_standalone_v3.4.html`：不参与线上部署的单文件版本

## 部署后更新

修改代码并推送到 GitHub 后，Cloudflare 会自动重新部署。网页更新一般不会删除同一域名下的本地学习进度。


## v3.1 关键修复

已修复点击“学习计划”“第 N 天”“继续学习”后网址改变但页面仍停留首页的问题。请使用本压缩包中的新文件，不要继续使用旧的 `WordLoop_standalone_v3.html`。


## v3.2 快捷切题

答题完成后，宽屏桌面浏览器右侧会显示固定的“下一题”按钮。页面底部按钮仍然保留。窄屏设备不会显示侧边按钮。


## v3.3 导航改进

- 左侧菜单可收起和展开。
- 答题后可用左侧“上一题”和右侧“下一题”快速浏览。
- 底部导航按钮继续保留。
- 后续功能规划见 `ROADMAP.md`。


## v3.4 侧栏与快捷导航

展开侧栏时按钮不再遮挡 Logo；收起后只显示 W Logo，悬停后变为展开侧栏图标。宽屏解析页的上一题、下一题按钮改为横向显示。
