<template>
    <div>
        <h3>拷贝合并
            <div class="info-icon"
                style="display: inline-block;  vertical-align: middle;  padding-left: 10px;  padding-right: 20px;  cursor: pointer;">
                <useSvgIcon icon="info" color="black" :width="Number(20)" @click="dialogVisible = !dialogVisible" />
            </div>
        </h3>
        <!-- help页弹窗 -->
        <el-dialog title="拷贝合并" v-model="dialogVisible" width="500px">
            <InfoBox />
        </el-dialog>

        <div class="input-in">
            输入路径：
            <el-input v-model="path_in" clearable></el-input>
        </div>
        <div class="input-out">
            输出路径：
            <el-input v-model="path_out" clearable></el-input>
        </div>
        <el-button @click="start">start</el-button>
        <div v-for="item in res_msg">{{item}}</div>
    </div>
</template>
<script setup>
import { ref } from "vue"
import { useStore } from "vuex"
const store = useStore()
const { PythonShell } = window.require("python-shell");
const path = window.require("path");
import useSvgIcon from "@/components/use_svg/useSvgIcon.vue";
import InfoBox from "./components/InfoBox.vue";

import UTF8 from "utf-8"

// help页弹窗控制
const dialogVisible = ref(false);

// 参数输入
const path_in = ref("D:\\s-linux\\project\\test_file\\test_in")
const path_out = ref("D:\\s-linux\\project\\test_file\\test_out")

// 函数返回值
const res_msg = ref([])

// 开始
const start = () => {
    const py_script = "sp_manager_go.py"
    const py_path = store.state.py_path

    let options = {
        mode: "text",
        encoding:"utf8",
        pythonOptions: ["-u"], // get print results in real-time
        scriptPath: py_path,
        args: ["run_copy_merge", JSON.stringify({ path_in: path_in.value, path_out: path_out.value })],
    };
    let pyshell = new PythonShell(py_script, options);
    pyshell.on("message", function (message) {
        res_msg.value.push(message)
        console.log(message);
        console.log(UTF8.isNotUTF8(message))
    });
    pyshell.end(function (err) {
        if (err) {
            throw err;
        }
        console.log("finished");
    });

}
</script>

<style lang="scss">
.el-input {
    width: 50%;
    padding: 10px;
}
</style>