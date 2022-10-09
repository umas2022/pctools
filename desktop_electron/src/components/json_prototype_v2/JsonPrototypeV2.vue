<template>
    <div class="prototype-main">
        <div v-if="props.data.version!='v2'">
            <h3>json不是v2版本,请检查page_lowcode.json格式</h3>
        </div>
        <div v-else>
            <!-- <el-button type="danger" @click="test_button">test</el-button> -->
            <!-- 标题栏 -->
            <h3>{{pg_title}}
                <div class="info-icon"
                    style="display: inline-block;  vertical-align: middle;  padding-left: 10px;  padding-right: 20px;  cursor: pointer;">
                    <useSvgIcon icon="info" color="black" :width="Number(20)" @click="dialogVisible = !dialogVisible" />
                </div>
            </h3>

            <!-- info弹窗 -->
            <el-dialog :title="pg_title" v-model="dialogVisible" width="500px">
                <div>
                    <div class="each-line" v-for="(item, key) in pg_info" :key="key">
                        {{ item }}
                    </div>
                </div>
            </el-dialog>

            <!-- 各种框分类 -->
            <div class="filter" v-for="item in as_data">
                <!-- 输入框 -->
                <div class="input-box" v-if="item.type=='input'">
                    {{item.data.label}}
                    <el-input v-model="item.data.value" clearable :placeholder="item.data.placeholder||'请输入'">
                    </el-input>
                    <!-- 注解 -->
                    <div class="info-icon" v-if="item.data.annotation">
                        <useSvgIcon icon="info" color="black" :width="Number(20)"
                            @click="item.data.annotation_visible = !item.data.annotation_visible" />
                    </div>
                    <div v-if="item.data.annotation_visible">
                        <div v-if="typeof(item.data.annotation)=='string'">
                            {{item.data.annotation}}
                        </div>
                        <div v-else v-for="each_line in item.data.annotation">
                            {{each_line}}
                        </div>
                    </div>
                </div>
                <!-- 选择框 -->
                <div class="select-box" v-if="item.type=='select'">
                    {{item.data.label}}
                    <el-select v-model="item.data.value">
                        <el-option v-for="each in item.data.option" :label="each.label" :value="each.value" />
                    </el-select>
                    <!-- 注解 -->
                    <div class="info-icon" v-if="item.data.annotation">
                        <useSvgIcon icon="info" color="black" :width="Number(20)"
                            @click="item.data.annotation_visible = !item.data.annotation_visible" />
                    </div>
                    <div v-if="item.data.annotation_visible">
                        <div v-if="typeof(item.data.annotation)=='string'">
                            {{item.data.annotation}}
                        </div>
                        <div v-else v-for="each_line in item.data.annotation">
                            {{each_line}}
                        </div>
                    </div>
                </div>
            </div>

            <!-- 显示log -->
            <div class="log-box">
                <ShowLogBox :data="log_res" :height=log_height />
            </div>

            <el-button @click="start">开始</el-button>

        </div>
    </div>
</template>
<script setup lang="ts">

import { ref, onMounted, reactive, provide } from "vue";
import { onUpdated, watch } from "@vue/runtime-core";
import type { ElScrollbar } from "element-plus";
import { get_wsurl } from "@/utils/api_config.js";
import ShowLogBox from "@/components/show_log/ShowLogBox.vue";
import useSvgIcon from "@/components/use_svg/useSvgIcon.vue";
// const get_wsurl = require("@/utils/api_config.js");

// 类型定义
// 输入框
type type_input = {
    key: string,
    label: string,
    value: string
    annotation: string | Array<string>
}
// 选择框
type select_option = {
    key: string,
    label: string,
}
type type_select = {
    key: string,
    label: string,
    value: string,
    option: Array<select_option>
    annotation: string
}
// 页面数据类型
type type_page = {
    type: string,
    // data: type_input | type_select // 这句求了个交集
    data: any
}
// 消息发送
type type_send = {
    function: string
}
// 父组件传参
const props = defineProps<{
    data: {
        title: string,
        version: string,
        info: object,
        page: Array<type_page>,
        function: string
    };
}>();



// json页面参数取出
const pg_title = props.data.title || ""
const pg_info = props.data.info || {}
const pg_data = props.data.page || {}
const pg_function = props.data.function

// json页面参数赋值
const as_data = ref(JSON.parse(JSON.stringify(pg_data)))

// help页弹窗控制
const dialogVisible = ref(false);
// 注解文本控制
onMounted(() => {
    as_data.value.forEach((each_step: type_page) => {
        each_step.data["annotation_visible"] = false
    })
})

// log高度控制
const log_height = reactive({ data: 0, time: 0 })
provide("log_height", log_height)
// log文本
const log_res = ref("")

// 开始按钮
const start = () => {
    log_height.data = 300
    log_height.time = Date.now()

    const send_data: type_send = { function: pg_function }
    as_data.value.forEach((item: type_page) => {
        let add_data: any = {}
        add_data[item.data.key] = item.data.value
        Object.assign(send_data, add_data)
    });

    // console.log(send_data)
    console.log("ws connecting ...");

    let wsdemo = new WebSocket(get_wsurl().local + "sp_operator");
    wsdemo.onopen = () => {
        wsdemo.send(JSON.stringify(send_data));
    };
    wsdemo.onmessage = (e) => {
        log_res.value = e.data;
    };
};

// 测试按钮
const test_button = () => {
    console.log(as_data.value)
}
</script>

<style lang="scss">
div.prototype-main {
    position: relative;
    height: 100%;
    text-align: center;
}

div.input-box {
    .el-input {
        width: 50%;
        padding: 10px;
    }

    .info-icon {
        display: inline-block;
        position: absolute;
        padding-top: 15px;
        cursor: pointer;
    }
}

div.select-box {
    .el-select {
        width: calc(50% - 20px);
        padding: 10px;
    }

    .info-icon {
        display: inline-block;
        position: absolute;
        padding-top: 15px;
        cursor: pointer;
    }
}


div.log-box {
    position: absolute;
    width: calc(100% + 1px);
    bottom: 0px;
}
</style>