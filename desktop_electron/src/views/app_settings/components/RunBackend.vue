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
        <div class="res" v-if="show_res">
            <el-scrollbar  always>
                <el-button type="danger" plain size="small" @click="res_msg=[];show_res=false">clear</el-button>
                <div class="msg" v-for="item in res_msg">
                    <div style="display:inline-block">-></div>
                    <div style="display:inline-block;padding-left: 10px;"></div>
                    <div style="display:inline-block">{{item}}</div>
                </div>
            </el-scrollbar>
        </div>
        <!-- 折叠info栏 -->
        <div class="info" v-if="setInfoFlagPort">
            <span>默认端口4090</span> <br>
            <span>脚本位置：{{be_full}}</span> <br>
            <span>由于后台启动无法正常结束后端, 导致下次使用时端口被占用, 暂时为后端单独开了一个终端</span> <br>
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
const { PythonShell } = window.require("python-shell");
const path = window.require("path");

// info栏折叠控制
const setInfoFlagPort = ref(false);

// python调用
const be_path = ref("D:\\s-linux\\project\\pctools")
// const be_script = ref("run_backend.py")
const be_script = ref("run_backterminal.py")
const be_full = computed(() => path.join(be_path.value, be_script.value))
const res_msg = ref([])
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
        if (e.data == "999") {
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

div.res {
    width: 80%;
    margin: auto;
    border: solid 3px gray;
    border-radius: 10px;
    position: relative;
    white-space: nowrap;

    .el-button {
        position: absolute;
        right: 0px;
    }

    .msg {
        display: flex;
        left: 0px;
    }
}
</style>