<template>
  <div class="app-main">
    <el-scrollbar>
      <GetList />
      <GetModule />
      <Interface />
    </el-scrollbar>

  </div>
</template>
<script setup lang="ts">
import GetList from "./cp_main/GetList.vue"
import GetModule from "./cp_main/GetModule.vue"
import Interface from "./cp_main/Interface.vue"

</script>
<style lang="scss" scoped>
div.app-main {
  height: 100vh;
  text-align: center;
  background-color: rgba(0, 0, 255, 0.05);
}
</style>