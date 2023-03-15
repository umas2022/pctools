<template>
    <div>
        <div class="main-box">
            <BasicTemplate>
                <!-- 标签 -->
                <template #tp-label>
                    <span>更新功能列表</span>
                </template>

                <!-- 控制 -->
                <template #tp-control>
                    <el-button @click="update_list" type="primary" plain>更新</el-button>
                </template>

                <!-- 折叠info栏 -->
                <template #tp-info>
                    <span class="line">1.更新python脚本目录列表,注意区分开发模式和生产模式</span><br />
                    <span class="line">2.开发:开发环境下的更新,目标为打包前的py_script文件夹(路径写死了)</span><br />
                    <span class="line">3.生产:生产环境下的更新,目标为electron打包后的public静态目录中的py_script文件夹(自动读取)</span><br />
                    <span class="line">4.目录由每个单独module下的intf.json的头部组成</span><br />
                    <span class="line">5.只有具有intf.json的文件夹会被识别为一个模组</span><br />
                    <span class="line">6.intf.json需要有正确的格式</span><br />
                    <span class="line">7.更新后在主页手动刷新方法列表</span>
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

const store_home: any = inject("store_home")

const update_list = () => {
    // 生产环境更新目录
    const send_data = {
        function: "list_update",
        data: { py_path: store_home.py_path }
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
