#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
养成系游戏 - Nurturing Pet Game
一款简单的宠物养成游戏
"""

import json
import os
import time
import random
from datetime import datetime, timedelta


class Pet:
    """宠物类 - Pet Class"""
    
    def __init__(self, name="小宠", pet_type="猫咪"):
        self.name = name
        self.pet_type = pet_type
        self.level = 1
        self.exp = 0
        self.health = 100
        self.happiness = 100
        self.hunger = 0
        self.energy = 100
        self.age = 0  # 天数
        self.skills = {}
        self.last_update = datetime.now().isoformat()
        self.created_at = datetime.now().isoformat()
        
    def update_time_based_stats(self):
        """更新基于时间流逝的属性"""
        last_time = datetime.fromisoformat(self.last_update)
        current_time = datetime.now()
        time_passed = (current_time - last_time).total_seconds() / 3600  # 小时
        
        if time_passed > 0:
            # 每小时变化
            self.hunger = min(100, self.hunger + time_passed * 5)
            self.energy = max(0, self.energy - time_passed * 3)
            self.happiness = max(0, self.happiness - time_passed * 2)
            
            # 饥饿和疲劳会影响健康
            if self.hunger > 80:
                self.health = max(0, self.health - time_passed * 2)
            if self.energy < 20:
                self.health = max(0, self.health - time_passed * 1)
                
            # 更新年龄（每24小时增加1天）
            days_passed = int(time_passed / 24)
            self.age += days_passed
            
            self.last_update = current_time.isoformat()
    
    def feed(self, food_type="普通食物"):
        """喂食"""
        food_effects = {
            "普通食物": {"hunger": -20, "happiness": 5, "exp": 5},
            "高级食物": {"hunger": -40, "happiness": 15, "exp": 10},
            "零食": {"hunger": -10, "happiness": 20, "exp": 3}
        }
        
        effect = food_effects.get(food_type, food_effects["普通食物"])
        self.hunger = max(0, self.hunger + effect["hunger"])
        self.happiness = min(100, self.happiness + effect["happiness"])
        self.add_exp(effect["exp"])
        
        return f"你给{self.name}喂了{food_type}！饥饿度-{abs(effect['hunger'])}，开心度+{effect['happiness']}"
    
    def play(self, play_type="玩耍"):
        """玩耍"""
        if self.energy < 20:
            return f"{self.name}太累了，需要休息！"
        
        play_effects = {
            "玩耍": {"happiness": 15, "energy": -15, "exp": 8},
            "训练": {"happiness": 5, "energy": -25, "exp": 15},
            "散步": {"happiness": 10, "energy": -10, "exp": 10}
        }
        
        effect = play_effects.get(play_type, play_effects["玩耍"])
        self.happiness = min(100, self.happiness + effect["happiness"])
        self.energy = max(0, self.energy + effect["energy"])
        self.add_exp(effect["exp"])
        
        return f"你和{self.name}进行了{play_type}！开心度+{effect['happiness']}, 体力{effect['energy']}"
    
    def sleep(self):
        """睡觉"""
        if self.energy > 80:
            return f"{self.name}现在不困，精力充沛！"
        
        energy_gain = 40
        self.energy = min(100, self.energy + energy_gain)
        self.health = min(100, self.health + 10)
        
        return f"{self.name}美美地睡了一觉！体力+{energy_gain}, 健康+10"
    
    def heal(self):
        """治疗"""
        if self.health >= 100:
            return f"{self.name}很健康，不需要治疗！"
        
        health_gain = 50
        self.health = min(100, self.health + health_gain)
        
        return f"给{self.name}进行了治疗！健康+{health_gain}"
    
    def add_exp(self, exp):
        """增加经验值"""
        self.exp += exp
        exp_needed = self.level * 100
        
        if self.exp >= exp_needed:
            self.exp -= exp_needed
            self.level += 1
            return True
        return False
    
    def get_status(self):
        """获取状态显示"""
        status_lines = [
            "=" * 50,
            f"🐾 宠物状态 - {self.name} ({self.pet_type})",
            "=" * 50,
            f"等级: {self.level} | 经验: {self.exp}/{self.level * 100}",
            f"年龄: {self.age}天",
            "",
            self._get_stat_bar("健康", self.health),
            self._get_stat_bar("开心", self.happiness),
            self._get_stat_bar("饥饿", self.hunger, reverse=True),
            self._get_stat_bar("体力", self.energy),
            "=" * 50,
        ]
        
        return "\n".join(status_lines)
    
    def _get_stat_bar(self, name, value, reverse=False):
        """生成状态条"""
        bar_length = 20
        filled = int((value / 100) * bar_length)
        bar = "█" * filled + "░" * (bar_length - filled)
        
        # 根据数值选择颜色指示
        if not reverse:
            if value > 70:
                indicator = "💚"
            elif value > 40:
                indicator = "💛"
            else:
                indicator = "❤️"
        else:
            if value < 30:
                indicator = "💚"
            elif value < 70:
                indicator = "💛"
            else:
                indicator = "❤️"
        
        return f"{indicator} {name}: [{bar}] {value:.0f}%"
    
    def to_dict(self):
        """转换为字典用于保存"""
        return {
            "name": self.name,
            "pet_type": self.pet_type,
            "level": self.level,
            "exp": self.exp,
            "health": self.health,
            "happiness": self.happiness,
            "hunger": self.hunger,
            "energy": self.energy,
            "age": self.age,
            "skills": self.skills,
            "last_update": self.last_update,
            "created_at": self.created_at
        }
    
    @classmethod
    def from_dict(cls, data):
        """从字典创建宠物"""
        pet = cls(data["name"], data["pet_type"])
        pet.level = data["level"]
        pet.exp = data["exp"]
        pet.health = data["health"]
        pet.happiness = data["happiness"]
        pet.hunger = data["hunger"]
        pet.energy = data["energy"]
        pet.age = data["age"]
        pet.skills = data.get("skills", {})
        pet.last_update = data["last_update"]
        pet.created_at = data["created_at"]
        return pet


class Game:
    """游戏主类"""
    
    def __init__(self):
        self.pet = None
        self.save_file = "pet_save.json"
        
    def start(self):
        """开始游戏"""
        self.clear_screen()
        self.show_title()
        
        # 检查是否有存档
        if os.path.exists(self.save_file):
            print("\n发现存档！")
            choice = input("是否继续游戏？(y/n): ").lower()
            if choice == 'y':
                self.load_game()
                if self.pet:
                    print(f"\n欢迎回来！{self.pet.name}很想念你！")
                    self.pet.update_time_based_stats()
                    time.sleep(2)
                    self.main_menu()
                    return
        
        # 创建新宠物
        self.create_pet()
        self.main_menu()
    
    def show_title(self):
        """显示游戏标题"""
        title = """
    ╔═══════════════════════════════════════════════╗
    ║                                               ║
    ║          🐾 养成系游戏 🐾                      ║
    ║         Nurturing Pet Game                    ║
    ║                                               ║
    ║          让我们一起养成可爱的宠物吧！            ║
    ║                                               ║
    ╚═══════════════════════════════════════════════╝
        """
        print(title)
    
    def create_pet(self):
        """创建新宠物"""
        print("\n=== 创建你的宠物 ===\n")
        
        print("选择宠物类型：")
        print("1. 🐱 猫咪")
        print("2. 🐶 小狗")
        print("3. 🐰 兔子")
        print("4. 🐼 熊猫")
        
        pet_types = {
            "1": "猫咪",
            "2": "小狗",
            "3": "兔子",
            "4": "熊猫"
        }
        
        choice = input("\n请选择 (1-4): ")
        pet_type = pet_types.get(choice, "猫咪")
        
        name = input(f"\n给你的{pet_type}起个名字: ")
        if not name:
            name = "小宠"
        
        self.pet = Pet(name, pet_type)
        print(f"\n🎉 恭喜！{name}加入了你的家庭！")
        time.sleep(2)
    
    def main_menu(self):
        """主菜单"""
        while True:
            self.clear_screen()
            
            if self.pet:
                self.pet.update_time_based_stats()
                print(self.pet.get_status())
                print()
            
            print("=== 主菜单 ===")
            print("1. 🍖 喂食")
            print("2. 🎾 玩耍")
            print("3. 😴 睡觉")
            print("4. 💊 治疗")
            print("5. 📊 查看状态")
            print("6. 💾 保存游戏")
            print("7. 📖 游戏说明")
            print("0. 🚪 退出游戏")
            
            choice = input("\n请选择: ")
            
            if choice == "1":
                self.feed_menu()
            elif choice == "2":
                self.play_menu()
            elif choice == "3":
                self.sleep_action()
            elif choice == "4":
                self.heal_action()
            elif choice == "5":
                self.show_status()
            elif choice == "6":
                self.save_game()
            elif choice == "7":
                self.show_help()
            elif choice == "0":
                self.exit_game()
                break
            else:
                print("无效选择，请重试！")
                time.sleep(1)
    
    def feed_menu(self):
        """喂食菜单"""
        self.clear_screen()
        print("=== 喂食 ===\n")
        print("选择食物：")
        print("1. 🍖 普通食物 (饥饿-20, 开心+5)")
        print("2. 🍗 高级食物 (饥饿-40, 开心+15)")
        print("3. 🍪 零食 (饥饿-10, 开心+20)")
        print("0. 返回")
        
        food_map = {
            "1": "普通食物",
            "2": "高级食物",
            "3": "零食"
        }
        
        choice = input("\n请选择: ")
        if choice == "0":
            return
        
        food = food_map.get(choice, "普通食物")
        result = self.pet.feed(food)
        print(f"\n{result}")
        
        if self.pet.add_exp(0):  # 检查是否升级
            print(f"\n🎉 恭喜！{self.pet.name}升级了！现在是{self.pet.level}级！")
        
        input("\n按回车继续...")
    
    def play_menu(self):
        """玩耍菜单"""
        self.clear_screen()
        print("=== 玩耍 ===\n")
        print("选择活动：")
        print("1. 🎾 玩耍 (开心+15, 体力-15)")
        print("2. 💪 训练 (开心+5, 体力-25, 经验多)")
        print("3. 🚶 散步 (开心+10, 体力-10)")
        print("0. 返回")
        
        play_map = {
            "1": "玩耍",
            "2": "训练",
            "3": "散步"
        }
        
        choice = input("\n请选择: ")
        if choice == "0":
            return
        
        play_type = play_map.get(choice, "玩耍")
        result = self.pet.play(play_type)
        print(f"\n{result}")
        
        if self.pet.add_exp(0):  # 检查是否升级
            print(f"\n🎉 恭喜！{self.pet.name}升级了！现在是{self.pet.level}级！")
        
        input("\n按回车继续...")
    
    def sleep_action(self):
        """睡觉动作"""
        self.clear_screen()
        result = self.pet.sleep()
        print(f"\n{result}")
        input("\n按回车继续...")
    
    def heal_action(self):
        """治疗动作"""
        self.clear_screen()
        result = self.pet.heal()
        print(f"\n{result}")
        input("\n按回车继续...")
    
    def show_status(self):
        """显示详细状态"""
        self.clear_screen()
        print(self.pet.get_status())
        print(f"\n创建时间: {self.pet.created_at[:19]}")
        print(f"最后互动: {self.pet.last_update[:19]}")
        input("\n按回车继续...")
    
    def save_game(self):
        """保存游戏"""
        try:
            with open(self.save_file, 'w', encoding='utf-8') as f:
                json.dump(self.pet.to_dict(), f, ensure_ascii=False, indent=2)
            print("\n✅ 游戏保存成功！")
        except Exception as e:
            print(f"\n❌ 保存失败: {e}")
        
        time.sleep(1)
    
    def load_game(self):
        """加载游戏"""
        try:
            with open(self.save_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            self.pet = Pet.from_dict(data)
            return True
        except Exception as e:
            print(f"加载存档失败: {e}")
            return False
    
    def show_help(self):
        """显示帮助"""
        self.clear_screen()
        help_text = """
╔═══════════════════════════════════════════════════════╗
║                     游戏说明                          ║
╚═══════════════════════════════════════════════════════╝

📖 游戏目标：
   照顾你的宠物，让它健康快乐地成长！

🎮 游戏机制：
   • 健康：宠物的健康状况，需要保持在高位
   • 开心：宠物的心情，影响成长速度
   • 饥饿：需要定期喂食，过度饥饿会损害健康
   • 体力：进行活动会消耗体力，需要睡觉恢复

⏰ 时间系统：
   • 游戏中时间会流逝
   • 离开游戏后，再次进入时属性会根据时间变化
   • 每24小时宠物年龄增加1天

💡 游戏提示：
   • 保持宠物各项属性在健康范围
   • 通过玩耍和训练获得经验值升级
   • 定期保存游戏以防进度丢失
   • 平衡各种活动，让宠物全面发展

🎯 成长系统：
   • 通过各种活动获得经验值
   • 累计经验可以升级
   • 等级越高，宠物越强大

祝你玩得开心！ 🎉
        """
        print(help_text)
        input("\n按回车继续...")
    
    def exit_game(self):
        """退出游戏"""
        self.clear_screen()
        print("\n感谢游玩！")
        
        choice = input("是否保存游戏？(y/n): ").lower()
        if choice == 'y':
            self.save_game()
        
        print(f"\n再见！{self.pet.name}期待下次见面！👋")
        time.sleep(2)
    
    def clear_screen(self):
        """清屏"""
        os.system('cls' if os.name == 'nt' else 'clear')


def main():
    """主函数"""
    game = Game()
    game.start()


if __name__ == "__main__":
    main()
