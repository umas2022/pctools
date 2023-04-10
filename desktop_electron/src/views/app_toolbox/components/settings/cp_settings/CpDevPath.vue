<template>
    <div class="cp-settings cp-port">
        <BasicTemplate>
            <!-- 标签 -->
            <template #tp-label>
                <span>开发模式路径</span>
            </template>

            <!-- 控制 -->
            <template #tp-control>
                <el-switch v-model="setDevPath" @click="setFuncPath" />
            </template>

            <!-- 折叠info栏 -->
            <template #tp-info>
                <span class="line">0.这个开关只有在开发环境中会显示</span> <br />
                <span class="line">1.开发时使用的是未打包前的python路径,需要打开这个开关</span> <br />
                <span class="line">2.开发模式路径定位到打包前的python脚本路径(写死在cp里了) </span> <br />
                <span class="line">3.程序启动时获取功能目录index.json使用这个路径</span> <br />
                <span class="line">4.当前:{{ py_path.value }}</span> <br />
            </template>
        </BasicTemplate>
    </div>
</template>
<script setup lang="ts">
import { onMounted, ref, inject, watch } from "vue";
import BasicTemplate from "./BasicTemplate.vue"
import { static_path, is_dev } from "@/utils/utils_path.js"
const path = window.require("path");


const store_config: any = inject("store_config")
const store_home: any = inject("store_home")
const refresh_config = (item: string) => {
    return store_config.value[item] ? store_config.value[item]["value"] : "config load failed"
}
watch(store_config, () => py_path.value = refresh_config("py_path"))
const py_path = ref(refresh_config("py_path"))


watch(store_config, () => py_server.value = refresh_config("py_server"))
const py_server = ref(refresh_config("py_server"))

const setDevPath = ref(is_dev());

// 开发模式路径
const dev_path = "D:\\s-code\\self\\pctools\\py_script"
const dev_server = "D:\\s-code\\self\\pctools\\py_server"
const setFuncPath = () => {
    if (setDevPath.value == true) {
        py_path.value = dev_path
        store_config.value["py_server"]["value"] = dev_server
    } else {
        py_path.value = path.join(static_path(), "py_script")
        store_config.value["py_server"]["value"] = path.join(static_path(), "py_server")
    }
    console.log("path in use : " + py_path.value)
};

onMounted(() => {
    // setFuncPath()
})
</script>
