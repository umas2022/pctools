import axios from "axios";
import axiosRetry from "axios-retry";
import * as conf from "./api_config";

// 空函数：打印返回值
function printRes(res) {
  console.log("printRes : " + res);
}

/**
 * axios基本函数，接收任意url
 * @param {string}  inputUrl        ip地址
 * @param {object}  inputHeaders    请求头；default = {}
 * @param {string}  inputApi        api名，带斜杠，如"oi_r/"
 * @param {string}  inputMethod     "get" / "put" / "post" ...
 * @param {int}     inputTimeout    超时时长；default = 5000 (set in conf)
 * @param {int}     inputRetry      重试次数；default = 1
 * @param {object}  inputData       body；default = {}
 * @param {function} inputFuncGetRes callback，获取返回值；default = printRes()
 * @param {function} inputFuncGetErr callback，获取错误信息；default = printRes()
 */
export function use_axios({
  inputUrl,
  inputHeaders,
  inputApi,
  inputMethod,
  inputTimeout = 5000,
  inputRetry = 1,
  inputData = {},
  inputFuncGetRes = printRes,
  inputFuncGetErr = printRes,
}) {
  // 设置重试次数和等待时间
  axiosRetry(axios, {
    retries: inputRetry, // 设置自动发送请求次数
    retryDelay: (retryCount) => {
      return retryCount * 1000; // 重复请求延迟
    },
    shouldResetTimeout: true, //  重置超时时间
    retryCondition: (error) => {
      //true为打开自动发送请求，false为关闭自动发送请求
      if (error.message.includes("timeout")) {
        return true;
      } else {
        return false;
      }
    },
  });

  // 发送请求
  axios({
    method: inputMethod,
    // url: inputUrl + inputApi + "/", //不加斜杠报错301
    url: inputUrl + inputApi, // 有些api不要斜杠，如user_id
    data: inputData,
    headers: inputHeaders,
    timeout: inputTimeout,
  })
    .then((res) => {
      inputFuncGetRes(res.data);
    })
    .catch((err) => {
      console.log("api_axios get error : ", err);
      inputFuncGetErr(err);
    });
}

/**
 * axios本地函数，向本地服务器发送请求
 * @param {string}  inputApi        api名，带斜杠，如"oi_r/"
 * @param {string}  inputMethod     "get" / "put" / "post" ...
 * @param {object}  inputData       body；default = {}
 * @param {function} inputFuncGetRes callback，获取返回值；default = printRes()
 * @param {function} inputFuncGetErr callback，获取错误信息；default = printRes()
 */
export function use_axios_local({
  inputApi,
  inputMethod,
  inputData = {},
  inputFuncGetRes = printRes,
  inputFuncGetErr = printRes,
}) {
  use_axios({
    inputUrl: conf.url.local,
    inputHeaders: {},
    inputApi,
    inputMethod,
    inputTimeout: 5000,
    inputRetry: 1,
    inputData: inputData,
    inputFuncGetRes: inputFuncGetRes,
    inputFuncGetErr: inputFuncGetErr,
  });
}
