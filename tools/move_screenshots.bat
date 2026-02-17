@echo off
chcp 65001 >nul

echo ===============================================
echo    移动截图到images目录
echo ===============================================
echo.

REM 通常Windows下载文件夹路径
set DOWNLOADS=%USERPROFILE%\Downloads

echo 正在查找下载的截图...
echo.

REM 移动所有游戏截图
move /Y "%DOWNLOADS%\1-Super_Mario_Bros.png" "images\" 2>nul
move /Y "%DOWNLOADS%\2-The_Legend_of_Zelda.png" "images\" 2>nul
move /Y "%DOWNLOADS%\3-Contra.png" "images\" 2>nul
move /Y "%DOWNLOADS%\4-Tank_Battle.png" "images\" 2>nul
move /Y "%DOWNLOADS%\5-Pac-Man.png" "images\" 2>nul
move /Y "%DOWNLOADS%\6-Donkey_Kong.png" "images\" 2>nul
move /Y "%DOWNLOADS%\7-Mega_Man.png" "images\" 2>nul
move /Y "%DOWNLOADS%\8-Castlevania.png" "images\" 2>nul
move /Y "%DOWNLOADS%\9-Metroid.png" "images\" 2>nul
move /Y "%DOWNLOADS%\10-Ninja_Gaiden.png" "images\" 2>nul
move /Y "%DOWNLOADS%\11-Tetris.png" "images\" 2>nul
move /Y "%DOWNLOADS%\12-Bomberman.png" "images\" 2>nul
move /Y "%DOWNLOADS%\13-Ice_Climber.png" "images\" 2>nul
move /Y "%DOWNLOADS%\14-Duck_Hunt.png" "images\" 2>nul
move /Y "%DOWNLOADS%\15-Punch-Out.png" "images\" 2>nul
move /Y "%DOWNLOADS%\16-Final_Fantasy.png" "images\" 2>nul
move /Y "%DOWNLOADS%\17-Dragon_Quest.png" "images\" 2>nul
move /Y "%DOWNLOADS%\18-Kirby_Adventure.png" "images\" 2>nul
move /Y "%DOWNLOADS%\19-Super_Mario_Bros_3.png" "images\" 2>nul
move /Y "%DOWNLOADS%\20-Metal_Gear.png" "images\" 2>nul
move /Y "%DOWNLOADS%\21-Double_Dragon.png" "images\" 2>nul
move /Y "%DOWNLOADS%\23-Shadow_of_the_Ninja.png" "images\" 2>nul
move /Y "%DOWNLOADS%\24-Rush_Attack.png" "images\" 2>nul
move /Y "%DOWNLOADS%\25-Lode_Runner.png" "images\" 2>nul
move /Y "%DOWNLOADS%\26-Solomons_Key.png" "images\" 2>nul
move /Y "%DOWNLOADS%\27-Bubble_Bobble.png" "images\" 2>nul
move /Y "%DOWNLOADS%\29-The_Legend_of_Kage.png" "images\" 2>nul
move /Y "%DOWNLOADS%\31-Mario_Golf.png" "images\" 2>nul
move /Y "%DOWNLOADS%\33-Excitebike.png" "images\" 2>nul
move /Y "%DOWNLOADS%\35-World_Cup.png" "images\" 2>nul
move /Y "%DOWNLOADS%\36-Tecmo_Bowl.png" "images\" 2>nul
move /Y "%DOWNLOADS%\37-Pinball.png" "images\" 2>nul
move /Y "%DOWNLOADS%\38-Balloon_Fight.png" "images\" 2>nul
move /Y "%DOWNLOADS%\39-Journey_to_the_West.png" "images\" 2>nul
move /Y "%DOWNLOADS%\41-Phoenix.png" "images\" 2>nul
move /Y "%DOWNLOADS%\42-Galaga.png" "images\" 2>nul
move /Y "%DOWNLOADS%\43-Space_Invaders.png" "images\" 2>nul
move /Y "%DOWNLOADS%\44-1942.png" "images\" 2>nul
move /Y "%DOWNLOADS%\45-Wrecking_Crew.png" "images\" 2>nul
move /Y "%DOWNLOADS%\46-Mario_Bros.png" "images\" 2>nul
move /Y "%DOWNLOADS%\48-Kung_Fu.png" "images\" 2>nul
move /Y "%DOWNLOADS%\49-Pooyan.png" "images\" 2>nul
move /Y "%DOWNLOADS%\50-Xevious.png" "images\" 2>nul
move /Y "%DOWNLOADS%\51-Adventure_Island.png" "images\" 2>nul

echo.
echo ===============================================
echo    ✅ 完成！
echo ===============================================
echo.
echo 截图已移动到 images/ 目录
echo 请刷新浏览器查看效果
echo.
pause
