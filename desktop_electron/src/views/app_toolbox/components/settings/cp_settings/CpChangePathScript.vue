<template>
    <div class="cp-path">
        <BasicTemplate>
            <!-- 标签 -->
            <template #tp-label>
                <span>修改脚本路径</span>
            </template>

            <!-- 控制 -->
            <template #tp-control>
                <div style="display:inline-block;width: calc(80% - 50px);">
                    <el-input v-model="py_path"></el-input>
                </div>
                <el-button type="primary" plain @click="reset_path">修改</el-button>
            </template>

            <!-- 折叠info栏 -->
            <template #tp-info>
                <span class="line">1.手动设置python脚本路径</span><br>
                <span class="line">2.路径定位到py_script文件夹</span><br>
                <span class="line">3.默认通过static_path函数自动定位到打包后的public路径下</span><br>
                <span class="line">4.当前: {{ py_path.value }}</span>
            </template>

        </BasicTemplate>

    </div>
</template>
<script setup lang="ts">
import { ref, inject,watch } from "vue";
import BasicTemplate from "./BasicTemplate.vue"
import { ElMessage } from "element-plus";
import { static_path, is_dev } from "@/utils/utils_path.js"
const fs = window.require("fs");
const path = window.require("path");

const store_config: any = inject("store_config")
const store_home: any = inject("store_home")
const refresh_config = (item: string) => {
    return store_config.value[item] ? store_config.value[item]["value"] : "config load failed"
}
watch(store_config, () => py_path.value = refresh_config("py_path"))
const py_path = ref(refresh_config("py_path"))

const reset_path = () => {
    py_path.value = py_path
    // 修改config.json文件
    const config_path = path.join(static_path(), "config.json")
    try {
        fs.writeFileSync(config_path, JSON.stringify(store_config.value));
    } catch (err) {
        console.error("config write error : " + err);
    }
    ElMessage.success("done")
};
</script>
