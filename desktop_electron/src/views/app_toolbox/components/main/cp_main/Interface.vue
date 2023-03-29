<template>
    <div class="animate-box animate__animated" ref="intf_ref">
        <!-- <el-button type="danger" @click="test_button">test</el-button> -->
        <div class="intf-main" v-if="store_home.intf_data.title">
            <!-- 标题栏 -->
            <div class="h3">{{ pg_title }}
                <div class="info-icon"
                    style="display: inline-block;  vertical-align: middle;  padding-left: 10px;  padding-right: 20px;  cursor: pointer;">
                    <useSvgIcon icon="info" color="black" :width="Number(20)" @click="display_gb_info(pg_info)" />
                </div>
            </div>

            <!-- 各种框分类 -->
            <div class="filter" v-for="item in pg_data">
                <!-- 输入框input -->
                <div class="input-box" v-if="item.type == 'input'">
                    <!-- show模式检测 -->
                    <div v-if="item.show != undefined && item.show.value == false" />
                    <div v-else>
                        <div style="display:inline-block;width:150px">
                            {{ item.data.label }}
                        </div>
                        <el-input v-model="item.data.value" clearable :placeholder="item.data.placeholder || '请输入'">
                        </el-input>
                        <!-- 注解 -->
                        <div class="info-icon" v-if="item.data.annotation">
                            <useSvgIcon icon="info" color="black" :width="Number(20)"
                                @click="item.data.annotation_visible = !item.data.annotation_visible" />
                        </div>
                        <div v-if="item.data.annotation_visible">
                            <div v-if="typeof (item.data.annotation) == 'string'">
                                {{ item.data.annotation }}
                            </div>
                            <div v-else v-for="each_line in item.data.annotation">
                                {{ each_line }}
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 选择框select -->
                <div class="select-box" v-if="item.type == 'select'">
                    <!-- show模式检测 -->
                    <div v-if="item.show != undefined && item.show.value == false" />
                    <div v-else>
                        <div style="display:inline-block;width:150px">
                            {{ item.data.label }}
                        </div>
                        <el-select v-model="item.data.value" @click="set_height(30)">
                            <el-option v-for="each in item.data.option" :label="each.label" :value="each.value" />
                        </el-select>
                        <!-- 注解 -->
                        <div class="info-icon" v-if="item.data.annotation">
                            <useSvgIcon icon="info" color="black" :width="Number(20)"
                                @click="item.data.annotation_visible = !item.data.annotation_visible" />
                        </div>
                        <div v-if="item.data.annotation_visible">
                            <div v-if="typeof (item.data.annotation) == 'string'">
                                {{ item.data.annotation }}
                            </div>
                            <div v-else v-for="each_line in item.data.annotation">
                                {{ each_line }}
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 开关switch -->
                <div class="switch-box" v-if="item.type == 'switch'">
                    <!-- show模式检测 -->
                    <div v-if="item.show != undefined && item.show.value == false" />
                    <div v-else>
                        <div style="display:inline-block;width:150px">
                            {{ item.data.label }}
                        </div>
                        <el-switch v-model="item.data.value">
                        </el-switch>
                        <!-- 注解 -->
                        <div class="info-icon" v-if="item.data.annotation">
                            <useSvgIcon icon="info" color="black" :width="Number(20)"
                                @click="item.data.annotation_visible = !item.data.annotation_visible" />
                        </div>
                        <div v-if="item.data.annotation_visible">
                            <div v-if="typeof (item.data.annotation) == 'string'">
                                {{ item.data.annotation }}
                            </div>
                            <div v-else v-for="each_line in item.data.annotation">
                                {{ each_line }}
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 按钮button -->
                <div class="button-box" v-if="item.type == 'button'">
                    <!-- show模式检测 -->
                    <div v-if="item.show != undefined && item.show.value == false" />
                    <div v-else>
                        <div style="display:inline-block;width:150px">
                            {{ item.data.label }}
                        </div>
                        <el-button @click="start(item.data.key)">{{ item.data.button }}</el-button>
                        <!-- 注解 -->
                        <div class="info-icon" v-if="item.data.annotation">
                            <useSvgIcon icon="info" color="black" :width="Number(20)"
                                @click="item.data.annotation_visible = !item.data.annotation_visible" />
                        </div>
                        <div v-if="item.data.annotation_visible">
                            <div v-if="typeof (item.data.annotation) == 'string'">
                                {{ item.data.annotation }}
                            </div>
                            <div v-else v-for="each_line in item.data.annotation">
                                {{ each_line }}
                            </div>
                        </div>
                    </div>
                </div>

            </div>




            <!-- 终端switch和开始按钮 -->
            <div class="start-box">
            <div style="display:inline-block;padding: 10px;">
                <span>使用终端 </span>
                <el-switch v-model="as_terminal" />
            </div>
            <div style="display:inline-block;padding: 10px;">
                <el-button @click="start">开始</el-button>
            </div></div>

            <!-- 显示log -->
            <div class="log-box">
                <ShowLogBox :data="log_res" :height=log_height />
            </div>

            <!-- 底部留白 -->
            <div style="height:100px"></div>

        </div>
    </div>
</template>
<script setup lang="ts">
import { ref, onMounted, reactive, inject, provide, computed, watch } from "vue";
import { get_wsurl } from "@/utils/api_config.js";
import ShowLogBox from "@/components/show_log/ShowLogBox.vue";
import useSvgIcon from "@/components/svgbox/useSvgIcon.vue";

const store_home: any = inject("store_home")
const display_gb_info: any = inject("display_gb_info")

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
// 开关
type type_switch = {
    key: string,
    label: string,
    value: boolean
    annotation: string | Array<string>
}
// 页面数据类型
type type_page = {
    type: string,
    // data: type_input | type_select // 这句求了个交集, 应该求并
    data: any,
    show: any
}
// 消息发送
type type_send = {
    function: string,
    terminal: boolean,
    py_path: string,
    button: any
}

// json页面参数取出
const pg_title = computed(() => { return store_home.intf_data.title || "" })
const pg_info = computed(() => { return store_home.intf_data.info || [] })
const pg_data = computed(() => { return store_home.intf_data.require || [] })

// 全局参数
const as_terminal = ref(false)

// log高度控制,加上时间让组件传参可以识别变化
const log_height = reactive({ data: 0, time: 0 })
provide("log_height", log_height)
// log文本
const log_res = ref("")
// 设置log栏高度,高位300,低位30
const set_height = (get_height: number) => {
    log_height.data = get_height
    log_height.time = Date.now()
}


// 开始按钮
const start = (button: any) => {
    if (typeof (button) != "string") {
        button = ""
    }
    if (!as_terminal.value) {
        set_height(300)
    }
    const send_data: type_send = {
        function: store_home.function,
        terminal: as_terminal.value,
        py_path: store_home.py_path,
        button: button
    }
    pg_data.value.forEach((item: type_page) => {
        let add_data: any = {}
        if (item.show) {
            if (item.show.value) {
                console.log(item.data.label)
                add_data[item.data.key] = item.data.value
            }
        }
        else {
            add_data[item.data.key] = item.data.value

        }
        Object.assign(send_data, add_data)
    });

    console.log("ws connecting ...");

    let wsdemo = new WebSocket(get_wsurl().local + "sp_searcher");
    wsdemo.onopen = () => {
        wsdemo.send(JSON.stringify({ function: "run", data: send_data }));
    };
    wsdemo.onmessage = (e) => {
        log_res.value = e.data;
    };
};


// 参数加载
onMounted(() => {
    pg_data.value.forEach((each_step: type_page) => {
        // 注解文本控制
        each_step.data["annotation_visible"] = false
    })
})

// // 切换动效
const first_time = ref(true)
const intf_ref = ref<HTMLDivElement>()
watch(pg_title, () => {
    if (first_time.value) {
        first_time.value = false
        intf_ref.value!.classList.add("animate__backInRight")
    } else {
        intf_ref.value!.classList.remove("animate__backInRight")
        intf_ref.value!.classList.add("animate__backOutLeft")
        setTimeout(() => {
            intf_ref.value!.classList.remove("animate__backOutLeft")
            intf_ref.value!.classList.add("animate__backInRight")
        }, 300)
    }
})

// show模式切换
const set_show_state = () => {
    pg_data.value.forEach((item: any) => {
        if (item.show) {
            item.show.value = computed(() => {
                return get_item_value(item.show.listen.key) == item.show.listen.value
            })
        }
    });
}
const get_item_value = (item_key: string) => {
    for (let num in pg_data.value) {
        let item = pg_data.value[num]
        if (item.data.key == item_key) {
            return item.data.value
        }
    }
}
onMounted(() => {
    set_show_state()
})
watch(() => store_home.intf_data.title, () => {
    set_show_state()
})


// 测试按钮
const test_button = () => {
    set_show_state()
}
</script>

<style lang="scss" scoped>
// 主体box
div.intf-main {
    position: relative;
    text-align: center;
    user-select: none; // 页面文字禁止被选中
}

// dialog弹窗
.el-overlay-dialog {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
}

// 输入框
div.input-box {
    user-select: none; // 页面文字禁止被选中
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

// 选择框
div.select-box {
    user-select: none; // 页面文字禁止被选中
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

// 开关
div.switch-box {
    padding: 10px;
    user-select: none; // 页面文字禁止被选中
    .el-switch {
        padding-left: 10px;
    }

    .info-icon {
        display: inline-block;
        position: absolute;
        padding-top: 6px;
        padding-left: 15px;
        cursor: pointer;
    }
}

// 按钮
div.button-box {
    padding: 10px;
    user-select: none; // 页面文字禁止被选中

    .info-icon {
        display: inline-block;
        position: absolute;
        padding-top: 6px;
        padding-left: 15px;
        cursor: pointer;
    }
}

// 开始
div.start-box{
    user-select: none; // 页面文字禁止被选中

}

// 日志
div.log-box {
    width: calc(100% - 180px);
    margin: auto;
}

</style>