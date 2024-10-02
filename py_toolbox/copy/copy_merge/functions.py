"""
create: 2024.10.02
modify: 2024.10.02
目录拷贝展平，合并文件夹名称
"""

import os
import shutil


def check_inputs(input_json):
    """赋值默认参数"""
    output_json = input_json
    if not 'if_count' in output_json:
        output_json['if_count'] = True
    return output_json


def count_files(path_in):
    """计算输入目录下的所有文件数量"""
    file_count = 0
    for _, _, files in os.walk(path_in):
        file_count += len(files)
    return file_count


def copy_with_structure_flatten(input_json):
    input_json = check_inputs(input_json)
    path_in = input_json["path_in"]
    path_out = input_json["path_out"]

    # 检查输入目录是否存在
    if not os.path.exists(path_in):
        print(f"Error: The source path {path_in} does not exist.")
        return

        # 计算文件总数
    if input_json['if_count']:
        total_files = count_files(path_in)
        if total_files == 0:
            print(f"No files to copy in {path_in}.")
            return
    else:
        total_files = 0

    file_index = 0  # 当前文件的序号

    # 遍历输入目录并保持结构复制到输出目录
    for root, dirs, files in os.walk(path_in):
        # 计算当前目录的相对路径（相对于path_in）
        rel_path = os.path.relpath(root, path_in)

        # 拷贝文件
        for file in files:
            file_index += 1
            src_file = os.path.join(root, file)

            # 构建新的文件名：将相对路径与文件名组合在一起，中间用 '.' 连接
            # 如果当前文件在子目录中，rel_path 会是子目录的路径
            if rel_path == '.':
                # 如果是根目录中的文件，不需要加目录名
                dest_file_name = file
            else:
                # 将目录名和文件名用 '.' 连接
                dest_file_name = f"{rel_path.replace(os.sep, '.')}.{file}"

            # 最终目标文件路径
            dest_file = os.path.join(path_out, dest_file_name)

            # 如果目标文件已存在，跳过复制并输出 pass
            if os.path.exists(dest_file):
                print(f"{file_index}/{total_files} Pass: {dest_file} already exists.")
            else:
                # 确保输出目录存在
                if not os.path.exists(path_out):
                    os.makedirs(path_out)

                shutil.copy2(src_file, dest_file)
                print(f"{file_index}/{total_files} Copied: {src_file} to {dest_file}")

    print(f"All files copied from {path_in} to {path_out} while flattening the directory structure.")

