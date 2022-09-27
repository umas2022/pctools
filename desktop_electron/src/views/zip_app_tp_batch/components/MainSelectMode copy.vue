<template>
  <div class="outer">
    <!-- <el-button type="danger" @click="testbutton">testbutton</el-button> -->
    <div class="select">
      <div class="select">
        方法：
        <el-select
          v-model="form[props.index].method"
          class="m-2"
          placeholder="Select"
          style="padding-right: 15px"
        >
          <el-option
            v-for="(item, index) in form_options.mode_options"
            :key="index"
            :label="item.label"
            :value="index"
            @click="option_change(index)"
          />
        </el-select>
        <div class="info-icon">
          <useSvgIcon
            icon="info"
            color="black"
            :width="Number(20)"
            @click="show_info = !show_info"
            style="cursor: pointer"
          />
        </div>
      </div>
    </div>

    <!-- 解释窗 -->
    <div class="info" v-if="show_info">
      <h5>{{ form_options.mode_options[form[props.index].method].commit }}</h5>
      <div class="inline left">
        <span class="escape">{{
          form_options.mode_options[form[props.index].method].example_in
        }}</span>
      </div>
      <div class="arrow inline">→</div>
      <div class="inline left">
        <span class="escape">{{
          form_options.mode_options[form[props.index].method].example_out
        }}</span>
      </div>
    </div>
  </div>
</template>
<script setup>
import { inject, onMounted, provide, ref, watch } from "@vue/runtime-core";
import useSvgIcon from "@/components/use_svg/useSvgIcon.vue";

// 父组件传参
const props = defineProps({
  index: Number,
});

// 按钮：是否显示说明
const show_info = ref(false);

// 组件参数：模式表单
const form = inject("form");
const form_options = inject("form_options");

// 选中的模式
const mode_select = form.value[props.index].method
provide("mode_select", mode_select);

// 选项切换触发，赋值组件参数mode_select
const option_change = (index) => {
  mode_select = form_options.mode_options[index];
};

// 初始选中0号
onMounted(() => {
  if (mode_select == "") {
    let first_key = Object.keys(form_options.mode_options)[0];
    form.value[props.index].method = first_key;
  }
});

// 测试按钮
const testbutton = () => {
  console.log("testbutton");
  console.log(mode_select);
};
</script>

<style lang="scss" scoped>
// 最外层
div.outer {
  padding: 10px;
}
// 空白
div.blank {
  width: 20px;
  height: 20px;
}
// 说明文本
span.escape {
  white-space: pre-wrap; //显示转义换行
}
// 箭头
div.arrow {
  padding: 0 30px 0 30px;
}
// info图标
div.info-icon {
  display: inline-block;
  vertical-align: middle; // 垂直居中
  height: 100%;
}

div.inline {
  display: inline-block;
}
div.left {
  text-align: left;
}
</style>