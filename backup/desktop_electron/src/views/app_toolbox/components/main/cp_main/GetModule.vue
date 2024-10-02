<template>
    <div class="cp-module">
        <div class="h3">
            获取功能
            <div class="info-icon"
                style="display: inline-block;  vertical-align: middle;  padding-left: 10px;  padding-right: 20px;  cursor: pointer;">
                <useSvgIcon icon="info" color="black" :width="Number(20)" @click="display_gb_info(pg_info)" />
            </div>
        </div>
        <el-select v-model="store_home.group" placeholder="选择组">
            <el-option v-for="(item, key) in store_home.index_list" :key="key" :label="store_home.index_list[key]['label']"
                :value="key" @click="store_home.function = ''" />
        </el-select>

        <AnimateDown :display="store_home.group != ''">
            <template #content>
                <el-select v-model="store_home.function" placeholder="选择功能" v-if="store_home.group != ''">
                    <el-option v-for="(item, key) in store_home.index_list[store_home.group]['data']" :key="key"
                        :label="item" :value="key" @click="get_intf" />
                </el-select>
            </template>
        </AnimateDown>

    </div>
</template>
<script setup lang="ts">
import { ref, inject, watch } from "vue"
import { get_wsurl } from "@/utils/api_config.js";
import AnimateDown from "@/components/animate_down/AnimateDown.vue"
import useSvgIcon from "@/components/svgbox/useSvgIcon.vue";
import { useStore } from "vuex";
const store = useStore();
const store_home: any = inject("store_home")


// info按钮
const display_gb_info: any = inject("display_gb_info")
const pg_info = [
    "1.选择组",
    "2.选择功能"
]


// 获取json
const get_intf = () => {

    console.log(store_home.index_list)
    // 更新目录
    const send_data = {
        function: "get_intf",
        data: { py_path: store.state.config["py_path"]["value"], module: store_home.function }
    }

    console.log("ws connecting ...");

    let wsdemo = new WebSocket(get_wsurl(store.state.config["port"]["value"]).local + "sp_searcher");
    wsdemo.onopen = () => {
        wsdemo.send(JSON.stringify(send_data));
    };
    wsdemo.onmessage = (e) => {
        // console.log(e.data);
        try {
            store_home.intf_data = JSON.parse(e.data)
        } catch { }
    };
}

</script>
<style scoped lang="scss">
div.cp-module {
    user-select: none; // 页面文字禁止被选中
}
</style>