<template>
  <div class="app-main">
    <AnimateDown :display="store_home.extract_display">
      <template #content>
        <GetList />
      </template>
    </AnimateDown>
    <GetModule />
    <Interface />
    <!-- 占位空白 -->
    <div class="block"></div>
  </div>
</template>
<script setup lang="ts">
import { inject } from "vue"
import GetList from "./cp_main/GetList.vue"
import GetModule from "./cp_main/GetModule.vue"
import Interface from "./cp_main/Interface.vue"
import AnimateDown from "@/components/animate_down/AnimateDown.vue"

const store_home: any = inject("store_home")

</script>
<style lang="scss" scoped>
div.app-main {
  height: 100%;
  text-align: center;
  background-color: rgba(0, 0, 255, 0.05);
}
div.block{
  height: 450px;
}
</style>