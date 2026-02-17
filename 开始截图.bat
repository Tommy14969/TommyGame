@echo off
chcp 65001 >nul
title NES 游戏截图工具

echo.
echo ===============================================
echo    🎮 NES 游戏自动截图工具
echo ===============================================
echo.
echo 正在打开截图页面...
echo.

REM 打开截图工具
start "" "tools/auto_screenshot.html"

echo.
echo ✅ 截图工具已打开！
echo.
echo 使用说明：
echo 1. 在打开的页面中点击"运行并截图"
echo 2. 游戏会自动运行3秒
echo 3. 截图会自动下载到您的下载文件夹
echo 4. 将下载的图片移动到 images/ 目录
echo 5. 刷新游戏站点查看效果
echo.
echo 💡 提示：您可以同时打开多个游戏进行截图
echo.

pause
