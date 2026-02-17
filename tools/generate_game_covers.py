"""
Generate NES game cover images using Python
Creates retro-style cover images for all games
"""

import sys
import io

# Set UTF-8 encoding for Windows console
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

from PIL import Image, ImageDraw, ImageFont
import json
import os
import re

# Game data matching the JavaScript database
GAMES = [
    {"id": 1, "title": "超级马里奥兄弟", "titleEn": "Super Mario Bros", "color": "#E60012"},
    {"id": 2, "title": "塞尔达传说", "titleEn": "The Legend of Zelda", "color": "#32CD32"},
    {"id": 3, "title": "魂斗罗", "titleEn": "Contra", "color": "#FF4500"},
    {"id": 4, "title": "坦克大战", "titleEn": "Tank Battle", "color": "#4169E1"},
    {"id": 5, "title": "吃豆人", "titleEn": "Pac-Man", "color": "#FFFF00"},
    {"id": 6, "title": "大金刚", "titleEn": "Donkey Kong", "color": "#8B4513"},
    {"id": 7, "title": "洛克人", "titleEn": "Mega Man", "color": "#00BFFF"},
    {"id": 8, "title": "恶魔城", "titleEn": "Castlevania", "color": "#4B0082"},
    {"id": 9, "title": "银河战士", "titleEn": "Metroid", "color": "#006400"},
    {"id": 10, "title": "忍者龙剑传", "titleEn": "Ninja Gaiden", "color": "#2F4F4F"},
    {"id": 11, "title": "俄罗斯方块", "titleEn": "Tetris", "color": "#FF1493"},
    {"id": 12, "title": "炸弹人", "titleEn": "Bomberman", "color": "#FF6347"},
    {"id": 13, "title": "冰山登山者", "titleEn": "Ice Climber", "color": "#00CED1"},
    {"id": 14, "title": "打鸭子", "titleEn": "Duck Hunt", "color": "#FFD700"},
    {"id": 15, "title": "拳无虚发", "titleEn": "Punch-Out!!", "color": "#DC143C"},
    {"id": 16, "title": "最终幻想", "titleEn": "Final Fantasy", "color": "#1E90FF"},
    {"id": 17, "title": "勇者斗恶龙", "titleEn": "Dragon Quest", "color": "#4169E1"},
    {"id": 18, "title": "星之卡比", "titleEn": "Kirby's Adventure", "color": "#FF69B4"},
    {"id": 19, "title": "马里奥兄弟3", "titleEn": "Super Mario Bros 3", "color": "#228B22"},
    {"id": 20, "title": "合金装备", "titleEn": "Metal Gear", "color": "#2F4F4F"},
    {"id": 21, "title": "双截龙", "titleEn": "Double Dragon", "color": "#8B0000"},
    {"id": 23, "title": "赤影战士", "titleEn": "Shadow of the Ninja", "color": "#000080"},
    {"id": 24, "title": "绿色兵团", "titleEn": "Rush'n Attack", "color": "#556B2F"},
    {"id": 25, "title": "淘金者", "titleEn": "Lode Runner", "color": "#DAA520"},
    {"id": 26, "title": "所罗门之钥", "titleEn": "Solomon's Key", "color": "#9400D3"},
    {"id": 27, "title": "泡泡龙", "titleEn": "Bubble Bobble", "color": "#00CED1"},
    {"id": 29, "title": "影之传说", "titleEn": "The Legend of Kage", "color": "#191970"},
    {"id": 31, "title": "马里奥高尔夫", "titleEn": "Mario Golf", "color": "#228B22"},
    {"id": 33, "title": "越野机车", "titleEn": "Excitebike", "color": "#8B4513"},
    {"id": 35, "title": "世界杯", "titleEn": "World Cup", "color": "#006400"},
    {"id": 36, "title": "特库莫碗", "titleEn": "Tecmo Bowl", "color": "#8B0000"},
    {"id": 37, "title": "弹珠台", "titleEn": "Pinball", "color": "#C0C0C0"},
    {"id": 38, "title": "气球塔防", "titleEn": "Balloon Fight", "color": "#87CEEB"},
    {"id": 39, "title": "西天取经", "titleEn": "Journey to the West", "color": "#FFD700"},
    {"id": 41, "title": "火之鸟", "titleEn": "Phoenix", "color": "#FF4500"},
    {"id": 42, "title": "小蜜蜂", "titleEn": "Galaga", "color": "#0000CD"},
    {"id": 43, "title": "太空侵略者", "titleEn": "Space Invaders", "color": "#00FF00"},
    {"id": 44, "title": "1942", "titleEn": "1942", "color": "#1E90FF"},
    {"id": 45, "title": "吸尘器", "titleEn": "Wrecking Crew", "color": "#CD853F"},
    {"id": 46, "title": "石匠", "titleEn": "Mario Bros", "color": "#228B22"},
    {"id": 48, "title": "功夫", "titleEn": "Kung Fu", "color": "#8B0000"},
    {"id": 49, "title": "猪小弟", "titleEn": "Pooyan", "color": "#FFC0CB"},
    {"id": 50, "title": "大蜜蜂", "titleEn": "Xevious", "color": "#4169E1"},
    {"id": 51, "title": "冒险岛", "titleEn": "Adventure Island", "color": "#228B22"},
]

def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def adjust_color(rgb, amount):
    """Adjust color brightness"""
    return tuple(max(0, min(255, c + amount)) for c in rgb)

def create_game_cover(game):
    """Create a retro-style game cover image"""
    width, height = 400, 300
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)

    # Main color
    main_color = hex_to_rgb(game['color'])
    dark_color = adjust_color(main_color, -80)
    lighter_color = adjust_color(main_color, 40)

    # Background gradient (simplified with strips)
    for y in range(height):
        ratio = y / height
        r = int(main_color[0] * (1 - ratio) + dark_color[0] * ratio)
        g = int(main_color[1] * (1 - ratio) + dark_color[1] * ratio)
        b = int(main_color[2] * (1 - ratio) + dark_color[2] * ratio)
        draw.rectangle([(0, y), (width, y+1)], fill=(r, g, b))

    # NES-style border
    border_width = 12
    draw.rectangle([(0, 0), (width-1, height-1)], outline=(255, 255, 255), width=3)
    draw.rectangle([(border_width, border_width), (width-border_width-1, height-border_width-1)],
                   outline=lighter_color, width=4)

    # Pixelated pattern
    for i in range(0, width, 20):
        for j in range(0, height, 20):
            if (i + j) % 40 == 0:
                draw.rectangle([(i, j), (i+8, j+8)], fill=(255, 255, 255, 30))

    # Title box background
    title_box_y = height - 100
    draw.rectangle([(20, title_box_y), (width-20, height-20)],
                   fill=(0, 0, 0, 180))

    # Draw game title
    try:
        # Try to use a larger font
        title_font = ImageFont.truetype("arial.ttf", 32)
        subtitle_font = ImageFont.truetype("arial.ttf", 18)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()

    # Chinese title
    title = game['title']
    draw.text((width//2, title_box_y + 15), title, fill=(255, 255, 255),
             font=title_font, anchor="mm")

    # English title
    subtitle = game['titleEn']
    draw.text((width//2, title_box_y + 55), subtitle, fill=(200, 200, 200),
             font=subtitle_font, anchor="mm")

    # Game ID badge
    draw.rectangle([(width - 60, 20), (width - 20, 50)], fill=main_color)
    try:
        id_font = ImageFont.truetype("arial.ttf", 20)
    except:
        id_font = ImageFont.load_default()
    draw.text((width - 40, 35), str(game['id']), fill=(255, 255, 255),
             font=id_font, anchor="mm")

    # Add "NES" watermark
    try:
        nes_font = ImageFont.truetype("arial.ttf", 14)
    except:
        nes_font = ImageFont.load_default()
    draw.text((30, 30), "NES", fill=(255, 255, 255, 150),
             font=nes_font, anchor="lm")

    return img

def main():
    # Create images directory
    images_dir = "images"
    os.makedirs(images_dir, exist_ok=True)

    print("🎮 生成游戏封面图...")
    print(f"目标目录: {images_dir}/\n")

    for game in GAMES:
        filename = f"{game['id']}-{game['titleEn'].replace(' ', '_')}.png"
        filepath = os.path.join(images_dir, filename)

        # Generate cover image
        img = create_game_cover(game)
        img.save(filepath, 'PNG')

        print(f"✅ 生成: {filename}")

    print(f"\n🎉 完成! 共生成 {len(GAMES)} 张游戏封面图")
    print(f"📁 保存位置: {images_dir}/")

if __name__ == "__main__":
    main()
