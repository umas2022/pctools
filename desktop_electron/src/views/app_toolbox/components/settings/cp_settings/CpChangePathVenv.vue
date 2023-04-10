<template>
    <div class="cp-path">
        <BasicTemplate>
            <!-- 标签 -->
            <template #tp-label>
                <span>环境安装路径</span>
            </template>

            <!-- 控制 -->
            <template #tp-control>
                <div style="display:inline-block;width: calc(80% - 50px);">
                    <el-input v-model="pre_path"></el-input>
                </div>
                <el-button type="primary" plain @click="reset_path">修改</el-button>
            </template>

            <!-- 折叠info栏 -->
            <template #tp-info>
                <span class="line">1.初始化python环境和后端启动的虚拟环境位置</span> <br>
                <span class="line">2.直接安装在程序目录下的话每次更新软件都要重新安装环境,所以直接独立出来了</span> <br>
                <span class="line">3.当前: {{ pre_path }}</span>
            </template>

        </BasicTemplate>

    </div>
</template>
<script setup lang="ts">
import { ref, inject, watch } from "vue";
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
watch(store_config, () => pre_path.value = refresh_config("path_venv"))
const pre_path = ref(refresh_config("path_venv"))


const reset_path = () => {
    store_config.value["path_venv"]["value"] = pre_path.value
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
