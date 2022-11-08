<template>
    <div class="cp-path">
        <BasicTemplate>
            <!-- 标签 -->
            <template #tp-label>
                <span>显示导航</span>
            </template>

            <!-- 控制 -->
            <template #tp-control>
                <el-button type="primary" plain @click="reset_path">切换</el-button>
            </template>

            <!-- 折叠info栏 -->
            <template #tp-info>
                <span>累了,不想写啥注释了</span> <br>
                <span>算了还是写一句,看左上角</span>
            </template>

        </BasicTemplate>

    </div>
</template>
<script setup lang="ts">
import { onMounted, ref, inject, reactive } from "vue";
import BasicTemplate from "./BasicTemplate.vue"

const store_frame: any = inject("store_frame")


const reset_path = () => {
    store_frame.show_nav = !store_frame.show_nav
    console.log(store_frame.show_nav)
};
</script>
