<template>
    <div>
        <div class="main-box">
            <span>更新目录</span>
            <!-- info按钮 -->
            <div class="info-icon">
                <useSvgIcon icon="info" color="black" :width="Number(20)" @click="show_info_flag = !show_info_flag" />
            </div>
            <el-button @click="update_list" type="primary" plain>更新</el-button>
            <!-- 折叠info栏 -->
            <div class="info" v-if="show_info_flag">
                <span>更新python脚本目录列表</span>
            </div>
            <!-- 分割线 -->
            <div style="width: 80%; margin: 0 auto">
                <el-divider></el-divider>
            </div>
        </div>
    </div>
</template>
<script setup>
import { onMounted, ref } from "vue";
import useSvgIcon from "@/components/use_svg/useSvgIcon.vue";
import { get_wsurl } from "@/utils/api_config.js";
import { ElMessage } from "element-plus";

const show_info_flag = ref(false)
const modify_path_flag = ref(false)
const py_path = ref("D:\\s-linux\\project\\pctools\\py_script");
onMounted(() => {
    let getPort = localStorage.getItem("py_path")
});

const update_list = () => {
    // 更新目录
    const send_data = {
        function: "list_update",
        data: { py_path: "D:\\s-linux\\project\\pctools\\py_script" }
    }

    console.log("ws connecting ...");

    let wsdemo = new WebSocket(get_wsurl().local + "sp_searcher");
    wsdemo.onopen = () => {
        wsdemo.send(JSON.stringify(send_data));
    };
    wsdemo.onmessage = (e) => {
        console.log(e.data);
        if (e.data=="done"){
            ElMessage.success("done")
        }
    };
}

</script>
<style lang="scss" scoped>
div.info-icon {
    display: inline-block;
    vertical-align: middle; // 垂直居中
    padding-left: 10px;
    padding-right: 20px;
    cursor: pointer;
}
</style>