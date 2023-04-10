<template>
    <div class="cp-path">
        <BasicTemplate>
            <!-- 标签 -->
            <template #tp-label>
                <span>修改脚本路径</span>
            </template>

            <!-- 控制 -->
            <template #tp-control>
                <div style="display:inline-block;width: calc(80% - 50px);">
                    <el-input v-model="pre_path"></el-input>
                </div>
                <el-button type="primary" plain @click="reset_path">修改</el-button>
            </template>

            <!-- 折叠info栏 -->
            <template #tp-info>
                <span class="line">1.手动设置python脚本路径</span>
                <span class="line">2.路径定位到py_script文件夹</span>
                <span class="line">3.默认通过static_path函数自动定位到打包后的public路径下</span>
                <span class="line">4.当前: {{ store_home.py_path }}</span>
            </template>

        </BasicTemplate>

    </div>
</template>
<script setup lang="ts">
import { ref, inject } from "vue";
import BasicTemplate from "./BasicTemplate.vue"
import { ElMessage } from "element-plus";

const store_home: any = inject("store_home")


const pre_path = ref(JSON.parse(JSON.stringify(store_home.py_path)))

const reset_path = () => {
    store_home.py_path = pre_path
    ElMessage.success("done")
};
</script>
