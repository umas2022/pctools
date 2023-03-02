<template>
    <div>
        <!-- 右上角展开按钮(加号) -->
        <el-tooltip class="box-item" effect="dark" content="目录展开" placement="bottom-end">
            <div class="extract button" @click="extract_change">
                <AnimateDown :display="store_home.current_page == 'home'">
                    <template #content>
                        <AnimateDown :display="!store_home.extract_display">
                            <template #content>
                                <el-icon :size="30">
                                    <Plus />
                                </el-icon>
                            </template>
                        </AnimateDown>
                    </template>
                </AnimateDown>
            </div>
        </el-tooltip>
        <!-- 右上角折叠按钮(减号) -->
        <el-tooltip class="box-item" effect="dark" content="目录折叠" placement="bottom-end">
            <div class="extract button" @click="extract_change">
                <AnimateDown :display="store_home.current_page == 'home'">
                    <template #content>
                        <AnimateDown :display="store_home.extract_display">
                            <template #content>
                                <el-icon :size="30">
                                    <Minus />
                                </el-icon>
                            </template>
                        </AnimateDown>
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

// 内容折叠
const extract_change = () => {
    store_home.extract_display = !store_home.extract_display
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

// 右上角展开按钮
div.extract :hover {
    background-color: rgba(0, 255, 0, 0.1);
}
</style>