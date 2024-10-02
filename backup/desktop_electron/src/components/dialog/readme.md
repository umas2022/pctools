# 全局弹窗

## DialogPopup
- animate动效控制的全局info弹窗
- Array<string> 传参:显示info内容
- boolean 传参:控制窗口显示
- 提供一个底部slot
<slot name="content"></slot>


## 注意
- position:fixed属性没有生效,不知道为什么,现在定位并不是基于绝对顶部而不是窗口顶部