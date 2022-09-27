<template>
  <div class="outer">
    <div class="input-item">
      使用终端：
      <el-switch v-model="form_head.terminal" />
    </div>
  </div>
</template>
<script setup>
import { inject, onMounted, ref, watch } from "@vue/runtime-core";
import useSvgIcon from "@/components/use_svg/useSvgIcon.vue";

const form_head = inject("form_head");

</script>

<style lang="scss" scoped>
.el-input {
  width: 50%;
  padding: 10px;
}
</style>