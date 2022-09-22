<template>
  <div>
    <h3>瀑布流多选批处理</h3>
    <el-button type="danger" @click="batch_start">开始处理</el-button>
  </div>
</template>
<script setup>
import { inject, ref, onMounted, computed, reactive } from "vue";
import { ElMessage } from "element-plus";
const fs = window.require("fs");

const img_form = inject("img_form");
const input_form = inject("input_form");

const batch_start = () => {
  for (let key in img_form.marked_list) {
    let img_path = img_form.img_list[key];
    let to_dir = input_form.path_save_list[img_form.marked_list[key]].path;
    save_to(img_path, to_dir);
  }
};

// 单张图片复制
const save_to = (img_path, to_dir) => {
  // 内部功能
  const built_in = {
    // 目标位置是否已存在同名文件
    exist_check: (to_path) => {
      return new Promise((resolve) => {
        fs.access(to_path, (access_err) => {
          if (access_err == null) {
            // access没有报错，文件已存在
            ElMessage({
              message: "file already exist",
              grouping: true,
              showClose: true,
              type: "warning",
            });
            resolve(true);
          } else {
            // access有报错，文件不存在
            resolve(false);
          }
        });
      });
    },
    // 文件复制
    file_copy: (img_path, to_path) => {
      return new Promise((res) => {
        let read_stream = fs.createReadStream(img_path);
        let write_stream = fs.createWriteStream(to_path);
        read_stream.pipe(write_stream);
        res();
      });
    },
    // 检查复制是否成功
    copy_check: (to_path) => {
      fs.access(to_path, (access_err) => {
        if (access_err == null) {
          // access没有报错，文件已存在
          ElMessage({
            message: "done",
            grouping: true,
            showClose: true,
            type: "success",
          });
        } else {
          // access有报错，文件已存在
          ElMessage({
            message: "copy process failed",
            grouping: true,
            showClose: true,
            type: "error",
          });
        }
      });
    },
  };

  // 调用
  let img_name = img_path.split("\\").at(-1);
  let to_path = to_dir + "\\" + img_name;
  built_in.exist_check(to_path).then((res) => {
    if (!res) {
      built_in.file_copy(img_path, to_path).then(() => {
        // 这里then不总能生效，加上延时保证判断结果
        setTimeout(() => {
          built_in.copy_check(to_path);
        }, 100);
      });
    }
  });
};
</script>
