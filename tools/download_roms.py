#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ROM文件下载助手
从FC_ROMS仓库批量下载游戏ROM

使用方法：
    python download_roms.py

注意：请确保您有权使用这些ROM文件，仅供个人学习研究使用
"""

import os
import sys
import requests
from pathlib import Path

# 设置Windows控制台编码
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# 50个游戏的列表
GAMES = [
    {"id": 1, "title": "Super_Mario_Bros", "fc_id": "0066"},
    {"id": 2, "title": "Legend_of_Zelda", "fc_id": "0101"},
    {"id": 3, "title": "Contra", "fc_id": "0420"},
    {"id": 4, "title": "Battle_City", "fc_id": "0065"},
    {"id": 5, "title": "Pac-Man", "fc_id": "0024"},
    {"id": 6, "title": "Donkey_Kong", "fc_id": "0001"},
    {"id": 7, "title": "Mega_Man", "fc_id": "0390"},
    {"id": 8, "title": "Castlevania", "fc_id": "0162"},
    {"id": 9, "title": "Metroid", "fc_id": "0145"},
    {"id": 10, "title": "Ninja_Gaiden", "fc_id": "0574"},
    {"id": 11, "title": "Tetris", "fc_id": "0593"},
    {"id": 12, "title": "Bomberman", "fc_id": "0094"},
    {"id": 13, "title": "Ice_Climber", "fc_id": "0031"},
    {"id": 14, "title": "Duck_Hunt", "fc_id": "0013"},
    {"id": 15, "title": "Punch-Out", "fc_id": "0368"},
    {"id": 16, "title": "Final_Fantasy", "fc_id": "0397"},
    {"id": 17, "title": "Dragon_Quest", "fc_id": "0129"},
    {"id": 18, "title": "Kirby_Adventure", "fc_id": "1208"},
    {"id": 19, "title": "Super_Mario_Bros_3", "fc_id": "0546"},
    {"id": 20, "title": "Metal_Gear", "fc_id": "0399"},
    {"id": 21, "title": "Double_Dragon", "fc_id": "0451"},
    {"id": 22, "title": "Renegade", "fc_id": "0260"},
    {"id": 23, "title": "Shadow_of_the_Ninja", "fc_id": "0857"},
    {"id": 24, "title": "Rush_n_Attack", "fc_id": "0252"},
    {"id": 25, "title": "Lode_Runner", "fc_id": "0019"},
    {"id": 26, "title": "Solomons_Key", "fc_id": "0142"},
    {"id": 27, "title": "Bubble_Bobble", "fc_id": "0356"},
    {"id": 28, "title": "Rainbow_Islands", "fc_id": "0495"},
    {"id": 29, "title": "Legend_of_Kage", "fc_id": "0121"},
    {"id": 30, "title": "Chrono_Trigger", "fc_id": "0000"},
    {"id": 31, "title": "Mario_Golf", "fc_id": "1040"},
    {"id": 32, "title": "Mario_Tennis", "fc_id": "0000"},
    {"id": 33, "title": "Excitebike", "fc_id": "0029"},
    {"id": 34, "title": "Street_Basketball", "fc_id": "0000"},
    {"id": 35, "title": "World_Cup", "fc_id": "0037"},
    {"id": 36, "title": "Tecmo_Bowl", "fc_id": "0901"},
    {"id": 37, "title": "Pinball", "fc_id": "0011"},
    {"id": 38, "title": "Balloon_Fight", "fc_id": "0030"},
    {"id": 39, "title": "Journey_to_the_West", "fc_id": "0179"},
    {"id": 40, "title": "Mitsume_Ga_Tooru", "fc_id": "0000"},
    {"id": 41, "title": "Phoenix", "fc_id": "0219"},
    {"id": 42, "title": "Galaga", "fc_id": "0033"},
    {"id": 43, "title": "Space_Invaders", "fc_id": "0038"},
    {"id": 44, "title": "1942", "fc_id": "0088"},
    {"id": 45, "title": "Wrecking_Crew", "fc_id": "0046"},
    {"id": 46, "title": "Mario_Bros", "fc_id": "0006"},
    {"id": 47, "title": "Helicopter", "fc_id": "0000"},
    {"id": 48, "title": "Kung_Fu", "fc_id": "0047"},
    {"id": 49, "title": "Pooyan", "fc_id": "0067"},
    {"id": 50, "title": "Xevious", "fc_id": "0025"},
    {"id": 51, "title": "Adventure_Island", "fc_id": "0155"},
    {"id": 52, "title": "Star_Ocean", "fc_id": "0000"},
]

# FC_ROMS GitHub API配置
GITHUB_API_BASE = "https://api.github.com/repos/zdg-kinlon/FC_ROMS/contents/ROM"
RAW_BASE = "https://raw.githubusercontent.com/zdg-kinlon/FC_ROMS/main/ROM"


def download_rom(game, roms_dir):
    """下载单个ROM文件"""
    fc_id = game["fc_id"]

    # 跳过无效ID
    if fc_id == "0000":
        print(f"⚠️  跳过 {game['title']} (ID无效)")
        return False

    try:
        # 获取文件夹内容
        url = f"{GITHUB_API_BASE}/{fc_id}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        contents = response.json()

        # 找到.nes文件
        nes_file = None
        for item in contents:
            if item["name"].endswith(".nes") or item["name"].endswith(".NES"):
                nes_file = item
                break

        if not nes_file:
            print(f"⚠️  {game['title']} (ID:{fc_id}) - 未找到.nes文件")
            return False

        # 下载文件
        download_url = nes_file["download_url"]
        file_response = requests.get(download_url, timeout=30, stream=True)
        file_response.raise_for_status()

        # 保存文件
        filename = f"{game['id']}-{game['title']}.nes"
        filepath = roms_dir / filename

        with open(filepath, 'wb') as f:
            for chunk in file_response.iter_content(chunk_size=8192):
                f.write(chunk)

        file_size = filepath.stat().st_size / 1024  # KB
        print(f"✅ {game['title']} - {file_size:.1f}KB")
        return True

    except requests.exceptions.RequestException as e:
        print(f"❌ {game['title']} (ID:{fc_id}) - 下载失败: {e}")
        return False
    except Exception as e:
        print(f"❌ {game['title']} (ID:{fc_id}) - 错误: {e}")
        return False


def main():
    """主函数"""
    print("=" * 60)
    print("🎮 FC游戏ROM下载助手")
    print("=" * 60)
    print()

    # 确认
    print("⚠️  请确认您已阅读并理解：")
    print("   1. 这些ROM文件仅供个人学习研究使用")
    print("   2. 请勿用于商业用途")
    print("   3. 您应该拥有相应的正版游戏")
    print()

    response = input("是否继续？(yes/no): ").strip().lower()
    if response not in ['yes', 'y', '是']:
        print("已取消")
        return

    print()
    print("开始下载...")
    print()

    # 创建roms目录
    project_root = Path(__file__).parent.parent
    roms_dir = project_root / "roms"
    roms_dir.mkdir(exist_ok=True)

    # 下载统计
    success_count = 0
    fail_count = 0

    # 逐个下载
    for i, game in enumerate(GAMES, 1):
        print(f"[{i}/{len(GAMES)}] ", end="")

        if download_rom(game, roms_dir):
            success_count += 1
        else:
            fail_count += 1

    # 显示结果
    print()
    print("=" * 60)
    print("下载完成！")
    print(f"✅ 成功: {success_count} 个")
    print(f"❌ 失败: {fail_count} 个")
    print(f"📁 ROM文件位置: {roms_dir}")
    print()
    print("现在可以启动网站测试游戏了：")
    print("  python -m http.server 8000")
    print("  访问 http://localhost:8000")
    print("=" * 60)


if __name__ == "__main__":
    main()
