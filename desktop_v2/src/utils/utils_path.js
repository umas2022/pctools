/**
 * 静态资源目录定位,python脚本的位置也由下面的函数确定
 * vue.config.js中需要设置文件拷贝{ from: 'public/static', to: 'static' }
 */


/**
 * 定位到静态资源static目录下
 * @returns {string} @/static
 */
export function static_path() {
const path = require("path");
const isDevelopment = process.env.NODE_ENV !== "production";
    let get_path = isDevelopment
        ? path.join(process.cwd(), "public/static")
        : path.join(process.cwd(), "resources/static")
    return get_path
}

/**
 * 当前是否为开发状态,布尔返回
 * @returns {boolean} @/static
 */
export function is_dev() {
    let dev = false
    const isDevelopment = process.env.NODE_ENV !== "production";
        let get_path = isDevelopment
            ? dev = true
            : dev = false
        return dev
    }