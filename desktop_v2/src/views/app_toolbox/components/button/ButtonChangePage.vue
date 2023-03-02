<template>
    <div>
        <!-- 右上角设置按钮(齿轮) -->
        <el-tooltip class="box-item" effect="dark" content="参数设置" placement="bottom-end"
            v-if="store_home.current_page == 'home'">
            <div class="go-settings button" @click="state_change">
                <AnimateDown :display="store_home.current_page == 'home'">
                    <template #content>
                        <el-icon :size="30">
                            <Setting />
                        </el-icon>
                    </template>
                </AnimateDown>
            </div>
        </el-tooltip>

        <!-- 右上角返回主页按钮(右箭头) -->
        <el-tooltip class="box-item" effect="dark" content="返回主页" placement="bottom-end"
            v-if="store_home.current_page == 'setting'">
            <div class="go-home button" @click="state_change">
                <AnimateDown :display="store_home.current_page == 'setting'">
                    <template #content>
                        <el-icon :size="30">
                            <Right />
                        </el-icon>
                    </template>
                </AnimateDown>
            </div>
        </el-tooltip>
    </div>
</template>

<script setup lang="ts">
import { inject, ref } from "vue"
import AnimateDown from "@/components/animate_down/AnimateDown.vue"

const store_home: any = inject("store_home")

// 父组件传参
const props = defineProps<{
    main_index?: HTMLDivElement,
    setting_index?: HTMLDivElement
}>();

const state_change = () => {
    // 去设置页
    if (store_home.current_page == "home") {
        store_home.current_page = "setting"
        props.main_index!.classList.remove("animate__backInLeft")
        props.main_index!.classList.add("animate__backOutLeft")
        setTimeout(() => {
            props.main_index!.classList.add("close")
        }, 500)
        setTimeout(() => {
            props.setting_index!.classList.remove("close")
            props.setting_index!.classList.remove("animate__backOutRight")
            props.setting_index!.classList.add("animate__backInRight")
        }, 300)
    }
    // 去主页
    else {
        store_home.current_page = "home"
        props.setting_index!.classList.add("animate__backOutRight")
        props.setting_index!.classList.remove("animate__backInRight")
        setTimeout(() => {
            props.setting_index!.classList.add("close")
        }, 500)
        setTimeout(() => {
            props.main_index!.classList.add("animate__backInLeft")
            props.main_index!.classList.remove("animate__backOutLeft")
            props.main_index!.classList.remove("close")
        }, 300)
    }
    console.log(store_home.current_page)
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

// 右上角去设置按钮
div.go-settings :hover {
    background-color: rgba(255, 0, 0, 0.05);
}

// 右上角返回主页
div.go-home :hover {
    background-color: rgba(0, 0, 255, 0.05);
}

div.close {
  display: none;
}
</style>