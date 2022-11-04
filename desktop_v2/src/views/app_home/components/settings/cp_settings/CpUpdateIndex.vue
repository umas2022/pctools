<template>
    <div>
        <div class="main-box">
            <BasicTemplate>
            <!-- 标签 -->
            <template #tp-label>
                <span>更新目录</span>
            </template>

            <!-- 控制 -->
            <template #tp-control>
                <el-button @click="update_list" type="primary" plain>更新</el-button>
            </template>

            <!-- 折叠info栏 -->
            <template #tp-info>
                <span>更新python脚本目录列表</span><br />
                <span>目录由每个单独module下的intf.json的头部组成</span> 
            </template>

        </BasicTemplate>

    </div>
    </div>
</template>
<script setup lang="ts">
import BasicTemplate from "./BasicTemplate.vue"
import { get_wsurl } from "@/utils/api_config.js";
import { ElMessage } from "element-plus";
import { inject } from "vue";

const store:any = inject("store")

const update_list = () => {
    // 更新目录
    const send_data = {
        function: "list_update",
        data: { py_path: store.py_path }
    }

    console.log("ws connecting ...");

    let wsdemo = new WebSocket(get_wsurl().local + "sp_searcher");
    wsdemo.onopen = () => {
        wsdemo.send(JSON.stringify(send_data));
    };
    wsdemo.onmessage = (e) => {
        console.log(e.data);
        if (e.data == "done") {
            ElMessage.success("done")
        }
    };
}

</script>
