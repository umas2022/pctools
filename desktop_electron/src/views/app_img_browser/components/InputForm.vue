<template>
  <div>
    <!-- 浏览路径 -->
    <div class="path-browse">
      <el-input v-model="input_form.path_browse" placeholder="path_browse" />
    </div>
    <!-- 保存路径：单个 -->
    <div v-if="input_form.path_save_list.length == 1">
      <div
        class="path-save-single"
        v-for="(item, index) in input_form.path_save_list"
        :key="item"
      >
        <el-input
          v-model="input_form.path_save_list[index].path"
          placeholder="path_save"
        />
        <el-input
          v-model="input_form.path_save_list[index].label"
          placeholder="path_save_name"
        />
        <el-button @click="add_save(index)" type="primary" plain>add</el-button>
      </div>
    </div>
    <!-- 保存路径：列表 -->
    <div v-else>
      <div
        class="path-save-list"
        v-for="(item, index) in input_form.path_save_list"
        :key="item"
      >
        <el-input
          v-model="input_form.path_save_list[index].path"
          placeholder="path_save"
        />
        <el-input
          v-model="input_form.path_save_list[index].label"
          placeholder="path_save_name"
        />
        <el-button @click="add_save(index)" type="primary" plain>
          add</el-button
        >
        <el-button @click="del_save(index)" type="danger" plain>del</el-button>
      </div>
    </div>
    <!-- 加载 -->
    <div>
      <el-button type="primary" plain @click="start_traverse">load</el-button>
    </div>
  </div>
</template>

<script setup>
import { inject } from "vue";
const fs = window.require("fs");

const input_form = inject("input_form");
const path_save_one = inject("path_save_one");
const img_form = inject("img_form");

// 按钮：增删
const add_save = (index) => {
  console.log(index);
  input_form.path_save_list.splice(
    index + 1,
    0,
    JSON.parse(JSON.stringify(path_save_one))
  );
};
const del_save = (index) => {
  input_form.path_save_list.splice(index, 1);
};

// 按钮：启动遍历
const start_traverse = () => {
  if (fs.existsSync(input_form.path_browse)) {
    img_form.img_list = fs.readdirSync(input_form.path_browse);
    img_form.img_list.forEach((each, index) => {
      img_form.img_list[index] = input_form.path_browse + "\\" + each;
    });
    img_form.current_index = 0;
  } else {
    ElMessage({
      message: "file path does not exist",
      grouping: true,
      showClose: true,
      type: "error",
    });
  }
};
</script>

<style lang="scss">
div.path-browse {
  width: 80%;
  margin: 0 auto;
}
div.path-save-single {
  width: 80%;
  margin: 0 auto;
  .el-input {
    width: calc(50% - 28px);
    padding-top: 10px;
  }
}
div.path-save-list {
  width: 80%;
  margin: 0 auto;
  .el-input {
    width: calc(50% - 60px);
    padding-top: 10px;
  }
}
</style>
