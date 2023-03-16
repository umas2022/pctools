# 使用cdn引入vue的简易html


```html
<html>

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1.0" />
    <!-- import Vue -->
    <script src="https://unpkg.com/vue@next"></script>
    <!-- import element CSS -->
    <link rel="stylesheet" href="https://unpkg.com/element-plus/dist/index.css">
    <!-- import element JavaScript -->
    <script src="https://unpkg.com/element-plus"></script>
    <title>local viewer</title>
</head>

<body>
    <div id="app">
        <div class="nav">
            <h3>导航</h3>
            <el-button @click="testbutton">testbutton</el-button>
            <div class="nav-item" v-for="item in file_list">
                <el-button @click="load_html(item)">go</el-button>
                {{item}}
            </div>
        </div>
        <div class="body">
            <h3 v-if="html_file ==''">内容</h3>
            {{html_file}}
            <iframe v-else :src="'data/'+html_file" frameborder="0"></iframe>
        </div>
    </div>
    </div>
    <script>
        const App = {
            data() {
                return {
                    // 被选中的html文件
                    html_file: "",
                    // 文件列表
                    file_list: ["test1.html", "test2.html"] 

                };
            },
            methods: {
                load_html: function (selected) {
                    this.html_file = selected
                },
                testbutton:function(){
                    console.log("!")
                }
            }
        };
        const app = Vue.createApp(App);
        app.use(ElementPlus);
        app.mount("#app");
    </script>
</body>
<style lang="scss">
    div#app {
        display: flex;
        height: 100%;
    }

    div.nav {
        border: solid 1px red;
        width: 30%;
        display: flex;
        flex-direction: column;
    }

    div.nav-item {

        border: solid 1px green;
        height: 50px;
    }

    div.body {
        border: solid 1px blue;
        width: 70%;
    }

    iframe {
        height: 100%;
        width: 100%;
    }
</style>

</html>
```