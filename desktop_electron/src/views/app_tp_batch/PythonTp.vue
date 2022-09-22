<template>
  <div>
    <h1>
      tp批处理（确保后端已经启动）
      <div class="info-icon">
        <useSvgIcon icon="info" color="black" :width="Number(20)" @click="dialogVisible = !dialogVisible" />
      </div>
    </h1>

    <!-- help页弹窗 -->
    <el-dialog title="Info" v-model="dialogVisible" width="500px">
      <InfoMain />
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="dialogVisible = false">关闭</el-button>
        </span>
      </template>
    </el-dialog>

    <!-- 测试按钮 -->
    <!-- <el-button type="danger" plain @click="testbutton">test</el-button> -->

    <!-- 快速选择 -->
    <MainQuickStart />

    <!-- 参数列表 -->
    <div style="padding:10px">
      <el-collapse style="width:80%;margin:auto">
        <el-collapse-item name="data_box">
          <template #title>
            <span style="margin:auto;width: 100%;">参数展开</span>
          </template>
          <div class="data-border" v-for="(item, index) in form" :key="index">
            <div class="data-box">
              <span v-if="form.length > 1" class="index-number">{{
              index + 1
              }}</span>
              <el-button v-if="form.length > 1" class="del" type="danger" plain @click="list_del(index)">del</el-button>
              <el-button class="add" type="primary" plain @click="list_add(index)">add</el-button>

              <!-- 输入路径 -->
              <MainPathInput :index="index" />

              <!-- 下拉选择：目标 -->
              <MainSelectTarget :index="index" />

              <!-- 下拉选择：模式 -->
              <MainSelectMode :index="index" />

              <!-- 下拉选择：输出 -->
              <MainSelectOutput :index="index" />

              <!-- 附加参数 -->
              <MainAddPara :index="index" />
            </div>
          </div>

          <!-- 开关选择：终端 -->
          <MainSwitchTerminal />

        </el-collapse-item>
      </el-collapse>
    </div>





    <!-- 发送请求 -->
    <MainWSconnect />

    <!-- log显示 -->
    <ShowLog :data="logprop" />
  </div>
</template>

<script  setup>
import { reactive, ref, provide } from "vue";
import useSvgIcon from "@/components/use_svg/useSvgIcon.vue";
// json config file
import mode_file from "./config_json/method.json";
import quick_file from "./config_json/quick.json";
import target_file from "./config_json/target.json";
import info_file from "./config_json/info.json";
import output_file from "./config_json/output.json";
//components
import MainPathInput from "./components/MainPathInput.vue";
import MainSelectMode from "./components/MainSelectMode.vue";
import MainSelectTarget from "./components/MainSelectTarget.vue";
import MainSelectOutput from "./components/MainSelectOutput.vue";
import MainSwitchTerminal from "./components/MainSwitchTerminal.vue";
import MainAddPara from "./components/MainAddPara.vue";
import MainWSconnect from "./components/MainWSconnect.vue";
import MainQuickStart from "./components/MainQuickStart.vue";
import InfoMain from "./components/InfoMain.vue";
import ShowLog from "@/components/show_log/ShowLog.vue";

// help页弹窗控制
const dialogVisible = ref(false);
const info_form = reactive({
  info_data: info_file.data,
});
provide("info_form", info_form);


// 后端log返回
const logprop = ref("");
provide("logprop", logprop);

// 快捷参数
const quick_form = reactive({
  quick_options: quick_file.data,
});
provide("quick_form", quick_form);

// 参数列表单个
const form_one = reactive({
  // 输入输出log路径
  path_in: "",
  path_out: "",
  log_path: "",

  // 目标参数
  target: "",

  // 模式参数
  method: "",

  // 输出参数
  output: "",

  // 附加参数 //暂时没有用到
  add_form: {
    para: "",
  },
});
provide("form_one", form_one);

// 参数列表可用值
const form_options = reactive({
  target_options: target_file.data,
  mode_options: mode_file.data,
  output_options: output_file.data,
});
provide("form_options", form_options);

// 总参数列表
const form = ref([form_one]);
provide("form", form);

// 独立参数
const form_head = reactive({
  // 是否使用终端
  terminal: false,
});
provide("form_head", form_head);

// 删除/添加按钮
const list_del = (index) => {
  form.value.splice(index, 1);
};
const list_add = (index) => {
  form.value.splice(index, 0, JSON.parse(JSON.stringify(form_one)));
};

// 测试按钮
const testbutton = () => {
  console.log(form_head);
};
</script>

<style scoped lang="scss">
  div.main {
  text-align: center;
}
// info感叹号图标
div.info-icon {
  display: inline-block;
  vertical-align: middle; // 垂直居中
  padding-left: 10px;
  padding-right: 20px;
  cursor: pointer;
}

//参数输入列表框
div.data-border {
  padding: 10px;
  position: relative;

  .data-box {
    width: 90%;
    margin: 0 auto;
    padding: 10px;
    box-shadow: 0 0 5px 5px rgb(240, 240, 240);
  }
}

// 参数框序号
span.index-number {
  color: rgba(128, 128, 128, 0.126);
  font-weight: bold; // 加粗
  font-size: 250px;
  position: absolute;
  display: flex;
  padding-left: 30px;
}

// delete按钮
.el-button.del {
  position: absolute;
  display: flex;
  right: calc(10% + 20px);
}

// add按钮
.el-button.add {
  position: absolute;
  display: flex;
  right: calc(10% + 20px);
  bottom: 20px+10px;
}
</style>


