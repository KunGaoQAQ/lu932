import os

def create_directory(directory):
    if os.path.exists(directory):
        return True
    try:
        os.makedirs(directory)
        return True
    except FileExistsError:
        return True
    except OSError:
        print(f"无法创建目录 {directory}，请检查权限或路径是否合法。")
        return False

def main():
    user_input = input("请输入要创建的目录路径：")
    result = create_directory(user_input)
    if result:
        print(f"目录 {user_input} 创建成功或已存在。")
    else:
        print(f"目录 {user_input} 创建失败。")

if __name__ == "__main__":
    main()
