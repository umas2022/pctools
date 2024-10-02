<template>
    <div class="test-body">
        <div class="head">
            <h1>test</h1>
            <span>选择目标: </span>
            <el-select v-model="label_select">
                <el-option v-for="item in label_list" :label="item.label" :value="item.value"></el-option>
            </el-select>
            <el-button @click="go_page">go</el-button>
        </div>
        <div class="test-main" v-if="label_select != ''">
            <el-scrollbar>
                <component :is="page_select" />
            </el-scrollbar>
        </div>
    </div>
</template>
<script lang="ts" setup>
import { ref, defineAsyncComponent, shallowRef } from "vue"

// 动态加载组件
const page_select = shallowRef()
const page_list = {
    // test_animate : anamate动效库
    AnimateIndex: defineAsyncComponent(() => import("./components/test_animate/AnimateIndex.vue")),
    // test_auto_clicker : 自动点击器半成品
    AutoClickerIndex: defineAsyncComponent(() => import("./components/test_auto_clicker/AutoIndex.vue")),
    // test_call_py : electron直接调用python测试
    CallPyIndex: defineAsyncComponent(() => import("./components/test_call_py/CallPyIndex.vue")),
    // test_click_like : 一个有趣的点赞动效
    LikeIndex: defineAsyncComponent(() => import("./components/test_click_like/LikeIndex.vue")),
    // test_csshake : csshake鬼畜振动
    ShakeIndex: defineAsyncComponent(() => import("./components/test_csshake/ShakeIndex.vue")),
    // test_hello_world : hello world !
    HelloIndex: defineAsyncComponent(() => import("./components/test_hello_world/HelloIndex.vue")),
    // test_icon : 自定义svg icon组件
    IconIndex: defineAsyncComponent(() => import("./components/test_icon/IconIndex.vue")),
    // test_img_browser : 本地图片浏览器(单张/瀑布流)
    ImgBrowserIndex: defineAsyncComponent(() => import("./components/test_img_browser/BrowserIndex.vue")),
    // test_ws_test : websocket连通测试
    WsIndex: defineAsyncComponent(() => import("./components/test_ws_test/DemoWebsocket.vue")),
}

// shallowRef仅对顶层ref,组件内部变化不触发页面更新
const label_select = shallowRef("")
const label_list = [
    { label: "animate动效库", value: "AnimateIndex" },
    { label: "自动点击器半成品", value: "AutoClickerIndex" },
    { label: "调用本地python", value: "CallPyIndex" },
    { label: "点赞动效", value: "LikeIndex" },
    { label: "csshake振动库", value: "ShakeIndex" },
    { label: "hello world", value: "HelloIndex" },
    { label: "图标引入", value: "IconIndex" },
    { label: "本地图片浏览器", value: "ImgBrowserIndex" },
    { label: "ws连接测试", value: "WsIndex" },
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