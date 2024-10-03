'''
create: 2024.10.03
modify: 2024.10.03
备份更新，首先删除path_out中的旧内容，再拷贝path_in目录
'''
import os
import shutil
import filecmp


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


def delete_inconsistent_files(path_in, path_out):
    """删除path_out中与path_in不一致的文件或目录"""
    for root, dirs, files in os.walk(path_out):
        # 计算对应的path_in中的路径
        rel_path = os.path.relpath(root, path_out)
        corresponding_in_path = os.path.join(path_in, rel_path)

        # 如果path_in中没有该目录，删除path_out中的该目录
        if not os.path.exists(corresponding_in_path):
            print(f"Deleting directory: {root}")
            shutil.rmtree(root)
            continue

        # 删除不在path_in中的文件
        for file in files:
            corresponding_file_in = os.path.join(corresponding_in_path, file)
            file_in_out = os.path.join(root, file)
            if not os.path.exists(corresponding_file_in):
                # 如果path_in中没有该文件，则删除
                print(f"Deleting file: {file_in_out}")
                os.remove(file_in_out)
            elif not filecmp.cmp(corresponding_file_in, file_in_out, shallow=False):
                # 如果文件内容不同，也删除
                print(f"Deleting inconsistent file: {file_in_out}")
                os.remove(file_in_out)


def copy_with_structure(input_json):
    input_json = check_inputs(input_json)
    path_in = input_json["path_in"]
    path_out = input_json["path_out"]

    # 检查输入目录是否存在
    if not os.path.exists(path_in):
        print(f"Error: The source path {path_in} does not exist.")
        return

    # 删除path_out中与path_in不一致的内容
    if os.path.exists(path_out):
        delete_inconsistent_files(path_in, path_out)

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
        # 计算目标目录中当前目录的路径
        rel_path = os.path.relpath(root, path_in)
        dest_dir = os.path.join(path_out, rel_path)

        # 如果目标目录不存在，创建它
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        # 拷贝文件
        for file in files:
            file_index += 1
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_dir, file)

            # 如果目标文件已存在，跳过复制并输出 pass
            if os.path.exists(dest_file):
                print(f"{file_index}/{total_files} Pass: {dest_file} already exists.")
            else:
                shutil.copy2(src_file, dest_file)
                print(f"{file_index}/{total_files} Copied: {src_file} to {dest_file}")

    print(
        f"All files copied from {path_in} to {path_out} while maintaining directory structure."
    )



