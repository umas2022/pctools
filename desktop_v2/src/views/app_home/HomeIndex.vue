<template>
  <div class="home">
    <!-- 手动生成背景图 -->
    <div class="bg-box">
      <div class="bg-one" v-for="i in 10">
        <img class="bg-img" src="static/background/pattern-1.svg" alt="">
      </div>
    </div>

    <!-- 内容主体 -->
    <div class="body">
      <MainIndex v-if="!show_settings" class="animate-box animate__animated animate__backInRight" />
      <SettingsIndex v-else class="animate-box animate__animated animate__backInLeft " />
    </div>

    <!-- 左上角设置按钮 -->
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

const path = window.require("path");

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

// div.home::before {
//   content: "";
//   position: absolute;
//   top: 0;
//   left: 0;
//   height: 100%;
//   width: 100%;
//   // background-image: url(D:\s-linux\project\pctools\desktop_v2\public\static\background\pattern-1.svg);
//   // background-image: url(v-bind(bg_path));
//   // background-image: url('/public/static/background/pattern-1.svg');
//   // background-image: url('./assets/background/pattern-1.svg');
//   // background-image: url('../../assets/background/pattern-1.svg');
//   // background-image: url('/src/assets/background/pattern-1.svg');

//   opacity: 0.15;
// }

div.bg-box {
  position: absolute;
  z-index: 0;
  height: 100%;
  width: 100%;
  white-space: nowrap;
  overflow: hidden;
  div.bg-one{
    position: relative;
    display: inline-block;
    *display:inline;
    height: 100%;
    z-index: 0;
  }
  img.bg-img {
  position: relative;
  top: 0;
  left: 0;
  height: 100%;
  opacity: 0.15;
}
}



img.bg-img::before {
  display: inline-block;
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
@import 'animate.css';

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