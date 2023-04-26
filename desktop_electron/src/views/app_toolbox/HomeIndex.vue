<template>
  <div class="home">
    <el-scrollbar @scroll="home_onscroll" ref="scrollbarRef">

      <!-- 手动生成背景图x10 -->
      <div class="bg-box">
        <div class="bg-one" v-for="i in 10">
          <img class="bg-img" :src=bg_path alt="">
        </div>
      </div>

      <!-- 全局info弹窗 -->
      <DialogPopup :data="info_data" :display="info_display">
        <template #content>
          <div style="margin:0 auto;padding:20px 0 0 0;width: 300px;">
            <el-icon>
              <Promotion />
            </el-icon>
            这是一行slot,希望今天的你也能喜欢
            <el-icon>
              <Promotion />
            </el-icon>
          </div>
        </template>
      </DialogPopup>

      <!-- 内容主体 -->
      <div class="body">
        <div class="animate-box animate__animated " ref="main_index" style="height:100%">
          <MainIndex />
        </div>
        <div class="animate-box animate__animated  close" ref="setting_index">
          <SettingsIndex />
        </div>
      </div>


      <!-- 右上角按钮 -->
      <div class="button-abs">
        <AnimateDown :display="!button_hide_all">
          <template #content>
            <div class="button-box">

              <!-- 右上角展开按钮(加号/减号) -->
              <ButtonExtract />

              <!-- 右上角切换背景按钮(刷新) -->
              <ButtonChangeBg />

              <!-- 右上角后端启动按钮(小飞机) -->
              <ButtonRunBe />

              <!-- 右上角新建窗口(显示器) -->
              <ButtonNewWindow />

              <!-- 右上角设置按钮(齿轮/右箭头) -->
              <ButtonChangePage :main_index="main_index" :setting_index="setting_index" />

            </div>

          </template>
        </AnimateDown>
      </div>

    </el-scrollbar>
  </div>
</template>
<script setup lang="ts">
import { provide, reactive, ref, onMounted, computed } from "vue"
import { useStore } from "vuex";
import type { ElScrollbar } from "element-plus";
import type { Ref } from "vue"
import { static_path, is_dev } from "@/utils/utils_path.js"
import { get_wsurl } from "@/utils/api_config.js"
import AnimateDown from "@/components/animate_down/AnimateDown.vue"
import DialogPopup from "@/components/dialog/DialogPopup.vue"
// 功能页/设置页
import MainIndex from "./components/main/MainIndex.vue"
import SettingsIndex from "./components/settings/SettingsIndex.vue"
// 右上角按钮
import ButtonExtract from "./components/button/ButtonExtract.vue"
import ButtonChangeBg from "./components/button/ButtonChangeBg.vue"
import ButtonRunBe from "./components/button/ButtonRunBe.vue"
import ButtonNewWindow from "./components/button/ButtonNewWindow.vue"
import ButtonChangePage from "./components/button/ButtonChangePage.vue"

const fs = window.require("fs");
const path = window.require("path");
const store = useStore()

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
const setting_index = ref<HTMLDivElement>()


// 切换背景图片
const bg_path = computed(() => "static/background/pattern-" + store_home.bg_num + ".svg")

// 后端连通性检测
const check_be = (flag: Ref<boolean>) => {
  let wsdemo = new WebSocket(get_wsurl(store.state.config["port"]["value"]).local + "app_test_ws");
  wsdemo.onopen = () => {
    flag.value = true
  };
}

// 初始化动作
onMounted(() => {
  // // 启动后端
  // const backend_started = ref(false)
  // check_be(backend_started)
  // setTimeout(() => {
  //   if (!backend_started.value) {
  //     run_back()
  //   }
  // }, 500)
})

// 滚动条触发事件
const button_hide_all = ref(false)
const scrollbarRef = ref<InstanceType<typeof ElScrollbar>>();
const home_onscroll = (scrollPos: { scrollTop: number }) => {
  let scrollTop = scrollPos.scrollTop
  if (scrollTop < 40) {
    button_hide_all.value = false
  } else {
    button_hide_all.value = true
  }
}

// 全局参数
const store_home = reactive({
  // 当前页面
  current_page: "home",
  // 隐藏顶部列表组件
  extract_display: true,
  // 背景图片序号
  bg_num: ref(Math.ceil(Math.random() * 33)),
  // 当前是否为开发状态
  is_dev: is_dev(),
  // 功能列表,储存后端返回的index.json
  index_list: [],
  // 选中的组
  group: "",
  // 选中的具体功能
  function: "",
  // 选中的功能对应的intf.json
  intf_data: {},
})
provide("store_home", store_home)

// store加载全局设置
const config_path = path.join(static_path(), "config.json")
onMounted(() => {
  fs.readFile(config_path, 'utf-8',
    (err: any, data: any) => {
      if (err) {
        console.log("load config err:", err);
      } else {

        data = JSON.parse(data)
        for (let key in data) {
          store.commit("init_config", { "key": key, "value": data[key] })
        }

        // 为空的项目设置初值
        let write_flag = false
        if (store.state.config["py_path"]["value"] == "") {
          store.state.config["py_path"]["value"] = path.join(static_path(), "py_script")
          write_flag = true
        }
        if (store.state.config["py_server"]["value"] == "") {
          store.state.config["py_server"]["value"] = path.join(static_path(), "py_server")
          write_flag = true
        }

        // 保存初值
        if (write_flag) {
          try {
            fs.writeFileSync(config_path, JSON.stringify(store.state.config));
          } catch (err) {
            console.error("config write error : " + err);
          }
        }

      }
    }
  );
});

</script>
<style lang="scss" scoped>
div.home {
  position: relative;
  height: 100vh;
}

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

// 内容主体
div.body {
  position: relative;
  height: 100%;
}

// 右上角按钮box
div.button-abs {
  position: absolute;
  top: 10px;
  width: calc(100% - 15px);
  height: 0; // 横向不遮挡其他元素
  display: flex;
  justify-content: flex-end; // 内部div右对齐
  z-index: 0;

  div.button-box {
    position: relative;
    display: flex;
    // border: solid 1px red;
  }
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