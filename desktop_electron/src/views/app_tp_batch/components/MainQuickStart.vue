<template>
  <div>
    <!-- 测试按钮 -->
    <!-- <el-button type="danger" plain @click="testbutton">test</el-button> -->

    快速选择：
    <el-select
      v-model="quickIndex"
      placeholder="选择"
      style="padding-right: 15px"
    >
      <el-option
        v-for="(item, index) in quickOptions"
        :key="item.value"
        :label="item.label"
        :value="index"
        @click="optionChange(index)"
      />
    </el-select>
    <!-- help文本 -->
    <div class="info-icon">
      <useSvgIcon
        icon="info"
        color="black"
        :width="Number(20)"
        @click="dialogVisible = !dialogVisible"
      />
    </div>
    <div v-if="dialogVisible" style="padding: 10px">
      {{ quickOptions[quickIndex]["info"] }}
    </div>
  </div>
</template>
<script setup>
import { inject, ref } from "@vue/runtime-core";
import useSvgIcon from "@/components/use_svg/useSvgIcon.vue";

// 所有参数
const form = inject("form");
const form_one = inject("form_one");
const form_head = inject("form_head")

// 所有预设值选项
const quick_form = inject("quick_form");
const quickOptions = quick_form.quick_options;
const first_key = Object.keys(quickOptions)[0];
const quickIndex = ref(first_key);
const optionChange = (index) => {
  let selectThis = quickOptions[index];
  form_head.terminal = selectThis.head.terminal
  form.value=[];
  for (let index = 0; index < selectThis.body.length; index++) {
    form.value.push(selectThis.body[index])
  }
};

// 显示help文本
const dialogVisible = ref(false);

// 测试按钮
const testbutton = () => {
  console.log("testbutton");
  console.log(form_head);
};
</script>

<style scoped lang="scss">
  div.main {
  text-align: center;
}
div.info-icon {
  display: inline-block;
  vertical-align: middle; // 垂直居中
  padding-left: 10px;
  padding-right: 20px;
  cursor: pointer;
}
</style>
