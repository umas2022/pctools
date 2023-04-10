<template>
  <div>
    <!-- 右上角启动新窗口(显示器) -->
    <el-tooltip class="box-item" effect="dark" content="启动新窗口" placement="bottom-end">
      <div class="run-back button" @click="start">
        <AnimateDown :display="store_home.current_page == 'home'">
          <template #content>
            <el-icon :size="30">
              <Monitor />
            </el-icon>
          </template>
        </AnimateDown>
      </div>
    </el-tooltip>
  </div>
</template>

<script setup lang="ts">
import { inject,watch,ref } from "vue"
import AnimateDown from "@/components/animate_down/AnimateDown.vue"
import { get_wsurl } from "@/utils/api_config.js";
const path = window.require("path");

const store_config: any = inject("store_config")
const store_home: any = inject("store_home")

const refresh_config = (item: string) => {
    return store_config.value[item] ? store_config.value[item]["value"] : "config load failed"
}
watch(store_config, () => py_path.value = refresh_config("py_path"))
const py_path = ref(refresh_config("py_path"))

// 开始按钮
const start = (button: any) => {
  let cmd_text = "C:\\Users\\umas\\AppData\\Local\\Programs\\desktop_electron\\电脑配件.exe"
  if (!store_home.is_dev){
    cmd_text = path.dirname(py_path.value) // desktop_electron\\resources\\static
    cmd_text = path.dirname(cmd_text) // desktop_electron\\resources\\static
    cmd_text = path.dirname(cmd_text) // desktop_electron\\resources
    cmd_text = path.dirname(cmd_text) // desktop_electron
    cmd_text = path.join(cmd_text,"电脑配件.exe")
    console.log(cmd_text)
  } 
    

    const send_data = {
        function: "sp_auto_cmd",
        terminal: false,
        py_path: py_path.value,
        cmd_text:cmd_text
    }

    console.log("ws connecting ...");

    let wsdemo = new WebSocket(get_wsurl().local + "sp_searcher");
    wsdemo.onopen = () => {
        wsdemo.send(JSON.stringify({ function: "run", data: send_data }));
    };
    wsdemo.onmessage = (e) => {
        console.log(e.data) ;
    };
};


</script>

<style lang="scss" scoped>
// 右上角按钮统一格式
div.button {
  cursor: pointer;

  :hover {
    border-radius: 5px;
  }
}

// 右上角后端按钮
div.run-back :hover {
  background-color: rgba(0, 123, 255, 0.127);
}
</style>