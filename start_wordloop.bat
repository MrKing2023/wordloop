@echo off
chcp 65001 >nul
title WordLoop v4.2.1 Local Server
set "PORT=8042"
set "PYTHON_EXE="

where py >nul 2>&1 && set "PYTHON_EXE=py"
if not defined PYTHON_EXE where python >nul 2>&1 && set "PYTHON_EXE=python"
if not defined PYTHON_EXE if exist "F:\anaconda3\python.exe" set "PYTHON_EXE=F:\anaconda3\python.exe"
if not defined PYTHON_EXE if exist "%USERPROFILE%\anaconda3\python.exe" set "PYTHON_EXE=%USERPROFILE%\anaconda3\python.exe"

if not defined PYTHON_EXE (
  echo 未找到 Python，无法启动 WordLoop 本地服务器。
  echo 请安装 Python，或在终端运行可用的 Python 后重试。
  pause
  exit /b 1
)

echo WordLoop v4.2.1 正在启动...
echo 网站目录：%~dp0public
echo 浏览器地址：http://127.0.0.1:%PORT%
echo 请勿直接双击 public\index.html；file:// 模式无法读取 JSON 词库。
echo 关闭本窗口即可停止服务。
start "" "http://127.0.0.1:%PORT%/?v=4.2.1"
"%PYTHON_EXE%" -m http.server %PORT% --directory "%~dp0public"
pause
