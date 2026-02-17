@echo off
chcp 65001 >nul
title NES 红白机游戏站

echo.
echo ===============================================
echo    🎮 NES 红白机游戏站 - 正在启动...
echo ===============================================
echo.

:: 检查 Python 是否安装
python --version >nul 2>&1
if %errorlevel% == 0 (
    echo ✅ 使用 Python 启动服务器...
    echo 📍 访问地址: http://localhost:8000
    echo.
    echo 按 Ctrl+C 可停止服务器
    echo.
    start http://localhost:8000
    python -m http.server 8000
    goto :end
)

:: Python 未安装，尝试 Node.js
node --version >nul 2>&1
if %errorlevel% == 0 (
    echo ✅ 使用 Node.js 启动服务器...
    echo 📍 访问地址: http://localhost:8000
    echo.
    echo 按 Ctrl+C 可停止服务器
    echo.
    start http://localhost:8000
    npx http-server -p 8000
    goto :end
)

:: 都没有安装
echo ❌ 错误：未找到 Python 或 Node.js
echo.
echo 请先安装以下任一工具：
echo   1. Python: https://www.python.org/downloads/
echo   2. Node.js: https://nodejs.org/
echo.
pause
exit

:end
