<template>
    <div class="cp-backend">
        <BasicTemplate>
            <!-- 标签 -->
            <template #tp-label>
                <span>开发日志</span>
            </template>

            <!-- 控制 -->
            <template #tp-control>
                <el-button type="primary" plain @click="info_display = !info_display">看</el-button>
            </template>

            <!-- 折叠info栏 -->
            <template #tp-info>
                <span class="line">1.develop.md</span> <br>
                <span class="line">2.在打包的python脚本中将md转换为html,保存在public中</span> <br>
                <span class="line">3.直接读取md文件的尝试都失败了</span> <br>
            </template>

        </BasicTemplate>

        <!-- 全局info弹窗显示开发日志 -->
        <DialogPopup :data="['']" :display="info_display">
            <template #content>
                <object :data="html_path" type="text/html" style="width:100%;height:calc( 100vh - 150px )"></object>
            </template>
        </DialogPopup>

    </div>

</template>
<script setup lang="ts">
import { ref } from "vue"
import { static_path } from "@/utils/utils_path.js"
import BasicTemplate from "./BasicTemplate.vue"
import DialogPopup from "@/components/dialog/DialogPopup.vue"
const path = window.require("path");


const html_path = ref(path.join(static_path(), "info/develop.html"))


// 窗口显示控制
const info_display = ref(false)
</script>
