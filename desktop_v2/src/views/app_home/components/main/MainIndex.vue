<template>
  <div class="app-main">
    <GetList />
    <GetModule />
    <Interface />
  </div>
</template>
<script setup lang="ts">
import GetList from "./cp_main/GetList.vue"
import GetModule from "./cp_main/GetModule.vue"
import Interface from "./cp_main/Interface.vue"

</script>
<style lang="scss" scoped>
div.app-main {
  text-align: center;
}
</style>