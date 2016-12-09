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
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
