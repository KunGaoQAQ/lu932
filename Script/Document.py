import os


def create_directory(dir=''):
    if os.path.exists(dir):
        return True
    try:
        os.makedirs(dir)
        return False
    except FileExistsError:
        # 当多个线程或进程同时尝试创建目录时可能会出现此异常
        return True
    except PermissionError:
        print(f"没有足够的权限创建目录: {dir}")
        return False
    except OSError as e:
        print(f"创建目录时发生错误: {e}")
        return False


if __name__ == "__main__":
    # 获取用户输入的文件夹路径
    directory = input("请输入要创建的文件夹路径: ")
    result = create_directory(directory)
    if result:
        print(f"目录 {directory} 已存在。")
    else:
        print(f"成功创建目录 {directory}。")
