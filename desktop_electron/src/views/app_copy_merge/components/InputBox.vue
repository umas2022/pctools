<template>
    <div>
        <div class="input-in">
            输入路径：
            <el-input v-model="data_set.path_in" clearable></el-input>
        </div>
        <div class="input-out">
            输出路径：
            <el-input v-model="data_set.path_out" clearable></el-input>
        </div>
    </div>
</template>
<script setup>
import { inject } from "vue"
const data_set = inject("data_set")


</script>

<style lang="scss">
.el-input {
    width: 50%;
    padding: 10px;
}
</style>