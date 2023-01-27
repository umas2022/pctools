<template>
    <div class="cp-backend">
        <BasicTemplate>
            <!-- 标签 -->
            <template #tp-label>
                <span>后端连通性测试</span>
            </template>

            <!-- 控制 -->
            <template #tp-control>
                <el-button type="primary" plain @click="check_be">测试</el-button>
            </template>

            <!-- 折叠info栏 -->
            <template #tp-info>
                <span class="line">1.测试后端连通性</span>
                <span class="line">2.访问的是后端app_test_ws,返回值为1~999,检测到999判断连通</span>
                <span class="line">3.这个api也被用来检测通信延迟,现在使用10个一组的消息打包之后基本不会有什么延迟</span>
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
