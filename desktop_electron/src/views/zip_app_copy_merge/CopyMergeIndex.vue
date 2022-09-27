<template>
    <div class="main-index">
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

        <!-- 输入框 -->
        <InputBox />

        <!-- WebSocket连接 -->
        <WsConnect />

        <!-- 显示log -->
        <div class="log-box">
            <ShowLogBox :data="data_set.res" :height=log_height />
        </div>
    </div>
</template>
<script setup>
import { ref, reactive, provide } from "vue"
import useSvgIcon from "@/components/use_svg/useSvgIcon.vue";
import InfoBox from "./components/InfoBox.vue";
import InputBox from "./components/InputBox.vue";
import WsConnect from "./components/WsConnect.vue"
import ShowLogBox from "@/components/show_log/ShowLogBox.vue";



// help页弹窗控制
const dialogVisible = ref(false);

// 参数集
const data_set = reactive({
    function: "run_copy_merge",
    path_in: "D:\\s-linux\\project\\test_file\\test_in",
    path_out: "D:\\s-linux\\project\\test_file\\test_out",
    res: ""
})
provide("data_set", data_set)

// log高度控制
const log_height = reactive({ data: 0, time: 0 })
provide("log_height", log_height)

</script>

<style lang="scss">
div.main-index {
    position: relative;
    height: 100%;
    text-align: center;
}

div.log-box {
    position: absolute;
    width: calc(100% + 1px);
    bottom: 0px;
}
</style>