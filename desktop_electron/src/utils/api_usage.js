/**
 * api访问函数
 */

import { use_axios_local } from "./api_axios.js"

/**
 * 通用回调, 直接打印返回值
 * @param {any} res 后端返回值
 */
export function log_res(res) {
    console.log("get res:")
    console.log(res)
}

/**
 * 获取后端ip地址
 * @param {Function} get_res 成功回调
 * @param {Function} get_err 失败回调
 */
export function home_ip(get_res, get_err) {
    use_axios_local({
        inputApi: "app_home_ip",
        inputMethod: "get",
        inputFuncGetRes: get_res,
        inputFuncGetErr: get_err
    })
}