<template>
  <div class="show-log" :style="{ 'padding-bottom': boxPadding + 'px' }">
    <!-- <el-button @click="testbutton" type="danger">test</el-button> -->

    <!-- 主框体 -->
    <div class="show-log-body" :style="{ height: boxHeight + 'px' }">
      <el-card class="box-card">
        <!-- 头部 -->
        <template #header>
          <div class="card-header">
            <div>
              <span>max_rows:{{ maxrow }}</span>
            </div>

            <el-button
              class="button"
              type="danger"
              plain
              round
              @click="clearbox"
            >
              clear
            </el-button>
          </div>
        </template>
        <!-- 内容 -->
        <el-scrollbar
          :height="boxHeight - 130 + 'px'"
          ref="scrollbarRef"
          always
        >
          <div ref="innerRef">
            <div
              v-for="(line, index) in logtext"
              :key="index"
              class="text item"
            >
              {{ line }}
            </div>
          </div>
        </el-scrollbar>
      </el-card>
    </div>
    <!-- 高度调整条 -->
    <div
      class="show-log-resizer"
      @mousedown="resizeStart"
      @mouseup="resizeStop"
      @mouseleave="resizeStop"
      @click="resizeStop"
    >
      <el-icon :size="30"><arrow-down-bold /></el-icon>
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

onUpdated(()=>{
  gotoBottom()
})

// 鼠标拖动框高度
var rawHeight = 400;
var rawPadding = 1000;
const boxHeight = ref(rawHeight);
const boxPadding = ref(rawPadding);
var heightRec = 0;
const resizeFunc = (evt) => {
  let heightNow = evt.y;
  boxHeight.value = rawHeight + heightNow - heightRec;
};
const resizeStart = (evt) => {
  heightRec = evt.y;
  window.addEventListener("mousemove", resizeFunc);
};
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
  // gotoBottom()

  console.log(maxpos.value);

  maxpos.value = innerRef.value.clientHeight - 195;
  // scrollbarRef.value.setScrollTop(maxpos.value);
  console.log(maxpos.value);
};
</script>

<style lang="scss" scoped>
div.show-log {
  width: 100%;
}
.show-log-body {
  display: flex;
  justify-content: center;
}

.box-card {
  width: 70%;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.text {
  font-size: 14px; /* 字号大小 */
  text-align: left; /* 文字左对齐 */
  white-space: nowrap; // 文字不换行
}
.item {
  margin-bottom: 5px; /* 行距 */
}

.show-log-resizer {
  margin: auto;
  background-color: rgba(106, 106, 106, 0.23);
  border-radius: 5px;
  height: 30px;
  width: 100px;
}
.show-log-resizer:hover {
  /* cursor: s-resize; */
  cursor: pointer;
}
</style>
