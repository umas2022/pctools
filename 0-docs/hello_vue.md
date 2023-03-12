# 快速搭建


- 安装vue并创建项目
```
npm install  -g @vue/cli
vue create localviewer
```

- 安装选项记录
```
Vue CLI v5.0.8
? Please pick a preset: Manually select features
? Check the features needed for your project: Babel, TS, Router, Vuex, CSS Pre-processors, 
Linter
? Choose a version of Vue.js that you want to start the project with 3.x
? Use class-style component syntax? Yes
? Use Babel alongside TypeScript (required for modern mode, auto-detected polyfills, transpiling JSX)? Yes
? Use history mode for router? (Requires proper server setup for index fallback in production) 
Yes
? Pick a CSS pre-processor (PostCSS, Autoprefixer and CSS Modules are supported by default): 
Sass/SCSS (with dart-sass)
? Pick a linter / formatter config: Basic
? Pick additional lint features: Lint on save
? Where do you prefer placing config for Babel, ESLint, etc.? In package.json
? Save this as a preset for future projects? No
```

- 修改App.vue,这里使用HomeView.vue作为入口,删除了About页
```html
<template>
  <div>
    <HomeView />
  </div>
</template>
<script setup lang="ts">
import HomeView from './views/HomeView.vue';
</script>
<style lang="scss"></style>
```

- 同样在router/index.ts删除about

- 引入element
```
npm install element-plus --save
```

- 在main.ts中引入element
```js
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
createApp(App).use(store).use(router).use(ElementPlus).mount('#app')
```













