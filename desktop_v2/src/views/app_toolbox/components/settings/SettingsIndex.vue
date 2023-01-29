<template>
  <div class="app-settings">
    <div class="h1">设置</div>
    <!-- 启动后端 -->
    <CpRunBackend />
    <!-- python环境初始化 -->
    <CpEnvInit />
    <!-- 后端测试 -->
    <CpBackendTest />
    <!-- 开发模式端口 -->
    <CpChangePort />
    <!-- 开发模式路径 -->
    <CpChangePath />
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
      <h3>create : 2021.12</h3>
      <h3 v-for="item in 20">by : umas</h3>
    </div>
  </div>
</template>

<script setup>
import CpChangePort from "./cp_settings/CpChangePort.vue"
import CpEnvInit from "./cp_settings/CpEnvInit.vue"
import CpChangePath from "./cp_settings/CpChangePath.vue"
import CpRunBackend from "./cp_settings/CpRunBackend.vue"
import CpBackendTest from "./cp_settings/CpBackendTest.vue"
import CpPyPath from "./cp_settings/CpPyPath.vue"
import CpUpdateIndex from "./cp_settings/CpUpdateIndex.vue"
import CpShowNav from "./cp_settings/CpShowNav.vue"
import CpDevelopLog from "./cp_settings/CpDevelopLog.vue"
</script>

<style scoped lang="scss">
div.app-settings {
  height: 100%;
  text-align: center;
  background-color: rgba(255, 0, 0, 0.05);
}
</style>

<!-- info文本格式 -->
<style lang="scss">
span.line {
  float: left; // span左对齐
  text-align: left; // span内文本左对齐
  word-break: break-all; //超出容器强制换行
  margin-left: 1em; // 所有行缩进
  text-indent: -1em; // 调整首行缩进

}
</style>


