# 合法获取ROM的途径

## ✅ 完全合法的方式

### 1. GitHub - FC_ROMS 仓库（强烈推荐）⭐
**网址**: https://github.com/zdg-kinlon/FC_ROMS

**特点**:
- ✅ **1053个官方ROM** - 完整的NES/FDS游戏集合
- ✅ 完全免费
- ✅ 参考官方档案《红白机终极档案》
- ✅ 包含日文、英文、中文名称的完整索引
- ✅ 按发售日期和编号组织
- ✅ 仅收录官方原版，无第三方修改版

**使用方法**:
1. 访问 https://github.com/zdg-kinlon/FC_ROMS
2. 查看README中的游戏索引表（包含1053个游戏的完整列表）
3. 找到想要的游戏编号（如 0066 = 超级马里奥兄弟）
4. 点击进入 `ROM` 文件夹
5. 在文件夹路径后添加编号（4位数），如 `ROM/0066`
6. 下载ROM文件
7. 保存到 `roms/` 目录
8. 重命名为规范格式：`ID-Game_Title.nes`

**游戏索引示例**:
```
0066 | 1985-09-13 | 超级马里奥兄弟 | Super Mario Bros.
0101 | 1986-02-21 | 塞尔达传说 | The Legend of Zelda
0420 | 1988-02-09 | 魂斗罗 | Contra
0065 | 1985-09-09 | 坦克大战 | Battle City
0024 | 1984-11-02 | 吃豆人 | Pac-Man
```

---

### 2. Internet Archive
**网址**: https://archive.org/details/softwarelibrary_mame

**特点**:
- ✅ 完全免费
- ✅ 大量NES ROM
- ✅ 合法存档
- ✅ 无需注册

**使用方法**:
1. 访问网站
2. 搜索游戏英文名（如 "Super Mario Bros"）
3. 找到NES ROM文件
4. 点击下载
5. 保存到 `roms/` 目录
6. 重命名为规范格式

---

### 2. 从您拥有的正版卡带提取

如果您拥有正版NES卡带，提取ROM是完全合法的：

**所需设备**:
- USB CopyNES (~$50-100)
- Kazzo (~$80)
- INL Retro Programmer (~$100)

**优势**:
- ✅ 100%合法
- ✅ 您拥有使用权
- ✅ 可永久保存

---

### 3. Homebrew 自制游戏（免费且合法）

**推荐网站**:

1. **itch.io NES游戏**
   - https://itch.io/games/tag-nes
   - 独立开发者制作的免费游戏
   - 完全合法，很多是开源的

2. **NESdev Homebrew**
   - http://www.nesdev.com/
   - 社区制作的原创游戏
   - 完全合法

3. **Sleigh's Homebrew**
   - https://sleigh.itch.io/
   - 高质量免费NES游戏

**推荐游戏**:
- `Driar` - 平台游戏
- `Concentration Room` - 射击游戏
- `Gaia's Journey` - RPG游戏
- `Twin Dragons` - 动作游戏

---

### 4. 公共领域游戏

一些老游戏已进入公共领域：

**Color Dreams 系列**:
- `Menace Beach`
- `Sunday Funday`
- `King of Kings`

**Active Enterprises**:
- `Action 52` (部分游戏)

---

## ⚠️ 需要注意的网站

以下网站提供ROM下载，但需要注意版权：

### ROM Hustler
- https://www.romhustler.com/roms/nes/
- 声称用于"备份测试"
- 法律地位模糊

### CoolROM
- https://www.coolrom.com/roms/nes/
- 常见ROM网站
- 使用前请了解当地法律

### EmuParadise
- 已停止直接下载
- 现在需要通过其他方式

---

## 🎯 推荐的合法获取流程

### 对于个人研究：

1. **首选**: 从您拥有的正版卡带提取
2. **次选**: Internet Archive 下载（已存档）
3. **补充**: Homebrew自制游戏
4. **测试**: 使用公共领域ROM

### 批量下载建议：

```python
# 示例：从Internet Archive下载
import requests

def download_from_archive(game_name, save_path):
    # Internet Archive的API
    base_url = "https://archive.org/metadata/"
    metadata_url = f"{base_url}{game_name}"

    response = requests.get(metadata_url)
    data = response.json()

    # 找到.nes文件
    for file in data.get('files', []):
        if file['name'].endswith('.nes'):
            download_url = f"https://archive.org/download/{game_name}/{file['name']}"
            rom_data = requests.get(download_url)
            with open(save_path, 'wb') as f:
                f.write(rom_data.content)
            return True
    return False
```

---

## 📋 推荐的测试ROM（完全合法）

### Homebrew游戏（免费且合法）

1. **Concentration Room**
   - 文件名: `Concentration_Room.nes`
   - 下载: https://www.nesdev.com/

2. **Driar**
   - 文件名: `Driar.nes`
   - 类型: 平台游戏

3. **Nova the Squirrel**
   - 文件名: `Nova_the_Squirrel.nes`
   - 类型: 动作冒险

### Internet Archive（合法存档）

搜索这些游戏名称：
- "Super Mario Bros (World)"
- "Legend of Zelda"
- "Pac-Man (NES)"

---

## 📝 使用建议

### 如果您想研究NES开发：

1. **使用Homebrew游戏** - 完全合法，很多开源
2. **查看NESdev文档** - 学习NES架构
3. **使用仿真器** - 测试自制程序

### 如果您想怀旧游玩：

1. **购买官方重制版** - Nintendo Switch Online
2. **使用模拟器** - FCEUX, Mesen
3. **从卡带提取** - 如果您拥有正版

---

## ⚖️ 法律提示

- **版权保护期**: 通常为出版后70-95年
- **个人使用**: 不自动等于合法
- **备份权利**: 仅适用于您拥有的介质
- **24小时规则**: 不是法律，只是网站约定

---

## 🎮 快速开始

### 推荐的合法ROM获取方式：

**方式1: Internet Archive（最简单）**
```
1. 访问: https://archive.org/details/softwarelibrary_mame
2. 搜索: "Super Mario Bros (NES)"
3. 下载: .nes 文件
4. 重命名: 1-Super_Mario_Bros.nes
5. 移动: roms/ 目录
```

**方式2: Homebrew游戏**
```
1. 访问: https://itch.io/games/tag-nes
2. 下载: 免费的NES游戏
3. 重命名: 按规范格式
4. 移动: roms/ 目录
```

---

**记住**: 合法使用ROM，尊重知识产权！⚖️
