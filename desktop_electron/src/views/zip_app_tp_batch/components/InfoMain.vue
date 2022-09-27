<template>
  <div>
    <div class="each-line" v-for="(item, key) in info_data" :key="key">{{ item }}</div>
  </div>
</template>
<script setup>
import { inject } from "@vue/runtime-core";

const info_form = inject("info_form");
const info_data = info_form.info_data.main.data;
</script>
<style scoped lang = "scss">
div.each-line{
  padding: 10px;
}
</style>