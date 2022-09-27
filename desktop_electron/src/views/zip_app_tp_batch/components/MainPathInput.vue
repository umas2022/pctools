<template>
  <div class="outter">
    <!-- <el-button type="danger" plain @click="testbutton">test</el-button> -->
    <div class="input-in">
      输入路径：
      <el-input v-model="form[props.index]['path_in']" clearable></el-input>
    </div>
    <div class="input-out">
      输出路径：
      <el-input v-model="form[props.index]['path_out']" clearable></el-input>
    </div>
    <div class="input-out">
      log路径 ：
      <el-input
        v-model="form[props.index]['log_path']"
        placeholder="置空不使用log文件"
        clearable
      ></el-input>
    </div>
  </div>
</template>
<script setup>
import { inject, onMounted } from "@vue/runtime-core";

// 父组件传参
const props = defineProps({
  index: Number,
});

const form = inject("form");

const testbutton = () => {
  console.log("testbutton");
  console.log(props.index);
};

onMounted(() => {
  if (form.value[props.index]["path_in"] == "") {
    form.value[props.index]["path_in"] = "D:/s-linux/project/test_file/test_in";
  }
  if (form.value[props.index]["path_out"] == "") {
    form.value[props.index]["path_out"] = "D:/s-linux/project/test_file/test_out";
  }

});
</script>

<style scoped>
  div.main {
  text-align: center;
}
div.outter {
  padding: 10px;
}
.el-input {
  width: 50%;
  padding: 10px;
}
</style>