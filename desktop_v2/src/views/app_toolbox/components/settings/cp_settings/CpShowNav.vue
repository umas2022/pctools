<template>
    <div class="cp-path">
        <BasicTemplate>
            <!-- 标签 -->
            <template #tp-label>
                <span>显示测试页导航</span>
            </template>

            <!-- 控制 -->
            <template #tp-control>
                <el-switch v-model="show_nav" @click="reset_path"></el-switch>
            </template>

            <!-- 折叠info栏 -->
            <template #tp-info>
                <span class="line">1.左上角显示导航按钮</span> <br>
                <span class="line">2.导航内目前都在开发中(烂尾)</span>
            </template>

        </BasicTemplate>

    </div>
</template>
<script setup lang="ts">
import { onMounted, ref, inject, reactive } from "vue";
import BasicTemplate from "./BasicTemplate.vue"

const store_frame: any = inject("store_frame")

const show_nav = ref(store_frame.show_nav)
const reset_path = () => {
    store_frame.show_nav = show_nav.value
    console.log(store_frame.show_nav)
};
</script>
