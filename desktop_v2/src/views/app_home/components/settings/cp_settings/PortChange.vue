<template>
    <div>
        <div class="cp-port">
            <!-- 开发模式port -->
            <span>开发模式端口</span>
            <div class="info-icon">
                <useSvgIcon icon="info" color="black" :width="Number(20)" @click="setInfoFlagPort = !setInfoFlagPort" />
            </div>
            <el-switch v-model="setValuePort" @click="setFuncPort" />
            <!-- 折叠info栏 -->
            <div class="info" v-if="setInfoFlagPort">
                <span>开发模式：localhost:4091 / </span>
                <span>生产模式：localhost:4090</span> <br />
            </div>
            <!-- 分割线 -->
            <div style="width: 80%; margin: 0 auto">
                <el-divider></el-divider>
            </div>
        </div>
    </div>
</template>
<script setup>
import { onMounted, ref, inject } from "vue";
import useSvgIcon from "@/components/use_svg/useSvgIcon.vue";

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
<style lang="scss" scoped>
div.info-icon {
    display: inline-block;
    vertical-align: middle; // 垂直居中
    padding-left: 10px;
    padding-right: 20px;
    cursor: pointer;
}
</style>