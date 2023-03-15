<template>
    <div class="test-main" style="height:1000px">
        <h1>animate动效库</h1>
        <el-button type="primary" plain @click="replay">replay</el-button>
        <div style="height:50px"></div>
        <div style="height:250px">
            <div v-if="show_animate" class="animate-box animate__animated animate__bounce">
                <span class="text">animate</span>
            </div>
        </div>
        <h3>https://animate.style/</h3>
        <h3>npm install animate.css --save</h3>
        <h3>@import 'animate.css';</h3>
        <h3>animate效果只有在加载时触发,button控制了一个v-if</h3>
        <div style="height:100px"></div>
    </div>
</template>
<script setup lang="ts">
import { ref } from 'vue';

const show_animate = ref(true)
const replay = () => {
    show_animate.value = false
    setTimeout(() => {
        show_animate.value = true
    }, 1)
}
</script>
<style lang="scss" scoped>
@import 'animate.css';

div.animate-box {
    display: flex;
    align-items: center;
    margin: auto;
    width: 300px;
    height: 200px;
    background-color: red;

    .text {
        color: rgb(0, 255, 115);
        font-weight: bold; // 加粗
        font-size: 60px;
        position: absolute;
        display: flex;
        padding-left: 30px;
    }
}
</style>