<template>
    <div>
        <!-- 右上角切换背景按钮(刷新) -->
        <el-tooltip class="box-item" effect="dark" content="切换背景" placement="bottom-end">
            <div class="change-bg button" @click="change_bg">
                <AnimateDown :display="store_home.current_page == 'home'">
                    <template #content>
                        <el-icon :size="30">
                            <Refresh />
                        </el-icon>
                    </template>
                </AnimateDown>
            </div>
        </el-tooltip>
    </div>
</template>

<script setup lang="ts">
import { inject } from "vue"
import AnimateDown from "@/components/animate_down/AnimateDown.vue"

const store_home: any = inject("store_home")

const change_bg = () => {
    store_home.bg_num += 1
    if (store_home.bg_num == 33) {
        store_home.bg_num = 1
    }
}

</script>

<style lang="scss">
// 右上角按钮统一格式
div.button {
    cursor: pointer;

    :hover {
        border-radius: 5px;
    }
}

// 右上角切换背景按钮
div.change-bg :hover {
    background-color: rgba(255, 191, 0, 0.2);
}
</style>