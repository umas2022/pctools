<template>
    <div class="cp-settings cp-port">
        <BasicTemplate>
            <!-- 标签 -->
            <template #tp-label>
                <span>开发模式端口</span>
            </template>

            <!-- 控制 -->
            <template #tp-control>
                <div style="display:inline-block;width: calc(80% - 50px);">
                    <el-input v-model="pre_port"></el-input>
                </div>
                <el-button  type="primary" plain @click="reset_port">修改</el-button>
            </template>

            <!-- 折叠info栏 -->
            <template #tp-info>
                <span class="line">1.开发模式：localhost:4091 / 生产模式：localhost:4090</span>
                <span class="line">2.调试时后端启动脚本可以接受一个端口号作为输入参数</span>
                <span class="line">3.后端改为前台启动之后,已经不再需要这个功能了,有时间改成手动输入端口号</span>
            </template>

        </BasicTemplate>
    </div>
</template>
<script setup lang="ts">
import { ref, inject } from "vue";
import { ElMessage } from "element-plus";
import BasicTemplate from "./BasicTemplate.vue"

const store_home:any = inject("store_home")

const pre_port = ref(JSON.parse(JSON.stringify(store_home.port)))

const reset_port = () => {
    store_home.port = pre_port
    localStorage.setItem("port",store_home.port)
    ElMessage.success("done")
};
</script>
