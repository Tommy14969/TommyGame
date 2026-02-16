# NES ROM 文件获取指南

## 📋 需要的52个ROM文件清单

### 命名格式
```
{ID}-{English_Title}.nes
```

### 完整列表

```bash
# 动作游戏 (Action)
1-Super_Mario_Bros.nes
6-Donkey_Kong.nes
7-Mega_Man.nes
8-Castlevania.nes
10-Ninja_Gaiden.nes
12-Bomberman.nes
13-Ice_Climber.nes
18-Kirby_Adventure.nes
19-Super_Mario_Bros_3.nes
21-Double_Dragon.nes
22-Renegade.nes
23-Shadow_of_the_Ninja.nes
24-Rush_n_Attack.nes
27-Bubble_Bobble.nes
28-Rainbow_Islands.nes
29-Legend_of_Kage.nes
37-Pinball.nes
38-Balloon_Fight.nes
45-Wrecking_Crew.nes
46-Mario_Bros.nes
47-Helicopter.nes
48-Kung_Fu.nes
49-Pooyan.nes
51-Adventure_Island.nes

# 冒险游戏 (Adventure)
2-Legend_of_Zelda.nes
9-Metroid.nes
20-Metal_Gear.nes

# 射击游戏 (Shooter)
3-Contra.nes
14-Duck_Hunt.nes
41-Phoenix.nes
42-Galaga.nes
43-Space_Invaders.nes
44-1942.nes
50-Xevious.nes

# 益智游戏 (Puzzle)
5-Pac-Man.nes
11-Tetris.nes
25-Lode_Runner.nes
26-Solomons_Key.nes

# 运动游戏 (Sports)
15-Punch-Out.nes
31-Mario_Golf.nes
32-Mario_Tennis.nes
33-Excitebike.nes
34-Street_Basketball.nes
35-World_Cup.nes
36-Tecmo_Bowl.nes

# 角色扮演 (RPG)
16-Final_Fantasy.nes
17-Dragon_Quest.nes
30-Chrono_Trigger.nes
52-Star_Ocean.nes

# 特殊游戏
39-Journey_to_the_West.nes
40-Mitsume_Ga_Tooru.nes
```

## 🔍 合法获取ROM的途径

### 方法1: GitHub - FC_ROMS（强烈推荐）⭐
**网址**: https://github.com/zdg-kinlon/FC_ROMS

这是最推荐的ROM获取方式！该仓库包含**1053个官方NES/FDS游戏**：

**特点**:
- ✅ 完整的官方ROM集合
- ✅ 参考权威的《红白机终极档案》
- ✅ 包含日文/英文/中文完整索引
- ✅ 按发售日期和编号组织
- ✅ 仅收录官方原版，无第三方修改版

**使用步骤**:
1. 访问 https://github.com/zdg-kinlon/FC_ROMS
2. 在README中查找游戏索引表
3. 找到想要的游戏编号（例如：0066 = 超级马里奥兄弟）
4. 直接访问编号文件夹：`https://github.com/zdg-kinlon/FC_ROMS/tree/main/ROM/0066`
5. 下载ROM文件
6. 重命名为规范格式：`{ID}-{English_Title}.nes`
7. 放入 `roms/` 目录

**常用游戏快速查找**:
| 游戏名称 | 仓库编号 | 建议文件名 |
|---------|---------|-----------|
| 超级马里奥兄弟 | 0066 | 1-Super_Mario_Bros.nes |
| 塞尔达传说 | 0101 | 2-Legend_of_Zelda.nes |
| 魂斗罗 | 0420 | 3-Contra.nes |
| 坦克大战 | 0065 | 4-Battle_City.nes |
| 吃豆人 | 0024 | 5-Pac-Man.nes |
| 俄罗斯方块 | 0593 | 11-Tetris.nes |
| 洛克人 | 0390 | 7-Mega_Man.nes |
| 恶魔城 | 0162 | 8-Castlevania.nes |
| 密特罗德 | 0145 | 9-Metroid.nes |
| 忍者龙剑传 | 0574 | 10-Ninja_Gaiden.nes |

**批量下载建议**:
```bash
# 可以使用 git clone 下载整个仓库（但会很大）
git clone https://github.com/zdg-kinlon/FC_ROMS.git

# 或者只下载需要的ROM文件
# 访问对应的编号文件夹单独下载
```

---

### 方法2: Internet Archive
访问：https://archive.org/details/softwarelibrary_mame

1. 搜索游戏名称（英文）
2. 找到对应的NES ROM文件
3. 下载.nes文件
4. 重命名为上述格式
5. 放入roms/目录

**示例：**
- 搜索 "Super Mario Bros"
- 下载 ROM 文件
- 重命名为 `1-Super_Mario_Bros.nes`
- 放入 `roms/` 目录

### 方法2: 从正版卡带提取
如果您拥有正版NES卡带：

**需要的硬件：**
- USB CopyNES
- Kazzo
- INL Retro Programmer

**提取步骤：**
1. 连接设备到电脑
2. 插入卡带
3. 使用配套软件提取ROM
4. 保存为.nes文件
5. 按规范命名

### 方法3: Homebrew（自制游戏）
许多独立开发者制作的NES游戏是免费的：

**推荐网站：**
- http://www.nesdev.com/ - NES开发社区
- https://www itch.io/ - 独立游戏平台（搜索NES标签）
- https://sleigh.itch.io/ - 许多免费NES homebrew游戏

### 方法4: 公共领域ROM
一些老游戏已经进入公共领域：

- **Color Dreams** 游戏（部分）
- **Active Enterprises** 游戏（部分）
- 各种未授权第三方游戏

## 📥 快速设置步骤

### 步骤1: 创建测试ROM（用于测试UI）
如果暂时没有ROM文件，可以创建占位文件测试UI：

```bash
cd nes-games-site/roms
touch 1-Super_Mario_Bros.nes
```

这样至少可以测试ROM加载错误提示。

### 步骤2: 下载单个ROM测试
先下载1-2个ROM测试功能：

**推荐测试游戏：**
1. `1-Super_Mario_Bros.nes` - 经典必玩
2. `5-Pac-Man.nes` - 简单易测试
3. `11-Tetris.nes` - 益智游戏

### 步骤3: 批量下载
使用以下工具批量下载：

**Windows PowerShell:**
```powershell
# 示例：从Internet Archive下载
$games = @(
    "1-Super_Mario_Bros.nes",
    "5-Pac-Man.nes",
    "11-Tetris.nes"
)

foreach ($game in $games) {
    $url = "https://archive.org/download/nes-roms/$game"
    Invoke-WebRequest -Uri $url -OutFile $game
}
```

### 步骤4: 验证文件
确保ROM文件正确：
```bash
cd roms
ls -lh *.nes
```

每个文件应该是：
- 大小：几KB到几百KB
- 格式：.nes文件
- 可读：不是损坏的文件

## ⚠️ 重要注意事项

### 版权警告
- ROM文件受版权保护
- 仅用于个人学习和研究
- 不得用于商业用途
- 24小时内删除未授权ROM
- 支持正版购买重制版

### 文件验证
确保下载的ROM是：
- ✅ .nes格式（不是.zip）
- ✅ 完整文件（不是部分下载）
- ✅ 正确的region（NTSC vs PAL）
- ✅ 无病毒/恶意软件

### 常见问题

**Q: ROM无法加载？**
A: 检查：
1. 文件名是否完全匹配（区分大小写）
2. 文件是否在roms/目录下
3. 文件是否完整（查看文件大小）

**Q: 游戏运行缓慢？**
A: JSNES是JavaScript模拟器，性能取决于浏览器。建议使用Chrome或Firefox。

**Q: 某些游戏无法运行？**
A: 部分游戏可能使用特殊的mapper芯片，JSNES可能不支持所有游戏。

## 🎮 测试流程

### 1. 单个ROM测试
```bash
# 放入一个ROM
cp /path/to/Super_Mario_Bros.nes roms/1-Super_Mario_Bros.nes

# 打开浏览器
http://localhost:8000

# 点击游戏 → 开始游戏
```

### 2. 批量测试
```bash
# 放入多个ROM
cp *.nes roms/

# 刷新页面，测试多个游戏
```

### 3. 功能测试
- [ ] 游戏能正常加载
- [ ] 键盘控制正常
- [ ] 音效正常（如果启用）
- [ ] 暂停/恢复正常
- [ ] 重置功能正常
- [ ] 存档/读档正常

## 📊 ROM文件统计

| 分类 | 游戏数量 | 文件大小范围 |
|------|----------|--------------|
| 动作 | 24 | 24KB - 256KB |
| 冒险 | 3 | 128KB - 512KB |
| 射击 | 7 | 24KB - 128KB |
| 益智 | 4 | 32KB - 64KB |
| 运动 | 7 | 40KB - 128KB |
| RPG | 4 | 256KB - 1024KB |
| 特殊 | 3 | 48KB - 256KB |

**总计：52个游戏，约5-20MB**

## 🔗 推荐资源

### 官方ROM资源
- **GitHub - FC_ROMS** https://github.com/zdg-kinlon/FC_ROMS
  - 1053个官方NES/FDS ROM
  - 完整游戏索引
  - 参考官方档案整理
  - ⭐ **强烈推荐**

### ROM数据库
- https://www.romhacking.net/ - ROM修改和翻译
- https://archive.org/details/softwarelibrary_mame - Internet Archive ROM库
- https://www.emuparadise.me/ - ROM库（需注意版权）
- https://www.coolrom.com/ - ROM库（需注意版权）

### NES开发
- https://www.nesdev.org/ - NES开发wiki
- https://www.nesdev.com/ - NES开发资源
- https://wiki.nesdev.com/ - 详细技术文档

### 模拟器
- JSNES - 本项目使用
- FCEUX - 功能强大的桌面模拟器
- Mesen - 现代高精度模拟器

---

**记住：请合法获取ROM文件，尊重版权！** ⚖️
