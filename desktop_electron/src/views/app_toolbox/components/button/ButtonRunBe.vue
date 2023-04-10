<template>
  <div>
    <!-- 右上角后端启动按钮(小飞机) -->
    <el-tooltip class="box-item" effect="dark" content="启动后端" placement="bottom-end">
      <div class="run-back button" @click="run_back">
        <AnimateDown :display="store_home.current_page == 'home'">
          <template #content>
            <el-icon :size="30">
              <Position />
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
const path = window.require("path");

const store_home: any = inject("store_home")
const store_config: any = inject("store_config")

const refresh_config = (item: string) => {
    return store_config.value[item] ? store_config.value[item]["value"] : "config load failed"
}
watch(store_config, () => py_server.value = refresh_config("py_server"))
const py_server = ref(refresh_config("py_server"))
watch(store_config, () => venv_path.value = refresh_config("path_venv"))
const venv_path = ref(refresh_config("path_venv"))

// 启动后端
const { PythonShell } = window.require("python-shell");
const run_back = () => {
  let be_path = store_config.value["py_server"]["value"]
  let be_script = "run_backend_venv.py"
  let options = {
    mode: "text",
    pythonOptions: ["-u"], // get print results in real-time
    scriptPath: be_path,
    args: [store_config.value["port"]["value"],venv_path.value],
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
  background-color: rgba(0, 0, 255, 0.06);
}
</style>