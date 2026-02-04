# 🎮 快速开始指南 | Quick Start Guide

## 中文版

### 🚀 5分钟上手

#### 1. 运行游戏
```bash
python3 nurturing_game.py
```

#### 2. 第一次游玩
- 选择你喜欢的宠物类型（猫咪、小狗、兔子、熊猫）
- 给宠物起一个可爱的名字
- 开始照顾你的宠物！

#### 3. 基本操作
```
主菜单:
1. 喂食 - 当饥饿度>60%时使用
2. 玩耍 - 提升开心度和经验
3. 睡觉 - 当体力<40%时使用
4. 治疗 - 当健康<70%时使用
5. 查看状态 - 查看宠物详细信息
6. 保存游戏 - 保存当前进度
7. 游戏说明 - 查看详细说明
0. 退出游戏
```

#### 4. 照顾要点
- ⚠️ **饥饿度高** → 喂食
- ⚠️ **体力低** → 睡觉
- ⚠️ **开心度低** → 玩耍/散步
- ⚠️ **健康度低** → 治疗

#### 5. 成长策略
- 🎯 **快速升级**: 选择"训练"活动，获得更多经验
- 💪 **平衡发展**: 交替进行各种活动
- ⏰ **定期照顾**: 每天登录照顾宠物

### 📸 游戏截图示例

```
==================================================
🐾 宠物状态 - 小白 (猫咪)
==================================================
等级: 5 | 经验: 45/500
年龄: 3天

💚 健康: [██████████████████░░] 95%
💚 开心: [████████████████░░░░] 85%
💛 饥饿: [████████░░░░░░░░░░░░] 42%
💚 体力: [██████████████░░░░░░] 73%
==================================================
```

### 💡 新手提示
1. 刚开始玩，先熟悉各个功能
2. 观察宠物状态栏的颜色提示（💚安全 💛注意 ❤️危险）
3. 离开游戏前记得保存
4. 可以运行 `python3 demo.py` 查看演示

---

## English Version

### 🚀 Get Started in 5 Minutes

#### 1. Run the Game
```bash
python3 nurturing_game.py
```

#### 2. First Time Playing
- Choose your favorite pet type (cat, dog, rabbit, panda)
- Give your pet a cute name
- Start taking care of your pet!

#### 3. Basic Controls
```
Main Menu:
1. Feed - Use when hunger >60%
2. Play - Increase happiness and experience
3. Sleep - Use when energy <40%
4. Heal - Use when health <70%
5. View Status - Check detailed pet information
6. Save Game - Save current progress
7. Game Help - View detailed instructions
0. Exit Game
```

#### 4. Care Tips
- ⚠️ **High Hunger** → Feed
- ⚠️ **Low Energy** → Sleep
- ⚠️ **Low Happiness** → Play/Walk
- ⚠️ **Low Health** → Heal

#### 5. Growth Strategy
- 🎯 **Quick Leveling**: Choose "Train" for more experience
- 💪 **Balanced Growth**: Alternate between different activities
- ⏰ **Regular Care**: Log in daily to care for your pet

### 📸 Game Screenshot Example

```
==================================================
🐾 Pet Status - Fluffy (Cat)
==================================================
Level: 5 | Experience: 45/500
Age: 3 days

💚 Health: [██████████████████░░] 95%
💚 Happiness: [████████████████░░░░] 85%
💛 Hunger: [████████░░░░░░░░░░░░] 42%
💚 Energy: [██████████████░░░░░░] 73%
==================================================
```

### 💡 Beginner Tips
1. Start by familiarizing yourself with all features
2. Watch the color indicators in status bars (💚Safe 💛Caution ❤️Danger)
3. Remember to save before leaving
4. Run `python3 demo.py` to see a demonstration

---

## 🎬 Try the Demo First

Before playing, you can see how the game works:
```bash
python3 demo.py
```

This will show you:
- How to create a pet
- How different activities work
- How time affects your pet
- How the status system works

---

## 🆘 Troubleshooting

### Issue: Game won't start
**Solution**: Make sure Python 3.6+ is installed
```bash
python3 --version
```

### Issue: Save file not loading
**Solution**: The save file might be corrupted. Delete `pet_save.json` and start fresh

### Issue: Can't see Chinese characters
**Solution**: Make sure your terminal supports UTF-8 encoding

---

## 📞 Need Help?

- Read the in-game help (option 7 in main menu)
- Check the full README.md for detailed information
- Run the demo script for a guided tour

**Enjoy the game! 🎉**
