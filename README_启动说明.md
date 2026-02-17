# 🎮 NES 游戏站 - 快速启动指南

## 一键启动

### 方法 1: 双击运行（推荐）
双击 **`启动游戏.bat`** 文件即可自动启动

### 方法 2: 右键运行
右键点击 **`启动游戏.ps1`** → 选择"使用 PowerShell 运行"

---

## 如果启动失败

### 确认已安装 Python
打开命令行输入：
```bash
python --version
```

如果显示版本号，说明已安装。否则请访问：
- https://www.python.org/downloads/
- 下载时勾选 "Add Python to PATH"

---

## 手动启动

### 使用 Python
```bash
python -m http.server 8000
```

### 使用 Node.js
```bash
npx http-server -p 8000
```

然后访问：**http://localhost:8000**

---

## 操作说明

| 按键 | 功能 |
|------|------|
| ↑ ↓ ← → | 方向键 |
| Z | A 按钮 |
| X | B 按钮 |
| Enter | Start |
| Shift | Select |

---

## 停止服务器

在命令行窗口按 **Ctrl + C** 即可停止
