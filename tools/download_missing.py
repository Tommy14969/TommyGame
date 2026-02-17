"""
Download the 3 missing game covers
"""

import requests
import sys
import io
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Missing games with alternative URLs
MISSING_GAMES = {
    "3-Contra": "https://www.mobygames.com/images/covers/l/29760-contra-nes-front-cover.jpg",
    "31-Mario_Golf": "https://www.mobygames.com/images/covers/l/41415-nes-open-tournament-golf-nes-front-cover.jpg",
    "46-Mario_Bros": "https://www.mobygames.com/images/covers/l/22286-mario-bros-nes-front-cover.jpg",
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
}

def download_cover(name, url):
    images_dir = Path("images")
    filepath = images_dir / f"{name}.png"

    try:
        print(f"⬇️  下载: {name}")
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()

        with open(filepath, 'wb') as f:
            f.write(response.content)

        size = filepath.stat().st_size
        print(f"   ✅ 成功: {name} ({size:,} bytes)")
        return True

    except Exception as e:
        print(f"   ❌ 失败: {name} - {e}")
        return False

print("🔄 下载失败的3个游戏封面...")
print()

success = 0
for name, url in MISSING_GAMES.items():
    if download_cover(name, url):
        success += 1

print()
print(f"✅ 完成! 成功: {success}/3")
