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
                <span class="line">4.当前: {{ py_path }}</span>
            </template>

        </BasicTemplate>

    </div>
</template>
<script setup lang="ts">
import { ref, inject,watch } from "vue";
import BasicTemplate from "./BasicTemplate.vue"
import { ElMessage } from "element-plus";
import { static_path, is_dev } from "@/utils/utils_path.js"
import { useStore } from "vuex";
const store = useStore();
const fs = window.require("fs");
const path = window.require("path");


const py_path = ref("")

watch(store.state.config,()=>{
    py_path.value = store.state.config["py_path"]["value"]
})

const reset_path = () => {
    // 修改store
    store.commit("set_config", { "key": "py_path", "value": py_path.value })

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
