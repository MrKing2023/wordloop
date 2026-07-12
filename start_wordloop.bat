@echo off
chcp 65001 >nul
title WordLoop v3 Local Server
cd /d "%~dp0"
echo WordLoop v3 正在启动...
echo 浏览器地址：http://localhost:8000
echo 关闭本窗口即可停止服务。
start "" http://localhost:8000
py -m http.server 8000 2>nul || python -m http.server 8000
pause
