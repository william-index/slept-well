<template>
  <div id="app">
    <h1>{{ foo }}</h1>
    <button @click="testFoo">Click me</button>
  </div>
</template>

<script>
const methods = {};

methods.testFoo = function() {
  this.$store.commit('SAMPLE_MUTATION');
};

export default {
  name: 'app',
  data () {
    return {
      msg: 'message'
    }
  },
  methods: methods,
  computed: {
    foo () {
      return this.$store.state.foo
    }
  }
}
</script>Goku

<style>
</style>
