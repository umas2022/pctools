<template>
  <div class="outter">
    <!-- 测试按钮 -->
    <!-- <el-button type="danger" @click="test_button">test</el-button> -->
    <!-- 控制按钮 -->
    <h3>单张展示</h3>
    <div class="control">
      <el-button type="primary" plain @click="go_previous">previous</el-button>
      <el-button type="primary" plain @click="go_next">next</el-button>
    </div>
    <div class="save">
      <el-button
        v-for="(item, index) in input_form.path_save_list"
        :key="index"
        type="success"
        plain
        @click="save_to(img_form.img_list[img_form.current_index], item.path)"
        >to {{ item.label }}</el-button
      >
    </div>
    <!-- 图片展示 -->
    <div class="img-cover" v-if="img_form.img_list[0]">
      <img
        :style="{ height: img_height }"
        :src="img_form.img_list[img_form.current_index]"
      />
    </div>
    
    <!-- 弹窗比较 -->
    <div class="compare">
      <el-dialog v-model="dialog_visible" title="compare" width="90%">
        <div class="rename">
          <span>rename : </span>
          <el-input v-model="new_name"></el-input>
          <el-button type="success" plain @click="save_as">save as</el-button>
          <el-button type="danger" plain @click="overwrite"
            >overwrite</el-button
          >
        </div>
        <div class="img-com">
          <h3>new</h3>
          <img
            :style="{ width: com_width }"
            :src="img_form.img_list[img_form.current_index]"
          />
          <h4>file size : 有空再说</h4>
        </div>
        <div class="img-com">
          <h3>exist</h3>
          <img :style="{ width: com_width }" :src="img_exist" />
          <h4>file size/info : 有空再说</h4>
        </div>
      </el-dialog>
    </div>
  </div>
</template>
<script setup>
import { inject, ref, onMounted, computed, reactive } from "vue";
import { ElMessage } from "element-plus";

const fs = window.require("fs");
const input_form = inject("input_form");
const img_form = inject("img_form");

// 图片尺寸控制
const window_height = ref();
const img_height = ref();
const resize = () => {
  window_height.value = window.innerHeight;
  img_height.value = window_height.value * 0.81 - 100 + "px";
};
onMounted(() => {
  resize();
  resize_com();
});
window.onresize = () => {
  resize();
  resize_com();
};



// 图片预加载
const preload = ref(0);

// 按钮：上一张
const go_previous = () => {
  if (img_form.current_index > 0) {
    img_form.current_index -= 1;
  } else {
    ElMessage({
      message: "end",
      grouping: true,
      showClose: true,
      type: "warning",
    });
  }
};
// 按钮：下一张
const go_next = () => {
  if (img_form.current_index < img_form.img_list.length - 1) {
    img_form.current_index += 1;
  } else {
    ElMessage({
      message: "end",
      grouping: true,
      showClose: true,
      type: "warning",
    });
  }
};

// 按钮：保存
const save_to = (img_path, to_dir) => {
  if (img_form.img_list[0]) {
    let img_name = img_path.split("\\").at(-1);
    let to_path = to_dir + "\\" + img_name;
    file_copy_check(img_path, to_path);
  } else {
    ElMessage({
      message: "file has not been loaded",
      grouping: true,
      showClose: true,
      type: "error",
    });
  }
};
// 文件复制封装存在性判断
const file_copy_check = (img_path, to_path) => {
  fs.access(to_path, (file_not_exist) => {
    if (file_not_exist) {
      // 不存在：复制文件
      file_copy(img_path, to_path);
    } else {
      // 已存在：报警进入弹窗比较
      ElMessage({
        message: "file already exist，弹窗比较的代码还没写",
        grouping: true,
        showClose: true,
        type: "warning",
      });

      img_exist.value = to_path;
      dialog_visible.value = false;
      dialog_visible.value = true;
      new_name.value = to_path.split("\\").at(-1).split(".");
      new_name.value.splice(-1, 0, "add");
      new_name.value = new_name.value.join(".");
      compare_form.img_path = img_path;
      compare_form.to_path = to_path;
    }
  });
};
// 文件复制
const file_copy = (img_path, to_path) => {
  // 复制
  const copy_process = () => {
    return new Promise((resolve, reject) => {
      let read_stream = fs.createReadStream(img_path);
      let write_stream = fs.createWriteStream(to_path);
      read_stream.pipe(write_stream);
      resolve();
    });
  };
  // 判断复制结果
  async function check_process() {
    await copy_process();
    fs.access(to_path, (file_not_exist) => {
      if (file_not_exist) {
        ElMessage({
          message: "process failed",
          grouping: true,
          showClose: true,
          type: "error",
        });
      } else {
        ElMessage({
          message: "done",
          grouping: true,
          showClose: true,
          type: "success",
        });
      }
    });
  }
  //调用
  check_process();
};

// 存在重名文件弹窗
const dialog_visible = ref(false);
// 展示重复文件，函数在onMounted和onresize中被调用
const img_exist = ref();
const com_width = ref();
const resize_com = () => {
  let window_width = window.innerWidth;
  com_width.value = (window_width * 0.81 - 100) / 2 + "px";
};

// 重命名另存
const new_name = ref("");
const compare_form = reactive({
  img_path: "",
  to_path: "",
});
const save_as = () => {
  let img_path = compare_form.img_path;
  let to_path = compare_form.to_path;
  to_path = to_path.split("\\");
  to_path[to_path.length - 1] = new_name.value;
  to_path = to_path.join("\\");
  file_copy_check(img_path, to_path);
};

// 覆写
const overwrite = () => {
  ElMessage({
    message: "no such function !",
    grouping: true,
    showClose: true,
    type: "error",
  });
};

// 测试按钮
const test_button = () => {
  console.log("test button");
  dialog_visible.value = !dialog_visible.value;
};
</script>

<style scoped lang = "scss">
div.outter {
  padding: 10px;

  .control {
    padding: 10px;
    display: inline-block;
  }

  .save {
    padding: 10px;
    display: inline-block;
  }

  .img-cover {
    padding: 10px;
  }
}

/* 比较弹窗 */
div.img-com {
  padding: 10px;
  display: inline-block;
  width: calc(50% - 20px);
  border: 5px;
  border-color: red;
}

div.rename {
  width: 60%;
  margin: 0 auto;

  .el-input {
    padding: 10px;
    width: calc(100% - 300px);
  }
}
</style>