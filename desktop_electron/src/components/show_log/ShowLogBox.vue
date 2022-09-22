<template>
    <div class="main-show-log">
        <!-- 右上角清空按钮 -->
        <div class="show-log-clear" @click="clearbox">
            <el-icon :size="20">
                <el-icon>
                    <Brush />
                </el-icon>
            </el-icon>
        </div>
        <!-- 右上角高度调整条 -->
        <div class="show-log-resizer" @mousedown="resizeStart" @mouseup="resizeStop" @mouseleave="resizeStop"
            @click="resizeStop">
            <el-icon :size="30">
                <arrow-down-bold />
            </el-icon>
        </div>

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
import { ref } from "@vue/reactivity";
import { onUpdated, watch } from "@vue/runtime-core";
import type { ElScrollbar } from "element-plus";

// 父组件传参
const props = defineProps<{
    data: string;
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
    maxpos.value = innerRef.value.clientHeight - 195;
    scrollbarRef.value.setScrollTop(maxpos.value);
};
// 监听传参变化，刷新文本显示和滚动条位置
watch(props, () => {
    logtext.value.push(props.data);
    if (logtext.value.length > maxrow.value) {
        logtext.value.shift();
    }
    gotoBottom();
});

onUpdated(() => {
    gotoBottom()
})

// 鼠标拖动框高度
var rawHeight = 200;
const boxHeight = ref(rawHeight);
// 记录初始高度
var heightRec = 0;
// 高度重设
const resizeFunc = (evt) => {
    let heightNow = evt.y;
    boxHeight.value = rawHeight - heightNow + heightRec;
    console.log(heightNow)
};
// 高度初始化
const resizeStart = (evt) => {
    heightRec = evt.y;
    window.addEventListener("mousemove", resizeFunc);
};
// 停止高度改变
const resizeStop = () => {
    rawHeight = boxHeight.value;
    window.removeEventListener("mousemove", resizeFunc);
};
// 监听高度变化，高度太小时直接触发结束
watch(boxHeight, () => {
    if (boxHeight.value < 100) {
        resizeStop();
    }
});

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
    }
}

// 框内文字
div.text {
    font-size: 14px; // 字号大小 
    text-align: left; // 文字左对齐
    white-space: nowrap; // 文字不换行
    margin-bottom: 5px;
}

// 尺寸拖动条
.show-log-resizer {
    position: absolute;
    z-index: 2;
    right: 50px;
    background-color: rgba(106, 106, 106, 0.23);
    border-radius: 5px;
    height: 30px;
    width: 100px;
    transform: rotate(180deg);
    cursor: pointer;
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
</style>
  