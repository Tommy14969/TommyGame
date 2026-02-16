# 快速测试指南

## 现在就可以测试！

由于刚刚集成了 FC_ROMS 仓库，获取ROM变得非常简单：

### 步骤1：下载一个测试ROM

访问：https://github.com/zdg-kinlon/FC_ROMS/tree/main/ROM/0066

下载超级马里奥兄弟的ROM文件。

### 步骤2：重命名文件

将下载的文件重命名为：`1-Super_Mario_Bros.nes`

### 步骤3：放入roms目录

移动文件到：`roms/1-Super_Mario_Bros.nes`

### 步骤4：启动网站

```bash
python -m http.server 8000
```

访问：http://localhost:8000

### 步骤5：开始游戏

1. 点击"超级马里奥兄弟"游戏卡片
2. 点击"开始游戏"按钮
3. 使用键盘控制：
   - 方向键：↑ ↓ ← →
   - A键：Z
   - B键：X
   - Start：Enter
   - Select：Shift

## 功能说明

如果ROM文件存在，您可以：
- ✅ 完整运行游戏
- ✅ 暂停/继续游戏
- ✅ 重置游戏
- ✅ 保存游戏进度（到浏览器本地存储）
- ✅ 读取之前保存的进度
- ✅ 调整音量（静音功能）

## 批量下载ROM

想要玩更多游戏？查看 `roms/QUICK_START_ROMS.md` 获取完整指南。
