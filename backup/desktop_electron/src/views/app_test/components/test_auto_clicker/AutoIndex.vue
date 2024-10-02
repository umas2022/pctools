<template>
  <div class="auto-main">
    <el-scrollbar>
      <h1>
        auto click
        <div class="info-icon">
          <useSvgIcon icon="info" color="black" :width="Number(20)" @click="dialogVisible = !dialogVisible" />
        </div>
      </h1>
      <h3>本页点击功能需要以管理员身份运行</h3>
      <h3>（界面先放一放, python功能先实现）</h3>

      <!-- help页弹窗 -->
      <el-dialog title="Info" v-model="dialogVisible" width="500px">
        <InfoMain />
        <template #footer>
          <span class="dialog-footer">
            <el-button @click="dialogVisible = false">关闭</el-button>
          </span>
        </template>
      </el-dialog>

      <!-- 环境检测 -->
      <div class="part">
        <EnvCheck style="border: solid red" />
      </div>
      <!-- 截图助手 -->
      <div class="part">
        <KitShotHelper style="border: solid blue" />
      </div>
      <!-- 对比助手 -->
      <div class="part">
        <KitCpHelper style="border: solid yellow" />
      </div>
      <!-- json录入 -->
      <div class="part">
        <ShowStep style="border: solid green" />
      </div>

      <div class="block" style="height: 150px"></div>
    </el-scrollbar>
  </div>
</template>
<script setup>
import { reactive, ref, provide, computed } from "vue";
import useSvgIcon from "@/components/svgbox/useSvgIcon.vue";
import InfoMain from "./components/InfoMain.vue";
import EnvCheck from "./components/EnvCheck.vue";
import ShowStep from "./components/ShowStep.vue";
import KitShotHelper from "./components/KitShotHelper.vue";
import KitCpHelper from "./components/KitCpHelper.vue";

// help页弹窗控制
const dialogVisible = ref(false);

</script>

<style lang="scss" scoped>
div.auto-main{
  text-align: center;
  height: 100%;
}
div.part {
  padding: 10px;
}

// info感叹号图标
div.info-icon {
  display: inline-block;
  vertical-align: middle; // 垂直居中
  padding-left: 10px;
  padding-right: 20px;
  cursor: pointer;
}
</style>