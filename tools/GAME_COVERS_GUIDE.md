# 🎮 NES游戏封面图获取指南

## 📥 方案A: 批量下载（推荐）

### 使用 NES.box 数据库
这个网站有所有NES游戏的官方封面图：

**下载步骤：**
1. 访问: https://nes.box/the-nes-library/
2. 每个游戏页面都有高质量封面图
3. 右键保存图片，命名为: `{游戏ID}-{英文名}.png`

### 使用 MobyGames 封面库
1. 访问: https://www.mobygames.com/browse/games/nes/
2. 搜索游戏名称
3. 下载封面图（北美版或日本版）

---

## 🌐 方案B: 使用网络资源

### 1. Wikipedia (维基百科)
每个NES游戏都有对应的Wikipedia页面，包含封面图：
- https://en.wikipedia.org/wiki/Super_Mario_Bros
- https://en.wikipedia.org/wiki/The_Legend_of_Zelda
- https://en.wikipedia.org/wiki/Contra_(video_game)

### 2. Internet Archive
完整NES游戏库（包含扫描的封面）：
https://archive.org/details/Nintendo_Entertainment_System

### 3. NESdev Wiki
开发者社区，包含游戏资源：
https://wiki.nesdev.com/w/index.php?title=Category:Games

### 4. Cover Galore
专业游戏封面网站：
https://www.covergalore.com/Nintendo-NES/1

---

## 🔧 方案C: 使用脚本自动下载

我为您准备了一个Python脚本，可以从公开API下载封面：

```bash
# 安装依赖
pip install requests pillow

# 运行下载脚本
python tools/download_nes_covers.py
```

---

## 📋 命名规范

下载后请按以下格式命名：
```
1-Super_Mario_Bros.png
2-The_Legend_of_Zelda.png
3-Contra.png
4-Tank_Battle.png
...
```

放入 `images/` 目录即可。

---

## ⚠️ 版权说明

这些封面图仅供：
- 个人学习使用
- 非商业项目
- 游戏收藏展示

请勿用于商业用途。

---

## 🎨 推荐的封面来源

| 来源 | 质量 | 难度 | 推荐度 |
|------|------|------|--------|
| NES.box | ⭐⭐⭐⭐⭐ | 简单 | ⭐⭐⭐⭐⭐ |
| MobyGames | ⭐⭐⭐⭐⭐ | 中等 | ⭐⭐⭐⭐⭐ |
| Wikipedia | ⭐⭐⭐⭐ | 简单 | ⭐⭐⭐⭐ |
| Cover Galore | ⭐⭐⭐⭐ | 简单 | ⭐⭐⭐⭐ |
| Internet Archive | ⭐⭐⭐ | 简单 | ⭐⭐⭐ |

---

## 💡 快速开始

**最快的方式：**
1. 访问 https://nes.box/the-nes-library/
2. 找到您的游戏
3. 下载封面图
4. 放入 `images/` 目录
5. 完成！

您的游戏站点会自动显示这些封面图。
