<template>
    <div class="cp-module">
        <h3>获取功能</h3>
        <el-select v-model="store.function" placeholder="选择功能">
            <el-option v-for="item in store.index_list" :key="item.key" :label="item.title" :value="item.key" />
        </el-select>

        <el-button @click="get_intf">获取</el-button>
        <!-- <div v-for="item in store.intf_data">{{ item }}</div> -->
    </div>
</template>
<script setup lang="ts">
import { ref, inject } from "vue"
import { get_wsurl } from "@/utils/api_config.js";

const store: any = inject("store")

const get_intf = () => {
    // 更新目录
    const send_data = {
        function: "get_intf",
        data: { py_path: store.py_path, module: store.function }
    }

    console.log("ws connecting ...");

    let wsdemo = new WebSocket(get_wsurl().local + "sp_searcher");
    wsdemo.onopen = () => {
        wsdemo.send(JSON.stringify(send_data));
    };
    wsdemo.onmessage = (e) => {
        // console.log(e.data);
        try {
            store.intf_data = JSON.parse(e.data)
        } catch { }
    };
}

</script>