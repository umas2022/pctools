<template>
    <div class="test-body">
        <div class="head">
            <span>选择目标: </span>
            <el-select v-model="label_select">
                <el-option v-for="item in label_list" :label="item.label" :value="item.value"></el-option>
            </el-select>
            <el-button @click="go_page">go</el-button>
        </div>
        <div class="test-main" v-if="label_select != ''">
            <component :is="page_select" />
        </div>
    </div>
</template>
<script lang="ts" setup>
import { ref, defineAsyncComponent, shallowRef } from "vue"

// 动态加载组件
const page_select = shallowRef()
const page_list = {
    BrowserIndex: defineAsyncComponent(() => import("./components/app_img_browser/BrowserIndex.vue")),
    AutoIndex: defineAsyncComponent(() => import("./components/app_auto_click/AutoIndex.vue"))
}

// shallowRef仅对顶层ref
const label_select = shallowRef("")
const label_list = [
    { label: "图片浏览", value: "BrowserIndex" },
    { label: "自动点击", value: "AutoIndex" }
]

// 由于el-select的显示bug,赋值需要单独进行
const go_page = () => {
    console.log(label_select.value)
    page_select.value = page_list[label_select.value as keyof typeof page_list]
}

</script>
<style lang="scss" scoped>
div.test-body {
    margin: 0 auto;
    text-align: center;
    height: 100%;

    div.test-main {
        height: 100%;
    }
}

div.head {
    border: 2px solid red;
    padding: 5px;
}
</style>