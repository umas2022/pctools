<template>
  <div class="outer">
    <!-- <el-button type="danger" @click="testbutton">testbutton</el-button> -->
    <!-- 第一行：目标、路径显示 -->
    <div class="select">
      <div class="input-row">
        <span class="input-item">
          目标：
          <el-select
            v-model="form[props.index].target"
            placeholder="Select"
            allow-create
            filterable
          >
            <el-option
              v-for="item in targetArr"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            />
          </el-select>
        </span>
      </div>
    </div>
  </div>
</template>
<script setup>
import { inject, onMounted, ref, watch } from "@vue/runtime-core";
import useSvgIcon from "@/components/use_svg/useSvgIcon.vue";

// 父组件传参
const props = defineProps({
  index: Number,
});

// 按钮：是否显示说明
const show_info = ref(false);

// 组件参数：目标表单
const form = inject("form");
const form_options = inject("form_options");

// 所有目标类型
const targetArr = form_options.target_options;

// 初始选中0号
onMounted(() => {
  if (form.value[props.index].target == "") {
    let first_key = Object.keys(targetArr)[0];
    form.value[props.index].target = targetArr[first_key].value;
  }
});

// 测试按钮
const testbutton = () => {
  console.log("testbutton");
  form[props.index].value.target = ".txt";
};
</script>

<style lang="scss" scoped>
// 最外层
div.outer {
  padding: 10px;
}
</style>