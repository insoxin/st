# 🐾 养成系游戏 | Nurturing Pet Game

[中文](#中文) | [English](#english)

---

## 中文

### 📖 简介

这是一款有趣的宠物养成系游戏！你可以选择自己喜欢的宠物（猫咪、小狗、兔子或熊猫），给它起名字，然后通过喂食、玩耍、训练等方式照顾它成长。

### ✨ 游戏特点

- 🎨 **多种宠物选择**：猫咪、小狗、兔子、熊猫，总有一款适合你
- 📊 **实时状态系统**：健康、开心、饥饿、体力等多维度属性
- ⏰ **真实时间流逝**：即使离开游戏，时间也在流逝，宠物状态会变化
- 🎮 **丰富的互动**：喂食、玩耍、训练、散步、睡觉等多种互动方式
- 📈 **成长系统**：通过互动获得经验值，宠物可以升级
- 💾 **保存/加载功能**：随时保存你的游戏进度

### 🎯 游戏机制

#### 属性说明
- **健康** (Health): 宠物的健康状况，保持在高位很重要
- **开心** (Happiness): 宠物的心情，影响成长速度
- **饥饿** (Hunger): 需要定期喂食，过度饥饿会损害健康
- **体力** (Energy): 活动会消耗体力，睡觉可以恢复

#### 活动选项
- **喂食**：降低饥饿度，提升开心度
  - 普通食物：饥饿-20，开心+5
  - 高级食物：饥饿-40，开心+15
  - 零食：饥饿-10，开心+20
  
- **玩耍**：提升开心度和经验，消耗体力
  - 玩耍：开心+15，体力-15
  - 训练：开心+5，体力-25（经验更多）
  - 散步：开心+10，体力-10
  
- **睡觉**：恢复体力和健康
- **治疗**：恢复健康值

### 🚀 快速开始

#### 环境要求
- Python 3.6+

#### 安装运行

```bash
# 克隆仓库
git clone https://github.com/insoxin/st.git
cd st

# 直接运行游戏
python3 nurturing_game.py

# 或者赋予执行权限后运行
chmod +x nurturing_game.py
./nurturing_game.py
```

### 🎮 游戏玩法

1. **首次游戏**：选择宠物类型，给宠物起名字
2. **照顾宠物**：
   - 当饥饿度高时，记得喂食
   - 当体力低时，让宠物睡觉
   - 当开心度低时，陪它玩耍
   - 当健康度低时，给它治疗
3. **宠物成长**：通过各种互动获得经验值，宠物会升级
4. **保存游戏**：记得定期保存游戏进度

### 💡 游戏提示

- ⚠️ 长时间不照顾宠物，它的状态会下降
- 🎯 平衡各种活动，让宠物全面发展
- 📊 注意观察宠物的各项属性，及时调整策略
- 💾 离开游戏前记得保存

### 📁 文件说明

- `nurturing_game.py` - 主游戏文件
- `pet_save.json` - 游戏存档文件（自动生成）

### 🔧 技术特点

- 纯 Python 实现，无需额外依赖
- 面向对象设计，代码结构清晰
- JSON 格式存档，易于扩展
- 控制台界面，简单易用

---

## English

### 📖 Introduction

This is a fun pet nurturing game! You can choose your favorite pet (cat, dog, rabbit, or panda), give it a name, and take care of it through feeding, playing, training, and more.

### ✨ Features

- 🎨 **Multiple Pet Types**: Cat, dog, rabbit, and panda - there's one for everyone
- 📊 **Real-time Status System**: Multi-dimensional attributes including health, happiness, hunger, and energy
- ⏰ **Real-time Progression**: Time passes even when you're away, affecting your pet's status
- 🎮 **Rich Interactions**: Feed, play, train, walk, sleep, and more
- 📈 **Growth System**: Gain experience through interactions and level up your pet
- 💾 **Save/Load Feature**: Save your progress anytime

### 🎯 Game Mechanics

#### Attributes
- **Health**: Your pet's health status - keep it high!
- **Happiness**: Your pet's mood - affects growth rate
- **Hunger**: Feed regularly - excessive hunger damages health
- **Energy**: Activities consume energy - sleep to recover

#### Activities
- **Feed**: Reduce hunger, increase happiness
  - Regular Food: Hunger -20, Happiness +5
  - Premium Food: Hunger -40, Happiness +15
  - Snack: Hunger -10, Happiness +20
  
- **Play**: Increase happiness and experience, consume energy
  - Play: Happiness +15, Energy -15
  - Train: Happiness +5, Energy -25 (more exp)
  - Walk: Happiness +10, Energy -10
  
- **Sleep**: Restore energy and health
- **Heal**: Restore health

### 🚀 Quick Start

#### Requirements
- Python 3.6+

#### Installation & Running

```bash
# Clone the repository
git clone https://github.com/insoxin/st.git
cd st

# Run the game
python3 nurturing_game.py

# Or make it executable and run
chmod +x nurturing_game.py
./nurturing_game.py
```

### 🎮 How to Play

1. **First Time**: Choose a pet type and give it a name
2. **Take Care of Your Pet**:
   - Feed when hunger is high
   - Let it sleep when energy is low
   - Play when happiness is low
   - Heal when health is low
3. **Pet Growth**: Gain experience through interactions to level up
4. **Save Progress**: Remember to save regularly

### 💡 Tips

- ⚠️ Pet status will decline if left unattended for long
- 🎯 Balance activities for well-rounded development
- 📊 Monitor attributes and adjust strategy accordingly
- 💾 Remember to save before leaving

### 📁 Files

- `nurturing_game.py` - Main game file
- `pet_save.json` - Save file (auto-generated)

### 🔧 Technical Features

- Pure Python implementation, no external dependencies
- Object-oriented design with clean code structure
- JSON-based save system for easy extension
- Console interface for simplicity

---

## 📄 License

MIT License

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 💖 Support

If you like this game, please give it a ⭐️!
