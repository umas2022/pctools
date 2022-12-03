<template>
  <div>
    <h3>问题</h3>
    <div class="each-line" v-for="(item, key) in info_data" :key="key">
      {{ item }}
    </div>
  </div>
</template>
<script setup>
import { ref } from "vue";
const info_data = ref([
  "目前卡在中文乱码",
]);
</script>
<style scoped lang = "scss">
div.each-line {
  padding: 10px;
}
</style>