<template>
  <div id="app">
    <h1>{{$route.meta.title}}</h1>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',

  created(){
    console.log(this.$route)
  },
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
