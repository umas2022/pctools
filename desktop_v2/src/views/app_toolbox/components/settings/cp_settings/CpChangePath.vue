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
                <span>开发模式路径定位到打包前的python脚本路径(写死了) </span> <br/>
                <span>在启动调取功能目录时会用到这个路径</span> <br />
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
