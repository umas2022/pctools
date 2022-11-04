<template>
  <div class="app-settings">
    <h1>设置</h1>
    <!-- 后端端口 -->
    <PortChange />
    <!-- 启动后端 -->
    <RunBackend />
    <!-- 脚本路径 -->
    <PyPath/>
    <!-- 更新目录 -->
    <UpdateIndex/>
    <h3>create : 2022.8.22</h3>
    <h3>by : umas</h3>
  </div>
</template>

<script setup>
import PortChange from "./cp_settings/PortChange.vue"
import RunBackend from "./cp_settings/RunBackend.vue"
import PyPath from "./cp_settings/PyPath.vue"
import UpdateIndex from "./cp_settings/UpdateIndex.vue"
</script>

<style scoped lang="scss">
div.app-settings {
  text-align: center;
}
</style>

