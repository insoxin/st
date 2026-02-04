#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
游戏演示脚本 - 展示游戏功能
Game Demo Script - Showcase game features
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from nurturing_game import Pet


def demo():
    """演示游戏功能"""
    print("=" * 60)
    print("🐾 养成系游戏演示 - Nurturing Game Demo 🐾")
    print("=" * 60)
    
    # 创建宠物
    print("\n【场景1：创建新宠物】")
    pet = Pet("小白", "猫咪")
    print(f"创建了一只名叫'{pet.name}'的{pet.pet_type}！")
    print(pet.get_status())
    
    # 喂食演示
    print("\n【场景2：喂食宠物】")
    print(pet.feed("普通食物"))
    print(f"当前饥饿度: {pet.hunger:.0f}%, 开心度: {pet.happiness:.0f}%")
    
    # 玩耍演示
    print("\n【场景3：和宠物玩耍】")
    print(pet.play("玩耍"))
    print(f"当前开心度: {pet.happiness:.0f}%, 体力: {pet.energy:.0f}%")
    
    # 训练演示
    print("\n【场景4：训练宠物】")
    print(pet.play("训练"))
    print(f"当前等级: {pet.level}, 经验: {pet.exp}/{pet.level * 100}")
    
    # 多次互动升级
    print("\n【场景5：多次互动让宠物升级】")
    for i in range(5):
        pet.add_exp(20)
    print(f"经过多次互动后...")
    print(f"等级: {pet.level}, 经验: {pet.exp}/{pet.level * 100}")
    
    # 时间流逝
    print("\n【场景6：时间流逝效果】")
    from datetime import datetime, timedelta
    pet.last_update = (datetime.now() - timedelta(hours=3)).isoformat()
    print("模拟3小时后...")
    pet.update_time_based_stats()
    print(f"饥饿度: {pet.hunger:.0f}%, 体力: {pet.energy:.0f}%, 开心度: {pet.happiness:.0f}%")
    
    # 睡觉恢复
    print("\n【场景7：睡觉恢复体力】")
    print(pet.sleep())
    print(f"当前体力: {pet.energy:.0f}%, 健康: {pet.health:.0f}%")
    
    # 最终状态
    print("\n【最终状态】")
    print(pet.get_status())
    
    print("\n" + "=" * 60)
    print("演示完成！现在可以运行 python3 nurturing_game.py 开始游戏")
    print("=" * 60)


if __name__ == "__main__":
    demo()
