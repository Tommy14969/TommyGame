@echo off
chcp 65001 >nul
title NES 游戏自动截图工具

echo.
echo ===============================================
echo    🎮 NES 游戏自动截图工具
echo ===============================================
echo.
echo 正在启动服务器...
echo.

REM 启动Python服务器
start /B python -m http.server 8000

REM 等待服务器启动
timeout /t 3 /nobreak >nul

echo.
echo ✅ 服务器已启动！
echo.
echo 正在打开自动截图页面...
echo.

REM 打开浏览器到自动截图页面
start http://localhost:8000/auto_screenshot_runner.html

echo.
echo ===============================================
echo    📋 使用说明
echo ===============================================
echo.
echo 1. ✅ 服务器已启动
echo 2. ✅ 浏览器已打开
echo 3. ⏳ 等待自动截图完成（约2-3分钟）
echo 4. 📁 截图会下载到您的下载文件夹
echo 5. 📦 将下载的图片移动到 images/ 目录
echo 6. 🎮 刷新游戏站点查看效果
echo.
echo ===============================================
echo.
echo ⚠️  重要提示：
echo - 请保持浏览器页面打开，直到所有游戏截图完成
echo - 不要关闭此窗口（服务器运行中）
echo - 截图完成后按 Ctrl+C 停止服务器
echo.
echo ===============================================
echo.

pause
