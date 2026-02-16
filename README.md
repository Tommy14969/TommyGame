# 红白机游戏导航站 | NES Game Hub

一个功能丰富的红白机（NES/Famicom）游戏网站，包含50+经典游戏，可在浏览器中直接畅玩。

![NES](https://img.shields.io/badge/NES-经典游戏-red)
![HTML5](https://img.shields.io/badge/HTML5-前端-orange)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-yellow)

## ✨ 功能特点

- 🎮 **50+ 经典游戏** - 包含超级马里奥、塞尔达传说、魂斗罗等经典游戏
- 🎨 **复古红白机风格** - 精心设计的80年代复古UI
- 📱 **响应式设计** - 完美支持桌面和移动设备
- 🔍 **搜索和筛选** - 按类型、名称搜索游戏
- ⭐ **收藏功能** - 收藏喜爱的游戏
- 📊 **游戏统计** - 追踪游戏历史
- 🎯 **即时存档** - 随时保存和加载游戏进度
- 🔊 **音效控制** - 静音/取消静音
- ⌨️ **键盘控制** - 完整的NES手柄映射

## 🕹️ 操作说明

### 键盘控制

| 按键 | 功能 |
|------|------|
| ↑ ↓ ← → | 方向键 |
| Z | A 按钮 |
| X | B 按钮 |
| Enter | Start |
| Shift | Select |

### 游戏功能

- **暂停/继续** - 暂停游戏
- **重置** - 重启游戏
- **存档** - 保存当前进度
- **读档** - 加载已存档进度
- **静音** - 开启/关闭音效

## 📦 安装和运行

### 1. 克隆项目

```bash
git clone <your-repo-url>
cd nes-games-site
```

### 2. 下载 JSNES 库

JSNES 是一个纯JavaScript的NES模拟器。请从以下地址获取：

```bash
# 方式1: 从CDN下载
wget https://cdn.jsdelivr.net/npm/jsnes@1.2.0/dist/jsnes.min.js -O js/jsnes.min.js

# 方式2: 使用npm
npm install jsnes
# 然后复制 node_modules/jsnes/dist/jsnes.min.js 到 js/ 目录
```

或者访问：https://github.com/fent/jsnes/releases

### 3. 准备游戏ROM

**⚠️ 重要提示：**

游戏ROM文件受版权保护。您需要：

1. **合法获取ROM** - 从您拥有的正版卡带中提取
2. **使用公共领域ROM** - 一些游戏已进入公共领域
3. **仅用于个人学习** - 请勿用于商业用途

**ROM文件位置：**
将`.nes`格式的ROM文件放入 `roms/` 目录。

**推荐的ROM列表（50个游戏）：**

```
roms/
├── 1-Super_Mario_Bros.nes
├── 2-Legend_of_Zelda.nes
├── 3-Contra.nes
├── 4-Battle_City.nes
├── 5-Pac-Man.nes
├── ... (共50个)
```

**获取ROM的合法途径：**

- 🎮 **GitHub - FC_ROMS（推荐）** - https://github.com/zdg-kinlon/FC_ROMS
  - 包含1053个官方NES/FDS ROM
  - 完整的游戏索引和编号系统
  - 参考《红白机终极档案》整理

- 📱 **从您拥有的卡带提取** - 使用USB CopyNES或类似设备

- 🌐 **公共领域ROM** - https://archive.org/details/softwarelibrary_mame

- 🎮 **官方授权** - Nintendo Switch Online等官方服务

**详细说明请查看**: `tools/LEGAL_ROM_SOURCES.md` 和 `roms/ROM_GUIDE.md`

### 4. 配置ROM路径

编辑 `js/app.js`，在 `startGame()` 方法中添加ROM加载逻辑：

```javascript
async loadGameROM(game) {
    const romPath = `roms/${game.id}-${game.titleEn.replace(/\s+/g, '_')}.nes`;

    try {
        const response = await fetch(romPath);
        if (!response.ok) {
            throw new Error('ROM not found');
        }
        const romData = await response.arrayBuffer();
        return new Uint8Array(romData);
    } catch (error) {
        console.error('Failed to load ROM:', error);
        throw error;
    }
}
```

### 5. 运行项目

**本地运行：**

```bash
# 使用Python内置服务器
python -m http.server 8000

# 或使用Node.js的http-server
npx http-server -p 8000
```

然后访问：http://localhost:8000

**部署到GitHub Pages：**

```bash
# 1. 创建GitHub仓库并推送
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main

# 2. 在GitHub设置中启用GitHub Pages
# Settings > Pages > Source: main branch
```

## 🎯 游戏列表

当前包含52个经典游戏：

| # | 游戏名称 | 类型 | 年份 |
|---|----------|------|------|
| 1 | 超级马里奥兄弟 | 动作 | 1985 |
| 2 | 塞尔达传说 | 冒险 | 1986 |
| 3 | 魂斗罗 | 射击 | 1987 |
| 4 | 坦克大战 | 动作 | 1985 |
| 5 | 俄罗斯方块 | 益智 | 1989 |
| ... | ... | ... | ... |

完整列表请查看 `js/games-data.js`

## 🛠️ 技术栈

- **前端**: HTML5, CSS3, JavaScript (ES6+)
- **模拟器**: JSNES
- **样式**: 自定义CSS + Font Awesome图标
- **存储**: LocalStorage (收藏、最近玩过、存档)
- **部署**: GitHub Pages

## 📁 项目结构

```
nes-games-site/
├── index.html          # 主页面
├── css/
│   └── style.css      # 样式文件
├── js/
│   ├── jsnes.min.js   # JSNES模拟器库（需下载）
│   ├── games-data.js  # 游戏数据
│   ├── emulator.js    # 模拟器封装
│   └── app.js         # 主应用逻辑
├── roms/              # 游戏ROM文件（需自行添加）
├── images/            # 游戏封面图片
└── README.md          # 说明文档
```

## 🔧 配置选项

### 修改游戏数据

编辑 `js/games-data.js` 添加或修改游戏信息：

```javascript
{
    id: 53,
    title: "游戏名称",
    titleEn: "Game Title",
    year: 1985,
    publisher: "Nintendo",
    genre: "action",
    rating: 4.5,
    description: "游戏描述",
    icon: "fa-gamepad",
    color: "#FF0000"
}
```

### 自定义样式

修改 `css/style.css` 中的CSS变量：

```css
:root {
    --nes-red: #E60012;
    --nes-gold: #FFD700;
    --nes-black: #1a1a1a;
}
```

## 🌐 部署

### GitHub Pages

1. 推送代码到GitHub
2. Settings > Pages > Source: main branch
3. 访问 `https://username.github.io/nes-games-site`

### Vercel

```bash
npm install -g vercel
vercel
```

### Netlify

拖放项目文件夹到 https://app.netlify.com/drop

## ⚠️ 版权声明

- 所有游戏版权归原版权方所有
- 本项目仅供学习和个人使用
- 请勿用于商业用途
- 使用本项目即表示您同意自行承担所有法律责任

## 🤝 贡献

欢迎提交Issue和Pull Request！

## 📄 许可证

MIT License

## 🙏 致谢

- [JSNES](https://github.com/fent/jsnes) - JavaScript NES模拟器
- [Font Awesome](https://fontawesome.com/) - 图标库
- 任天堂 - 创造了这些经典游戏

## 📞 联系方式

如有问题，请提交Issue或发送邮件。

---

**享受游戏，致敬经典！** 🎮✨
