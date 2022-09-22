<template>
  <div class="main">
    <h1>设置</h1>
    <h5>一些参数</h5>
    <!-- 后端端口 -->
    <PortChange />
    <!-- 启动后端 -->
    <RunBackend />
    <h3>create : 2022.8.22</h3>
    <h3>by : umas</h3>
  </div>
</template>

<script setup>
import PortChange from "./components/PortChange.vue"
import RunBackend from "./components/RunBackend.vue"
</script>

<style scoped lang="scss">
div.main {
  text-align: center;
}
</style>

