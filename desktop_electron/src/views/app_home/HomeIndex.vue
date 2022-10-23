<template>
  <div class="main">
    <h1>Home</h1>
    <div style="height:100%">
      <JsonPrototype :data=lowcode >
        <template #bottom>
          <img src="static/img/home.gif" alt="" width="100" style="padding:30px">
        </template>
      </JsonPrototype>
    </div>
  </div>
</template>

<script setup lang="ts">
import JsonPrototype from "@/components/json_prototype_v2/JsonPrototypeV2.vue"
const lowcode = require("./page_lowcode.json") 
</script>

<style lang="scss" scoped>
div.main {
  text-align: center;
  height: calc(100% - 90px);
}

</style>
