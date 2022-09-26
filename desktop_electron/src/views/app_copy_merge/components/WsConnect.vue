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
  
  // 开始按钮
  const start = () => {
    const send_data = JSON.parse(JSON.stringify(data_set));
    delete send_data.res
    console.log("ws connecting ...");
  
    let wsdemo = new WebSocket(get_wsurl().local + "sp_operator");
    wsdemo.onopen = () => {
      wsdemo.send(JSON.stringify(send_data));
    };
    wsdemo.onmessage = (e) => {
      data_set.res = e.data;
      // console.log(e.data)
    };
  };
  
  </script>
  
  <style scoped>
  div.ws-connect {
    padding: 10px 0 20px 0;
  }
  </style>
  