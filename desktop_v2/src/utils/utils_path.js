/**
 * 静态资源目录定位
 * vue.config.js中需要配置{ from: 'public/static', to: 'static' }
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
