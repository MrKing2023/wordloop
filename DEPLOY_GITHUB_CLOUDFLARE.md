# WordLoop v3.3：上传 GitHub 并部署到 Cloudflare Pages

本项目是纯静态网站，不需要安装依赖，也不需要执行前端构建。

## 一、解压项目

解压下载的 ZIP。准备上传的是解压后文件夹里面的内容，不是 ZIP 本身。

仓库根目录应直接看到：

```text
index.html
styles.css
app.js
enhancements.js
plan_v3.js
word_bank_200.json
README.md
ROADMAP.md
```

不要只上传 `WordLoop_standalone_v3.3.html`。Cloudflare 正式部署使用 `index.html` 和其他分离文件。

## 二、在 GitHub 创建仓库

1. 登录 GitHub。
2. 右上角点击 `+` → `New repository`。
3. Repository name 建议填写：`wordloop`。
4. Description 可填写：`AI-assisted vocabulary learning website`。
5. Public 或 Private 均可；Cloudflare Pages 支持连接两种仓库。
6. 建议不要勾选 Add a README、.gitignore 或 License，因为项目压缩包中已经包含 README。
7. 点击 `Create repository`。

## 三、用浏览器上传项目文件

如果新仓库为空：

1. 点击页面中的 `uploading an existing file`。
2. 打开解压后的项目文件夹。
3. 全选文件夹里面的所有文件和子文件夹，拖到 GitHub 上传区域。
4. 确认 `index.html` 位于仓库根目录，不是在额外的一层文件夹里。
5. Commit message 填写：`Initial WordLoop v3.3`。
6. 点击 `Commit changes`。

如果仓库已经有文件：

1. 点击 `Add file` → `Upload files`。
2. 拖入项目文件。
3. 提交到 `main` 分支。

## 四、连接 Cloudflare Pages

1. 登录 Cloudflare Dashboard。
2. 进入 `Workers & Pages`。
3. 点击 `Create application`。
4. 选择 `Pages`。
5. 选择 `Connect to Git` 或 `Import an existing Git repository`。
6. 选择 GitHub，并安装/授权 `Cloudflare Workers and Pages`。
7. 建议只授权刚创建的 `wordloop` 仓库。
8. 选择该仓库，点击 `Begin setup`。

## 五、构建配置

使用以下设置：

```text
Project name: wordloop（也可以自定义）
Production branch: main
Framework preset: None
Build command: exit 0
Build output directory: .
Root directory (advanced): 留空
Environment variables: 不需要
```

说明：

- `.` 表示仓库根目录，因为 `index.html` 就在根目录。
- 本项目无需 npm、Vite 或其他构建步骤。
- 如果 Cloudflare 界面允许 Build command 留空，也可留空；这里采用 `exit 0` 作为明确的无构建命令配置。

设置完成后点击 `Save and Deploy`。

## 六、部署成功

部署完成后会获得类似地址：

```text
https://wordloop.pages.dev
```

若项目名已被占用，Cloudflare 会生成其他可用的 `pages.dev` 地址。

以后每次修改 GitHub 的 `main` 分支，Cloudflare Pages 都会自动重新部署。

## 七、常见问题

### 打开网站显示 404

检查 GitHub 仓库根目录是否直接存在：

```text
index.html
```

最常见错误是把整个项目文件夹又套了一层上传，导致文件变成：

```text
仓库根目录/WordLoop_v3_3_navigation_sidebar/index.html
```

正确结构应该是：

```text
仓库根目录/index.html
```

### 页面能打开，但样式或功能缺失

确认以下文件与 `index.html` 位于同一级：

```text
styles.css
app.js
enhancements.js
plan_v3.js
```

### 学习进度是否会保留

当前进度仍保存在每台设备的浏览器本地：

- 同一设备、同一浏览器、同一 `pages.dev` 地址会继续使用原进度；
- 手机、平板、电脑之间暂时不同步；
- 不要频繁更换 Cloudflare 项目地址；
- 定期使用网站中的 JSON 导出功能备份。

### AI API 密钥

未来加入 AI 判分时，不要把 API Key 写进 `app.js`、`enhancements.js` 或其他前端文件。应通过 Cloudflare Workers / Pages Functions 在服务端调用模型。
