<template>
  <div class="main">
    <h1>Home</h1>
    <img src="static/img/home.gif" alt="" width="100">
    <div style="height:100%">
      <JsonPrototype :data=lowcode />
    </div>
  </div>
</template>

<script setup lang="ts">
import JsonPrototype from "@/components/json_prototype/JsonPrototype.vue"
const lowcode = require("./page_lowcode.json") 
</script>

<style lang="scss" scoped>
div.main {
  text-align: center;
  height: calc(100% - 199px);
}

</style>
