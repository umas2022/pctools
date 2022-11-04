<template>
    <h3>显示目录</h3>
    <el-button @click="update_list">更新目录</el-button>
    <el-button @click="get_list">获取目录</el-button>
    <div v-for="item in index_list">{{ item }}</div>
</template>
<script setup lang="ts">
import { ref } from "vue"
import { get_wsurl } from "@/utils/api_config.js";

const index_list = ref("")
const update_list = () => {
    // 更新目录
    const send_data = {
        function: "run_list_update",
        data: { py_path: "D:\\s-linux\\project\\pctools\\py_script" }
    }

    console.log("ws connecting ...");

    let wsdemo = new WebSocket(get_wsurl().local + "sp_searcher");
    wsdemo.onopen = () => {
        wsdemo.send(JSON.stringify(send_data));
    };
    wsdemo.onmessage = (e) => {
        console.log(e.data);
    };
}

const get_list = () => {
    // 获取目录
    const send_data = {
        function: "get_list",
        data: { py_path: "D:\\s-linux\\project\\pctools\\py_script" }
    }

    console.log("ws connecting ...");

    let wsdemo = new WebSocket(get_wsurl().local + "sp_searcher");
    wsdemo.onopen = () => {
        wsdemo.send(JSON.stringify(send_data));
    };
    wsdemo.onmessage = (e) => {
        console.log(e.data);
        try {
            index_list.value = JSON.parse(e.data).data
        } catch { }
    };
}
</script>