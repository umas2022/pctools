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

  // 拷贝功能合集
  {
    path: "/copy",
    name: "copy",
    meta: {
      hidden: false,
      name: "-拷贝-",
    },
    component: () => import("../views/frame_copy/CopyIndex.vue"),
    children: [
      // 应用：拷贝合并
      {
        path: "/merge",
        name: "merge",
        meta: {
          hidden: false,
          name: "拷贝合并√",
        },
        component: () =>
          import("../views/app_copy_merge/CopyMergeIndex.vue"),
      },
      // 应用：完全备份
      {
        path: "/backup",
        name: "backup",
        meta: {
          hidden: false,
          name: "完全备份",
        },
        component: () =>
          import("../views/app_copy_merge/CopyMergeIndex.vue"),
      },
      // 应用：拷贝检查
      {
        path: "/check",
        name: "check",
        meta: {
          hidden: false,
          name: "拷贝检查",
        },
        component: () =>
          import("../views/app_copy_merge/CopyMergeIndex.vue"),
      }
    ]
  },
  // 压缩功能合集
  {
    path: "/compress",
    name: "compress",
    meta: {
      hidden: false,
      name: "-压缩-",
    },
    component: () => import("../views/frame_compress/CompressIndex.vue"),
    children: [
      // 应用：视频压缩
      {
        path: "/video",
        name: "video",
        meta: {
          hidden: false,
          name: "视频压缩",
        },
        component: () =>
          import("../views/app_compress_video/CompressVideoIndex.vue"),
      },
      // 应用：图片压缩
      {
        path: "/image",
        name: "image",
        meta: {
          hidden: false,
          name: "图片压缩",
        },
        component: () =>
          import("../views/app_compress_video/CompressVideoIndex.vue"),
      }
    ]
  },
  // 删除功能合集
  {
    path: "/remove",
    name: "remove",
    meta: {
      hidden: false,
      name: "-删除-",
    },
    component: () => import("../views/frame_remove/RemoveIndex.vue"),
    children: [
      // 应用：删除差异
      {
        path: "/difference",
        name: "difference",
        meta: {
          hidden: false,
          name: "删除差异",
        },
        component: () =>
          import("../views/app_remove_difference/RemoveDifferenceIndex.vue"),
      },
      // 应用：删除后缀
      {
        path: "/suffix",
        name: "suffix",
        meta: {
          hidden: false,
          name: "删除后缀",
        },
        component: () =>
          import("../views/app_remove_difference/RemoveDifferenceIndex.vue"),
      },
      // 应用：删除关键字
      {
        path: "/keyword",
        name: "keyword",
        meta: {
          hidden: false,
          name: "删除关键字",
        },
        component: () =>
          import("../views/app_remove_difference/RemoveDifferenceIndex.vue"),
      }
    ]
  },

  // 应用：图片浏览器
  {
    path: "/img_browser",
    name: "img_browser",
    meta: {
      hidden: false,
      name: "图片分拣",
    },
    component: () =>
      import("../views/app_img_browser/BrowserIndex.vue"),
  },
  // 应用：python tp 批处理
  {
    path: "/tp_batch",
    name: "tp_batch",
    meta: {
      hidden: false,
      name: "tp批处理",
    },
    component: () =>
      import("../views/app_tp_batch/PythonTp.vue"),
  },


  // 应用：设置页
  {
    path: "/setting",
    name: "setting",
    meta: {
      hidden: false,
      name: "设置",
    },
    component: () =>
      import("../views/app_settings/AppSettings.vue"),
  },
  // dev 开发中合集
  {
    path: "/dev",
    name: "dev",
    meta: {
      hidden: false,
      name: "(饼合集)",
    },
    component: () => import("../views/frame_dev/DevIndex.vue"),
    children: [
      // 应用：网络进度追踪
      {
        path: "/tracker",
        name: "tracker",
        meta: {
          hidden: false,
          name: "进度追踪",
        },
        component: () =>
          import("../views/app_tracker/TrackerIndex.vue"),
      },
      // 应用：自动点击
      {
        path: "/auto_click",
        name: "auto_click",
        meta: {
          hidden: false,
          name: "自动点击",
        },
        component: () =>
          import("../views/app_auto_click/AutoIndex.vue"),
      }
    ]
  },
  // test 开发测试合集
  {
    path: "/test",
    name: "test",
    meta: {
      hidden: false,
      name: "(test合集)",
    },
    component: () => import("../views/frame_test/TestIndex.vue"),
    children: [
      // 空白页
      {
        path: "/blank",
        name: "blank",
        meta: {
          hidden: false,
          name: "blank",
        },
        component: () => import("../views/test_blank/BlankIndex.vue"),
      },
      // hello world
      {
        path: "/hello_world",
        name: "hello_world",
        meta: {
          hidden: false,
          name: "hello world",
        },
        component: HelloWorld,
      },
      // 图标显示
      {
        path: "/show_icon",
        name: "show_icon",
        meta: {
          hidden: false,
          name: "显示图标",
        },
        component: () => import("../views/test_icon/IconIndex.vue"),
      },
      // 后端通信测试
      {
        path: "/ws_test",
        name: "ws_test",
        meta: {
          hidden: false,
          name: "ws通信测试",
        },
        component: () => import("../views/test_ws_test/DemoWebsocket.vue"),
      },
      // python调用测试
      {
        path: "/call_py",
        name: "call_py",
        meta: {
          hidden: false,
          name: "python调用",
        },
        component: () => import("../views/test_call_py/CallPyIndex.vue"),
      },
      // csshake震动效果
      {
        path: "/csshake",
        name: "csshake",
        meta: {
          hidden: false,
          name: "csshake震动库",
        },
        component: () => import("../views/test_csshake/ShakeIndex.vue"),
      },
      // animate动效
      {
        path: "/animate",
        name: "animate",
        meta: {
          hidden: false,
          name: "animate动效",
        },
        component: () => import("../views/test_animate/AnimateIndex.vue"),
      },
      // css点赞效果
      {
        path: "/click_like",
        name: "click_like",
        meta: {
          hidden: false,
          name: "css点赞效果",
        },
        component: () => import("../views/test_click_like/LikeIndex.vue"),
      }
    ],
  },


];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
