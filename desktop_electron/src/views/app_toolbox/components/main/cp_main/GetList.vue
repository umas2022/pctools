<template>
    <div class="cp-getlist">
        <div class="h3">获取目录<div class="info-icon"
                style="display: inline-block;  vertical-align: middle;  padding-left: 10px;  padding-right: 20px;  cursor: pointer;">
                <useSvgIcon icon="info" color="black" :width="Number(20)" @click="display_gb_info(pg_info)" />
            </div>
        </div>
        <span style="padding:10px">组数量:</span>
        <span style="padding:10px">{{ Object.keys(store_home.index_list).length }}</span>
        <span style="padding:10px">方法数量:</span>
        <span style="padding:10px">{{ func_total }}</span>
        <el-button @click="get_list">刷新</el-button>
    </div>
</template>
<script setup lang="ts">
import { ref, inject, onMounted } from "vue"
import type { Ref } from "vue"
import { get_wsurl } from "@/utils/api_config.js";
import { ElMessage } from "element-plus";
import useSvgIcon from "@/components/svgbox/useSvgIcon.vue";
import path from "path";

const store_home: any = inject("store_home")

// info按钮
const display_gb_info: any = inject("display_gb_info")
const pg_info = [
    "1.首次启动时等待后端启动完成后手动点击刷新",
    "2.前端启动时以3秒间隔向后端请求3次"
]

// 方法数量
const func_total = ref(0)

const get_list = () => {
    console.log(store_home.is_dev)
    console.log(store_home.py_path)
    console.log(path.basename(store_home.py_path))
    // 获取目录
    const send_data = {
        function: "get_list",
        data: { py_path: store_home.py_path }
    }

    console.log("ws connecting ...");

    let wsdemo = new WebSocket(get_wsurl().local + "sp_searcher");
    wsdemo.onopen = () => {
        wsdemo.send(JSON.stringify(send_data));
    };
    wsdemo.onmessage = (e) => {
        try {
            store_home.index_list = JSON.parse(e.data).data

            // 折叠目录获取栏
            if (store_home.index_list.length != 0) {
                setTimeout(() => {
                    store_home.extract_display = false
                }, 1000)
            }

            // 计数所有方法
            func_total.value = 0
            for (let key in store_home.index_list) {
                for (let sub_key in store_home.index_list[key]["data"]) {
                    func_total.value += 1
                }
            }
        } catch {
            console.log(e.data)
        }
    };
}

// 间隔3秒多次重试获取list
const get_list_repeat = (re_times: number) => {
    // 时间间隔
    let time_interval = 3000
    // 单次获取函数
    const get_list_check = () => {
        get_list()
        if (store_home.index_list.length != 0) {
            clearInterval(set_id)
        }
    }
    // 设置定时器
    let set_id = setInterval(get_list_check, time_interval)
    setTimeout(() => {
        clearInterval(set_id)
    }, (re_times - 1) * time_interval)
}

// 启动时尝试获取3次list
onMounted(() => {
    if (store_home.index_list.length == 0) {
        get_list_repeat(3)
    }
})
</script>
<style lang="scss" scoped>
div.cp-getlist{
  user-select: none; // 页面文字禁止被选中
}
div.info-icon {
    display: flex;
    cursor: pointer;
}
</style>