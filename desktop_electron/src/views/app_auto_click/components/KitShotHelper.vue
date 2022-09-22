<template>
  <div class="main">
    <h3>shot helper</h3>
    <span>中文输入匹配不到目标，推测是中文编码错误</span> <br>
    <span>使用英文匹配时会截出黑条，暂时在python中指定窗口名</span> <br>
    <div class="input">
      目标窗口：
      <el-input v-model="input_form.window" disabled ></el-input> <br />
      保存位置：
      <el-input v-model="input_form.save_path"></el-input><br />
      文件名称：
      <el-input style="width: 250px" v-model="input_form.save_name"></el-input>
      <el-input style="width: 150px" v-model="input_form.name_suffix"></el-input
      ><br />
    </div>
    <el-button type="primary" plain @click="shot_window">截图</el-button>
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
  // window: "碧蓝航线", // 中文乱码问题暂未解决
  window: "碧蓝航线",
  save_path: "D:\\s-linux\\project\\test_file\\shot_save",
  save_name: "test",
  name_suffix: ".jpg",
});

const check_msg = ref([]);
const shot_window = () => {
  let py_file = path.join(py_path, "shot_window.py");
  let pyshell = new PythonShell(py_file);
  pyshell.send(input_form.window);
  pyshell.send(
    path.join(input_form.save_path, input_form.save_name) +
      input_form.name_suffix
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