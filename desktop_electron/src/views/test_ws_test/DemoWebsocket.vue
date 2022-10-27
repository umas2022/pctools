<template>
  <div>
    <h1>Websocket Demo</h1>
    <h5>Websocket通信demo, 后端无延时发送0~999</h5>

    <div class="mb-4">
      <el-button type="primary" @click="wsConnect">connect</el-button>
    </div>
    <div style="padding: 30px">
      {{ wsRes }}
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref } from "@vue/reactivity";
import { wsurl } from "../../utils/api_config";

// 变量：接收websocket返回值
const wsRes = ref("");

// 按钮：websocket连接
const wsConnect = () => {
  console.log("wsConnect");
  let wsdemo = new WebSocket(wsurl.local + "app_test_ws");
  wsdemo.onopen = () => {
    wsdemo.send("hello");
    console.log("connected !");
  };
  wsdemo.onmessage = (e) => {
    // console.log(e)
    wsRes.value = e.data;
  };
};
</script>
