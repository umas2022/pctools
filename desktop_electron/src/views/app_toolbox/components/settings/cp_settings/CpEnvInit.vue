<template>
    <div class="cp-backend">
        <BasicTemplate>
            <!-- 标签 -->
            <template #tp-label>
                <span>py环境初始化</span>
            </template>

            <!-- 控制 -->
            <template #tp-control>
                <el-button type="primary" plain @click="env_init">安装</el-button>
            </template>

            <!-- 折叠info栏 -->
            <template #tp-info>
                <span class="line">1.python模块安装,不安装python本体,电脑要先手动装python</span>
                <span class="line">2.在项目py_script同级目录下创建venv虚拟环境,安装过程中会弹出三个终端:安装virtualenv,创建虚拟环境,安装requirements</span>
                <span class="line">3.环境初始化脚本在这里:py_script/utils_env_init/setup_venv.py</span>
                <span class="line">4.默认不使用清华源,有需要可以脚本里改</span>
                <span class="line">5.写脚本时候用的是python3.10.9</span>
            </template>

        </BasicTemplate>
    </div>

</template>
<script setup lang="ts">
import { ref, computed, inject,watch } from "vue";
import BasicTemplate from "./BasicTemplate.vue"
import { useStore } from "vuex";
const store = useStore();
const path = window.require("path");
const { PythonShell } = window.require("python-shell");



// python调用
const be_script = "setup_venv.py"
const res_msg = ref([""])

const env_init = () => {
    let options = {
        mode: "text",
        pythonOptions: ["-u"], // get print results in real-time
        scriptPath: path.join(store.state.config["py_path"]["value"], "utils_env_init"),
        args: [store.state.config["path_venv"]["value"]]
    };
    let pyshell = new PythonShell(be_script, options);
    pyshell.on("message", function (message: string) {
        res_msg.value.push(message)
        console.log(message);
    });
    pyshell.end(function (err: string) {
        if (err) {
            throw err;
        }
        console.log("CpEnvInit: done");
    });
}

</script>
