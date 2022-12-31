<template>
    <div class="cp-getlist">
        <div class="h3">获取目录</div>
        <span style="padding:10px">当前方法数量:</span>
        <span style="padding:10px">{{ store_home.index_list.length }}</span>
        <el-button @click="get_list">刷新</el-button>
    </div>

</template>
<script setup lang="ts">
import { ref, inject, onMounted } from "vue"
import { get_wsurl } from "@/utils/api_config.js";
import { ElMessage } from "element-plus";

const store_home: any = inject("store_home")

const get_list = () => {
    // 获取目录
    const send_data = {
        function: "get_list",
        data: { py_path: store_home.py_path }
    }

    console.log("ws connecting ...");

    let wsdemo = new WebSocket(get_wsurl().local + "sp_searcher");
    wsdemo.onopen = () => {
        wsdemo.send(JSON.stringify(send_data));
    };
    wsdemo.onmessage = (e) => {
        // console.log(e.data);
        try {
            store_home.index_list = JSON.parse(e.data).data
            console.log(store_home.index_list.length)
            if (store_home.index_list.length != 0) {
                setTimeout(() => {
                    store_home.extract_display = false
                }, 1000)
            }
        } catch {
            if (e.data != "done") {
                ElMessage.error(e.data)
            }
        }
    };


}

onMounted(() => {
    if (store_home.index_list.length == 0) {
        get_list()
    }
})
</script>
<style lang="scss" scoped>

</style>