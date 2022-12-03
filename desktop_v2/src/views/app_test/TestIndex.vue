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
    HelloIndex: defineAsyncComponent(() => import("./components/test_hello_world/HelloIndex.vue")),
    LikeIndex: defineAsyncComponent(() => import("./components/test_click_like/LikeIndex.vue")),
    AnimateIndex: defineAsyncComponent(() => import("./components/test_animate/AnimateIndex.vue")),
    CallPyIndex: defineAsyncComponent(() => import("./components/test_call_py/CallPyIndex.vue")),
    ShakeIndex: defineAsyncComponent(() => import("./components/test_csshake/ShakeIndex.vue")),
    IconIndex: defineAsyncComponent(() => import("./components/test_icon/IconIndex.vue")),
    WsIndex: defineAsyncComponent(() => import("./components/test_ws_test/DemoWebsocket.vue")),
}

// shallowRef仅对顶层ref,组件内部变化不触发页面更新
const label_select = shallowRef("")
const label_list = [
    { label: "hello world", value: "HelloIndex" },
    { label: "点赞动效", value: "LikeIndex" },
    { label: "animate动效库", value: "AnimateIndex" },
    { label: "调用本地python", value: "CallPyIndex" },
    { label: "csshake振动库", value: "ShakeIndex" },
    { label: "图标引入", value: "IconIndex" },
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