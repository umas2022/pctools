<template>
  <div class="app-settings">
    <el-scrollbar>

      <div class="h1">设置</div>
      <!-- 后端端口 -->
      <CpPortChange />
      <!-- 启动后端 -->
      <CpRunBackend />
      <!-- 脚本路径 -->
      <CpPyPath />
      <!-- 更新目录 -->
      <CpUpdateIndex />
      <!-- 尾部占位 -->
      <div class="rear" style="padding:20px">
        <h3>create : 2022.8.22</h3>
        <h3>by : umas</h3>
        <h3>by : umas</h3>
        <h3>by : umas</h3>
        <h3>by : umas</h3>
        <h3>by : umas</h3>
        <h3>by : umas</h3>
      </div>

    </el-scrollbar>
  </div>
</template>

<script setup>
import CpPortChange from "./cp_settings/CpPortChange.vue"
import CpRunBackend from "./cp_settings/CpRunBackend.vue"
import CpPyPath from "./cp_settings/CpPyPath.vue"
import CpUpdateIndex from "./cp_settings/CpUpdateIndex.vue"
</script>

<style scoped lang="scss">
div.app-settings {
  height: 100vh;
  text-align: center;
  background-color: rgba(255, 0, 0, 0.05);
}
</style>


