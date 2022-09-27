<template>
  <div class="ws-connect">
    <el-button type="primary" plain @click="start">开始</el-button>
    <el-button type="info" plain @click="clear">清空</el-button>
  </div>
</template>
<script setup>
import { reactive } from "@vue/reactivity";
import { inject } from "@vue/runtime-core";
import { get_wsurl } from "@/utils/api_config";
import { ElMessage } from "element-plus";

// 传参
const logprop = inject("logprop");
const form = inject("form");
const form_head = inject("form_head");

// 开始按钮
const start = () => {
  const form_simplify = JSON.parse(JSON.stringify(form.value));

  const send_data = {
    head: form_head,
    body: form_simplify,
  };

  console.log(send_data);
  // console.log(form_simplify[0]);

  console.log("ws connecting ...");

  let wsdemo = new WebSocket(get_wsurl().local + "tp_tools");
  wsdemo.onopen = () => {
    wsdemo.send(JSON.stringify(send_data));
  };
  wsdemo.onmessage = (e) => {
    logprop.value = e.data;
  };
};

//清空按钮
const clear = () => {
  ElMessage.error("没做这个功能")
};
</script>

<style scoped>
div.ws-connect {
  padding: 10px 0 20px 0;
}
</style>
