#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
过滤掉没有ROM的游戏
"""
import re
import os

# 缺失的ROM ID（没有对应ROM文件的游戏）
missing_roms = [22, 28, 30, 32, 34, 40, 47, 52]

# 读取原文件
with open('D:/ClaudeCodeProjects/nes-games-site/js/games-data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 解析游戏数据
games = []
pattern = r'\{\s*id:\s*(\d+),.*?(?=\n\s*\},\s*\n\s*\{|$)'
matches = re.finditer(pattern, content, re.DOTALL)

for match in matches:
    game_id = int(match.group(1))
    if game_id not in missing_roms:
        # 提取完整的游戏对象
        start = match.start()
        # 找到结束位置
        bracket_count = 0
        in_object = False
        end = start
        for i in range(start, len(content)):
            if content[i] == '{':
                bracket_count += 1
                in_object = True
            elif content[i] == '}':
                bracket_count -= 1
                if in_object and bracket_count == 0:
                    end = i + 1
                    break

        game_text = content[start:end]
        games.append((game_id, game_text))

# 生成新文件
output = []
output.append('// NES Games Database - 44 Classic Games (with ROMs)\n')
output.append('const gamesDatabase = [\n')

for game_id, game_text in sorted(games, key=lambda x: x[0]):
    output.append(game_text)
    output.append(',\n')

output[-1] = '\n];\n\n'

# 添加genreNames
# 从原文件提取genreNames
genre_match = re.search(r'const genreNames = \{.*?\};', content, re.DOTALL)
if genre_match:
    output.append(genre_match.group(0) + '\n')

# 写入新文件
with open('D:/ClaudeCodeProjects/nes-games-site/js/games-data.js', 'w', encoding='utf-8') as f:
    f.writelines(output)

print(f'Filtered games database')
print(f'Original: 52 games')
print(f'Removed: {len(missing_roms)} games (IDs: {missing_roms})')
print(f'Remaining: {len(games)} games')
