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
                    <el-input v-model="path_venv"></el-input>
                </div>
                <el-button type="primary" plain @click="reset_path">修改</el-button>
            </template>

            <!-- 折叠info栏 -->
            <template #tp-info>
                <span class="line">1.初始化python环境和后端启动的虚拟环境位置</span> <br>
                <span class="line">2.直接安装在程序目录下的话每次更新软件都要重新安装环境,所以直接独立出来了</span> <br>
                <span class="line">3.当前: {{ path_venv }}</span>
            </template>

        </BasicTemplate>

    </div>
</template>
<script setup lang="ts">
import { ref, inject, watch } from "vue";
import BasicTemplate from "./BasicTemplate.vue"
import { ElMessage } from "element-plus";
import { static_path, is_dev } from "@/utils/utils_path.js"
import { useStore } from "vuex";
const store = useStore();
const fs = window.require("fs");
const path = window.require("path");


const path_venv = ref("")
watch(store.state.config,()=>{
    path_venv.value = store.state.config["path_venv"]["value"]
})


const reset_path = () => {
    // 修改store
    store.commit("set_config", { "key": "path_venv", "value": path_venv.value })

    // 修改config.json文件
    const config_path = path.join(static_path(), "config.json")
    try {
        fs.writeFileSync(config_path, JSON.stringify(store.state.config));
    } catch (err) {
        console.error("config write error : " + err);
    }
    ElMessage.success("done")
};
</script>
