#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量重命名ROM文件以匹配游戏数据
"""
import os
import shutil
from pathlib import Path

# 游戏ID和实际文件名的映射
GAME_NAMES = {
    1: "Super_Mario_Bros",
    2: "The_Legend_of_Zelda",  # 添加 "The_"
    3: "Contra",
    4: "Battle_City",
    5: "Pac-Man",  # 修正为 Pac-Man
    6: "Donkey_Kong",
    7: "Mega_Man",
    8: "Castlevania",
    9: "Metroid",
    10: "Ninja_Gaiden",
    11: "Tetris",
    12: "Bomberman",
    13: "Ice_Climber",
    14: "Duck_Hunt",
    15: "Punch-Out",  # 修正为 Punch-Out
    16: "Final_Fantasy",
    17: "Dragon_Quest",
    18: "Kirby_Adventure",
    19: "Super_Mario_Bros_3",
    20: "Metal_Gear",
    21: "Double_Dragon",
    23: "Shadow_of_the_Ninja",
    24: "Rush_n_Attack",
    25: "Lode_Runner",
    26: "Solomons_Key",  # 修正为 Solomon's
    27: "Bubble_Bobble",
    29: "Legend_of_Kage",
    31: "Mario_Golf",
    33: "Excitebike",
    35: "World_Cup",
    36: "Tecmo_Bowl",
    37: "Pinball",
    38: "Balloon_Fight",
    39: "Journey_to_the_West",
    41: "Phoenix",
    42: "Galaga",
    43: "Space_Invaders",
    44: "1942",
    45: "Wrecking_Crew",
    46: "Mario_Bros",
    48: "Kung_Fu",
    49: "Pooyan",
    50: "Xevious",
    51: "Adventure_Island",
}

def rename_roms():
    roms_dir = Path("D:/ClaudeCodeProjects/nes-games-site/roms")

    if not roms_dir.exists():
        print("❌ roms目录不存在")
        return

    print("🔄 开始重命名ROM文件...\n")

    renamed = 0
    skipped = 0

    # 列出所有ROM文件
    for old_file in roms_dir.glob("*.nes"):
        # 提取ID
        try:
            parts = old_file.stem.split("-", 1)
            if len(parts) != 2:
                print(f"⚠️  跳过: {old_file.name} (格式不正确)")
                skipped += 1
                continue

            game_id = int(parts[0])

            # 检查是否需要重命名
            if game_id in GAME_NAMES:
                new_name = f"{game_id}-{GAME_NAMES[game_id]}.nes"
                new_file = roms_dir / new_name

                # 如果新文件名和旧文件名不同
                if new_file != old_file:
                    # 如果目标文件已存在，先删除
                    if new_file.exists():
                        print(f"⚠️  目标文件已存在: {new_name}")
                        old_file.unlink()

                    # 重命名
                    shutil.move(str(old_file), str(new_file))
                    print(f"✅ {old_file.name} -> {new_name}")
                    renamed += 1
                else:
                    print(f"✓ {old_file.name} (已正确)")
            else:
                print(f"⚠️  未知游戏ID {game_id}: {old_file.name}")
                skipped += 1

        except ValueError as e:
            print(f"❌ 错误: {old_file.name} - {e}")
            skipped += 1

    print(f"\n✅ 完成！")
    print(f"重命名: {renamed} 个")
    print(f"跳过: {skipped} 个")
    print(f"总计: {renamed + skipped} 个")

if __name__ == "__main__":
    rename_roms()
