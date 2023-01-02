<template>
  <div class="env-check-main">
    <h3>env check</h3>
    <el-button @click="env_check" type="primary" plain>check</el-button>
    <el-button @click="check_msg=[]" type="warning" plain>clear</el-button>
    <div v-for="item in check_msg">{{item}}</div>
  </div>
</template>
<script setup>
const { PythonShell } = window.require("python-shell");
const path = window.require("path");
import { ElMessage } from "element-plus";
import {ref} from "vue"

const py_path =
  process.env.NODE_ENV === "development"
    ? path.join(process.cwd(), "../py_script/box_autoclick/electron_call")
    : path.join(process.cwd(), "resources/static/python/box_auto_click/electron_call");

const check_msg = ref([])
const env_check = () => {
  let py_file = path.join(py_path, "env_check.py")
  let pyshell = new PythonShell(py_file);
  pyshell.send("js_input_1");
  pyshell.send("js_input_2");

  pyshell.on("message", function (message) {
    console.log(message);
    check_msg.value.push(message)
  });

  pyshell.end(function (err) {
    if (err) {
      throw err;
    }
    console.log("EnvCheck: done");
  });
};




</script>
<style lang="scss">
// div.env-check-main {
//   height: 100px;
// }
</style>