import sys
import os
import shutil


def save_file(file_save_path, src_file_path):
    """
    :param file_save_path: 拷贝文件目录（通过命令行参数设置）
    :param src_file_path: 原始文件路径（从版本控制工具得到）
    :return: 拷贝文件路径
    """
    file_name = os.path.basename(src_file_path)

    dest_file_path = os.path.join(file_save_path, file_name)

    shutil.copy(src_file_path, dest_file_path)

    return dest_file_path


if __name__ == '__main__':
    if len(sys.argv) < 5:
        exit("")

    # 编辑器路径
    editor_path = sys.argv[1]

    # 拷贝文件路径
    save_path = sys.argv[2]

    # 远端文件路径（版本控制工具传入）
    remote_path = save_file(save_path, sys.argv[3])

    # 本地文件路径（版本控制工具传入）
    local_path = save_file(save_path, sys.argv[4])

    # 调用UE4Editor -diff
    diff_command = editor_path + " -diff " + remote_path + " " + local_path

    os.system(diff_command)
