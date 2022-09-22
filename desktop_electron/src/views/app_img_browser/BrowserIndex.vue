<template>
  <div class="main">
    <h1>
      img browser
      <div class="info-icon">
        <useSvgIcon
          icon="info"
          color="black"
          :width="Number(20)"
          @click="dialogVisible = !dialogVisible"
        />
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
    <!-- <el-button type="danger" @click="test_button">test_button</el-button> -->

    <!-- 参数输入栏 -->
    <InputForm />

    <!-- 单张图片展示 -->
    <SingleShow v-if="ready_flag" />
    <SingleFooter v-if="ready_flag" />

    <!-- 批处理函数 -->
    <BatchFunc v-if="ready_flag" />

    <!-- 瀑布流图片展示 -->
    <WaterfallLayout v-if="ready_flag" />

    <!-- 底部留白 -->
    <div class="block" style="height: 150px"></div>
  </div>
</template>

<script setup>
import { reactive, ref, provide, computed } from "vue";
import useSvgIcon from "@/components/use_svg/useSvgIcon.vue";
import InfoMain from "./components/InfoMain.vue";
import InputForm from "./components/InputForm.vue";
import SingleShow from "./components/SingleShow.vue";
import SingleFooter from "./components/SingleFooter.vue";
import WaterfallLayout from "./components/WaterfallLayout.vue";
import BatchFunc from "./components/BatchFunc.vue";

// help页弹窗控制
const dialogVisible = ref(false);

// 输入栏参数
const input_form = reactive({
  // path_browse: "D:\\s-samu\\apa\\nova",
  // path_save_list: [
  //   {
  //     path: "D:\\s-samu\\apa\\apa500-18",
  //     label: "apa500-18",
  //   },
  //   {
  //     path: "D:\\s-samu\\apa\\nova",
  //     label: "nova",
  //   },
  // ],
  path_browse: "C:\\Users\\umas\\OneDrive\\o-gallery\\壁纸2",
  path_save_list: [
    {
      path: "D:\\s-linux\\project\\test_file\\test_in",
      label: "o-1",
    },
    {
      path: "D:\\s-linux\\project\\test_file\\test_out",
      label: "o-2",
    },
  ],
});
const path_save_one = reactive({
  path: "",
  label: "",
});
provide("input_form", input_form);
provide("path_save_one", path_save_one);

// 图片参数
const img_form = reactive({
  // 所有图片完整路径列表
  img_list: [],
  // 当前展示的图片序号
  current_index: 0,
  // 被标记的图片 {序号:方法}
  marked_list: {},
});
provide("img_form", img_form);

// 图片是否读取完成flag
const ready_flag = computed(() => {
  return img_form.img_list.length > 0;
});
provide("ready_flag", ready_flag);

// 测试按钮
const test_button = () => {
  console.log(img_form.marked_list);
};
</script>

<style lang="scss" scoped>
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
</style>
