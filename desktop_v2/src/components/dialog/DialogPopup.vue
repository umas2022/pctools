<template>
    <div class="gcp-dialog">
        <!-- 显示信息 -->
        <div class="info close animate-box animate__animated animate__fadeOutDown" ref="info_ref">
            <div class="each-line" v-for="(item, key) in $props.data" style="padding:8px">
                {{ item }}
            </div>
            <slot name="content"></slot>
        </div>
        <!-- 深色背景 -->
        <div class="info-blocker close animate-box animate__animated animate__fadeOut " @click="state_change"
            ref="blocker_ref">
        </div>
    </div>
</template>
  
<script setup lang="ts">
import { ref, watch } from "vue";
import useSvgIcon from "@/components/svgbox/useSvgIcon.vue";

// 父组件传参
const props = defineProps<{
    data: Array<string>;
    display: boolean
}>();
watch(() => props.display, () => {
    state_change()
})

const state_change_flag = ref(false)
const info_ref = ref<HTMLDivElement>()
const blocker_ref = ref<HTMLDivElement>()

const state_change = () => {
    state_change_flag.value = !state_change_flag.value
    if (state_change_flag.value) {
        info_ref.value!.classList.remove("animate__fadeOutDown")
        info_ref.value!.classList.add("animate__fadeInDown")
        info_ref.value!.classList.remove("close")
        info_ref.value!.style.zIndex = "11"
        blocker_ref.value!.style.zIndex = "10"
        blocker_ref.value!.classList.remove("animate__fadeOut")
        blocker_ref.value!.classList.add("animate__fadeIn")
        blocker_ref.value!.classList.remove("close")
    } else {
        info_ref.value!.classList.remove("animate__fadeInDown")
        info_ref.value!.classList.add("animate__fadeOutDown")
        setTimeout(() => {
            info_ref.value!.style.zIndex = "0"
            blocker_ref.value!.style.zIndex = "0"
            info_ref.value!.classList.add("close")
        }, 800)
        blocker_ref.value!.classList.remove("animate__fadeIn")
        blocker_ref.value!.classList.add("animate__fadeOut")
        setTimeout(() => {
            blocker_ref.value!.classList.add("close")
        }, 800)
    }
}

</script>
  
<style scoped lang="scss">
@import 'animate.css';

div.gcp-dialog {
    // font-weight: lighter;
    font-weight: bold;
    font-size: 16px;
    text-align: left;
}


div.info {
    display: inline-block;
    position: absolute;
    background-color: rgba(255, 255, 255, 0.9);
    width: 500px;
    left: calc(50% - 250px);
    top: 50px;
    padding: 10px;
    border: solid 3px gray;
    border-radius: 15px;
}

div.info-blocker {
    position: fixed;
    height: 100%;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
    content: ' ';
    background: rgba(0, 0, 0, .2);
}

div.close {
    display: none;
}
</style>
  

  
  