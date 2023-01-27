<template>
    <div class="cp-settings cp-port">
        <BasicTemplate>
            <!-- 标签 -->
            <template #tp-label>
                <span>开发模式路径</span>
            </template>

            <!-- 控制 -->
            <template #tp-control>
                <el-switch v-model="setDevPath" @click="setFuncPort" />
            </template>

            <!-- 折叠info栏 -->
            <template #tp-info>
                <span class="line">1.开发时使用的是未打包前的python路径,需要打开这个开个</span> <br/>
                <span class="line">2.开发模式路径定位到打包前的python脚本路径(写死在cp里了) </span> <br/>
                <span class="line">3.程序启动时获取功能目录index.json使用这个路径</span> <br />
            </template>

        </BasicTemplate>
    </div>
</template>
<script setup>
import { onMounted, ref, inject } from "vue";
import BasicTemplate from "./BasicTemplate.vue"
import { static_path } from "@/utils/utils_path.js"
const path = window.require("path");


const store_home = inject("store_home")
// 开发模式port
const setInfoFlagPort = ref(false);
const setDevPath = ref(false);

const setFuncPort = () => {
    if (setDevPath.value == true) {
        store_home.py_path = "D:\\s-linux\\project\\pctools\\backend_v2\\py_script"
    } else {
        store_home.py_path = path.join(static_path(), "backend_v2/py_script")
    }
    console.log("path in use : " + store_home.py_path)
};
</script>
