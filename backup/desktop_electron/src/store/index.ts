import { createStore } from "vuex";

export default createStore({
  state: {
    config: {} as { [key: string]: any }
  },
  getters: {
    get_config(state) {
      return state.config
    }
  },
  mutations: {
    set_config(state, payload: { [key: string]: any }) {
      state.config[payload.key]["value"] = payload.value
    },
    init_config(state, payload: { [key: string]: any }) {
      state.config[payload.key] = payload.value
    }
  },
  actions: {},
  modules: {},
});
