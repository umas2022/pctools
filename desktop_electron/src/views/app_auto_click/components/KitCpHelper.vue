<template>
  <div class="main">
    <h3>compare helper</h3>
    <div class="input">
      保存位置：
      <el-input v-model="input_form.save_path"></el-input><br />
      文件名1 ：
      <el-input style="width: 250px" v-model="input_form.save_name_1"></el-input>
      <el-input style="width: 150px" v-model="input_form.name_suffix_1"></el-input
      ><br />
      文件名2 ：
      <el-input style="width: 250px" v-model="input_form.save_name_2"></el-input>
      <el-input style="width: 150px" v-model="input_form.name_suffix_2"></el-input
      ><br />
    </div>
    <el-button type="primary" plain @click="shot_window">比较</el-button>
    <el-button @click="check_msg=[]" type="warning" plain>clear</el-button>
    <div v-for="item in check_msg">{{ item }}</div>
  </div>
</template>
<script setup>
import { reactive, ref } from "vue";
const { PythonShell } = window.require("python-shell");
const path = window.require("path");
import { ElMessage } from "element-plus";

const py_path =
  process.env.NODE_ENV === "development"
    ? path.join(process.cwd(), "../tools_python/box_autoclick/electron_call")
    : path.join(
        process.cwd(),
        "resources/static/python/box_auto_click/electron_call"
      );

const input_form = reactive({
  save_path: "D:\\s-linux\\project\\test_file\\shot_save",
  save_name_1: "test",
  name_suffix_1: ".jpg",
  save_name_2: "test2",
  name_suffix_2: ".jpg",
});

const check_msg = ref([]);
const shot_window = () => {
  let py_file = path.join(py_path, "compare_ssim.py");
  let pyshell = new PythonShell(py_file);
  pyshell.send(
    path.join(input_form.save_path, input_form.save_name_1) +
      input_form.name_suffix_1
  );
  pyshell.send(
    path.join(input_form.save_path, input_form.save_name_2) +
      input_form.name_suffix_2
  );

  pyshell.on("message", function (message) {
    console.log(message);
    check_msg.value.push(message);
  });

  pyshell.end(function (err) {
    if (err) {
      throw err;
    }
    ElMessage.success("done");
  });
};
</script>
<style lang="scss" scoped>
div.input {
  .el-input {
    width: 400px;
  }
}
</style>