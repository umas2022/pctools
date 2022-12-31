<template>
    <div class="cp-animate  animate__animated animate__backInDown" ref="ani_ref">
        <slot name="content"></slot>
    </div>
</template>
<script setup lang="ts">
import { ref, watch,onMounted } from "vue";
// 父组件传参
const props = defineProps<{
    display: boolean
}>();

// 组件ref
const ani_ref = ref<HTMLDivElement>()

// 初始状态
onMounted(()=>{
    if(!props.display){
        ani_ref.value!.classList.add("close")
    }
})

// 触发状态切换
watch(() => props.display, () => {
    state_change()
})


const state_change = () => {
    if (props.display) {
        ani_ref.value!.classList.remove("animate__backOutUp")
        ani_ref.value!.classList.add("animate__backInDown")
        ani_ref.value!.classList.remove("close")
        ani_ref.value!.style.zIndex = "11"
    } else {
        ani_ref.value!.classList.remove("animate__backInDown")
        ani_ref.value!.classList.add("animate__backOutUp")
        setTimeout(() => {
            ani_ref.value!.style.zIndex = "0"
            ani_ref.value!.classList.add("close")
        }, 800)
    }
}
</script>


<style scoped lang="scss">
@import 'animate.css';
// div.cp-animate {
//     border: solid 3px red;
// }
div.close {
    display: none;
}
</style>

