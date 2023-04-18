<template>
    <div class="cp-settings cp-port">
        <BasicTemplate>
            <!-- 标签 -->
            <template #tp-label>
                <span>通信端口</span>
            </template>

            <!-- 控制 -->
            <template #tp-control>
                <div style="display:inline-block;width: calc(80% - 50px);">
                    <el-input v-model="pre_port"></el-input>
                </div>
                <el-button type="primary" plain @click="reset_port">修改</el-button>
            </template>

            <!-- 折叠info栏 -->
            <template #tp-info>
                <span class="line">1.后端端口,当前:{{ pre_port }}</span> <br>
                <span class="line">2.调试时后端启动脚本可以接受一个端口号作为输入参数</span> <br>
                <span class="line">3.后端改为前台启动之后,已经不再需要这个功能了,有时间改成手动输入端口号</span>
            </template>

        </BasicTemplate>
    </div>
</template>
<script setup lang="ts">
import { ref, inject, watch, onMounted } from "vue";
import { ElMessage } from "element-plus";
import BasicTemplate from "./BasicTemplate.vue"
import { static_path, is_dev } from "@/utils/utils_path.js"
const fs = window.require("fs");
const path = window.require("path");

const store_config: any = inject("store_config")
const store_home: any = inject("store_home")

const refresh_config = (item: string) => {
    return store_config.value[item] ? store_config.value[item]["value"] : "config load failed"
}
watch(store_config, () => pre_port.value = refresh_config("port"))
const pre_port = ref(refresh_config("port"))


const reset_port = () => {
    store_config.value["port"]["value"] = pre_port.value
    // localStorage给axios用
    localStorage.setItem("port", store_config.value["port"]["value"])
    // 修改config.json文件
    const config_path = path.join(static_path(), "config.json")
    try {
        fs.writeFileSync(config_path, JSON.stringify(store_config.value));
    } catch (err) {
        console.error("config write error : " + err);
    }

    ElMessage.success("done")
};

watch(store_config, () => localStorage.setItem("port", store_config.value["port"]["value"]))

</script>
