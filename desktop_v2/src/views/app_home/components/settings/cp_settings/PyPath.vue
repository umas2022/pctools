<template>
    <div>
        <div class="cp-path">
            <span>脚本路径</span>
            <div v-if="!modify_path_flag" style="display:inline-block;padding:10px">{{ store.py_path }}</div>
            <div v-else style="display:inline-block;padding:10px">
                <el-input v-model="store.py_path"></el-input>
            </div>
            <!-- info按钮 -->
            <div class="info-icon">
                <useSvgIcon icon="info" color="black" :width="Number(20)" @click="show_info_flag = !show_info_flag" />
            </div>

            <el-button v-if="!modify_path_flag" type="primary" plain @click="reset_path">修改</el-button>
            <el-button v-else type="primary" plain @click="reset_path">保存</el-button>

            <!-- 折叠info栏 -->
            <div class="info" v-if="show_info_flag">
                <span>python脚本位置 </span>
            </div>
            <!-- 分割线 -->
            <div style="width: 80%; margin: 0 auto">
                <el-divider></el-divider>
            </div>
        </div>
    </div>
</template>
<script setup>
import { onMounted, ref,inject,reactive } from "vue";
import useSvgIcon from "@/components/use_svg/useSvgIcon.vue";

const store = inject("store")

const show_info_flag = ref(false)
const modify_path_flag = ref(false)

const reset_path = () => {
    modify_path_flag.value = !modify_path_flag.value
    console.log(store.py_path)
};
</script>
<style lang="scss" scoped>
div.info-icon {
    display: inline-block;
    vertical-align: middle; // 垂直居中
    padding-left: 10px;
    padding-right: 20px;
    cursor: pointer;
}
</style>