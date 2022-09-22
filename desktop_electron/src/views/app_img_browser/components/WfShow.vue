<template>
  <div class="main">
    <!-- 图片 -->
    <div
      class="img"
      @mouseenter="show_bar = true"
      @mouseleave="show_bar = false"
    >
      <img :width="option.img_width" :src="option.img_src" />
    </div>
    <!-- 标记栏 -->
    <div
      class="mark-bar"
      v-show="show_bar"
      @mouseenter="show_bar = true"
      @mouseleave="show_bar = false"
    >
      <div class="mark" v-for="(item, index) in input_form.path_save_list">
        <el-button type="success" @click="mark_this(index)">{{
          item.label
        }}</el-button>
      </div>
      <!-- 测试按钮 -->
      <!-- <el-button type="danger" @click="test_button">test_button</el-button> -->
    </div>
    <!-- 标记遮罩层 -->
    <div class="mask" v-if="mark_flag">
      <span>{{ mark_index }}</span>
    </div>
  </div>
</template>
<script setup>
import { ref, onMounted, watch } from "vue";

// 父组件传参
const props = defineProps({
  option: Object,
});
const option = ref(props.option);
const img_form = option.value.img_form;
const input_form = option.value.input_form;

// 显示/隐藏底部按钮
const show_bar = ref(false);

// mark
const mark_flag = ref(false);
const mark_index = ref(0);
const mark_this = (destination) => {
  mark_flag.value = !mark_flag.value;
  mark_index.value = destination + 1;

  if (mark_flag.value) {
    img_form.marked_list[option.value.img_index] = destination;
  } else {
    delete img_form.marked_list[option.value.img_index];
  }
};

// 测试按钮
const test_button = () => {
  console.log(option.value);
};
</script>
<style scoped lang="scss">
div.main {
  width: 100%;
  background-color: rgba(0, 0, 255, 0.187);
  position: relative;
  div.img {
    position: relative;
    z-index: 1;
  }
  //   标记按钮栏
  div.mark-bar {
    position: absolute;
    display: inline-block;
    bottom: 0;
    left: 0;
    z-index: 3;
    div.mark {
      display: inline-block;
      padding: 5px;
    }
  }
  //   遮罩层
  div.mask {
    position: absolute;
    // display: inline-block;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 255, 0.361);
    z-index: 2;
    vertical-align: middle;
    span {
      // color: rgba(128, 128, 128, 0.126);
      color: rgb(255, 0, 0);
      font-weight: bold; // 加粗
      font-size: 100px;
      position: relative;
      top: calc(50% - 80px);
    }
  }
}
</style>