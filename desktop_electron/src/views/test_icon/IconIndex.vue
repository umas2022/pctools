<template>
  <div>
    <h1>icon test</h1>
    <h3>基本引入</h3>
    <useSvgIcon icon="info" color="black" :width="Number(20)" />
    <h3>点击旋转</h3>
    <use-svg-icon
      :class="[rotate_flag ? 'vertical' : 'horizontal']"
      @click="rotate_flag = !rotate_flag"
      icon="menu"
      color="black"
      :width="Number(35)"
    />
  </div>
</template>
<script setup>
import useSvgIcon from "@/components/use_svg/useSvgIcon.vue";
import { ref } from "@vue/reactivity";

const rotate_flag = ref(false);
</script>
<style scoped lang = "scss">

.horizontal{
  transition: all 1s;
}
.vertical{
  transform: rotate(-90deg);
  transition: all 1s;
}
</style>