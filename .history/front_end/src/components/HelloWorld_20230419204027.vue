<template>
    <div>
      <h1>{{ title }}</h1>
      <p>{{ message }}</p>
    </div>
  </template>
  
  <script>
  export default {
    name: 'HelloWorld',
    data() {
      return {
        title: 'Hello, world!',
        message: 'Welcome to my app'
      }
    }
  }
  </script>
  