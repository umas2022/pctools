<template>
    <div class="cp-getlist">
        <div class="h3">获取目录</div>
        <span style="padding:10px">当前方法数量:</span>
        <span style="padding:10px">{{ store.index_list.length }}</span>
        <el-button @click="get_list">获取</el-button>
    </div>

</template>
<script setup lang="ts">
import { ref, inject, onMounted } from "vue"
import { get_wsurl } from "@/utils/api_config.js";

const store: any = inject("store")

const get_list = () => {
    // 获取目录
    const send_data = {
        function: "get_list",
        data: { py_path: store.py_path }
    }

    console.log("ws connecting ...");

    let wsdemo = new WebSocket(get_wsurl().local + "sp_searcher");
    wsdemo.onopen = () => {
        wsdemo.send(JSON.stringify(send_data));
    };
    wsdemo.onmessage = (e) => {
        console.log(e.data);
        try {
            store.index_list = JSON.parse(e.data).data
        } catch { }
    };
}

onMounted(() => {
    get_list()
})
</script>
<style lang="scss" scoped>

</style>