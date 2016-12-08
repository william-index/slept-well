import Vue from 'vue'
import Vuex from 'vuex'
import App from './App.vue'
import store from './vuex/store.js';


new Vue({
  el: '#app',
  render: h => h(App),
  store: store
})
