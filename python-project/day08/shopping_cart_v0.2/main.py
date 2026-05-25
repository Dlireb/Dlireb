import sys
import os
# 将项目根目录加入Python路径，确保各模块可导入
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ui.ui import UserInterface

def main():
    """程序主入口"""
    # 1. 初始化UI界面，注入依赖服务
    ui = UserInterface()
    try:
        ui.main_program()

    except KeyboardInterrupt:
        print("[系统]程序已被用户安全退出！！！")
    except Exception as e:
        print(f"[错误] {str(e)}")
        print("  系统退出！！！  ")
    finally:
        print(" 欢迎下次光临！！！")
if __name__ == "__main__":
    main()