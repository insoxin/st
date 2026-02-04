#!/bin/bash
# 养成系游戏启动脚本 | Nurturing Game Launcher

echo "╔═══════════════════════════════════════════════╗"
echo "║      欢迎来到养成系游戏！                      ║"
echo "║      Welcome to Nurturing Pet Game!           ║"
echo "╚═══════════════════════════════════════════════╝"
echo ""

# 检查Python版本
if ! command -v python3 &> /dev/null; then
    echo "❌ 错误: 未找到 Python 3"
    echo "❌ Error: Python 3 not found"
    echo "请安装 Python 3.6 或更高版本"
    echo "Please install Python 3.6 or higher"
    exit 1
fi

PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo "✅ Python 版本: $PYTHON_VERSION"
echo ""

# 显示菜单
echo "请选择一个选项 | Please select an option:"
echo "1. 🎮 开始游戏 | Start Game"
echo "2. 🎬 观看演示 | Watch Demo"
echo "3. 🧪 运行测试 | Run Tests"
echo "4. 📖 查看文档 | View Documentation"
echo "0. ❌ 退出 | Exit"
echo ""

read -p "选择 | Choice: " choice

case $choice in
    1)
        echo ""
        echo "🎮 启动游戏..."
        python3 nurturing_game.py
        ;;
    2)
        echo ""
        echo "🎬 运行演示..."
        python3 demo.py
        ;;
    3)
        echo ""
        echo "🧪 运行测试..."
        python3 test_game.py
        ;;
    4)
        echo ""
        echo "📖 打开 README.md..."
        if command -v cat &> /dev/null; then
            cat README.md | head -50
            echo ""
            echo "... (查看完整文档请打开 README.md)"
        else
            echo "请打开 README.md 查看文档"
        fi
        ;;
    0)
        echo ""
        echo "👋 再见！"
        exit 0
        ;;
    *)
        echo ""
        echo "❌ 无效选择"
        echo "直接运行游戏: python3 nurturing_game.py"
        ;;
esac
