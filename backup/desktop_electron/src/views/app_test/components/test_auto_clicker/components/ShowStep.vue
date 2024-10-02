<template>
    <div class="show-step-main">
        <!-- <el-button type="danger" @click="test_button">test_button</el-button> -->
        <!-- 加载文件 -->
        <div class="load-json">
            <h3>load json file</h3>
            <span>新建配置文件？</span> <br>
            <span> json_dir : {{ json_dir }}</span>
            <div>
                <el-button type="primary" plain @click="load_json">reload</el-button>
            </div>
            <el-select v-model="json_select_index">
                <el-option v-for="(item, index ) in json_name_list" :key="index" :label="item" :value="index"
                    @click="select_this" />
            </el-select>
        </div>

        <!-- 输入配置参数 -->
        <div class="input-config" v-if="json_select_index != null">
            <h3>input config</h3>
            <span>加注释</span> <br>
            <el-button type="primary" plain @click="modify_flag_config = !modify_flag_config">modify </el-button>
            <div v-for="(item, index) in json_content.config">{{ index }} :
                <span v-if="!modify_flag_config">{{ item }}
                </span>
                <el-input v-else v-model="json_content.config[index]"></el-input>
            </div>
            <el-button v-if="modify_flag_config" type="primary" plain @click="write_json">overwrite</el-button>
        </div>

        <!-- 显示内容 -->
        <div class="show-step" v-if="json_select_index != null">
            <h3>show content</h3>
            <span>输入合法性检测</span> <br>
            <span>默认应该能折叠起来</span> <br>
            <span>如果step太长的话加一个导航条</span> <br>
            <el-button type="primary" plain @click="modify_flag_step = !modify_flag_step">modify </el-button>
            <div class="each-step" v-for="(item1, index1 ) in json_content.step" :key="index1">
                <div class="for-show" v-if="!modify_flag_step">
                    <span class="list-index">{{ index1 }}</span>
                    <div v-for="(item2, index2 ) in item1" :key="index2">
                        <span v-if="typeof (item2) == 'object'">
                            {{ index2 }} : [object]
                        </span>
                        <span v-else>
                            {{ index2 }} : {{ item2 }}
                        </span>
                    </div>
                </div>
                <div class="for-modify" v-else>
                    <span class="list-index">{{ index1 }}</span>
                    <div v-for="(item2, index2 ) in item1" :key="index2">
                        <span v-if="typeof (item2) == 'object'">
                            {{ index2 }} : [object]
                        </span>
                        <span v-else>
                            {{ index2 }} : <el-input v-model="json_content.step[index1][index2]"></el-input>
                        </span>
                    </div>
                </div>
            </div>
            <el-button v-if="modify_flag_step" type="primary" plain @click="write_json">overwrite</el-button>
        </div>
    </div>
</template>
<script setup lang="ts">
import { onMounted, ref, watch } from "vue"
import { ElMessage } from "element-plus";
const fs = window.require("fs")
const path = window.require("path")

// // 加载json文件
// const json_dir = process.env.NODE_ENV === "development"
//     ? path.join(process.cwd(), "public/static/python/auto_click/preset_json")
//     : path.join(process.cwd(), "resources/static/python/auto_click/preset_json")
const json_dir = "D:\\s-code\\test\\preset_json"
const json_path_list = ref()
const json_name_list = ref()
const load_json = () => {
    if (fs.existsSync(json_dir)) {
        json_name_list.value = fs.readdirSync(json_dir);
        json_path_list.value = new Array(json_name_list.value.length).fill(0)
        json_name_list.value.forEach((each: string, index: number) => {
            json_path_list.value[index] = json_dir + "\\" + each;
        });
    } else {
        ElMessage({
            message: "file path does not exist",
            grouping: true,
            showClose: true,
            type: "error",
        });
    }
}
// 选择：选中json文件
const json_select_index = ref()
const json_content = ref({ config: "", step: [] })
const select_this = () => {
    let selected = json_path_list.value[json_select_index.value]
    fs.readFile(selected, (err: string, data: string) => {
        if (err) {
            ElMessage.error("json file read failed")
        } else {
            json_content.value = JSON.parse(data)
        }
    })

}


// flag：修改config
const modify_flag_config = ref(false)
// 写入json
const write_json = () => {
    let selected = json_path_list.value[json_select_index.value]
    fs.writeFile(selected, JSON.stringify(json_content.value), (err: string) => {
        if (err) {
            ElMessage.error("json file write failed")
        } else {
            ElMessage.success("json write done")
        }
    })
}


// flag: 修改step
const modify_flag_step = ref(false)


// 测试按钮
const test_button = () => {
    console.log("test button")
    console.log(typeof (json_content.value.step) == "object")
}

// 初始化加载
onMounted(() => {
    load_json()
})
</script>


<style lang="scss">
div.load-json {
    border-style: solid;
    width: 95%;
    margin: 0 auto;
    padding: 10px;
}

div.input-config {
    border-style: solid;
    width: 95%;
    margin: 0 auto;
    padding: 10px;

    .el-input {
        width: calc(50% - 50px);
    }
}

div.show-step {
    border-style: solid;
    width: 95%;
    margin: 0 auto;
    padding: 10px;
    position: relative;

    span.list-index {
        // color: rgba(128, 128, 128, 0.126);
        color: rgb(255, 0, 0);
        font-weight: bold; // 加粗
        font-size: 80px;
        position: absolute;
        display: flex;
        padding-left: 30px;
    }

    div.each-step {
        padding: 10px;
        border: solid red;

        div.for-modify {
            .el-input {
                width: calc(50% - 50px);
            }
        }
    }


}
</style>