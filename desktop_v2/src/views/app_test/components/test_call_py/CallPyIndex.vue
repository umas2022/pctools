<template>
  <div class="test-main" style="height:1000px">
    <h1>call local python script</h1>
    <el-button type="success" plain @click="run_py_1">run 1</el-button>
    <el-button type="success" plain @click="run_py_2">run 2</el-button>
    <h3>使用PythonShell调用本地python脚本</h3>
    <h3>run1多次传递单个参数,多次接收返回值</h3>
    <h3>run2单次传递多个参数,接收单个返回值</h3>
  </div>
</template>
<script setup>
const { PythonShell } = window.require("python-shell");
const path = window.require("path");
import { ElMessage } from "element-plus";

// let py_path = path.join(__static, "static/python/hello_world_1.py");
const py_path =
  process.env.NODE_ENV === "development"
    ? path.join(process.cwd(), "public/static/python/test")
    : path.join(process.cwd(), "resources/static/python/test");

// 法1：多次传递单个参数
const run_py_1 = () => {
  let py_script = path.join(py_path, "hello_world_1.py");
  let pyshell = new PythonShell(py_script);

  pyshell.send("js_input_1");
  pyshell.send("js_input_2");

  pyshell.on("message", function (message) {
    ElMessage.success(message);
    console.log(message);
  });

  pyshell.end(function (err) {
    if (err) {
      throw err;
    }
    console.log("finished");
  });
};
// 法2：单次传递多个参数
const run_py_2 = () => {
  let options = {
    mode: "text",
    pythonOptions: ["-u"], // get print results in real-time
    scriptPath: py_path,
    args: ["value1", "value2", "value3"],
  };

  PythonShell.run("hello_world_2.py", options, function (err, results) {
    if (err) throw err;
    else {
      console.log(results);
      ElMessage.success(JSON.stringify(results));
    }
  });
};
</script>
