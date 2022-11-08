<template>
    <div class="cp-module">
        <div class="h3">获取功能</div>
        <el-select v-model="store_home.function" placeholder="选择功能">
            <el-option v-for="item in store_home.index_list" :key="item.key" :label="item.title" :value="item.key" @click="get_intf"/>
        </el-select>

        <!-- <el-button @click="get_intf">获取</el-button> -->
    </div>
</template>
<script setup lang="ts">
import { ref, inject } from "vue"
import { get_wsurl } from "@/utils/api_config.js";

const store_home: any = inject("store_home")

const get_intf = () => {
    // 更新目录
    const send_data = {
        function: "get_intf",
        data: { py_path: store_home.py_path, module: store_home.function }
    }

    console.log("ws connecting ...");

    let wsdemo = new WebSocket(get_wsurl().local + "sp_searcher");
    wsdemo.onopen = () => {
        wsdemo.send(JSON.stringify(send_data));
    };
    wsdemo.onmessage = (e) => {
        // console.log(e.data);
        try {
            store_home.intf_data = JSON.parse(e.data)
        } catch { }
    };
}

</script>