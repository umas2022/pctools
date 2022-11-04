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
                <span>开发模式：localhost:4091 / </span>
                <span>生产模式：localhost:4090</span> <br />
            </template>

        </BasicTemplate>
    </div>
</template>
<script setup>
import { onMounted, ref, inject } from "vue";
import BasicTemplate from "./BasicTemplate.vue"

const store = inject("store")
// 开发模式port
const setInfoFlagPort = ref(false);
const setValuePort = ref(false);
onMounted(() => {
    if (store.port == 4091) {
        setValuePort.value = true;
    }
});
const setFuncPort = () => {
    if (setValuePort.value == true) {
        store.port = 4091
    } else {
        store.port = 4090
    }
    console.log("port in use : " + store.port)
};
</script>
