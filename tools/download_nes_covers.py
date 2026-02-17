"""
Download real NES game cover images from legitimate sources
"""

import os
import sys
import io

# Fix UTF-8 encoding for Windows console
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

import requests
from pathlib import Path
import time

# Real URLs to NES game cover art from various public sources
# These are from Wikipedia, Internet Archive, and other legitimate databases
GAME_COVER_URLS = {
    "1-Super_Mario_Bros": "https://upload.wikimedia.org/wikipedia/en/0/03/Super_Mario_Bros._box.png",
    "2-The_Legend_of_Zelda": "https://upload.wikimedia.org/wikipedia/en/9/95/The_Legend_of_Zelda_%281986%29.png",
    "3-Contra": "https://upload.wikimedia.org/wikipedia/en/2/22/ContraNES.jpg",
    "4-Tank_Battle": "https://upload.wikimedia.org/wikipedia/en/8/86/Battle_City_%28NES%29.png",
    "5-Pac-Man": "https://upload.wikimedia.org/wikipedia/en/5/5a/Pac-Man_NES_cover.png",
    "6-Donkey_Kong": "https://upload.wikimedia.org/wikipedia/en/8/86/Donkey_Kong_%281981%29.png",
    "7-Mega_Man": "https://upload.wikimedia.org/wikipedia/en/6/60/Mega_Man_%28NES%29_cover.png",
    "8-Castlevania": "https://upload.wikimedia.org/wikipedia/en/9/94/Castlevania_box.png",
    "9-Metroid": "https://upload.wikimedia.org/wikipedia/en/9/96/Metroid_box.png",
    "10-Ninja_Gaiden": "https://upload.wikimedia.org/wikipedia/en/a/a2/Ninja_Gaiden_%28NES%29_cover.png",
    "11-Tetris": "https://upload.wikimedia.org/wikipedia/en/6/63/Tetris_%28NES%29.png",
    "12-Bomberman": "https://upload.wikimedia.org/wikipedia/en/6/6f/Bomberman_%28NES%29.png",
    "13-Ice_Climber": "https://upload.wikimedia.org/wikipedia/en/4/4d/Ice_Climber_%28NES%29_cover.png",
    "14-Duck_Hunt": "https://upload.wikimedia.org/wikipedia/en/f/f3/Duck_Hunt_cover.jpg",
    "15-Punch-Out": "https://upload.wikimedia.org/wikipedia/en/a/a6/Mike_Tyson%27s_Punch-Out%21%21_cover.png",
    "16-Final_Fantasy": "https://upload.wikimedia.org/wikipedia/en/6/62/Final_Fantasy_%28NES%29.png",
    "17-Dragon_Quest": "https://upload.wikimedia.org/wikipedia/en/4/45/Dragon_Quest_cover.png",
    "18-Kirby_Adventure": "https://upload.wikimedia.org/wikipedia/en/6/6c/Kirby%27s_Adventure_cover.png",
    "19-Super_Mario_Bros_3": "https://upload.wikimedia.org/wikipedia/en/c/c3/Super_Mario_Bros._3_box.png",
    "20-Metal_Gear": "https://upload.wikimedia.org/wikipedia/en/a/a5/Metal_Gear_%28NES%29_cover.png",
    "21-Double_Dragon": "https://upload.wikimedia.org/wikipedia/en/7/71/Double_Dragon_%28NES%29.png",
    "23-Shadow_of_the_Ninja": "https://upload.wikimedia.org/wikipedia/en/4/4d/Shadow_of_the_Ninja_%28NES%29.png",
    "24-Rush_Attack": "https://upload.wikimedia.org/wikipedia/en/b/bf/Rush%27n_Attack_%28NES%29.png",
    "25-Lode_Runner": "https://upload.wikimedia.org/wikipedia/en/2/2a/Lode_Runner_%28NES%29.png",
    "26-Solomons_Key": "https://upload.wikimedia.org/wikipedia/en/8/88/Solomon%27s_Key_%28NES%29.png",
    "27-Bubble_Bobble": "https://upload.wikimedia.org/wikipedia/en/4/49/Bubble_Bobble_%28NES%29_cover.png",
    "29-The_Legend_of_Kage": "https://upload.wikimedia.org/wikipedia/en/e/e5/The_Legend_of_Kage_%28NES%29.png",
    "31-Mario_Golf": "https://upload.wikimedia.org/wikipedia/en/8/8e/NES_Open_Tournament_Golf_cover.png",
    "33-Excitebike": "https://upload.wikimedia.org/wikipedia/en/c/c2/Excitebike_%28NES%29.png",
    "35-World_Cup": "https://upload.wikimedia.org/wikipedia/en/e/e4/World_Cup_Soccer_%28NES%29.png",
    "36-Tecmo_Bowl": "https://upload.wikimedia.org/wikipedia/en/4/47/Tecmo_Bowl_%28NES%29.png",
    "37-Pinball": "https://upload.wikimedia.org/wikipedia/en/c/c3/Pinball_%28NES%29.png",
    "38-Balloon_Fight": "https://upload.wikimedia.org/wikipedia/en/8/87/Balloon_Fight_%28NES%29.png",
    "39-Journey_to_the_West": "https://upload.wikimedia.org/wikipedia/en/5/5a/Journey_to_the_West_%28NES%29.png",
    "41-Phoenix": "https://upload.wikimedia.org/wikipedia/en/e/e7/Phoenix_%28NES%29.png",
    "42-Galaga": "https://upload.wikimedia.org/wikipedia/en/9/9f/Galaga_%28NES%29.png",
    "43-Space_Invaders": "https://upload.wikimedia.org/wikipedia/en/7/75/Space_Invaders_%28NES%29.png",
    "44-1942": "https://upload.wikimedia.org/wikipedia/en/2/24/1942_%28NES%29.png",
    "45-Wrecking_Crew": "https://upload.wikimedia.org/wikipedia/en/6/6b/Wrecking_Crew_%28NES%29.png",
    "46-Mario_Bros": "https://upload.wikimedia.org/wikipedia/en/5/5d/Mario_Bros._%28NES%29.png",
    "48-Kung_Fu": "https://upload.wikimedia.org/wikipedia/en/f/f6/Kung-Fu_%28NES%29.png",
    "49-Pooyan": "https://upload.wikimedia.org/wikipedia/en/2/29/Pooyan_%28NES%29.png",
    "50-Xevious": "https://upload.wikimedia.org/wikipedia/en/a/a8/Xevious_%28NES%29.png",
    "51-Adventure_Island": "https://upload.wikimedia.org/wikipedia/en/0/04/Adventure_Island_%28NES%29.png",
}

def download_image(url, filename, index, total):
    """Download a single image"""
    images_dir = Path("images")
    images_dir.mkdir(exist_ok=True)

    filepath = images_dir / filename

    try:
        print(f"[{index}/{total}] ⬇️  下载: {filename}")

        response = requests.get(url, timeout=30, stream=True)
        response.raise_for_status()

        # Save image
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        print(f"          ✅ 成功: {filename}")
        return True

    except Exception as e:
        print(f"          ❌ 失败: {filename}")
        print(f"          错误: {str(e)}")
        return False

def main():
    print("=" * 60)
    print("🎮 NES 游戏封面下载工具")
    print("=" * 60)
    print()
    print(f"准备下载 {len(GAME_COVER_URLS)} 张游戏封面...")
    print("来源: Wikipedia (合法公开资源)")
    print()

    success_count = 0
    failed = []

    for index, (game_name, url) in enumerate(GAME_COVER_URLS.items(), 1):
        filename = f"{game_name}.png"

        if download_image(url, filename, index, len(GAME_COVER_URLS)):
            success_count += 1
        else:
            failed.append(game_name)

        # Be nice to the server
        time.sleep(0.5)

    print()
    print("=" * 60)
    print(f"✅ 下载完成!")
    print(f"   成功: {success_count}/{len(GAME_COVER_URLS)}")
    print(f"   失败: {len(failed)}")
    print()

    if failed:
        print("失败的封面:")
        for name in failed:
            print(f"  - {name}")
        print()
        print("提示: 您可以手动从以下网站下载这些封面:")
        print("  - https://nes.box/the-nes-library/")
        print("  - https://www.mobygames.com/")
        print("  - https://www.covergalore.com/")

    print()
    print("📁 保存位置: images/")
    print("🎮 刷新浏览器即可看到新的封面!")

if __name__ == "__main__":
    main()
