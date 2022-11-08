<template>
  <div class="wf-main">
    <h3>真瀑布流展示</h3>
    <!-- <el-button type="primary" plain @click="waterfall_reset">reload</el-button> -->
    <div class="body" v-show="show_body">
      <!-- 分列 -->
      <div v-for="col in cols_current" class="flow" :id="'flow_' + (col - 1)"></div>
      <!-- 看到这个就开始加载新图 -->
      <div class="reload"></div>
    </div>
    <div>
      <h3>划太快, 加载速度跟不上 / 到底了</h3>
      <el-button type="danger" @click="rear_add_10">手动加载</el-button>
    </div>
  </div>
  <!-- 单张弹窗大图 -->
  <el-dialog v-model="dialog_form.dialog_visible" title="compare" width="70%">
    <div class="img-com">
      <h3>{{dialog_form.selected}}</h3>
      <img :style="{ width: win_width*0.6+'px' }" :src="dialog_form.selected" />
    </div>
  </el-dialog>

</template>
<script setup>
import { inject, ref, onMounted, createApp, reactive } from "vue";
import WfShow from "./WfShow";

const img_form = inject("img_form");
const input_form = inject("input_form")

// 显示body
const show_body = ref(false);

// 预设值列表
const preset_dict = {
  // 瀑布流最大列数
  cols_max: 5,
  // 每列初始化加载数量
  initial_load: 3,
  // 单张图片最小宽度
  img_width_min: 300,
  // 每次新加载的图片数量
  new_amount: 10,
};

// 当前列数
const cols_current = ref(1);
// 最短的列
const shortest_index = ref(0);
// 当前图片宽度
const img_width_current = ref(300);
// 窗口宽度
const win_width = ref(0)
// 当前展示的最后图片序号
const last_index = ref(0);
// 初始化计算列数、宽度、序号
const cal_cols = () => {
   win_width.value = document.documentElement.clientWidth;
  if (win_width.value < preset_dict.img_width_min) {
    cols_current.value = 1;
    img_width_current.value = win_width.value * 0.8;
  } else if (win_width.value / preset_dict.img_width_min > preset_dict.cols_max) {
    cols_current.value = preset_dict.cols_max;
    img_width_current.value =
      Math.floor(win_width.value / preset_dict.cols_max) * 0.8;
  } else {
    cols_current.value = Math.floor(win_width.value / preset_dict.img_width_min);
    img_width_current.value = Math.floor(win_width.value / cols_current.value) * 0.8;
  }
};

// 计算最短列
async function find_shortest() {
  let get_index = 0;
  let shortest_height = 0;
  for (let col = 0; col < cols_current.value; col++) {
    let col_id = "flow_" + col;
    let element = document.getElementById(col_id);
    let col_height = 0;
    // 初始化加载时会出现读不到id的情况
    if (element) {
      col_height = element.offsetHeight;
    } else {
      return 0;
    }
    if (col == 0) {
      shortest_height = col_height;
    } else {
      if (shortest_height > col_height) {
        shortest_height = col_height;
        get_index = col;
      }
    }
  }
  shortest_index.value = get_index;
  return get_index;
}

// 标记最底部的图片
// 使用了一层背景遮罩, 不需要这个功能了
const mark_last = () => {
  // let last_one = document.getElementsByClassName("last_drop");
  // if (last_one.length > 0) {
  //   last_one[0].classList.remove("last_drop");
  // }
  // shortest_index.value = find_shortest();
  // let col_id = "flow_" + shortest_index.value;
  // let flow_shortest = document.getElementById(col_id);
  // last_one = flow_shortest.children[flow_shortest.children.length - 1];
  // last_one.classList.add("last_drop");
};

// 尾部增加一张图片
async function rear_add() {
  find_shortest().then(() => {
    let col_id = "flow_" + shortest_index.value;
    let flow_shortest = document.getElementById(col_id);

    let new_drop = document.createElement("div");
    new_drop.setAttribute("class", "drop");
    let drop_id = "drop_" + flow_shortest.children.length;
    new_drop.setAttribute("id", drop_id);

    // // 仅添加一张图片
    // let new_img = document.createElement("img");
    // new_img.setAttribute("width", img_width_current.value);
    // new_img.src = img_form.img_list[last_index.value];
    // new_drop.appendChild(new_img);

    // 添加vue组件
    let vprops = {
      option: {
        img_src: img_form.img_list[last_index.value],
        img_width: img_width_current.value,
        img_index: last_index.value,
        img_form: img_form,
        input_form: input_form,
        dialog_form:dialog_form
      },
    };
    let new_img = createApp(WfShow, vprops);
    new_img.mount(new_drop);

    flow_shortest.appendChild(new_drop);

    last_index.value += 1;
    mark_last();
  });
}

// 尾部增加多个图片
const rear_add_10 = () => {
  const timer = setInterval(() => {
    rear_add();
  }, 100);
  setTimeout(() => {
    clearInterval(timer);
  }, 100 * preset_dict.new_amount);
};

// 测试按钮
const test_button = () => {
  // rear_add_10();
  console.log(img_width_current.value);
  rear_add();
  console.log(img_width_current.value);
};

// 初始化函数
async function waterfall_reset() {
  show_body.value = true;
  cal_cols();
  mark_last();
}

// 初始化
onMounted(() => {
  waterfall_reset().then(() => {
    rear_add_10();
  });

  // 监听当前视图并加载新图片
  var reload_flag = document.getElementsByClassName("reload")[0];
  const io = new IntersectionObserver(() => {
    rear_add_10();
  });
  io.observe(reload_flag);
});

// 尺寸重置
window.onresize = () => {
  waterfall_reset();
};

// 单张弹窗大图控制
const dialog_form = reactive({
  dialog_visible :false,
  selected:""
})

</script>
<style scoped lang="scss">
div.flow {
  display: inline-block;
  border: solid 3px red;
  vertical-align: top;
}

div.wf-main {
  position: relative;
  z-index: 0;

  div.body {
    position: inherit;
    z-index: 3;
  }

  div.reload {
    position: absolute;
    bottom: 0px;
    width: 100%;
    height: 500px;
    background-color: rgba(255, 0, 0, 0.164);
    // cursor: pointer;
    // z-index: 1; // 没有生效？还是有pointer
  }
}
</style>
