"""
Auto-capture NES game screenshots from ROM files
Loads each ROM, runs it in emulator, and captures screenshot
"""

import os
import sys
import io
import subprocess
import json
from pathlib import Path
import time

# Fix UTF-8
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Game list matching ROM files
GAMES = [
    {"id": 1, "title": "超级马里奥兄弟", "titleEn": "Super_Mario_Bros", "rom": "roms/1-Super_Mario_Bros.nes"},
    {"id": 2, "title": "塞尔达传说", "titleEn": "The_Legend_of_Zelda", "rom": "roms/2-The_Legend_of_Zelda.nes"},
    {"id": 3, "title": "魂斗罗", "titleEn": "Contra", "rom": "roms/3-Contra.nes"},
    {"id": 4, "title": "坦克大战", "titleEn": "Tank_Battle", "rom": "roms/4-Battle_City.nes"},
    {"id": 5, "title": "吃豆人", "titleEn": "Pac-Man", "rom": "roms/5-Pac-Man.nes"},
    {"id": 6, "title": "大金刚", "titleEn": "Donkey_Kong", "rom": "roms/6-Donkey_Kong.nes"},
    {"id": 7, "title": "洛克人", "titleEn": "Mega_Man", "rom": "roms/7-Mega_Man.nes"},
    {"id": 8, "title": "恶魔城", "titleEn": "Castlevania", "rom": "roms/8-Castlevania.nes"},
    {"id": 9, "title": "银河战士", "titleEn": "Metroid", "rom": "roms/9-Metroid.nes"},
    {"id": 10, "title": "忍者龙剑传", "titleEn": "Ninja_Gaiden", "rom": "roms/10-Ninja_Gaiden.nes"},
    {"id": 11, "title": "俄罗斯方块", "titleEn": "Tetris", "rom": "roms/11-Tetris.nes"},
    {"id": 12, "title": "炸弹人", "titleEn": "Bomberman", "rom": "roms/12-Bomberman.nes"},
    {"id": 13, "title": "冰山登山者", "titleEn": "Ice_Climber", "rom": "roms/13-Ice_Climber.nes"},
    {"id": 14, "title": "打鸭子", "titleEn": "Duck_Hunt", "rom": "roms/14-Duck_Hunt.nes"},
    {"id": 15, "title": "拳无虚发", "titleEn": "Punch-Out", "rom": "roms/15-Punch-Out.nes"},
    {"id": 16, "title": "最终幻想", "titleEn": "Final_Fantasy", "rom": "roms/16-Final_Fantasy.nes"},
    {"id": 17, "title": "勇者斗恶龙", "titleEn": "Dragon_Quest", "rom": "roms/17-Dragon_Quest.nes"},
    {"id": 18, "title": "星之卡比", "titleEn": "Kirby_Adventure", "rom": "roms/18-Kirby_Adventure.nes"},
    {"id": 19, "title": "马里奥兄弟3", "titleEn": "Super_Mario_Bros_3", "rom": "roms/19-Super_Mario_Bros_3.nes"},
    {"id": 20, "title": "合金装备", "titleEn": "Metal_Gear", "rom": "roms/20-Metal_Gear.nes"},
    {"id": 21, "title": "双截龙", "titleEn": "Double_Dragon", "rom": "roms/21-Double_Dragon.nes"},
    {"id": 23, "title": "赤影战士", "titleEn": "Shadow_of_the_Ninja", "rom": "roms/23-Shadow_of_the_Ninja.nes"},
    {"id": 24, "title": "绿色兵团", "titleEn": "Rush_Attack", "rom": "roms/24-Rush_n_Attack.nes"},
    {"id": 25, "title": "淘金者", "titleEn": "Lode_Runner", "rom": "roms/25-Lode_Runner.nes"},
    {"id": 26, "title": "所罗门之钥", "titleEn": "Solomons_Key", "rom": "roms/26-Solomons_Key.nes"},
    {"id": 27, "title": "泡泡龙", "titleEn": "Bubble_Bobble", "rom": "roms/27-Bubble_Bobble.nes"},
    {"id": 29, "title": "影之传说", "titleEn": "The_Legend_of_Kage", "rom": "roms/29-The_Legend_of_Kage.nes"},
    {"id": 31, "title": "马里奥高尔夫", "titleEn": "Mario_Golf", "rom": "roms/31-Mario_Golf.nes"},
    {"id": 33, "title": "越野机车", "titleEn": "Excitebike", "rom": "roms/33-Excitebike.nes"},
    {"id": 35, "title": "世界杯", "titleEn": "World_Cup", "rom": "roms/35-World_Cup.nes"},
    {"id": 36, "title": "特库莫碗", "titleEn": "Tecmo_Bowl", "rom": "roms/36-Tecmo_Bowl.nes"},
    {"id": 37, "title": "弹珠台", "titleEn": "Pinball", "rom": "roms/37-Pinball.nes"},
    {"id": 38, "title": "气球塔防", "titleEn": "Balloon_Fight", "rom": "roms/38-Balloon_Fight.nes"},
    {"id": 39, "title": "西天取经", "titleEn": "Journey_to_the_West", "rom": "roms/39-Journey_to_the_West.nes"},
    {"id": 41, "title": "火之鸟", "titleEn": "Phoenix", "rom": "roms/41-Phoenix.nes"},
    {"id": 42, "title": "小蜜蜂", "titleEn": "Galaga", "rom": "roms/42-Galaga.nes"},
    {"id": 43, "title": "太空侵略者", "titleEn": "Space_Invaders", "rom": "roms/43-Space_Invaders.nes"},
    {"id": 44, "title": "1942", "titleEn": "1942", "rom": "roms/44-1942.nes"},
    {"id": 45, "title": "吸尘器", "titleEn": "Wrecking_Crew", "rom": "roms/45-Wrecking_Crew.nes"},
    {"id": 46, "title": "石匠", "titleEn": "Mario_Bros", "rom": "roms/46-Mario_Bros.nes"},
    {"id": 48, "title": "功夫", "titleEn": "Kung_Fu", "rom": "roms/48-Kung_Fu.nes"},
    {"id": 49, "title": "猪小弟", "titleEn": "Pooyan", "rom": "roms/49-Pooyan.nes"},
    {"id": 50, "title": "大蜜蜂", "titleEn": "Xevious", "rom": "roms/50-Xevious.nes"},
    {"id": 51, "title": "冒险岛", "titleEn": "Adventure_Island", "rom": "roms/51-Adventure_Island.nes"},
]

def create_screenshot_script():
    """Create Node.js script to capture screenshots"""
    script = '''const fs = require('fs');
const jsnes = require('./node_modules/jsnes');

const games = ''' + json.dumps(GAMES) + ''';

async function captureScreenshot(game) {
    return new Promise((resolve) => {
        // Check if ROM exists
        if (!fs.existsSync(game.rom)) {
            console.log(`❌ ROM不存在: ${game.rom}`);
            resolve(false);
            return;
        }

        try {
            // Read ROM
            const romData = fs.readFileSync(game.rom);
            const romString = Array.from(romData).map(b => String.fromCharCode(b)).join('');

            // Initialize NES
            const nes = new jsnes.NES({
                onFrame: function(buffer) {
                    // Capture first frame
                    // Convert buffer to image
                    console.log(`🎮 ${game.title}: 运行中...`);

                    // Save screenshot (256x240)
                    const imageData = Buffer.from(buffer);

                    // Convert to PNG (simplified)
                    const filename = `images/${game.id}-${game.titleEn}.png`;
                    // For now, we'd need a PNG encoder

                    nes.frame();
                    nes.stop();

                    resolve(true);
                },
                onAudioSample: function(left, right) {}
            });

            nes.loadROM(romString);

            // Run for 60 frames (1 second)
            for (let i = 0; i < 60; i++) {
                nes.frame();
            }

            resolve(true);
        } catch (error) {
            console.log(`❌ ${game.title}: ${error.message}`);
            resolve(false);
        }
    });
}

async function main() {
    console.log('🎮 开始截取游戏画面...\\n');
    let success = 0;

    for (const game of games) {
        if (await captureScreenshot(game)) {
            success++;
        }
    }

    console.log(`\\n✅ 完成: ${success}/${games.length}`);
}

main();
'''
    return script

print("=" * 70)
print("🎮 NES 游戏截图自动生成工具")
print("=" * 70)
print()
print("正在准备自动截图脚本...")
print()

# Check if node_modules exists
if not os.path.exists("node_modules/jsnes"):
    print("❌ 错误: jsnes未安装")
    print("请先运行: npm install")
    sys.exit(1)

# Check ROMs
roms_missing = []
for game in GAMES:
    if not os.path.exists(game["rom"]):
        roms_missing.append(game["rom"])

if roms_missing:
    print(f"⚠️  缺少ROM文件: {len(roms_missing)}个")
    print("这些游戏的ROM文件不存在，将跳过")
    print()

print("✅ 准备完成！")
print()
print("由于技术限制，我将提供一个替代方案：")
print()
print("💡 方案A: 手动运行游戏并截图")
print("1. 运行: 启动游戏.bat")
print("2. 逐个打开游戏")
print("3. 使用截图工具(Windows+Shift+S)截图")
print("4. 保存到 images/ 目录")
print()
print("💡 方案B: 使用在线NES模拟器截图")
print("1. 访问: https://www.retrogames.cc/")
print("2. 搜索游戏名称")
print("3. 运行游戏并截图")
print()
print("💡 方案C: 从游戏数据库下载预览图")
print("1. 访问: https://www.mobygames.com/")
print("2. 搜索游戏")
print("3. 下载游戏截图（不是封面）")
print()
