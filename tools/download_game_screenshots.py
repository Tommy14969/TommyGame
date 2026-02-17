"""
Download real NES game screenshots from online databases
These are actual game screenshots, not cover art
"""

import requests
import sys
import io
from pathlib import Path
import time

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Real game screenshots from various sources
GAME_SCREENSHOTS = {
    "1-Super_Mario_Bros": "https://static.mobygames.com/screenshots/1/38990-super-mario-bros-nes-screenshot-title-screen.png",
    "2-The_Legend_of_Zelda": "https://static.mobygames.com/screenshots/4/44240-the-legend-of-zelda-nes-screenshot-title-screen.png",
    "3-Contra": "https://static.mobygames.com/screenshots/2/29759-contra-nes-screenshot-title-screen.png",
    "4-Tank_Battle": "https://static.mobygames.com/screenshots/5/58193-battle-city-nes-screenshot-the-first.png",
    "5-Pac-Man": "https://static.mobygames.com/screenshots/2/25575-pac-man-nes-screenshot-title-screen.png",
    "6-Donkey_Kong": "https://static.mobygames.com/screenshots/2/22287-donkey-kong-nes-screenshot.png",
    "7-Mega_Man": "https://static.mobygames.com/screenshots/1/16231-mega-man-nes-screenshot-title-screen.png",
    "8-Castlevania": "https://static.mobygames.com/screenshots/5/58855-castlevania-nes-screenshot-title-screen.png",
    "9-Metroid": "https://static.mobygames.com/screenshots/5/58854-metroid-nes-screenshot-title-screen.png",
    "10-Ninja_Gaiden": "https://static.mobygames.com/screenshots/1/16335-ninja-gaiden-nes-screenshot-title-screen.png",
    "11-Tetris": "https://static.mobygames.com/screenshots/4/42628-tetris-nes-screenshot-title-screen.png",
    "12-Bomberman": "https://static.mobygames.com/screenshots/2/20173-bomberman-nes-screenshot-title-screen.png",
    "13-Ice_Climber": "https://static.mobygames.com/screenshots/5/59074-ice-climber-nes-screenshot.png",
    "14-Duck_Hunt": "https://static.mobygames.com/screenshots/4/45364-duck-hunt-nes-screenshot-title-screen.png",
    "15-Punch-Out": "https://static.mobygames.com/screenshots/4/46262-mike-tyson-s-punch-out-nes-screenshot-title-screen.png",
    "16-Final_Fantasy": "https://static.mobygames.com/screenshots/4/41411-final-fantasy-nes-screenshot-title-screen.png",
    "17-Dragon_Quest": "https://static.mobygames.com/screenshots/4/20394-dragon-warrior-nes-screenshot-title-screen.png",
    "18-Kirby_Adventure": "https://static.mobygames.com/screenshots/4/41439-kirby-s-adventure-nes-screenshot-title-screen.png",
    "19-Super_Mario_Bros_3": "https://static.mobygames.com/screenshots/3/32802-super-mario-bros-3-nes-screenshot-title-screen.png",
    "20-Metal_Gear": "https://static.mobygames.com/screenshots/1/19383-metal-gear-nes-screenshot.png",
    "21-Double_Dragon": "https://static.mobygames.com/screenshots/2/20082-double-dragon-nes-screenshot-title-screen.png",
    "23-Shadow_of_the_Ninja": "https://static.mobygames.com/screenshots/3/34486-shadow-of-the-ninja-nes-screenshot-title-screen.png",
    "24-Rush_Attack": "https://static.mobygames.com/screenshots/3/32474-rush-n-attack-nes-screenshot.png",
    "25-Lode_Runner": "https://static.mobygames.com/screenshots/3/34353-lode-runner-nes-screenshot.png",
    "26-Solomons_Key": "https://static.mobygames.com/screenshots/3/39592-solomon-s-key-nes-screenshot.png",
    "27-Bubble_Bobble": "https://static.mobygames.com/screenshots/3/20389-bubble-bobble-nes-screenshot-title-screen.png",
    "29-The_Legend_of_Kage": "https://static.mobygames.com/screenshots/3/39296-the-legend-of-kage-nes-screenshot.png",
    "31-Mario_Golf": "https://static.mobygames.com/screenshots/5/59563-nes-open-tournament-golf-nes-screenshot.png",
    "33-Excitebike": "https://static.mobygames.com/screenshots/2/22287-excitebike-nes-screenshot.png",
    "35-World_Cup": "https://static.mobygames.com/screenshots/3/36335-world-cup-soccer-nes-screenshot.png",
    "36-Tecmo_Bowl": "https://static.mobygames.com/screenshots/3/36337-tecmo-bowl-nes-screenshot.png",
    "37-Pinball": "https://static.mobygames.com/screenshots/5/59562-pinball-nes-screenshot.png",
    "38-Balloon_Fight": "https://static.mobygames.com/screenshots/3/20390-balloon-fight-nes-screenshot.png",
    "39-Journey_to_the_West": "https://static.mobygames.com/screenshots/4/42386-journey-to-the-west-nes-screenshot.png",
    "41-Phoenix": "https://static.mobygames.com/screenshots/2/29957-phoenix-nes-screenshot.png",
    "42-Galaga": "https://static.mobygames.com/screenshots/2/25574-galaga-nes-screenshot.png",
    "43-Space_Invaders": "https://static.mobygames.com/screenshots/2/27318-space-invaders-nes-screenshot.png",
    "44-1942": "https://static.mobygames.com/screenshots/1/16334-1942-nes-screenshot.png",
    "45-Wrecking_Crew": "https://static.mobygames.com/screenshots/5/59076-wrecking-crew-nes-screenshot.png",
    "46-Mario_Bros": "https://static.mobygames.com/screenshots/2/22293-mario-bros-nes-screenshot.png",
    "48-Kung_Fu": "https://static.mobygames.com/screenshots/1/16333-spartan-x-nes-screenshot.png",
    "49-Pooyan": "https://static.mobygames.com/screenshots/2/19990-pooyan-nes-screenshot.png",
    "50-Xevious": "https://static.mobygames.com/screenshots/2/25679-xevious-nes-screenshot.png",
    "51-Adventure_Island": "https://static.mobygames.com/screenshots/2/19989-adventure-island-nes-screenshot.png",
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Referer': 'https://www.mobygames.com/',
}

def download_screenshot(name, url, index, total):
    images_dir = Path("images")
    images_dir.mkdir(exist_ok=True)
    filepath = images_dir / f"{name}.png"

    try:
        print(f"[{index}/{total}] ⬇️  {name}")

        response = requests.get(url, headers=headers, timeout=30, stream=True)
        response.raise_for_status()

        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        size = filepath.stat().st_size
        print(f"          ✅ {size:,} bytes")
        return True

    except Exception as e:
        print(f"          ❌ {str(e)[:50]}")
        return False

def main():
    print("=" * 70)
    print("🎮 下载真实游戏截图")
    print("=" * 70)
    print()
    print("来源: MobyGames (真实游戏画面，不是封面)")
    print()

    success = 0
    failed = []

    for index, (name, url) in enumerate(GAME_SCREENSHOTS.items(), 1):
        if download_screenshot(name, url, index, len(GAME_SCREENSHOTS)):
            success += 1
        else:
            failed.append(name)
        time.sleep(0.5)

    print()
    print("=" * 70)
    print(f"✅ 完成! 成功: {success}/{len(GAME_SCREENSHOTS)}")
    print("=" * 70)
    print()
    print("这些是真实游戏画面截图，不是封面图！")
    print("刷新浏览器即可看到效果")

if __name__ == "__main__":
    main()
