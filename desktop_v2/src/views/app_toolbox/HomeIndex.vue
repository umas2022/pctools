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
        <div class="animate-box animate__animated  close" ref="settings_index">
          <SettingsIndex />
        </div>
      </div>


      <!-- 右上角按钮 -->
      <div class="button-abs">
        <AnimateDown :display="!button_hide_all">
          <template #content>
            <div class="button-box">

              <!-- 右上角展开按钮(加号) -->
              <el-tooltip class="box-item" effect="dark" content="目录展开" placement="bottom-end">
                <div class="extract button" @click="extract_change">
                  <AnimateDown :display="home_display">
                    <template #content>
                      <AnimateDown :display="!store_home.extract_display">
                        <template #content>
                          <el-icon :size="30">
                            <Plus />
                          </el-icon>
                        </template>
                      </AnimateDown>
                    </template>
                  </AnimateDown>
                </div>
              </el-tooltip>

              <!-- 右上角折叠按钮(减号) -->
              <el-tooltip class="box-item" effect="dark" content="目录折叠" placement="bottom-end">
                <div class="extract button" @click="extract_change">
                  <AnimateDown :display="home_display">
                    <template #content>
                      <AnimateDown :display="store_home.extract_display">
                        <template #content>
                          <el-icon :size="30">
                            <Minus />
                          </el-icon>
                        </template>
                      </AnimateDown>
                    </template>
                  </AnimateDown>
                </div>
              </el-tooltip>

              <!-- 右上角切换背景按钮(刷新) -->
              <el-tooltip class="box-item" effect="dark" content="切换背景" placement="bottom-end">
                <div class="change-bg button" @click="change_bg">
                  <AnimateDown :display="home_display">
                    <template #content>
                      <el-icon :size="30">
                        <Refresh />
                      </el-icon>
                    </template>
                  </AnimateDown>
                </div>
              </el-tooltip>

              <!-- 右上角后端启动按钮(小飞机) -->
              <el-tooltip class="box-item" effect="dark" content="启动后端" placement="bottom-end">
                <div class="run-back button" @click="run_back">
                  <AnimateDown :display="home_display">
                    <template #content>
                      <el-icon :size="30">
                        <Position />
                      </el-icon>
                    </template>
                  </AnimateDown>
                </div>
              </el-tooltip>

              <!-- 右上角设置按钮(齿轮) -->
              <el-tooltip class="box-item" effect="dark" content="参数设置" placement="bottom-end" v-if="home_display">
                <div class="go-settings button" @click="state_change">
                  <AnimateDown :display="home_display">
                    <template #content>
                      <el-icon :size="30">
                        <Setting />
                      </el-icon>
                    </template>
                  </AnimateDown>
                </div>
              </el-tooltip>

              <!-- 右上角返回主页按钮(右箭头) -->
              <el-tooltip class="box-item" effect="dark" content="返回主页" placement="bottom-end" v-if="!home_display">
                <div class="go-home button" @click="state_change">
                  <AnimateDown :display="!home_display">
                    <template #content>
                      <el-icon :size="30">
                        <Right />
                      </el-icon>
                    </template>
                  </AnimateDown>
                </div>
              </el-tooltip>

            </div>

          </template>
        </AnimateDown>
      </div>

    </el-scrollbar>
  </div>
</template>
<script setup lang="ts">
import { provide, reactive, ref, onMounted, computed } from "vue"
import type { ElScrollbar } from "element-plus";
import type { Ref } from "vue"
import { static_path } from "@/utils/utils_path.js"
import { get_wsurl } from "@/utils/api_config.js"
import MainIndex from "./components/main/MainIndex.vue"
import SettingsIndex from "./components/settings/SettingsIndex.vue"
import AnimateDown from "@/components/animate_down/AnimateDown.vue"
import DialogPopup from "@/components/dialog/DialogPopup.vue"
const path = window.require("path");


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
const home_display = ref(true)

const state_change = () => {
  home_display.value = !home_display.value
  // 显示设置页
  if (!home_display.value) {
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

// 启动后端
const { PythonShell } = window.require("python-shell");
const run_back = () => {
  let be_path = path.dirname(store_home.py_path)
  let be_script = "run_backterminal.py"
  let options = {
    mode: "text",
    pythonOptions: ["-u"], // get print results in real-time
    scriptPath: be_path,
    // args: ["4091"],
    args: ["win"],
  };
  let pyshell = new PythonShell(be_script, options);
  pyshell.on("message", function (message: string) {
    console.log(message);
  });
  pyshell.end(function (err: string) {
    if (err) {
      throw err;
    }
    console.log("finished");
  });
}

// 内容折叠
const extract_change = () => {
  store_home.extract_display = !store_home.extract_display
}

// 切换背景图片
const bg_num = ref(Math.ceil(Math.random() * 33))
const bg_path = computed(() => "static/background/pattern-" + bg_num.value + ".svg")
const change_bg = () => {
  bg_num.value += 1
  if (bg_num.value == 33) {
    bg_num.value = 1
  }
}

// 后端连通性检测
const check_be = (flag: Ref<boolean>) => {
  let wsdemo = new WebSocket(get_wsurl().local + "app_test_ws");
  wsdemo.onopen = () => {
    flag.value = true
  };
}

// 初始化动作
onMounted(() => {
  // 启动后端
  const backend_started = ref(false)
  check_be(backend_started)
  setTimeout(() => {
    if (!backend_started.value) {
      run_back()
    }
  }, 500)
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
  // 后端端口
  port: 4090,
  // 脚本调用位置,用于后端通信,通过设置页的switch切换开发目录和生产目录
  py_path: path.join(static_path(), "backend_v2/py_script"),
  // 功能列表,后端返回的index.json
  index_list: [],
  // 选中的组
  group: "",
  // 选中的具体功能
  function: "",
  // 对应功能的intf.json
  intf_data: {},
  // 页面内容折叠
  extract_display: true
})
provide("store_home", store_home)




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

// 内容主体
div.body {
  position: relative;
  height: 100%;
}

// 右上角按钮box
div.button-abs {
  position: absolute;
  top: 10px;
  // border: solid 1px blue;
  width: calc(100% - 15px);
  display: flex;
  justify-content: flex-end; // 内部div右对齐

  div.button-box {
    position: relative;
    display: flex;
    // border: solid 1px red;

    // 右上角按钮统一格式
    div.button {
      cursor: pointer;

      :hover {
        border-radius: 5px;
      }
    }

    // 右上角切换按钮
    div.go-settings :hover {
      background-color: rgba(255, 0, 0, 0.05);
    }

    // 右上角返回主页
    div.go-home :hover {
      background-color: rgba(0, 0, 255, 0.05);
    }

    // 右上角后端按钮
    div.run-back :hover {
      background-color: rgba(0, 0, 255, 0.06);
    }

    // 右上角切换背景按钮
    div.change-bg :hover {
      background-color: rgba(255, 191, 0, 0.2);
    }

    // 右上角展开按钮
    div.extract :hover {
      background-color: rgba(0, 255, 0, 0.1);
    }
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