<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <button @click="test()">CheckThis</button>
    <li>{{ text }}</li>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }, 
  data(){
    return{
      text: 'null'
    }
  },methods: {
    test(){
      axios.get('test')
            .then(res=>{
              this.text = res.data;
            })
            .catch(err=>{
              this.text = 'error' + err;
            })
      // this.text = 'nice!'
    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
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
