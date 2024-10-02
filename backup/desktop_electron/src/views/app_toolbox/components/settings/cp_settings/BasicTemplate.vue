<template>
    <div class="cp-template">
        <!-- 上分割线 -->
        <div class="divider top" />

        <!-- 标签 -->
        <div class="label">
            <slot name="tp-label"></slot>
            <div class="info-icon">
                <useSvgIcon icon="info" color="black" :width="Number(20)" @click="state_change" />
            </div>
        </div>

        <!-- 控制 -->
        <div class="control">
            <slot name="tp-control"></slot>
        </div>

        <!-- 折叠info栏 -->
        <div class="info animate-box animate__animated animate__fadeOutDown" ref="info_ref">
            <slot name="tp-info"></slot>
        </div>
        <div class="info-blocker close animate-box animate__animated animate__fadeOut " @click="state_change"
            ref="blocker_ref"> </div>

        <!-- 下分割线 -->
        <div  class="divider bottom" />
    </div>
</template>
  
<script setup lang="ts">
import { onMounted, ref, inject } from "vue";
import useSvgIcon from "@/components/svgbox/useSvgIcon.vue";

const state_change_flag = ref(false)
const info_ref = ref<HTMLDivElement>()
const blocker_ref = ref<HTMLDivElement>()

const state_change = () => {
    state_change_flag.value = !state_change_flag.value

    if (state_change_flag.value) {
        info_ref.value!.classList.remove("animate__fadeOutDown")
        info_ref.value!.classList.add("animate__fadeInDown")
        info_ref.value!.classList.remove("close")
        info_ref.value!.style.zIndex = "2"
        blocker_ref.value!.classList.remove("animate__fadeOut")
        blocker_ref.value!.classList.add("animate__fadeIn")
        blocker_ref.value!.classList.remove("close")
    } else {
        info_ref.value!.classList.remove("animate__fadeInDown")
        info_ref.value!.classList.add("animate__fadeOutDown")
        setTimeout(() => {
            info_ref.value!.style.zIndex = "0"
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

div.cp-template {
    position: relative;
    height: 70px;
}

div.label {
    display: inline-block;
    text-align: right;
    width: 200px;
    position: absolute;
    right: 50%;
    top: calc(50% - 11px);
    z-index: 0;
    user-select: none; // 页面文字禁止被选中
    div.info-icon {
        display: inline-block;
        vertical-align: middle; // 垂直居中
        padding-left: 10px;
        padding-right: 20px;
        cursor: pointer;
        z-index: 2;
    }
}

div.control {
    display: flex;
    position: absolute;
    left: 50%;
    top: calc(50% - 15px);
    z-index: 0;
    user-select: none; // 页面文字禁止被选中
    width: calc(40% - 20px);

}

div.info {
    display: inline-block;
    position: absolute;
    background-color: rgba(255, 255, 255, 0.8);
    width: 500px;
    left: calc(50% - 250px);
    top: 50px;
    padding: 10px;
    border: solid 3px gray;
    border-radius: 15px;
}

div.info-blocker {
    position: fixed;
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

// 分隔线
div.divider {
    height: 3px;
    border-top: 3px solid rgba(0, 0, 0, 0.2);
    width: 80%;
    margin: 0 auto;

    &.bottom {
        border-top: 3px solid rgba(0, 0, 0, 0.4);
        position: absolute;
        bottom: 0px;
        left: 0;
        right: 0;
    }
}
</style>

  
  