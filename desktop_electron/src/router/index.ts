import { createRouter, createWebHashHistory, RouteRecordRaw } from "vue-router";
import HomeView from "../views/HomeView.vue";
import HelloWorld from "../views/test_hello_world/HelloIndex.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    alias: "/toolbox",
    name: "toolbox",
    meta: {
      hidden: false,
      name: "toolbox",
    },
    component: () =>
      import("../views/app_toolbox/HomeIndex.vue"),
  },
  {
    path: "/test",
    name: "test",
    meta: {
      hidden: false,
      name: "test",
    },
    component: () =>
      import("../views/app_test/TestIndex.vue"),
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
