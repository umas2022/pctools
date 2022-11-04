<template>
  <div class="home">
    <el-scrollbar>
      <MainIndex v-if="!show_settings"/>
      <SettingsIndex v-else/>

      <!-- 设置按钮 -->
      <div class="go-settings" @click="show_settings = !show_settings">
        <el-icon :size="30" v-if="!show_settings">
          <Setting />
        </el-icon>
        <el-icon :size="30" v-else>
          <ArrowLeftBold />
        </el-icon>
      </div>
    </el-scrollbar>
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
  port:4090,
  py_path:"D:\\s-linux\\project\\pctools\\py_script",
  index_list:[],
  function:"",
  intf_data:{}
})
provide("store",store)

</script>
<style lang="scss" scoped>
div.home {
  position: relative;
}

.el-scrollbar {
  height: 520px;
}

div.go-settings {
  position: absolute;
  z-index: 2;
  left: 0px;
  top: 0px;
  cursor: pointer;
}
</style>