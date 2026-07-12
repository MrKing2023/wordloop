# WordLoop v4.2.1 更新说明

## 本地词库加载诊断与修复

- 明确阻止把 `file://` 误判为端口或词库数据问题，并显示可执行的本地服务器启动说明。
- JSON 加载错误现在列出实际尝试过的 URL 和最后一个 HTTP/解析错误，方便区分路径、404 与格式问题。
- `start_wordloop.bat` 升级到 v4.2.1，使用独立端口 `8042`，避免旧版 8000 端口仍指向其他目录。
- 启动脚本支持 `py`、`python`、`F:\anaconda3\python.exe` 和用户目录 Anaconda。
- 静态资源版本参数更新为 `4.2.1`，减少浏览器继续使用 v4.1/v4.2 旧脚本的情况。

标准数据路径保持不变：

```text
public/data/cet6/
public/data/kaoyan/
public/data/library_manifest.json
```
