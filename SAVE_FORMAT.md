# 游戏存档格式说明 | Save File Format Documentation

## 存档文件位置 | Save File Location
- 文件名: `pet_save.json`
- 位置: 游戏根目录
- 格式: JSON

## 存档结构示例 | Save Structure Example

```json
{
  "name": "小白",
  "pet_type": "猫咪",
  "level": 5,
  "exp": 45,
  "health": 95.0,
  "happiness": 85.0,
  "hunger": 42.0,
  "energy": 73.0,
  "age": 3,
  "skills": {},
  "last_update": "2026-02-04T07:12:26.123456",
  "created_at": "2026-02-01T10:30:00.000000"
}
```

## 字段说明 | Field Descriptions

| 字段 (Field) | 类型 (Type) | 说明 (Description) |
|-------------|------------|-------------------|
| `name` | String | 宠物名字 (Pet name) |
| `pet_type` | String | 宠物类型：猫咪/小狗/兔子/熊猫 (Pet type) |
| `level` | Integer | 等级 (Level) |
| `exp` | Integer | 经验值 (Experience points) |
| `health` | Float | 健康度 0-100 (Health) |
| `happiness` | Float | 开心度 0-100 (Happiness) |
| `hunger` | Float | 饥饿度 0-100 (Hunger level) |
| `energy` | Float | 体力 0-100 (Energy) |
| `age` | Integer | 年龄（天数）(Age in days) |
| `skills` | Object | 技能数据（保留功能）(Skills - reserved) |
| `last_update` | String | 最后更新时间 ISO 8601 格式 (Last update timestamp) |
| `created_at` | String | 创建时间 ISO 8601 格式 (Creation timestamp) |

## 注意事项 | Notes

### 备份存档 | Backup Your Save
游戏不会自动备份存档，建议定期手动备份 `pet_save.json` 文件。

The game doesn't automatically backup saves. It's recommended to manually backup `pet_save.json` regularly.

### 修改存档 | Editing Saves
虽然可以手动编辑存档文件，但请注意：
- 确保 JSON 格式正确
- 属性值应在合理范围内（0-100）
- 时间戳应使用 ISO 8601 格式

While you can manually edit the save file, please note:
- Ensure proper JSON format
- Keep attribute values within reasonable ranges (0-100)
- Use ISO 8601 format for timestamps

### 恢复默认 | Reset to Default
如果存档损坏，删除 `pet_save.json` 文件即可重新开始。

If the save is corrupted, simply delete `pet_save.json` to start fresh.

### 跨设备 | Cross-Device Play
可以复制 `pet_save.json` 到其他设备继续游戏。

You can copy `pet_save.json` to other devices to continue playing.

## 自动时间更新 | Automatic Time Updates

游戏会自动计算离线时间并更新宠物状态：
- 每小时饥饿度 +5
- 每小时体力 -3  
- 每小时开心度 -2
- 饥饿>80时，每小时健康 -2
- 体力<20时，每小时健康 -1

The game automatically calculates offline time and updates pet status:
- Hunger +5 per hour
- Energy -3 per hour
- Happiness -2 per hour
- Health -2 per hour when hunger >80
- Health -1 per hour when energy <20

## 扩展性 | Extensibility

存档格式预留了 `skills` 字段用于未来功能扩展，可以添加：
- 宠物技能系统
- 成就系统
- 道具背包
- 等等

The save format reserves the `skills` field for future features, such as:
- Pet skill system
- Achievement system
- Item inventory
- And more
