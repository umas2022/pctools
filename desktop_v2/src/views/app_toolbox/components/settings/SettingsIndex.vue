<template>
  <div class="app-settings">
    <el-scrollbar>

      <div class="h1">设置</div>
      <!-- 启动后端 -->
      <CpRunBackend />
      <!-- 后端测试 -->
      <CpBackendTest />
      <!-- 开发模式端口 -->
      <CpPortChange />
      <!-- 脚本路径 -->
      <CpPyPath />
      <!-- 更新目录 -->
      <CpUpdateIndex />
      <!-- 显示导航条 -->
      <CpShowNav />
      <!-- 开发日志 -->
      <CpDevelopLog />
      <!-- 尾部占位 -->
      <div class="rear" style="padding:20px">
        <h3>create : 2021.12.25</h3>
        <h3>by : umas</h3>
        <h3>by : umas</h3>
        <h3>by : umas</h3>
        <h3>by : umas</h3>
        <h3>by : umas</h3>
        <h3>by : umas</h3>
        <h5>写这么多只是想试试滚动条是不是还活着</h5>
      </div>

    </el-scrollbar>
  </div>
</template>

<script setup>
import CpPortChange from "./cp_settings/CpPortChange.vue"
import CpRunBackend from "./cp_settings/CpRunBackend.vue"
import CpBackendTest from "./cp_settings/CpBackendTest.vue"
import CpPyPath from "./cp_settings/CpPyPath.vue"
import CpUpdateIndex from "./cp_settings/CpUpdateIndex.vue"
import CpShowNav from "./cp_settings/CpShowNav.vue"
import CpDevelopLog from "./cp_settings/CpDevelopLog.vue"
</script>

<style scoped lang="scss">
div.app-settings {
  height: 100vh;
  text-align: center;
  background-color: rgba(255, 0, 0, 0.05);
}
</style>


