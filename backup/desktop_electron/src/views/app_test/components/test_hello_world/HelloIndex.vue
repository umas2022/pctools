<template>
  <div>
    <div>
      <h1>Hello World</h1>
    </div>
    <div>
      <h3>绝对路径读取：</h3>
      <span id="show-txt">{{ txtData_1 }}</span>
    </div>
    <div>
      <h3>相对路径读取：</h3>
      <span id="show-txt">{{ txtData_2 }}</span>
      <h3>相对路径：</h3>
      <span id="show-txt">{{ txt_path }}</span>
    </div>
  </div>
</template>
<script setup>
import { onMounted, ref } from "vue";
const path = window.require("path");
const fs = window.require("fs");

const txtData_1 = ref(".txt file load failed");
const txtData_2 = ref(".txt file load failed");
const txt_path = ref(path.join(__static, "static/test/data.txt"));
onMounted(() => {
  fs.readFile(
    "D:\\s-code\\self\\pctools\\desktop_electron\\public\\static\\test\\data.txt",
    (err, data) => {
      txtData_1.value = data;
      console.log("err:", err);
    }
  );

  txtData_2.value = fs.readFileSync(txt_path.value, "utf8");

  // console.log(__dirname)
  
  console.log("path: "+path.join(process.cwd()))
});
</script>
