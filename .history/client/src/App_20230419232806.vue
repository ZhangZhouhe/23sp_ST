<template>
    <div id="app">
        <p>{{ greeting }}</p>
        <p>{{ flaskGreeting }}</p>
    </div>
</template>
<script>
import HelloWorld from './components/HelloWorld.vue'
export default {
    name: 'App',
    components: {
        HelloWorld
    },
    data: function(){
        return {
            greeting: 'Hello, Vue!',
            flaskGreeting: ""
        }
    },
    created: async function(){
        const gResponse = await fetch("http://localhost:5000/greeting");
        const gObject = await gResponse.json();
        this.flaskGreeting = gObject.greeting;
    }
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
