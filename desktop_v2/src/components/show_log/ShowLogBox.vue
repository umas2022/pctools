<template>
    <div class="main-show-log">
        <!-- 右上角清空按钮 -->
        <div class="show-log-clear" @click="clearbox">
            <el-icon :size="20">
                <Brush />
            </el-icon>
        </div>
        <!-- 右上角最小化 -->
        <div class="show-log-mini" @click="setFixedHeight(30)">
            <!-- <el-icon :size="25">
                <arrow-down />
            </el-icon> -->
            <el-icon :size="25">
                <Minus />
            </el-icon>
        </div>
        <!-- 右上角最大化 -->
        <div class="show-log-max" @click="setFixedHeight(300)">
            <!-- <el-icon :size="25">
                <arrow-up />
            </el-icon> -->
            <el-icon :size="25">
                <Plus />
            </el-icon>
        </div>
        <!-- 底部高度调整条 -->
        <div class="show-log-resizer" @mousedown="resizeStart" @click="resizeStop"> </div>

        <!-- 主框体 -->
        <div class="show-log-body" :style="{ height: boxHeight + 'px' }">
            <!-- 内容 -->
            <el-scrollbar :height="boxHeight - 10 + 'px'" ref="scrollbarRef" always>
                <div ref="innerRef">
                    <div v-for="(line, index) in logtext" :key="index" class="text">
                        {{ line }}
                    </div>
                </div>
            </el-scrollbar>
        </div>
    </div>
</template>
  
<script lang="ts" setup>
import { ref, onMounted } from "vue";
import { onUpdated, watch } from "@vue/runtime-core";
import type { ElScrollbar } from "element-plus";

// 父组件传参
const props = defineProps<{
    data: string;
    // height需要带一个时间戳, 否则相同的data不能触发watch
    height: {
        data: number;
        time: number;
    };
}>();

// 显示文本
const logtext = ref(["log text here"]);
// 最大行数
const maxrow = ref(100);

// 清空按钮
const clearbox = () => {
    logtext.value = [];
};

// 滚动条位置控制始终在最下方
const scrollpos = ref(0);
const maxpos = ref(0);
const innerRef = ref<HTMLDivElement>();
const scrollbarRef = ref<InstanceType<typeof ElScrollbar>>();
const gotoBottom = () => {
    maxpos.value = innerRef.value!.clientHeight - 185;
    scrollbarRef.value!.setScrollTop(maxpos.value);
};
// 监听传参变化, 刷新文本显示和滚动条位置
watch(() => props.data, () => {
    // 数组合并
    logtext.value.push(...JSON.parse(props.data))
    while (logtext.value.length > maxrow.value) {
        logtext.value.shift();
    }
    gotoBottom();
}, { deep: true });

// 组件更新时触发：滚动至底部
onUpdated(() => {
    gotoBottom()
})

// 鼠标拖动框高度
var rawHeight = 30;
const boxHeight = ref(rawHeight);
// 记录初始高度
var heightRec = 0;
// 鼠标拖动设定高度
const resizeFunc = (evt: MouseEvent) => {
    // 当前高度
    let heightNow = evt.y;
    boxHeight.value = rawHeight + (heightNow - heightRec);
    const body_div = document.querySelector<HTMLElement>(".show-log-body")!
    if (body_div) {
        body_div.style.cssText += " transition: 0s"
    }
};
// 鼠标拖动高度初始化
const resizeStart = (evt: MouseEvent) => {
    heightRec = evt.y;
    window.addEventListener("mousemove", resizeFunc);
};
// 停止鼠标拖动高度改变
const resizeStop = () => {
    rawHeight = boxHeight.value;
    window.removeEventListener("mousemove", resizeFunc);
    const body_div = document.querySelector<HTMLElement>(".show-log-body")!
    if (body_div) {
        body_div.style.cssText += " transition: 0.5s"
    }
};
// 直接设定高度
const setFixedHeight = (height: number) => {
    boxHeight.value = height
    rawHeight = height
}

// 监听传参变化, 刷新窗口高度
watch(() => props.height, () => {
    // 数组合并
    setFixedHeight(props.height.data)
    gotoBottom();
}, { deep: true });

// // 监听高度变化, 高度太小时直接触发结束
// watch(boxHeight, () => {
//     if (boxHeight.value < 100) {
//         resizeStop();
//     }
// });

onMounted(() => {
    document.onmouseup = () => {
        resizeStop()
    }
})

// 测试按钮
const testbutton = () => {
    console.log("testbutton at ShowLog");
    console.log(maxpos.value);
};
</script>
  
<style lang="scss" scoped>
// 最外层
div.main-show-log {
    position: relative;
    width: 100%;
    bottom: 0;

    div.show-log-body {
        padding-left: 5px;
        border: 2px solid rgba(128, 128, 128, 0.342);
        background-color: rgba(255, 255, 255, 0.788);
        border-radius: 5px;
        transition: 0.5s;
    }
}

// 框内文字
div.text {
    font-size: 14px; // 字号大小 
    text-align: left; // 文字左对齐
    white-space: nowrap; // 文字不换行
    margin-bottom: 5px;
}



// 清空按钮
.show-log-clear {
    position: absolute;
    z-index: 2;
    right: 15px;
    background-color: rgba(0, 55, 255, 0.171);
    border-radius: 5px;
    height: 30px;
    width: 30px;
    cursor: pointer;

    .el-icon {
        padding-top: 3px;
    }
}

// 最小化按钮
.show-log-mini {
    position: absolute;
    z-index: 2;
    right: 50px;
    background-color: rgba(106, 106, 106, 0.23);
    border-radius: 5px;
    height: 30px;
    width: 30px;
    cursor: pointer;

    .el-icon {
        padding-top: 3px;
    }
}

// 最大化按钮
.show-log-max {
    position: absolute;
    z-index: 2;
    right: 85px;
    background-color: rgba(106, 106, 106, 0.23);
    border-radius: 5px;
    height: 30px;
    width: 30px;
    cursor: pointer;

    .el-icon {
        padding-top: 2px;
    }
}

// 尺寸拖动条
.show-log-resizer {
    position: absolute;
    bottom: -10px;
    right: calc(50% - 150px);
    z-index: 2;
    background-color: rgba(106, 106, 106, 0.23);
    border-radius: 5px;
    height: 10px;
    width: 300px;
    transform: rotate(180deg);
    cursor: n-resize;

    .el-icon {
        top: 0px;
    }
}
</style>
  