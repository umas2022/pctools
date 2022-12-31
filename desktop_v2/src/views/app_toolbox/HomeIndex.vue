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
          这是一行slot,希望今天的你也能喜欢
          <el-icon>
            <Promotion />
          </el-icon>
        </div>
      </template>

    </DialogPopup>



    <!-- 右上角设置按钮(齿轮) -->
    <div class="go-settings" @click="state_change">
      <AnimateDown :display="button_display">
        <template #content>
          <el-icon :size="30">
            <Setting />
          </el-icon>
        </template>
      </AnimateDown>
    </div>
    <!-- 右上角返回主页按钮(右箭头) -->
    <div class="go-settings" @click="state_change">
      <AnimateDown :display="!button_display">
        <template #content>
          <el-icon :size="30">
            <ArrowRightBold />
          </el-icon>
        </template>
      </AnimateDown>
    </div>
    <!-- 右上角后端启动按钮(小飞机) -->
    <div class="run-back" @click="run_back">
      <AnimateDown :display="button_display">
        <template #content>
          <el-icon :size="30">
            <Position />
          </el-icon>
        </template>
      </AnimateDown>
    </div>
    <!-- 右上角展开按钮(加号) -->
    <div class="extract" @click="extract_change">
      <AnimateDown :display="button_display">
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
    <!-- 右上角折叠按钮(减号) -->
    <div class="extract" @click="extract_change">
      <AnimateDown :display="button_display">
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

    <!-- 内容主体 -->
    <div class="body">
      <div class="animate-box animate__animated " ref="main_index">
        <MainIndex />
      </div>
      <div class="animate-box animate__animated  close" ref="settings_index">
        <SettingsIndex />
      </div>
    </div>

  </div>
</template>
<script setup lang="ts">
import { provide, reactive, ref, } from "vue"
import { useStore } from "vuex"
import MainIndex from "./components/main/MainIndex.vue"
import SettingsIndex from "./components/settings/SettingsIndex.vue"
import AnimateDown from "@/components/animate_down/AnimateDown.vue"
import DialogPopup from "@/components/dialog/DialogPopup.vue"

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
const settings_index = ref<HTMLDivElement>()
const button_display = ref(true)

const state_change = () => {
  button_display.value = !button_display.value
  // 显示设置页
  if (!button_display.value) {
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
  let be_path = store.state.pro_path
  console.log(be_path)
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

// 全局参数
const store_home = reactive({
  // 后端端口
  port: 4090,
  // 脚本调用位置,用于启动后端
  py_path: "D:\\s-linux\\project\\pctools\\py_script",
  index_list: [],
  function: "",
  intf_data: {},
  // 内容折叠
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

// 右上角切换按钮
div.go-settings {
  position: absolute;
  padding: 10px;
  z-index: 2;
  right: 0px;
  top: 0px;
  cursor: pointer;

  :hover {
    border-radius: 5px;
    background-color: rgba(0, 255, 255, 0.2);
  }
}

// 右上角后端按钮
div.run-back {
  position: absolute;
  padding: 10px;
  z-index: 2;
  right: 35px;
  top: 0px;
  cursor: pointer;

  :hover {
    border-radius: 5px;
    background-color: rgba(0, 255, 255, 0.2);
  }
}

// 右上角展开按钮
div.extract {
  position: absolute;
  padding: 10px;
  z-index: 2;
  right: 68px;
  top: 0px;
  cursor: pointer;

  :hover {
    border-radius: 5px;
    background-color: rgba(0, 255, 255, 0.2);
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