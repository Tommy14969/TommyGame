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

let currentIndex = 0;
let successCount = 0;
let failCount = 0;

function log(msg, type) {
    const logDiv = document.getElementById('log');
    const item = document.createElement('div');
    item.className = 'log-item ' + type;
    item.textContent = msg;
    logDiv.appendChild(item);
    logDiv.scrollTop = logDiv.scrollHeight;
}

function updateStatus(html) {
    document.getElementById('status').innerHTML = html;
}

function updateProgress() {
    document.getElementById('progress').textContent = `${currentIndex}/${games.length}`;
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function captureGame(game) {
    log(`[${game.id}] 开始: ${game.titleEn}`, 'info');
    
    try {
        const response = await fetch(game.rom);
        if (!response.ok) throw new Error('ROM not found');
        
        const romData = await response.arrayBuffer();
        const romArray = new Uint8Array(romData);
        const romString = Array.from(romArray).map(b => String.fromCharCode(b)).join('');
        
        const canvas = document.getElementById('canvas');
        const ctx = canvas.getContext('2d');
        
        const nes = new jsnes.NES({
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
        
        for (let i = 0; i < 90; i++) {
            nes.frame();
        }
        
        const imageData = canvas.toDataURL('image/png');
        const link = document.createElement('a');
        link.href = imageData;
        link.download = `${game.id}-${game.titleEn}.png`;
        link.click();
        
        log(`[${game.id}] 成功: ${game.titleEn}`, 'success');
        successCount++;
        return true;
        
    } catch (error) {
        log(`[${game.id}] 失败: ${game.titleEn} - ${error.message}`, 'error');
        failCount++;
        return false;
    }
}

async function startCapture() {
    const btn = document.getElementById('startBtn');
    btn.disabled = true;
    btn.textContent = '⏳ 截图中...';
    
    log('开始自动截图', 'info');
    
    for (let i = 0; i < games.length; i++) {
        currentIndex = i + 1;
        updateProgress();
        updateStatus(`<div>正在截图: ${games[i].titleEn}</div><div style="font-size:14px;color:#aaa;margin-top:10px;">进度: ${currentIndex}/${games.length}</div>`);
        await captureGame(games[i]);
        await sleep(1500);
    }
    
    updateStatus(`<div style="color:#00ff88;font-size:20px;">完成！</div><div style="margin-top:15px;">成功: ${successCount} | 失败: ${failCount}</div><div style="font-size:14px;color:#aaa;margin-top:10px;">请将下载的图片移动到 images/ 目录</div>`);
    log(`完成 - 成功: ${successCount}, 失败: ${failCount}`, 'success');
    btn.textContent = '✓ 完成';
}
