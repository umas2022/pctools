<template>
  <div class="main-frame">
    <div class="menu" v-if="store_frame.show_nav">
      <div class="ctrl-icon" >
        <use-svg-icon class="svg" :class="[rotate_flag ? 'vertical' : 'horizontal']"
          :style="{ padding: svg_padding + 'px' }" @click="click_show" icon="menu" color="black" :width="svg_size" />
      </div>
      <div style="height:50px"></div>
      <PartMenu v-if="show_header" />
    </div>

    <div class="body" @click="test_button">
      <PartBody />
    </div>
  </div>
</template>

<script  setup lang="ts">
import { ref, reactive, provide, onMounted } from "vue";
import useSvgIcon from "@/components/svgbox/useSvgIcon.vue";
import PartMenu from "./components/PartMenu.vue";
import PartBody from "./components/PartBody.vue";

// 默认打开header
const show_header = ref(false);
// 默认不旋转菜单按钮
const rotate_flag = ref(true);
// 菜单初始宽度(5px边框)
const menu_width = ref(5);
// 菜单图标的尺寸
const svg_size = ref(15);
const svg_padding = ref(2);

// 点击事件
// 如果不加区分直接用三元表达式取反, 点击过快时setTimeout中的取反会被跳过
const click_show = () => {
  // 关闭menu
  if (show_header.value) {
    show_header.value = false;
    rotate_flag.value = true;
    menu_width.value = 5;
    svg_size.value = 15;
    svg_padding.value = 2;
  }
  // 打开menu
  else {
    setTimeout(() => {
      show_header.value = true;
    }, 1000);
    rotate_flag.value = false;
    menu_width.value = 200;
    svg_size.value = 35;
    svg_padding.value = 6;
  }
};

// frame全局变量仓库
const store_frame = reactive({
  // 是否显示左上角导航按钮
  show_nav: false
})
provide("store_frame", store_frame)


onMounted(() => {
  let path = window.location.hash
  if (path != "#/") {
    store_frame.show_nav = true
  }
})

// 测试按钮
const test_button = () => {
}
</script>

<style lang="scss" scoped>
div.main-frame {
  position: relative;
}

//左上角按钮
div.ctrl-icon {
  position: absolute;
  left: 5px;
  z-index: 2;
  cursor: pointer;

  .svg {
    background-color: rgba(128, 128, 128, 0);
    border-radius: 30px;
  }

  .horizontal {
    transform: rotate(180deg);
    transition: all 1s;
  }

  .vertical {
    transform: rotate(-90deg);
    transition: all 1s;
  }
}

// 左侧菜单栏
div.menu {
  background-color: rgba(128, 128, 128, 0.2);
  box-sizing: border-box;
  border-right: 5px solid rgba(0, 0, 0, 0.1);
  border-radius: 5px;
  transition: all 1s;
  height: calc(100vh - 15px);
  width: calc(1px * v-bind(menu_width));
  float: left;
  overflow-y: hidden;
  overflow-x: hidden;
}


// 右侧主体
div.body {
  background-color: rgba(255, 255, 255, 0);
  transition: all 1s;
  height: calc(100vh - 15px);
  width: calc(100% - 1px * v-bind(menu_width));
  float: left;
  overflow-y: hidden;
  overflow-x: hidden;

}
</style>

<!-- 全局style -->
<style lang="scss">
* {
  user-select: none; // 页面文字禁止被选中
}
</style>
