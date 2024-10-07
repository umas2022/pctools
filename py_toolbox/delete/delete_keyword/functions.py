'''
create: 2024.10.07
modify: 2024.10.07
删除包含keyword关键字的文件，若if_copy为True，则在path_out目录拷贝一份目录再进行删除，不改动原路径下文件
'''
import os
import shutil


def check_inputs(input_json):
    """赋值默认参数"""
    output_json = input_json
    if not 'if_count' in output_json:
        output_json['if_count'] = True
    if not 'if_copy' in output_json:
        output_json['if_copy'] = True
    return output_json


def count_files(path_in, keyword):
    """计算输入目录下不包含关键字的所有文件数量"""
    print("counting ...")
    file_count = 0
    for _, _, files in os.walk(path_in):
        file_count += len([file for file in files if keyword not in file])
    return file_count


def copy_or_delete_files(input_json):
    input_json = check_inputs(input_json)
    path_in = input_json["path_in"]
    path_out = input_json["path_out"]
    keyword = input_json.get("keyword", "")
    if_copy = input_json["if_copy"]

    # 检查输入目录是否存在
    if not os.path.exists(path_in):
        print(f"Error: The source path {path_in} does not exist.")
        return

    # 如果需要计数，计算需要处理的文件总数
    if input_json['if_count']:
        total_files = count_files(path_in, keyword)
        if total_files == 0:
            print(f"No files to process in {path_in}.")
            return
    else:
        total_files = 0

    file_index = 0  # 当前文件的序号

    if if_copy:
        # 拷贝文件
        for root, dirs, files in os.walk(path_in):
            # 计算目标目录中当前目录的路径
            rel_path = os.path.relpath(root, path_in)
            dest_dir = os.path.join(path_out, rel_path)

            # 如果目标目录不存在，创建它
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)

            for file in files:
                if keyword not in file:
                    file_index += 1
                    src_file = os.path.join(root, file)
                    dest_file = os.path.join(dest_dir, file)

                    # 如果目标文件已存在，跳过复制并输出 pass
                    if os.path.exists(dest_file):
                        print(f"{file_index}/{total_files} Pass: {dest_file} already exists.")
                    else:
                        shutil.copy2(src_file, dest_file)
                        print(f"{file_index}/{total_files} Copied: {src_file} to {dest_file}")

        print(f"All files copied from {path_in} to {path_out} excluding files with '{keyword}' in the name.")
    
    else:
        # 删除包含关键字的文件
        for root, dirs, files in os.walk(path_in):
            for file in files:
                if keyword in file:
                    file_index += 1
                    file_to_delete = os.path.join(root, file)
                    os.remove(file_to_delete)
                    print(f"{file_index}/{total_files} Deleted: {file_to_delete}")

        print(f"All files containing '{keyword}' in {path_in} have been deleted.")

