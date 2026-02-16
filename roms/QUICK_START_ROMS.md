# 快速开始：从FC_ROMS获取游戏ROM

## 🎮 最简单的方式获取ROM

**GitHub仓库**: https://github.com/zdg-kinlon/FC_ROMS

这个仓库包含**1053个官方NES/FDS游戏ROM**，是目前最完整的红白机ROM集合！

---

## 📋 三步快速获取

### 步骤1：查找游戏编号

访问 https://github.com/zdg-kinlon/FC_ROMS 查看README中的游戏索引表。

**最热门游戏速查表**：

| # | 游戏中文名 | 游戏英文名 | 仓库编号 |
|---|----------|-----------|---------|
| 1 | 超级马里奥兄弟 | Super Mario Bros. | 0066 |
| 2 | 塞尔达传说 | The Legend of Zelda | 0101 |
| 3 | 魂斗罗 | Contra | 0420 |
| 4 | 坦克大战 | Battle City | 0065 |
| 5 | 吃豆人 | Pac-Man | 0024 |
| 6 | 俄罗斯方块 | Tetris | 0593 |
| 7 | 洛克人 | Mega Man | 0390 |
| 8 | 恶魔城 | Castlevania | 0162 |
| 9 | 密特罗德 | Metroid | 0145 |
| 10 | 忍者龙剑传 | Ninja Gaiden | 0574 |
| 11 | 打鸭子 | Duck Hunt | 0013 |
| 12 | 冰山登山者 | Ice Climber | 0031 |
| 13 | 气球大战 | Balloon Fight | 0030 |
| 14 | 淘金者 | Lode Runner | 0019 |
| 15 | 泡泡龙 | Bubble Bobble | 0356 |
| 16 | 双截龙 | Double Dragon | 0451 |
| 17 | 热血硬派 | Renegade | 0260 |
| 18 | 赤影战士 | Shadow of the Ninja | 0857 |
| 19 | 绿色兵团 | Rush'n Attack | 0252 |
| 20 | 马里奥兄弟3 | Super Mario Bros. 3 | 0546 |

### 步骤2：访问并下载ROM

**方式A - 直接访问（推荐）**：
```
https://github.com/zdg-kinlon/FC_ROMS/tree/main/ROM/0066
```
将编号 `0066` 替换为您需要的游戏编号，然后点击下载文件。

**方式B - 浏览文件夹**：
1. 访问 https://github.com/zdg-kinlon/FC_ROMS
2. 点击 `ROM` 文件夹
3. 在URL后添加 `/编号`（如 `/ROM/0066`）
4. 下载ROM文件

### 步骤3：重命名并放置

下载后，将ROM文件重命名为规范格式并放入 `roms/` 目录：

```bash
# 命名格式：{ID}-{English_Title}.nes
mv下载的文件.nes roms/1-Super_Mario_Bros.nes
```

**示例**：
- 下载 `Super Mario Bros (World).nes`
- 重命名为 `1-Super_Mario_Bros.nes`
- 移动到 `roms/` 目录

---

## 🎯 完整示例：下载超级马里奥兄弟

```bash
# 1. 访问仓库并查找编号
# 超级马里奥兄弟 = 0066

# 2. 访问下载页面
https://github.com/zdg-kinlon/FC_ROMS/tree/main/ROM/0066

# 3. 下载ROM文件
# 点击文件，然后点击 "Download" 或 "Raw"

# 4. 重命名并移动
# Windows:
move "下载的文件.nes" "roms\1-Super_Mario_Bros.nes"

# Mac/Linux:
mv "下载的文件.nes" "roms/1-Super_Mario_Bros.nes"

# 5. 启动网站
python -m http.server 8000
# 访问 http://localhost:8000
```

---

## 📚 完整游戏分类

该仓库的游戏按发售日期编号，从 `0001` 到 `1252`，涵盖：

- **动作游戏**：马里奥、洛克人、恶魔城等
- **冒险游戏**：塞尔达、密特罗德等
- **射击游戏**：魂斗罗、1942等
- **益智游戏**：俄罗斯方块、吃豆人等
- **角色扮演**：最终幻想、勇者斗恶龙等
- **运动游戏**：高尔夫、网球、棒球等

---

## 🔍 高级技巧

### 批量下载多个游戏

```bash
# 使用wget批量下载
#!/bin/bash
games=(
    "0066:1-Super_Mario_Bros.nes"
    "0101:2-Legend_of_Zelda.nes"
    "0420:3-Contra.nes"
    "0065:4-Battle_City.nes"
)

for game in "${games[@]}"; do
    IFS=':' read -r number name <<< "$game"
    url="https://raw.githubusercontent.com/zdg-kinlon/FC_ROMS/main/ROM/$number/"
    echo "下载 $name 从 $url"
    # 需要根据实际文件名调整
done
```

### 克隆整个仓库

```bash
# ⚠️ 警告：仓库很大（可能数百MB）
git clone https://github.com/zdg-kinlon/FC_ROMS.git

# 然后从 FC_ROMS/ROM/ 目录中复制需要的ROM文件
cp FC_ROMS/ROM/0066/*.nes roms/1-Super_Mario_Bros.nes
```

---

## ⚠️ 重要提示

### 版权说明
- 这些ROM文件仅供个人学习和研究使用
- 请勿用于商业用途
- 如果您拥有正版卡带，下载备份ROM是合法的
- 支持正版，购买官方重制版

### 使用建议
- 建议先下载2-3个游戏测试功能
- ROM文件大小通常在40KB - 1MB之间
- 确保文件完整且未损坏
- 使用NTSC版本以获得最佳兼容性

---

## 🆘 遇到问题？

**Q: 找不到某个游戏？**
A: 查看仓库README中的完整游戏索引，包含1053个游戏

**Q: ROM无法加载？**
A: 检查：
1. 文件名是否正确（区分大小写）
2. 文件是否在 `roms/` 目录下
3. 文件是否完整下载

**Q: 游戏运行不正常？**
A: 某些游戏可能需要特定的mapper支持，JSNES可能不兼容所有游戏

**Q: 如何知道游戏的正确编号？**
A: 在仓库README中搜索游戏名称（中文或英文）

---

## 📞 更多资源

- **完整游戏索引**：https://github.com/zdg-kinlon/FC_ROMS（查看README）
- **项目指南**：`roms/ROM_GUIDE.md`
- **合法来源**：`tools/LEGAL_ROM_SOURCES.md`

---

**享受游戏，致敬经典！** 🎮✨

---

*本指南仅供参考，请遵守当地法律法规，合法使用ROM文件*
