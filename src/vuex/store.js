import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

const state = {
  foo: 0
};

const mutations = {
  SAMPLE_MUTATION (state) {
    state.foo++;
  }
};

export default new Vuex.Store({
  state,
  mutations
});
