<template>
  <div style="padding: 10px">
    <!-- <el-button type="danger" @click="testbutton">testbutton</el-button> -->
    <!-- 动态引入组件 -->
    <component :is="cp_select" />
  </div>
</template>
<script setup>
import {
  computed,
  defineAsyncComponent,
  inject,
  ref,
  shallowRef,
  watch,
} from "@vue/runtime-core";

// 动态加载组件列表
const cp_list = {
  AddBlank: defineAsyncComponent(() => import("./AddBlank.vue")),
};

// 父组件传参
const props = defineProps({
  index: Number,
});

// 组件参数
const form = inject("form");
const form_options = inject("form_options");
const mode_select = computed(() => {
  try {
    return form_options.mode_options[form.value[props.index].method];
  } catch (e) {
    return "";
  }
});

const addons = computed(() => {
  if (mode_select.value == undefined) {
    return "AddBland";
  } else {
    return mode_select.value.addons == undefined ||
      mode_select.value.addons == ""
      ? "AddBlank"
      : mode_select.value.addons;
  }
});

// 选中的组件, 不能响应式更新, 在watch中手动更新
var cp_select = shallowRef(cp_list[addons.value]);

// 测试按钮
const testbutton = () => {
  console.log("testbutton");
  console.log(mode_select.value);
};

// 监听变化动态更新组件
watch(addons, () => {
  cp_select.value = cp_list[addons.value];
});
</script>
<style>
div.main {
  text-align: center;
}
</style>