import os
import sys

def check_file(file):
    if not os.path.isfile(file):
        print(f"\"{file}\"", "不是文件")
        return False
    file_name = os.path.splitext(file)
    if file_name[1] not in ('.jpg', '.png', '.gif'):
        print(f"\"{file}\"", "=> 格式不符")
        return False
    return True

def rename(dir, patten):
    if not os.path.exists(dir):
        print('目标不存在！\n')
    if not os.path.isdir(dir):
        print('目标不是一个目录！\n')
        return
    dir = os.path.abspath(dir)  # 获得绝对路径
    print('目标路径：', dir)
    file_list = [x for x in os.listdir(dir) if check_file(os.path.join(dir, x))]  # 获取该路径下的全部文件
    for id, file in enumerate(file_list):
        _, postfix = os.path.splitext(file)
        new_file = f'{patten}-{id+1}{postfix}'
        print(file, "=>", new_file)
        os.rename(os.path.join(dir, file), os.path.join(dir, new_file))
    print('\n重命名完成！')


if __name__ == '__main__':
    print("\n欢迎使用文件批量重命名工具！\n")
    argv = sys.argv[1:]
    print('正在批量重命名...\n')
    rename(argv[0], argv[1])
