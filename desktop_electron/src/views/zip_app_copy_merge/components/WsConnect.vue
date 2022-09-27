<template>
    <div class="ws-connect">
      <el-button @click="start">开始</el-button>
    </div>
  </template>
  <script setup>
  import { inject } from "@vue/runtime-core";
  import { get_wsurl } from "@/utils/api_config";
  import { ElMessage } from "element-plus";
  
  // 传参
  const data_set = inject("data_set")
  const log_height = inject("log_height")
  
  // 开始按钮
  const start = () => {
    log_height.data = 300
    log_height.time = Date.now()

    const send_data = JSON.parse(JSON.stringify(data_set));
    delete send_data.res
    console.log("ws connecting ...");
  
    let wsdemo = new WebSocket(get_wsurl().local + "sp_operator");
    wsdemo.onopen = () => {
      wsdemo.send(JSON.stringify(send_data));
    };
    wsdemo.onmessage = (e) => {
      data_set.res = e.data;
    };
  };
  
  </script>
  
  <style scoped>
  div.ws-connect {
    padding: 10px 0 20px 0;
  }
  </style>
  