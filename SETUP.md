# 🚀 快速启动指南

## 立即开始（5分钟内运行）

### 步骤 1: 下载 JSNES 库

创建 `js/jsnes.min.js` 文件：

**方式A: 手动下载**
1. 访问 https://cdn.jsdelivr.net/npm/jsnes@1.2.0/dist/jsnes.min.js
2. 右键 → 另存为 → 保存到 `js/jsnes.min.js`

**方式B: 使用curl/wget**
```bash
# 在项目根目录执行
curl -o js/jsnes.min.js https://cdn.jsdelivr.net/npm/jsnes@1.2.0/dist/jsnes.min.js

# 或使用wget
wget https://cdn.jsdelivr.net/npm/jsnes@1.2.0/dist/jsnes.min.js -O js/jsnes.min.js
```

### 步骤 2: 准备测试ROM（可选）

**推荐方式：从GitHub获取ROM** ⭐

访问 https://github.com/zdg-kinlon/FC_ROMS
- 包含**1053个官方NES/FDS游戏ROM**
- 完整的游戏索引和编号系统
- 参考《红白机终极档案》整理

**快速获取步骤**：
1. 访问仓库查看游戏索引
2. 找到游戏编号（如：超级马里奥兄弟 = 0066）
3. 访问 `ROM/0066` 文件夹下载
4. 重命名为 `1-Super_Mario_Bros.nes`
5. 放入 `roms/` 目录

**详细指南**：查看 `roms/QUICK_START_ROMS.md`

---

**如果您有合法的NES ROM文件**：

1. 将ROM文件放入 `roms/` 目录
2. 命名格式：`游戏ID-英文名.nes`
   - 例如：`1-Super_Mario_Bros.nes`

**临时测试方案（无需ROM）：**
项目已包含UI和所有功能，ROM集成部分会显示"正在加载模拟器..."提示。

### 步骤 3: 启动本地服务器

**使用Python:**
```bash
python -m http.server 8000
```

**使用Node.js:**
```bash
npx http-server -p 8000
```

**使用PHP:**
```bash
php -S localhost:8000
```

### 步骤 4: 打开浏览器

访问: http://localhost:8000

## ✅ 功能验证

打开网站后，您应该看到：

- [x] 红白机风格的复古界面
- [x] 52个游戏卡片展示
- [x] 分类筛选功能
- [x] 搜索功能
- [x] 点击游戏显示详情弹窗
- [x] 点击"开始游戏"打开模拟器界面
- [x] 收藏功能（点击星标）
- [x] 最近玩过功能
- [x] 响应式设计（缩放浏览器测试）

## 🎮 完整ROM集成（可选）

如果您想完整运行所有游戏，需要：

### 1. 获取JSNES库
```bash
# 确认文件已下载
ls -lh js/jsnes.min.js
```

### 2. 修改index.html
在 `</body>` 前添加：
```html
<script src="js/jsnes.min.js"></script>
<script src="js/emulator.js"></script>
```

### 3. 准备ROM文件
将ROM文件放入 `roms/` 目录，命名格式：
```
roms/1-Super_Mario_Bros.nes
roms/2-Legend_of_Zelda.nes
roms/3-Contra.nes
...
```

### 4. 更新app.js
在 `startGame()` 方法中添加ROM加载：

```javascript
async startGame(game) {
    document.getElementById('gameModal').classList.remove('active');

    const emuModal = document.getElementById('emulatorModal');
    document.getElementById('emuTitle').textContent = `正在运行：${game.title}`;
    emuModal.classList.add('active');

    this.addToRecentlyPlayed(game.id);

    // 初始化模拟器
    const canvas = document.getElementById('nesCanvas');
    if (!window.nesEmulator) {
        window.nesEmulator = new NESEmulator(canvas);
        await window.nesEmulator.init();
    }

    // 加载ROM
    try {
        const romPath = `roms/${game.id}-${game.titleEn.replace(/\s+/g, '_')}.nes`;
        const response = await fetch(romPath);

        if (!response.ok) {
            throw new Error('ROM file not found');
        }

        const romData = await response.arrayBuffer();
        const romArray = new Uint8Array(romData);

        window.nesEmulator.loadROM(romArray);
        this.showNotification(`${game.title} 开始运行！`);

    } catch (error) {
        this.showNotification('ROM文件未找到，请将ROM放入roms/目录');
        console.error('Failed to load ROM:', error);
    }
}
```

## 🎨 自定义样式

### 修改主题色

编辑 `css/style.css`:
```css
:root {
    --nes-red: #E60012;      /* 主红色 */
    --nes-gold: #FFD700;     /* 金色 */
    --nes-black: #1a1a1a;    /* 黑色 */
}
```

### 添加游戏

编辑 `js/games-data.js`:
```javascript
{
    id: 53,
    title: "游戏名",
    titleEn: "Game Name",
    year: 1985,
    publisher: "Nintendo",
    genre: "action",
    rating: 4.5,
    description: "描述",
    icon: "fa-gamepad",
    color: "#FF0000"
}
```

## 📱 部署到GitHub Pages

### 1. 创建仓库
```bash
git init
git add .
git commit -m "Initial commit"
```

### 2. 推送到GitHub
```bash
git remote add origin https://github.com/username/nes-games-site.git
git branch -M main
git push -u origin main
```

### 3. 启用GitHub Pages
- 访问仓库Settings > Pages
- Source: Deploy from a branch
- Branch: main / (root)
- 保存

### 4. 访问网站
https://username.github.io/nes-games-site

## ⚠️ 常见问题

**Q: ROM文件从哪里获取？**
A: 推荐访问 https://github.com/zdg-kinlon/FC_ROMS
   - 包含1053个官方NES/FDS ROM
   - 完整的游戏索引
   - 参考《红白机终极档案》整理
   - 查看 `roms/QUICK_START_ROMS.md` 获取详细指南

**Q: 为什么游戏无法运行？**
A: 需要下载JSNES库到 `js/jsnes.min.js`

**Q: 如何添加更多游戏？**
A: 在 `js/games-data.js` 中添加游戏信息

**Q: 可以修改按键吗？**
A: 可以，编辑 `js/app.js` 中的 `setupKeyboardControls()` 方法

## 📞 需要帮助？

- 查看 README.md 获取完整文档
- 提交Issue报告问题
- 查看JSNES文档: https://github.com/fent/jsnes

---

**祝您游戏愉快！** 🎮✨
