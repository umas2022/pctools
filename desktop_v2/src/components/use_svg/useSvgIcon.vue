
<template>
  <div class="icon-div">
    <div class="inner">
      <!-- 使用方法 -->
      <!-- import useSvgIcon from "@/components/use_svg/useSvgIcon.vue"; -->
      <!-- <useSvgIcon icon="info" color="black" :width="Number(20)" /> -->
      <!-- 输入参数icon为public/static/svg文件夹下svg文件的名字 -->
      <!-- 颜色仅支持<style>列出的颜色 -->
      <img :src="svgPath" :width="svgWidth" :class="svgColorClass" />
    </div>
  </div>
</template>
<script lang="ts" setup>
import { computed } from "@vue/runtime-core";

// 父组件传参
const props = defineProps({
  icon: { type: String, required: true },
  width: { type: Number, default: 30 },
  color: { type: String, default: "black" },
});

// 拼接svg路径
const svgPath = computed(() => {
  return "static/svg/" + props.icon + ".svg";
});
// svg宽度
const svgWidth = computed(() => {
  return props.width;
});
// 颜色（仅支持style列出的颜色）
// filter计算网站：https://codepen.io/sosuke/pen/Pjoqqp
const svgColorClass = computed(() => {
  return "filter-" + props.color;
});

// 测试按钮
const testbutton = () => {
  console.log("props:", props.width);
};
</script>

<style scoped lang="scss">
// 外框样式
.icon-div {
  display: inline-block;
  .inner {
    display: flex;
  }
}
// 设置了默认1秒的变形过程
img {
  transition: all 1s;
}
// 可用颜色列表
.filter-green {
  filter: invert(48%) sepia(79%) saturate(2476%) hue-rotate(86deg)
    brightness(118%) contrast(119%);
}
.filter-black {
  filter: invert(0%) sepia(90%) saturate(7500%) hue-rotate(60deg)
    brightness(88%) contrast(112%);
}
.filter-white {
  filter: invert(98%) sepia(98%) saturate(0%) hue-rotate(311deg)
    brightness(101%) contrast(105%);
}
</style>