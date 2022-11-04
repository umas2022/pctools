<template>
    <div class="cp-backend">
        <BasicTemplate>
            <!-- 标签 -->
            <template #tp-label>
                <span>启动后端</span>
            </template>

            <!-- 控制 -->
            <template #tp-control>
                <el-button type="primary" plain @click="run_be">启动</el-button>
                <el-button type="primary" plain @click="check_be">测试</el-button>
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
import { onMounted, ref, computed } from "vue";
import { ElMessage } from "element-plus";
import BasicTemplate from "./BasicTemplate.vue"
import { get_wsurl } from "@/utils/api_config.js";
const path = window.require("path");
const { PythonShell } = window.require("python-shell");


// python调用
const be_path = ref("D:\\s-linux\\project\\pctools")
// const be_script = ref("run_backend.py")
const be_script = ref("run_backterminal.py")
const be_full = computed(() => path.join(be_path.value, be_script.value))
const res_msg = ref([""])
const show_res = ref(false)
const run_be = () => {
    show_res.value = true
    let options = {
        mode: "text",
        pythonOptions: ["-u"], // get print results in real-time
        scriptPath: be_path.value,
        // args: ["4091"],
        args: ["win"],
    };
    let pyshell = new PythonShell(be_script.value, options);
    pyshell.on("message", function (message:string) {
        res_msg.value.push(message)
        console.log(message);
    });
    pyshell.end(function (err:string) {
        if (err) {
            throw err;
        }
        console.log("finished");
    });
}

const check_be = () => {
    console.log("wsConnect");
    let wsdemo = new WebSocket(get_wsurl().local + "app_test_ws");
    wsdemo.onopen = () => {
        wsdemo.send("hello");
        console.log("connected !");
    };
    wsdemo.onmessage = (e) => {
        // console.log(e.data)
        if (e.data == "999") {
            ElMessage.success("success")
        }
    };
}
</script>
