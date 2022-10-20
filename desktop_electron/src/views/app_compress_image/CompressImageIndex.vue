<template>
    <div style="height:100%">
        <JsonPrototype :data=lowcode />
    </div>
</template>
<script setup lang="ts">
import JsonPrototype from "@/components/json_prototype_v2/JsonPrototypeV2.vue"
const lowcode = require("./page_lowcode.json") 
</script>