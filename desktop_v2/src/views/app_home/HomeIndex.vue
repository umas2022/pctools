<template>
  <div class="home">
    <div class="background"></div>
    <div class="body">
      <MainIndex v-if="!show_settings" />
      <SettingsIndex v-else />
    </div>
    <!-- 设置按钮 -->
    <div class="go-settings" @click="show_settings = !show_settings">
      <el-icon :size="30" v-if="!show_settings">
        <Setting />
      </el-icon>
      <el-icon :size="30" v-else>
        <ArrowLeftBold />
      </el-icon>
    </div>
  </div>
</template>
<script setup lang="ts">
import { provide, reactive, ref } from "vue"

import MainIndex from "./components/main/MainIndex.vue"
import SettingsIndex from "./components/settings/SettingsIndex.vue"

// 页面切换
const show_settings = ref(false)

// 全局参数
const store = reactive({
  port: 4090,
  py_path: "D:\\s-linux\\project\\pctools\\py_script",
  index_list: [],
  function: "",
  intf_data: {}
})
provide("store", store)

</script>
<style lang="scss" scoped>
div.home {
  position: relative;
  height: 100vh;
}

div.home::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
  background-image: url(@/assets/pattern-1.svg);
  opacity: 0.15;
}



.el-scrollbar {
  height: 520px;
}

div.go-settings {
  position: absolute;
  padding: 10px;
  z-index: 2;
  left: 0px;
  top: 0px;
  cursor: pointer;
}
</style>

<!-- 全局style -->
<style lang="scss">
div.h1 {
  font-weight: bold; // 加粗
  font-size: 33px;
  padding: 10px;
}

div.h3 {
  font-weight: bold; // 加粗
  font-size: 20px;
  padding: 10px;
}
</style>