#!/usr/bin/env python3
"""
NES ROM 下载脚本模板
仅供合法ROM下载使用

⚠️ 重要提示：
- 仅用于下载您有权使用的ROM文件
- 从正版卡带提取的ROM备份
- 公共领域或授权的ROM
- Homebrew自制游戏
- 请遵守当地版权法律
"""

import os
import requests
from pathlib import Path

# ROM文件列表
ROM_FILES = [
    # 格式: (ID, English_Name, 描述)
    (1, "Super_Mario_Bros", "从您的正版卡带备份或合法来源获取"),
    (2, "Legend_of_Zelda", "从您的正版卡带备份或合法来源获取"),
    (3, "Contra", "从您的正版卡带备份或合法来源获取"),
    # ... 添加更多游戏
]

# 配置
ROMS_DIR = Path(__file__).parent.parent / "roms"
BASE_URL = ""  # ⚠️ 请填写您的合法ROM来源URL


def download_rom(rom_id, rom_name, description):
    """下载单个ROM文件"""
    filename = f"{rom_id}-{rom_name}.nes"
    filepath = ROMS_DIR / filename

    # 检查是否已存在
    if filepath.exists():
        print(f"✓ {filename} 已存在，跳过")
        return True

    # ⚠️ 需要您填写实际的下载URL
    url = f"{BASE_URL}/{filename}"  # 根据实际情况修改

    try:
        print(f"正在下载: {filename}...")
        print(f"  来源: {url}")
        print(f"  说明: {description}")

        # 取消下面的注释来启用下载（请确保您有权下载这些文件）
        """
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()

        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        print(f"✓ {filename} 下载成功")
        """
        print(f"⚠️ {filename} 需要手动下载（请确认您有权使用）")

        return True

    except Exception as e:
        print(f"✗ {filename} 下载失败: {e}")
        return False


def main():
    """主函数"""
    print("=" * 60)
    print("NES ROM 下载工具")
    print("=" * 60)
    print()
    print("⚠️ 使用前请确认：")
    print("  1. 您有权使用这些ROM文件")
    print("  2. 用于个人学习和研究")
    print("  3. 遵守当地版权法律")
    print()
    print(f"ROM保存目录: {ROMS_DIR}")
    print()

    # 确认
    confirm = input("确认要继续吗？(yes/no): ")
    if confirm.lower() != 'yes':
        print("已取消")
        return

    # 创建目录
    ROMS_DIR.mkdir(exist_ok=True)

    # 下载ROM
    success_count = 0
    fail_count = 0

    for rom_id, rom_name, description in ROM_FILES:
        if download_rom(rom_id, rom_name, description):
            success_count += 1
        else:
            fail_count += 1
        print()

    # 统计
    print("=" * 60)
    print(f"下载完成: 成功 {success_count}, 失败 {fail_count}")
    print("=" * 60)


if __name__ == "__main__":
    main()
