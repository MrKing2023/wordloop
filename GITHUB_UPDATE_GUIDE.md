# WordLoop v4.1.1 GitHub 与自动部署

项目维护使用本地 Git 仓库并推送到 `MrKing2023/wordloop` 的 `main` 分支。Cloudflare、EdgeOne 和 CloudBase 如已连接该分支，会在推送后自动构建。

## 更新方式

将完整项目与 v4.1.1 补丁合并到仓库后，检查并提交：

```bash
git add .
git commit -m "Add WordLoop v4.1.1 CET-6 library"
git push origin main
```

## 必须确认的目录

上传后 GitHub 中应存在：

```text
public/data/cet6/cet6_lexicon.json
public/data/cet6/cet6_cards_100.json
public/lexicon_v4.js
public/lexicon_v4.css
public/data/library_manifest.json
```

标准文件必须位于 `public/data/cet6/`。GitHub 版本不需要额外复制根目录备用 JSON；`lexicon_v4.js` 已保留备用路径兼容逻辑。

## 部署

- Cloudflare：连接 GitHub 后通常会自动重新部署；
- EdgeOne Pages：输出目录设置为 `public`；
- CloudBase Git 平台部署：目标目录 `./`，安装和构建命令留空，构建产物目录 `./public`，部署路径 `/`；
- CloudBase 手动部署：使用单独的 CloudBase 压缩包，包内网站文件应直接位于根目录；
- 部署完成后打开“词库中心”，确认 CET-6 显示 `5407 基础词条 · 100 学习卡`。

## 缓存

网站更新后仍显示旧版时：

1. 强制刷新页面；
2. 清除该网站缓存，但不要清除网站数据；
3. 检查部署平台是否发布了最新 Git commit。

现有 `localStorage` 学习记录会保留。第一次启用 CET-6 时，100 张卡片才会写入当前浏览器的学习状态。
