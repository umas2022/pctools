<template>
    <div class="test-main" style="height:1000px">
        <h1>CSShake鬼畜震动库</h1>
        <div class="shake shake-crazy shake-box">
            <span class="text">crazy!</span>
        </div>
        <h3>npm i csshake -s</h3>
        <h3>@import '~csshake';</h3>
        <h3>http://elrumordelaluz.github.io/csshake/</h3>
    </div>
</template>
<style lang="scss" scoped>
@import '~csshake';

div.shake-box {
    display: flex;
    align-items: center;
    margin: auto;
    width: 300px;
    height: 200px;
    background-color: red;

    .text {
        color: rgb(0, 255, 115);
        font-weight: bold; // 加粗
        font-size: 80px;
        // position: absolute;
        display: flex;
        padding-left: 30px;
    }
}
</style>