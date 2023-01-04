<template>
    <div class="cp-backend">
        <BasicTemplate>
            <!-- 标签 -->
            <template #tp-label>
                <span>启动后端</span>
            </template>

            <!-- 控制 -->
            <template #tp-control>
                <el-button type="danger" plain @click="run_be">启动</el-button>
            </template>

            <!-- 折叠info栏 -->
            <template #tp-info>
                <span>使用PythonShell直接启动后端, 默认端口4090</span> <br>
                <span>脚本位置：{{ be_full }}</span> <br>
                <span>由于后台启动无法正常结束后端导致下次使用时端口被占用, 暂时为后端单独开了一个终端</span> <br>
            </template>

        </BasicTemplate>
    </div>

</template>
<script setup lang="ts">
import { onMounted, ref, computed,inject } from "vue";
import { ElMessage } from "element-plus";
import BasicTemplate from "./BasicTemplate.vue"
import { get_wsurl } from "@/utils/api_config.js";
const path = window.require("path");
const { PythonShell } = window.require("python-shell");

const store_home: any = inject("store_home")


// python调用
const be_path = store_home.prj_path
const be_script = "run_backterminal.py"
const be_full = computed(() => path.join(be_path, be_script))
const res_msg = ref([""])
const show_res = ref(false)
const run_be = () => {
    show_res.value = true
    let options = {
        mode: "text",
        pythonOptions: ["-u"], // get print results in real-time
        scriptPath: be_path,
        // args: ["4091"],
        args: ["win"],
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
        console.log("CpRunBackend: done");
    });
}


</script>
