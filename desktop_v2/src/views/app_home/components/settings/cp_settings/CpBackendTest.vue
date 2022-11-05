<template>
    <div class="cp-backend">
        <BasicTemplate>
            <!-- 标签 -->
            <template #tp-label>
                <span>后端测试</span>
            </template>

            <!-- 控制 -->
            <template #tp-control>
                <el-button type="primary" plain @click="check_be">测试</el-button>
            </template>

            <!-- 折叠info栏 -->
            <template #tp-info>
                <span>测试后端连通性</span> <br>
                <span>注释</span> <br>
            </template>

        </BasicTemplate>
    </div>

</template>
<script setup lang="ts">
import { ElMessage } from "element-plus";
import BasicTemplate from "./BasicTemplate.vue"
import { get_wsurl } from "@/utils/api_config.js";


const check_be = () => {
    console.log("wsConnect");
    let wsdemo = new WebSocket(get_wsurl().local + "app_test_ws");
    wsdemo.onopen = () => {
        wsdemo.send("hello");
        console.log("connected !");
    };
    wsdemo.onmessage = (e) => {
        // console.log(e.data)
        if (e.data == "999") {
            ElMessage.success("success")
        }
    };
}
</script>
