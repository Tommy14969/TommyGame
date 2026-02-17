# 🎮 兼容性问题说明

## 已知问题

### 1. Mapper 不支持

某些游戏使用了 JSNES 模拟器不支持的 Mapper。

**问题游戏：**
- ❌ **魂斗罗 (Contra)** - 使用 Mapper 23
  - 错误信息：`uses a mapper not supported by JSNES`
  - 原因：当前ROM版本使用了JSNES不支持的mapper

**解决方案：**

1. **下载使用兼容Mapper的ROM版本**
   - 寻找使用 Mapper 2 或 Mapper 0 的 Contra 版本
   - 推荐来源：
     - https://www.nesdev.org/
     - https://forums.nesdev.com/

2. **从这些来源下载：**
   - https://github.com/fredden/nestopia
   - https://github.com/punesemu/puNES
   - 这些模拟器项目通常有测试ROM

3. **验证ROM Mapper：**
   ```bash
   # 使用Python检查ROM的Mapper
   python tools/check_rom_mapper.py roms/3-Contra.nes
   ```

---

### 2. 文件名不匹配

**问题：**
- 游戏数据中的英文名与ROM文件名不一致
- 示例：`Tank Battle` vs `Battle_City.nes`

**已修复：**
- ✅ 坦克大战：已更改为 `Battle_City`

---

## JSNES 支持的 Mapper

JSNES 主要支持以下 Mapper：

| Mapper | 支持状态 | 常见游戏 |
|--------|----------|----------|
| 0 (NROM) | ✅ | Donkey Kong, Ice Climber |
| 1 (MMC1) | ✅ | Zelda, Metroid, Final Fantasy |
| 2 (UxROM) | ✅ | Mega Man, Castlevania, Contra (某些版本) |
| 3 (CNROM) | ✅ | Arkanoid, Bomberman |
| 4 (MMC3) | ✅ | Super Mario Bros 3, Kirby |
| 5 (MMC5) | ⚠️ | 部分支持 |
| 7 (AxROM) | ✅ | Battletoads, Marble Madness |
| 66 (GxROM) | ✅ | SMB/Duck Hunt |

**不支持的常见 Mapper：**
- ❌ Mapper 23 (Konami VRC2/VRC4)
- ❌ Mapper 21 (VRC3)
- ❌ Mapper 85 (Konami VRC7)

---

## 如何修复 Mapper 问题

### 方法1: 下载兼容的ROM

1. 访问可靠的ROM来源
2. 搜索游戏名 + "mapper 2" 或 "mapper 0"
3. 下载并替换现有ROM

### 方法2: 使用ROM转换工具

```bash
# 如果您有原始ROM，可以使用工具转换Mapper
# 注意：这仅适用于您拥有的ROM
```

### 方法3: 使用其他模拟器

对于不兼容的游戏，可以考虑：
- **在线模拟器**：https://www.retrogames.cc/
- **其他NES模拟器**：Nestopia, Mesen, puNES

---

## 游戏兼容性列表

### ✅ 完全兼容 (41/44)

大多数游戏都能正常运行，包括：
- Super Mario Bros
- The Legend of Zelda
- Mega Man
- Castlevania
- Metroid
- 等等...

### ⚠️ Mapper问题 (2-3个)

- **Contra (魂斗罗)** - Mapper 23
- 某些特定版本的游戏

### ✅ 已修复

- **Tank Battle (坦克大战)** - 文件名问题已修复

---

## 更新日志

**2024-02-17**
- 修复坦克大战文件名不匹配问题
- 改进Mapper错误提示信息
- 添加ROM兼容性检查工具

---

## 需要帮助？

如果您的ROM无法运行，请：

1. 检查文件名是否匹配
2. 验证ROM的Mapper类型
3. 尝试其他版本的ROM
4. 查看浏览器控制台的错误信息

**注意：请只使用您合法拥有的ROM文件。**
