/**
 * axios配置文件
 * create:2022.5.20
 * 使用store替代了localStorage,这里不再定义端口
 */



/**
 * 本地后端地址(http)
 */
export function get_url(port){
  return{
    local:"http://localhost:" + port + "/",
  }
}

/**
 * 本地后端地址(websocket)
 */
export function get_wsurl(port){
  return{
    local:"ws://localhost:" + port + "/",
  }
}
