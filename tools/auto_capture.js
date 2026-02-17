const fs = require('fs');
const path = require('path');
const https = require('https');

// Game list
const games = [
    {id: 1, titleEn: "Super_Mario_Bros", rom: "roms/1-Super_Mario_Bros.nes"},
    {id: 2, titleEn: "The_Legend_of_Zelda", rom: "roms/2-The_Legend_of_Zelda.nes"},
    {id: 3, titleEn: "Contra", rom: "roms/3-Contra.nes"},
    {id: 4, titleEn: "Tank_Battle", rom: "roms/4-Battle_City.nes"},
    {id: 5, titleEn: "Pac-Man", rom: "roms/5-Pac-Man.nes"},
    {id: 6, titleEn: "Donkey_Kong", rom: "roms/6-Donkey_Kong.nes"},
    {id: 7, titleEn: "Mega_Man", rom: "roms/7-Mega_Man.nes"},
    {id: 8, titleEn: "Castlevania", rom: "roms/8-Castlevania.nes"},
    {id: 9, titleEn: "Metroid", rom: "roms/9-Metroid.nes"},
    {id: 10, titleEn: "Ninja_Gaiden", rom: "roms/10-Ninja_Gaiden.nes"},
    {id: 11, titleEn: "Tetris", rom: "roms/11-Tetris.nes"},
    {id: 12, titleEn: "Bomberman", rom: "roms/12-Bomberman.nes"},
    {id: 13, titleEn: "Ice_Climber", rom: "roms/13-Ice_Climber.nes"},
    {id: 14, titleEn: "Duck_Hunt", rom: "roms/14-Duck_Hunt.nes"},
    {id: 15, titleEn: "Punch-Out", rom: "roms/15-Punch-Out.nes"},
    {id: 16, titleEn: "Final_Fantasy", rom: "roms/16-Final_Fantasy.nes"},
    {id: 17, titleEn: "Dragon_Quest", rom: "roms/17-Dragon_Quest.nes"},
    {id: 18, titleEn: "Kirby_Adventure", rom: "roms/18-Kirby_Adventure.nes"},
    {id: 19, titleEn: "Super_Mario_Bros_3", rom: "roms/19-Super_Mario_Bros_3.nes"},
    {id: 20, titleEn: "Metal_Gear", rom: "roms/20-Metal_Gear.nes"},
    {id: 21, titleEn: "Double_Dragon", rom: "roms/21-Double_Dragon.nes"},
    {id: 23, titleEn: "Shadow_of_the_Ninja", rom: "roms/23-Shadow_of_the_Ninja.nes"},
    {id: 24, titleEn: "Rush_Attack", rom: "roms/24-Rush_n_Attack.nes"},
    {id: 25, titleEn: "Lode_Runner", rom: "roms/25-Lode_Runner.nes"},
    {id: 26, titleEn: "Solomons_Key", rom: "roms/26-Solomons_Key.nes"},
    {id: 27, titleEn: "Bubble_Bobble", rom: "roms/27-Bubble_Bobble.nes"},
    {id: 29, titleEn: "The_Legend_of_Kage", rom: "roms/29-The_Legend_of_Kage.nes"},
    {id: 31, titleEn: "Mario_Golf", rom: "roms/31-Mario_Golf.nes"},
    {id: 33, titleEn: "Excitebike", rom: "roms/33-Excitebike.nes"},
    {id: 35, titleEn: "World_Cup", rom: "roms/35-World_Cup.nes"},
    {id: 36, titleEn: "Tecmo_Bowl", rom: "roms/36-Tecmo_Bowl.nes"},
    {id: 37, titleEn: "Pinball", rom: "roms/37-Pinball.nes"},
    {id: 38, titleEn: "Balloon_Fight", rom: "roms/38-Balloon_Fight.nes"},
    {id: 39, titleEn: "Journey_to_the_West", rom: "roms/39-Journey_to_the_West.nes"},
    {id: 41, titleEn: "Phoenix", rom: "roms/41-Phoenix.nes"},
    {id: 42, titleEn: "Galaga", rom: "roms/42-Galaga.nes"},
    {id: 43, titleEn: "Space_Invaders", rom: "roms/43-Space_Invaders.nes"},
    {id: 44, titleEn: "1942", rom: "roms/44-1942.nes"},
    {id: 45, titleEn: "Wrecking_Crew", rom: "roms/45-Wrecking_Crew.nes"},
    {id: 46, titleEn: "Mario_Bros", rom: "roms/46-Mario_Bros.nes"},
    {id: 48, titleEn: "Kung_Fu", rom: "roms/48-Kung_Fu.nes"},
    {id: 49, titleEn: "Pooyan", rom: "roms/49-Pooyan.nes"},
    {id: 50, titleEn: "Xevious", rom: "roms/50-Xevious.nes"},
    {id: 51, titleEn: "Adventure_Island", rom: "roms/51-Adventure_Island.nes"},
];

console.log('🎮 NES游戏自动截图工具');
console.log('=' .repeat(60));
console.log('');

// Since we can't easily run jsnes in Node.js without canvas,
// we'll create a simple HTML file that can be automated
console.log('创建自动化截图页面...');

const htmlContent = `<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Auto Screenshot</title>
    <script src="js/jsnes.min.js"></script>
</head>
<body>
    <canvas id="canvas" width="256" height="240" style="display:none;"></canvas>
    <div id="status">准备中...</div>

    <script>
        const games = ${JSON.stringify(games)};
        let currentIndex = 0;
        let nes = null;
        let ctx = null;

        function sleep(ms) {
            return new Promise(resolve => setTimeout(resolve, ms));
        }

        async function captureGame(game) {
            const status = document.getElementById('status');
            status.textContent = \`[\${currentIndex + 1}/\${games.length}] 截图: \${game.titleEn}\`;

            try {
                const response = await fetch(game.rom);
                const romData = await response.arrayBuffer();
                const romArray = new Uint8Array(romData);
                const romString = Array.from(romArray).map(b => String.fromCharCode(b)).join('');

                const canvas = document.getElementById('canvas');
                ctx = canvas.getContext('2d');

                nes = new jsnes.NES({
                    onFrame: (buffer) => {
                        const imageData = ctx.createImageData(256, 240);
                        for (let i = 0; i < buffer.length; i++) {
                            const pixel = buffer[i];
                            const idx = i * 4;
                            imageData.data[idx] = (pixel >> 16) & 0xFF;
                            imageData.data[idx + 1] = (pixel >> 8) & 0xFF;
                            imageData.data[idx + 2] = pixel & 0xFF;
                            imageData.data[idx + 3] = 255;
                        }
                        ctx.putImageData(imageData, 0, 0);
                    },
                    onAudioSample: () => {}
                });

                nes.loadROM(romString);

                // Run for 60 frames (1 second)
                for (let i = 0; i < 60; i++) {
                    nes.frame();
                }

                // Capture screenshot
                canvas.toBlob(blob => {
                    const url = URL.createObjectURL(blob);
                    const a = document.createElement('a');
                    a.href = url;
                    a.download = \`images/\${game.id}-\${game.titleEn}.png\`;
                    a.click();
                    URL.revokeObjectURL(url);
                });

                await sleep(500);
                return true;
            } catch (error) {
                console.error(\`Error: \${game.titleEn}\`, error);
                return false;
            }
        }

        async function processAll() {
            for (let i = 0; i < games.length; i++) {
                currentIndex = i;
                await captureGame(games[i]);
                await sleep(1000);
            }
            document.getElementById('status').textContent = '✅ 完成！请将下载的图片移动到images/目录';
        }

        // Start after page loads
        window.onload = () => {
            console.log('开始自动截图...');
            processAll();
        };
    </script>
</body>
</html>`;

fs.writeFileSync('auto_screenshot_runner.html', htmlContent);
console.log('✅ 创建完成: auto_screenshot_runner.html');
console.log('');
console.log('使用说明:');
console.log('1. 在浏览器中打开 auto_screenshot_runner.html');
console.log('2. 脚本会自动运行所有游戏并截图');
console.log('3. 截图会下载到您的下载文件夹');
console.log('4. 将下载的图片移动到 images/ 目录');
console.log('');
console.log('⚠️  注意：需要在本地服务器环境下运行（file:// 协议无法加载ROM）');
console.log('');
console.log('请先运行: 启动游戏.bat');
console.log('然后访问: http://localhost:8000/auto_screenshot_runner.html');
