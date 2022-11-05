<template>
  <div class="home">
    <!-- 手动生成背景图 -->
    <div class="bg-box">
      <div class="bg-one" v-for="i in 10">
        <img class="bg-img" src="static/background/pattern-1.svg" alt="">
      </div>
    </div>

    <!-- 全局info弹窗 -->
    <DialogPopup :data="info_data" :display="info_display">
      <template #content>
        <div style="margin:0 auto;padding:20px 0 0 0;width: 250px;">
          <el-icon>
            <Promotion />
          </el-icon>
          这是一行slot,希望你能喜欢
          <el-icon>
            <Promotion />
          </el-icon>
        </div>
      </template>

    </DialogPopup>

    <!-- 内容主体 -->
    <div class="body">
      <div class="animate-box animate__animated " ref="main_index">
        <MainIndex />
      </div>
      <div class="animate-box animate__animated  close" ref="settings_index">
        <SettingsIndex />
      </div>
    </div>

    <!-- 左上角设置按钮 -->
    <div class="go-settings" @click="state_change">
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
import DialogPopup from "@/components/dialog/DialogPopup.vue";

// 显示全局info
const info_data = ref([""])
const info_display = ref(false)
const display_gb_info = (data_input: Array<string>) => {
  info_display.value = !info_display.value
  info_data.value = data_input
}
provide("display_gb_info", display_gb_info)

// 页面切换
const main_index = ref<HTMLDivElement>()
const settings_index = ref<HTMLDivElement>()
const show_settings = ref(false)

const state_change = () => {
  show_settings.value = !show_settings.value
  // 显示设置页
  if (show_settings.value) {
    main_index.value!.classList.remove("animate__backInLeft")
    main_index.value!.classList.add("animate__backOutLeft")
    setTimeout(() => {
      main_index.value!.classList.add("close")
    }, 500)
    setTimeout(() => {
      settings_index.value!.classList.remove("close")
      settings_index.value!.classList.remove("animate__backOutRight")
      settings_index.value!.classList.add("animate__backInRight")
    }, 300)
  }
  // 显示主页
  else {
    settings_index.value!.classList.add("animate__backOutRight")
    settings_index.value!.classList.remove("animate__backInRight")
    setTimeout(() => {
      settings_index.value!.classList.add("close")
    }, 500)
    setTimeout(() => {
      main_index.value!.classList.add("animate__backInLeft")
      main_index.value!.classList.remove("animate__backOutLeft")
      main_index.value!.classList.remove("close")
    }, 300)
  }
}

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

// 背景图片
div.bg-box {
  position: absolute;
  z-index: 0;
  height: 100%;
  width: 100%;
  white-space: nowrap;
  overflow: hidden;

  div.bg-one {
    position: relative;
    display: inline-block;
    *display: inline;
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

div.close {
  display: none;
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