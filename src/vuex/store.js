import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

const state = {
  foo: 'baz'
};

const mutations = {
  SAMPLE_MUTATION (state) {
    state.foo = 'bar';
  }
};

export default new Vuex.Store({
  state,
  mutations
});
