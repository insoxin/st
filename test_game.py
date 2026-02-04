#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试养成系游戏的核心功能
Test script for nurturing game core functionality
"""

import sys
import os

# 添加当前目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from nurturing_game import Pet, Game
import json


def test_pet_creation():
    """测试宠物创建"""
    print("测试1: 宠物创建...")
    pet = Pet("测试猫", "猫咪")
    assert pet.name == "测试猫"
    assert pet.pet_type == "猫咪"
    assert pet.level == 1
    assert pet.health == 100
    assert pet.happiness == 100
    assert pet.hunger == 0
    assert pet.energy == 100
    print("✅ 宠物创建测试通过")


def test_feed():
    """测试喂食功能"""
    print("\n测试2: 喂食功能...")
    pet = Pet("测试猫", "猫咪")
    pet.hunger = 50
    
    result = pet.feed("普通食物")
    assert pet.hunger < 50
    assert "喂了普通食物" in result
    print("✅ 喂食功能测试通过")


def test_play():
    """测试玩耍功能"""
    print("\n测试3: 玩耍功能...")
    pet = Pet("测试猫", "猫咪")
    
    initial_happiness = pet.happiness
    initial_energy = pet.energy
    
    result = pet.play("玩耍")
    assert pet.energy < initial_energy
    assert "玩耍" in result
    print("✅ 玩耍功能测试通过")


def test_sleep():
    """测试睡觉功能"""
    print("\n测试4: 睡觉功能...")
    pet = Pet("测试猫", "猫咪")
    pet.energy = 30
    
    result = pet.sleep()
    assert pet.energy > 30
    assert "睡了一觉" in result
    print("✅ 睡觉功能测试通过")


def test_heal():
    """测试治疗功能"""
    print("\n测试5: 治疗功能...")
    pet = Pet("测试猫", "猫咪")
    pet.health = 40
    
    result = pet.heal()
    assert pet.health > 40
    assert "治疗" in result
    print("✅ 治疗功能测试通过")


def test_level_up():
    """测试升级功能"""
    print("\n测试6: 升级功能...")
    pet = Pet("测试猫", "猫咪")
    
    # 添加足够的经验值升级
    pet.exp = 95
    leveled_up = pet.add_exp(10)
    
    assert leveled_up == True
    assert pet.level == 2
    print("✅ 升级功能测试通过")


def test_save_load():
    """测试保存和加载功能"""
    print("\n测试7: 保存和加载功能...")
    
    # 创建宠物
    pet = Pet("保存测试", "小狗")
    pet.level = 5
    pet.exp = 50
    pet.health = 80
    
    # 保存
    data = pet.to_dict()
    
    # 加载
    loaded_pet = Pet.from_dict(data)
    
    assert loaded_pet.name == "保存测试"
    assert loaded_pet.pet_type == "小狗"
    assert loaded_pet.level == 5
    assert loaded_pet.exp == 50
    assert loaded_pet.health == 80
    print("✅ 保存和加载功能测试通过")


def test_status_display():
    """测试状态显示"""
    print("\n测试8: 状态显示...")
    pet = Pet("显示测试", "兔子")
    
    status = pet.get_status()
    assert "显示测试" in status
    assert "兔子" in status
    assert "健康" in status
    assert "开心" in status
    assert "饥饿" in status
    assert "体力" in status
    print("✅ 状态显示测试通过")


def test_energy_constraint():
    """测试体力限制"""
    print("\n测试9: 体力限制...")
    pet = Pet("测试猫", "猫咪")
    pet.energy = 10
    
    result = pet.play("训练")
    assert "太累了" in result
    print("✅ 体力限制测试通过")


def test_time_based_updates():
    """测试基于时间的更新"""
    print("\n测试10: 时间流逝更新...")
    pet = Pet("测试猫", "猫咪")
    
    # 模拟时间流逝
    from datetime import datetime, timedelta
    pet.last_update = (datetime.now() - timedelta(hours=2)).isoformat()
    
    initial_hunger = pet.hunger
    pet.update_time_based_stats()
    
    assert pet.hunger > initial_hunger
    print("✅ 时间流逝更新测试通过")


def run_all_tests():
    """运行所有测试"""
    print("=" * 50)
    print("开始测试养成系游戏核心功能")
    print("=" * 50)
    
    try:
        test_pet_creation()
        test_feed()
        test_play()
        test_sleep()
        test_heal()
        test_level_up()
        test_save_load()
        test_status_display()
        test_energy_constraint()
        test_time_based_updates()
        
        print("\n" + "=" * 50)
        print("🎉 所有测试通过！游戏核心功能正常！")
        print("=" * 50)
        return True
    except AssertionError as e:
        print(f"\n❌ 测试失败: {e}")
        return False
    except Exception as e:
        print(f"\n❌ 发生错误: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
