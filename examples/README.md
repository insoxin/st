# 示例存档说明 | Example Save Files

本目录包含一些示例存档文件，可以用于测试和参考。

This directory contains example save files for testing and reference.

## 使用方法 | How to Use

将任意示例文件复制为 `pet_save.json` 到游戏根目录即可使用：

Copy any example file as `pet_save.json` to the game root directory:

```bash
# 使用健康宠物存档 | Use healthy pet save
cp examples/example_save_healthy.json pet_save.json

# 使用新手存档 | Use beginner save
cp examples/example_save_beginner.json pet_save.json
```

## 存档列表 | Save File List

### 1. example_save_healthy.json - 健康成长的宠物
**描述**: 一只已经养育15天、10级的健康猫咪
- 等级: 10
- 年龄: 15天
- 各项属性优秀

**Description**: A healthy cat at level 10, raised for 15 days
- Level: 10
- Age: 15 days
- Excellent attributes

### 2. example_save_beginner.json - 新生宠物
**描述**: 刚创建的1级小狗，适合新手体验
- 等级: 1
- 年龄: 0天
- 所有属性满值

**Description**: Newly created level 1 puppy, good for beginners
- Level: 1
- Age: 0 days
- All attributes at maximum

## 注意 | Notes

⚠️ 复制存档会覆盖当前游戏进度，请先备份原有的 `pet_save.json`！

⚠️ Copying saves will overwrite current progress. Backup your original `pet_save.json` first!
