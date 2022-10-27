<template>
  <div>
    <h3>还没实现的功能</h3>
    <div class="each-line" v-for="(item, key) in info_data" :key="key">
      {{ item }}
    </div>
  </div>
</template>
<script setup>
import { ref } from "vue";
const info_data = ref([
  "点击查看大图",
  "动作选择：复制/剪切/删除",
  "撤销",
  "多层文件夹",
  "预览列表",
  "键盘/鼠标滚轮操作",
  "删除已读",
  "添加网络源",
  "瀑布流考虑增加双层遮罩, 高位遮罩加载5张, 低位10张",
  "返回顶部",
  "瀑布流显示当前数量和进度"
]);
</script>
<style scoped lang = "scss">
div.each-line {
  padding: 10px;
}
</style>