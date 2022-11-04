<template>
    <div class="cp-path">
        <BasicTemplate>
            <!-- 标签 -->
            <template #tp-label>
                <span>脚本路径</span>
            </template>

            <!-- 控制 -->
            <template #tp-control>
                <el-button v-if="!modify_path_flag" type="primary" plain @click="reset_path">修改</el-button>
                <el-button v-else type="primary" plain @click="reset_path">保存</el-button>
                <div v-if="!modify_path_flag" style="display:inline-block;padding:10px">
                     <span style="font-size:small">{{ store.py_path }}</span>
                </div>
                <div v-else style="display:inline-block;padding:10px">
                    <el-input v-model="store.py_path"></el-input>
                </div>
            </template>

            <!-- 折叠info栏 -->
            <template #tp-info>
                <span>python脚本位置: {{ store.py_path }}</span>
            </template>

        </BasicTemplate>

    </div>
</template>
<script setup>
import { onMounted, ref, inject, reactive } from "vue";
import BasicTemplate from "./BasicTemplate.vue"

const store = inject("store")

const modify_path_flag = ref(false)

const reset_path = () => {
    modify_path_flag.value = !modify_path_flag.value
    console.log(store.py_path)
};
</script>
