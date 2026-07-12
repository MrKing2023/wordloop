# WordLoop v3.4：GitHub + Cloudflare Workers 部署

本项目是纯静态网站，不需要前端构建。线上发布由 Cloudflare Workers Static Assets 完成。

## 仓库结构

```text
wordloop/
├── public/
│   ├── index.html
│   ├── styles.css
│   ├── app.js
│   ├── enhancements.js
│   ├── plan_v3.js
│   ├── word_bank_200.json
│   └── wordloop-import-template.csv
├── wrangler.jsonc
├── README.md
└── CHANGELOG_v3.4.md
```

Wrangler 只上传 `public/`，因此 `.git`、README、更新说明、测试报告和单文件离线版不会公开为网站资源。

## Cloudflare 构建设置

```text
Production branch: main
Build command: exit 0
Deploy command: npx wrangler deploy
Root directory: /
Build variables: 无
```

`wrangler.jsonc` 已明确启用 `workers.dev` 和预览地址，因此部署时不会再出现缺少这两个配置的警告。

## 更新网站

1. 修改 `public/` 中的网页文件。
2. 在本地验证页面。
3. 提交并推送到 GitHub 的 `main` 分支。
4. Cloudflare 会自动构建并部署。

部署日志应只列出 `public/` 中的 7 个静态资源，不应再出现 `.git/objects`、README 或测试报告。

## 本地验证

Windows 可双击 `start_wordloop.bat`，或运行：

```bash
python -m http.server 8000 --directory public
```

然后访问 `http://localhost:8000`。

## 中国大陆访问

`workers.dev` 在中国大陆的可达性无法仅靠代码配置保证。整理部署目录可以解决误上传问题，但不会改变网络线路。

成本最低的下一步是绑定一个自定义域名后，分别用移动、电信和联通网络实测。若仍不稳定，再考虑国内对象存储镜像与备案。不要为了这一点把项目从 Workers 改回 Pages；两者都不能自动获得 Cloudflare 中国大陆网络。

## 数据与密钥

- 学习进度保存在当前域名的浏览器 `localStorage` 中；更换域名后不会自动迁移。
- 定期通过网站“导入导出”页面备份 JSON。
- 未来加入 AI 判分时，不要把 API Key 写入 `public/`；应通过服务端 Worker 的 Secret 保存。
