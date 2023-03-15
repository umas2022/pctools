<template>
    <div class="cp-settings cp-port">
        <BasicTemplate>
            <!-- 标签 -->
            <template #tp-label>
                <span>开发模式端口</span>
            </template>

            <!-- 控制 -->
            <template #tp-control>
                <el-switch v-model="setValuePort" @click="setFuncPort" />
            </template>

            <!-- 折叠info栏 -->
            <template #tp-info>
                <span class="line">1.开发模式：localhost:4091 / 生产模式：localhost:4090</span>
                <span class="line">2.调试时后端启动脚本可以接受一个端口号作为输入参数</span>
                <span class="line">3.后端改为前台启动之后,已经不再需要这个功能了,有时间改成手动输入端口号</span>
            </template>

        </BasicTemplate>
    </div>
</template>
<script setup>
import { onMounted, ref, inject } from "vue";
import BasicTemplate from "./BasicTemplate.vue"

const store_home = inject("store_home")
// 开发模式port
const setInfoFlagPort = ref(false);
const setValuePort = ref(false);
onMounted(() => {
    if (store_home.port == 4091) {
        setValuePort.value = true;
    }
});
const setFuncPort = () => {
    if (setValuePort.value == true) {
        store_home.port = 4091
    } else {
        store_home.port = 4090
    }
    console.log("port in use : " + store_home.port)
};
</script>
