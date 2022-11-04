<template>
    <h3>单个功能</h3>
    <el-button @click="get_intf">获取功能</el-button>
    <div v-for="item in intf_data">{{ item }}</div>
</template>
<script setup lang="ts">
import { ref } from "vue"
import { get_wsurl } from "@/utils/api_config.js";

const intf_data = ref("")
const get_intf = () => {
    // 更新目录
    const send_data = {
        function: "get_intf",
        data: { py_path: "D:\\s-linux\\project\\pctools\\py_script", "module": "sp_compress_image" }
    }

    console.log("ws connecting ...");

    let wsdemo = new WebSocket(get_wsurl().local + "sp_searcher");
    wsdemo.onopen = () => {
        wsdemo.send(JSON.stringify(send_data));
    };
    wsdemo.onmessage = (e) => {
        // console.log(e.data);
        try {
            intf_data.value = JSON.parse(e.data).require
        } catch { }
    };
}

</script>