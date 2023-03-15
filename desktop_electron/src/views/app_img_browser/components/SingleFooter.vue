<template>
  <div>
    <div class="show-name">
      <span v-if="img_form.img_list[0]"
        >name :
        {{ img_form.img_list[img_form.current_index].split("\\").at(-1) }}</span
      >
    </div>
    <div class="show-size">
      <span>size : {{ file_size }} mb</span>
      <span
        >dimension : {{ file_dimension.width }} x
        {{ file_dimension.height }}</span
      >
    </div>
    <div class="show-index">
      <span>current : {{ img_form.current_index + 1 }}</span>
      <span>total : {{ img_form.img_list.length }}</span>
      <span>goto :</span>
      <el-input style="width: 100px" v-model="input_index"></el-input>
      <el-button type="success" plain @click="goto_index">go</el-button>
    </div>
  </div>
</template>
<script setup>
import { inject, reactive, ref, watch } from "vue";
import { ElMessage } from "element-plus";

const fs = window.require("fs");
const sizeOf = window.require("image-size");
const img_form = inject("img_form");

// 文件大小
const file_size = ref(0);
const file_dimension = reactive({ height: 0, width: 0 });
watch(img_form, () => {
  let current_path = img_form.img_list[img_form.current_index];

  let stats = fs.statSync(current_path);
  file_size.value = stats.size;
  file_size.value = file_size.value / 1024 / 1024;
  file_size.value = file_size.value.toFixed(2);

  let dimensions = sizeOf(current_path);
  file_dimension.width = dimensions.width;
  file_dimension.height = dimensions.height;
});

// 跳转按钮
const input_index = ref("");
const goto_index = () => {
  if (input_index.value == "") {
    ElMessage({
      message: "please input index!",
      grouping: true,
      showClose: true,
      type: "error",
    });
  } else {
    if (!isNaN(input_index.value)) {
      if (
        input_index.value > 0 &&
        input_index.value <= img_form.img_list.length
      ) {
        img_form.current_index = input_index.value - 1;
      } else {
        ElMessage({
          message: "index out of range!",
          grouping: true,
          showClose: true,
          type: "error",
        });
      }
    } else {
      ElMessage({
        message: "index must be number!",
        grouping: true,
        showClose: true,
        type: "error",
      });
    }
  }
  console.log(typeof input_index.value);
};
</script>
<style scoped>
span {
  padding: 10px;
}
</style>