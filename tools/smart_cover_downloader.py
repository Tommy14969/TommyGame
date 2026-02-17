"""
Smart NES Game Cover Downloader
Downloads real game covers from multiple sources with proper headers and retry logic
"""

import os
import sys
import io
import requests
from pathlib import Path
import time
import json

# Fix UTF-8 encoding for Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Multiple sources for game covers
COVER_SOURCES = {
    "mobygames": {
        "base": "https://www.mobygames.com",
        "search": "/search/quick?q="
    },
    "igdb": {
        "base": "https://images.igdb.com/igdb/image/upload/t_cover_big/",
    },
    "steam": {
        "base": "https://cdn.cloudflare.steamstatic.com/steam/apps/",
    }
}

# Game cover URLs with multiple fallback sources
GAME_COVERS = {
    "1-Super_Mario_Bros": [
        "https://www.mobygames.com/images/covers/l/38990-super-mario-bros-nes-front-cover.jpg",
        "https://cdn.cloudflare.steamstatic.com/steam/apps/576470/capsule_616x353.jpg",
    ],
    "2-The_Legend_of_Zelda": [
        "https://www.mobygames.com/images/covers/l/44240-the-legend-of-zelda-nes-front-cover.jpg",
    ],
    "3-Contra": [
        "https://www.mobygames.com/images/covers/l/29759-contra-nes-front-cover.jpg",
    ],
    "4-Tank_Battle": [
        "https://www.mobygames.com/images/covers/l/58193-battle-city-nes-front-cover.jpg",
    ],
    "5-Pac-Man": [
        "https://www.mobygames.com/images/covers/l/25575-pac-man-nes-front-cover.jpg",
    ],
    "6-Donkey_Kong": [
        "https://www.mobygames.com/images/covers/l/22287-donkey-kong-nes-front-cover.jpg",
    ],
    "7-Mega_Man": [
        "https://www.mobygames.com/images/covers/l/16231-mega-man-nes-front-cover.jpg",
    ],
    "8-Castlevania": [
        "https://www.mobygames.com/images/covers/l/58855-castlevania-nes-front-cover.jpg",
    ],
    "9-Metroid": [
        "https://www.mobygames.com/images/covers/l/58854-metroid-nes-front-cover.jpg",
    ],
    "10-Ninja_Gaiden": [
        "https://www.mobygames.com/images/covers/l/16335-ninja-gaiden-nes-front-cover.jpg",
    ],
    "11-Tetris": [
        "https://www.mobygames.com/images/covers/l/42628-tetris-nes-front-cover.jpg",
    ],
    "12-Bomberman": [
        "https://www.mobygames.com/images/covers/l/20173-bomberman-nes-front-cover.jpg",
    ],
    "13-Ice_Climber": [
        "https://www.mobygames.com/images/covers/l/59074-ice-climber-nes-front-cover.jpg",
    ],
    "14-Duck_Hunt": [
        "https://www.mobygames.com/images/covers/l/45364-duck-hunt-nes-front-cover.jpg",
    ],
    "15-Punch-Out": [
        "https://www.mobygames.com/images/covers/l/46262-mike-tyson-s-punch-out-nes-front-cover.jpg",
    ],
    "16-Final_Fantasy": [
        "https://www.mobygames.com/images/covers/l/41411-final-fantasy-nes-front-cover.jpg",
    ],
    "17-Dragon_Quest": [
        "https://www.mobygames.com/images/covers/l/20394-dragon-warrior-nes-front-cover.jpg",
    ],
    "18-Kirby_Adventure": [
        "https://www.mobygames.com/images/covers/l/41439-kirby-s-adventure-nes-front-cover.jpg",
    ],
    "19-Super_Mario_Bros_3": [
        "https://www.mobygames.com/images/covers/l/32802-super-mario-bros-3-nes-front-cover.jpg",
    ],
    "20-Metal_Gear": [
        "https://www.mobygames.com/images/covers/l/19383-metal-gear-nes-front-cover.jpg",
    ],
    "21-Double_Dragon": [
        "https://www.mobygames.com/images/covers/l/20082-double-dragon-nes-front-cover.jpg",
    ],
    "23-Shadow_of_the_Ninja": [
        "https://www.mobygames.com/images/covers/l/34486-shadow-of-the-ninja-nes-front-cover.jpg",
    ],
    "24-Rush_Attack": [
        "https://www.mobygames.com/images/covers/l/32474-rush-n-attack-nes-front-cover.jpg",
    ],
    "25-Lode_Runner": [
        "https://www.mobygames.com/images/covers/l/34353-lode-runner-nes-front-cover.jpg",
    ],
    "26-Solomons_Key": [
        "https://www.mobygames.com/images/covers/l/39592-solomon-s-key-nes-front-cover.jpg",
    ],
    "27-Bubble_Bobble": [
        "https://www.mobygames.com/images/covers/l/20389-bubble-bobble-nes-front-cover.jpg",
    ],
    "29-The_Legend_of_Kage": [
        "https://www.mobygames.com/images/covers/l/39296-the-legend-of-kage-nes-front-cover.jpg",
    ],
    "31-Mario_Golf": [
        "https://www.mobygames.com/images/covers/l/59563-nes-open-tournament-golf-nes-front-cover.jpg",
    ],
    "33-Excitebike": [
        "https://www.mobygames.com/images/covers/l/22287-excitebike-nes-front-cover.jpg",
    ],
    "35-World_Cup": [
        "https://www.mobygames.com/images/covers/l/36335-world-cup-soccer-nes-front-cover.jpg",
    ],
    "36-Tecmo_Bowl": [
        "https://www.mobygames.com/images/covers/l/36337-tecmo-bowl-nes-front-cover.jpg",
    ],
    "37-Pinball": [
        "https://www.mobygames.com/images/covers/l/59562-pinball-nes-front-cover.jpg",
    ],
    "38-Balloon_Fight": [
        "https://www.mobygames.com/images/covers/l/20390-balloon-fight-nes-front-cover.jpg",
    ],
    "39-Journey_to_the_West": [
        "https://www.mobygames.com/images/covers/l/42386-journey-to-the-west-nes-front-cover.jpg",
    ],
    "41-Phoenix": [
        "https://www.mobygames.com/images/covers/l/29957-phoenix-nes-front-cover.jpg",
    ],
    "42-Galaga": [
        "https://www.mobygames.com/images/covers/l/25574-galaga-nes-front-cover.jpg",
    ],
    "43-Space_Invaders": [
        "https://www.mobygames.com/images/covers/l/27318-space-invaders-nes-front-cover.jpg",
    ],
    "44-1942": [
        "https://www.mobygames.com/images/covers/l/16334-1942-nes-front-cover.jpg",
    ],
    "45-Wrecking_Crew": [
        "https://www.mobygames.com/images/covers/l/59076-wrecking-crew-nes-front-cover.jpg",
    ],
    "46-Mario_Bros": [
        "https://www.mobygames.com/images/covers/l/22293-mario-bros-nes-front-cover.jpg",
    ],
    "48-Kung_Fu": [
        "https://www.mobygames.com/images/covers/l/16333-spartan-x-nes-front-cover.jpg",
    ],
    "49-Pooyan": [
        "https://www.mobygames.com/images/covers/l/19990-pooyan-nes-front-cover.jpg",
    ],
    "50-Xevious": [
        "https://www.mobygames.com/images/covers/l/25679-xevious-nes-front-cover.jpg",
    ],
    "51-Adventure_Island": [
        "https://www.mobygames.com/images/covers/l/19989-adventure-island-nes-front-cover.jpg",
    ],
}

def download_with_retry(urls, filename, index, total, max_retries=3):
    """Download image with retry logic and multiple URL fallbacks"""
    images_dir = Path("images")
    images_dir.mkdir(exist_ok=True)
    filepath = images_dir / filename

    # Headers to mimic browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }

    for attempt in range(max_retries):
        for url_idx, url in enumerate(urls):
            try:
                print(f"[{index}/{total}] ⬇️  尝试: {filename} (来源 {url_idx + 1})")

                response = requests.get(url, headers=headers, timeout=30, stream=True)
                response.raise_for_status()

                # Check if we got an image
                content_type = response.headers.get('content-type', '')
                if 'image' not in content_type.lower():
                    print(f"          ⚠️  不是图片: {content_type}")
                    continue

                # Save image
                with open(filepath, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)

                # Verify file size
                file_size = filepath.stat().st_size
                if file_size < 1000:  # Less than 1KB is probably an error page
                    print(f"          ⚠️  文件太小: {file_size} bytes")
                    filepath.unlink()
                    continue

                print(f"          ✅ 成功: {filename} ({file_size:,} bytes)")
                return True

            except requests.exceptions.HTTPError as e:
                if e.response.status_code == 404:
                    print(f"          ❌ 404: 图片不存在")
                elif e.response.status_code == 403:
                    print(f"          ⚠️  403: 访问被拒绝")
                else:
                    print(f"          ⚠️  HTTP错误: {e}")
            except Exception as e:
                print(f"          ⚠️  错误: {str(e)[:50]}")

        if attempt < max_retries - 1:
            wait_time = (attempt + 1) * 2
            print(f"          🔄 等待 {wait_time}秒后重试...")
            time.sleep(wait_time)

    print(f"          ❌ 失败: {filename} (所有来源均失败)")
    return False

def main():
    print("=" * 70)
    print("🎮 NES 游戏封面智能下载器")
    print("=" * 70)
    print()
    print(f"准备下载 {len(GAME_COVERS)} 张游戏封面...")
    print("来源: MobyGames (高质量官方封面)")
    print()

    success_count = 0
    failed = []

    for index, (game_name, urls) in enumerate(GAME_COVERS.items(), 1):
        filename = f"{game_name}.png"

        if download_with_retry(urls, filename, index, len(GAME_COVERS)):
            success_count += 1
        else:
            failed.append(game_name)

        # Be nice to the server
        time.sleep(1)

    print()
    print("=" * 70)
    print(f"✅ 下载完成!")
    print(f"   成功: {success_count}/{len(GAME_COVERS)}")
    print(f"   失败: {len(failed)}")
    print("=" * 70)
    print()

    if failed:
        print("失败的封面:")
        for name in failed:
            print(f"  - {name}")
        print()
        print("💡 提示: 您可以手动从以下网站下载这些封面:")
        print("   - https://nes.box/the-nes-library/ (推荐)")
        print("   - https://www.mobygames.com/")
        print("   - https://www.covergalore.com/")
        print()

    print("📁 保存位置: images/")
    print("🎮 刷新浏览器即可看到新的封面!")
    print()

    # Generate manual download guide for failed games
    if failed:
        guide_file = Path("images/FAILED_DOWNLOADS.md")
        with open(guide_file, 'w', encoding='utf-8') as f:
            f.write("# 未下载的游戏封面\n\n")
            f.write("以下游戏封面未能自动下载，请手动下载:\n\n")
            for name in failed:
                game_id = name.split('-')[0]
                f.write(f"## {name}\n")
                f.write(f"- NES.box: https://nes.box/the-nes-library/ (搜索 ID {game_id})\n")
                f.write(f"- MobyGames: 搜索游戏名称\n\n")
        print(f"📝 失败列表已保存到: {guide_file}")

if __name__ == "__main__":
    main()
