<template>
    <div>
        <span>启动后端</span>
        <div class="info-icon">
            <useSvgIcon icon="info" color="black" :width="Number(20)" @click="setInfoFlagPort = !setInfoFlagPort" />
        </div>

        <!-- 按钮 -->
        <el-button type="primary" plain @click="run_be">启动</el-button>
        <el-button type="primary" plain @click="check_be">测试</el-button>
        <!-- python返回值 -->
        <div v-if="show_res">
            <el-button type="danger" plain @click="res_msg=[];show_res=false">clear</el-button>
            <div v-for="item in res_msg">{{item}}</div>
        </div>
        <!-- 折叠info栏 -->
        <div class="info" v-if="setInfoFlagPort">
            <span>脚本位置：D:\s-linux\project\pctools\run_backend.py</span> <br>
            <span>默认启动4090端口</span> <br>
            <span>后端应该在windows启动项中随开机启动，启动项位置： </span> <br>
            <span>C:\Users\umas\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\startup.vbs</span> <br />
        </div>
        <!-- 分割线 -->
        <div style="width: 80%; margin: 0 auto">
            <el-divider></el-divider>
        </div>
    </div>

</template>
<script setup>
import { onMounted, ref, computed } from "vue";
import useSvgIcon from "@/components/use_svg/useSvgIcon.vue";
import { ElMessage } from "element-plus";
import { get_wsurl } from "../../../utils/api_config";
import Cookies from "js-cookie";
const { PythonShell } = window.require("python-shell");
const path = window.require("path");

// info栏折叠控制
const setInfoFlagPort = ref(false);

// python调用
const be_path = ref("D:\\s-linux\\project\\onebox")
const be_script = ref("run_backend.py")
const be_full = computed(() => path.join(be_path.value, be_script.value))
const res_msg = ref([])
const show_res = ref(false)
const run_be = () => {
    show_res.value = true
    let options = {
        mode: "text",
        pythonOptions: ["-u"], // get print results in real-time
        scriptPath: be_path.value,
        args: ["win"],
    };
    let pyshell = new PythonShell(be_script.value, options);
    pyshell.on("message", function (message) {
        res_msg.value.push(message)
        console.log(message);
    });
    pyshell.end(function (err) {
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
        if(e.data=="999"){
            ElMessage.success("success")
        }
    };
}
</script>
<style lang="scss">
div.info-icon {
    display: inline-block;
    vertical-align: middle; // 垂直居中
    padding-left: 10px;
    padding-right: 20px;
    cursor: pointer;
}
</style>