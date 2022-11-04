<template>
  <!-- 在App.vue中引用  -->
  <div class="main-menu">
    <el-scrollbar>
      <el-menu class="el-menu-vertical-demo" background-color="rgba(255, 255, 255, 0)"
        active-text-color="rgba(0, 0, 255, 0.5)" @select="handleSelect" router>
        <template v-for="(item, index) in routers">
          <template v-if="item.meta.hidden == false">
            <!-- 一级路由 -->
            <el-menu-item class="single" :key="index" :index="item.path" v-if="item.children == undefined">
              <h3>{{ item.meta.name }}</h3>
            </el-menu-item>

            <!-- 多级路由 -->
            <el-sub-menu class="multi" :key="index+1" :index="item.path" v-else>
              <template #title><h3>{{ item.meta.name }}</h3></template>
              <el-menu-item v-for="(item, index) in item.children" :key="index" :index="item.path">
                <h3>{{ item.meta.name }}</h3>
              </el-menu-item>
            </el-sub-menu>
          </template>
        </template>
      </el-menu>
    </el-scrollbar>
  </div>
</template>

<script  setup>
import { reactive } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();
const routers = reactive(router.options.routes);

const handleSelect = (key, keyPath) => {
  console.log(key, keyPath);
};
</script>
<style lang="scss" scoped>
div.main-menu {
  height: calc(100vh - 80px);
}

.single {
  border-bottom: 2px solid rgba(0, 0, 0, 0.187);
  border-radius: 10px;
}

.el-sub-menu {
  border-bottom: 2px solid rgba(0, 0, 0, 0.187);
  border-radius: 10px;
}
</style>
