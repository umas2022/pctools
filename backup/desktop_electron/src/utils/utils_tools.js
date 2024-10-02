/**
 * 工具函数
 */


/**
 * 将字符串数组转为小写
 * @param {array} raw_dic 原始数组
 * @returns 小写数组
 */
export function dic_lower(raw_dic) {
  let dic_save = [];
  raw_dic.forEach((label) => {
    dic_save.push(label.toLowerCase());
  });
  return dic_save;
}


/**
 * 获取当前时间json
 * @returns time_json
 */
export function get_time() {
  let date = new Date();
  let time_json = {
    "year": date.getFullYear(),
    "month": date.getMonth() + 1,
    "day": date.getDate(),
    "hours": date.getHours(),
    "minutes": date.getMinutes(),
    "seconds": date.getSeconds()
  }
  return time_json
}