import { createRouter, createWebHashHistory, RouteRecordRaw } from "vue-router";
import HomeView from "../views/HomeView.vue";
import HelloWorld from "../views/test_hello_world/HelloIndex.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    alias: "/home",
    name: "home",
    meta: {
      hidden: false,
      name: "home",
    },
    component: () =>
      import("../views/app_home/HomeIndex.vue"),
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
