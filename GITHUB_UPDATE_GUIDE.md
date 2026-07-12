# WordLoop v4.2.1 手动推送 GitHub

本版本已合并到本地 Git 仓库并完成验证。由项目维护者手动推送到 `main` 后，已连接的静态托管平台会自动构建。

## 推送命令

```powershell
cd F:\vibe_coding\idea_inbox\wordloop
git push origin main
```

## 必须确认的文件

```text
public/index.html
public/lexicon_v4.js
start_wordloop.bat
public/data/library_manifest.json
public/data/kaoyan/kaoyan_lexicon.json
public/data/kaoyan/kaoyan_cards_100.json
tools/lexicon_builder/build_kaoyan_v4_2.py
tools/lexicon_builder/validate_release_v4_2.py
```

GitHub/Cloudflare 使用标准 `data/kaoyan/` 路径。CloudBase 专用包同时附带根目录备用 JSON。

本地预览请双击 `start_wordloop.bat`，访问 `http://127.0.0.1:8042/`。不要直接双击 `public/index.html`。

部署完成后进入“词库中心”，考研英语应显示：

```text
4112 基础词条 · 100 学习卡
```
