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
                <span class="line">1.python模块安装,不安装python,电脑要先手动装python</span>
                <span class="line">2.PythonShell模块不一定好用,也懒得测试了</span>
                <span class="line">3.环境初始化脚本在这里:backend_v2/py_script/utils_env_init/setup_terminal.py</span>
                <span class="line">4.默认使用pip命令,不使用清华源,有需要要手动去脚本里改</span>
                <span class="line">5.写脚本时候用的是python3.10.9</span>
            </template>

        </BasicTemplate>
    </div>

</template>
<script setup lang="ts">
import { ref, computed, inject } from "vue";
import BasicTemplate from "./BasicTemplate.vue"
const path = window.require("path");
const { PythonShell } = window.require("python-shell");

const store_home: any = inject("store_home")

// python调用
const be_path = computed(() => path.join(store_home.py_path, "utils_env_init"))
const be_script = "setup_terminal.py"
const be_full = computed(() => path.join(be_path.value, be_script))
const res_msg = ref([""])
const env_init = () => {
    let options = {
        mode: "text",
        pythonOptions: ["-u"], // get print results in real-time
        scriptPath: be_path.value,
        args: ["win"], // 没什么用的输入参数
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
