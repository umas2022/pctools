/**
 * axios配置文件
 * create:2022.5.20
 * 注意：var值只有启动时会初始化一次, 应用中修改的cookie值不能实时更新, 使用时应调用get函数而不是var值
 */


/**
 * 本地后端端口号, 在app_settings页面中存入localStorage
 * 应用中应使用get_port函数获取最新的端口, 而不是直接读取port变量
 * （经测试打包后electron无法使用cookie）
 * 生产环境：4090
 * 开发环境：4091
 */
export var port = localStorage.getItem("port") || 4090 
export function get_port(){
  return localStorage.getItem("port") || 4090 
}

/**
 * 本地后端地址(http)
 */
export var url = {
  local: "http://localhost:" + port + "/",
};
export function get_url(){
  return{
    local:"http://localhost:" + get_port() + "/",
  }
}

/**
 * 本地后端地址(websocket)
 * 用例：wsurl.local+"copy_to_one_ws"
 */
export var wsurl = {
  local: "ws://localhost:" + port + "/",
}
export function get_wsurl(){
  return{
    local:"ws://localhost:" + get_port() + "/",
  }
}
