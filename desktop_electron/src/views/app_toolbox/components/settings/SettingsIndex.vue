<template>
  <div class="app-settings">
    <div class="h1">设置</div>
    <!-- python环境初始化 -->
    <CpEnvInit />
    <!-- 更新目录 -->
    <CpUpdateIndex />
    <!-- 后端测试 -->
    <CpBackendTest />

    <!-- 通信端口设置 -->
    <CpChangePort />
    <!-- 开发模式路径 -->
    <CpChangePath v-if="IsDev"/>
    <!-- 手动输入脚本路径 -->
    <CpChangePathScript />
    <CpChangePathServer />
    
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
import { static_path,is_dev } from "@/utils/utils_path.js"

import CpChangePort from "./cp_settings/CpChangePort.vue"
import CpEnvInit from "./cp_settings/CpEnvInit.vue"
import CpChangePath from "./cp_settings/CpChangePath.vue"
import CpBackendTest from "./cp_settings/CpBackendTest.vue"
import CpChangePathScript from "./cp_settings/CpChangePathScript.vue"
import CpChangePathServer from "./cp_settings/CpChangePathServer.vue"
import CpUpdateIndex from "./cp_settings/CpUpdateIndex.vue"
import CpShowNav from "./cp_settings/CpShowNav.vue"
import CpDevelopLog from "./cp_settings/CpDevelopLog.vue"

// 判断开发模式
const IsDev = is_dev()

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


