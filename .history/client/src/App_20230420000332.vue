<template>
    <el-button type="primary">Primary</el-button>
    <HelloWorld msg="hi"/>
</template>
<script>
import HelloWorld from './components/HelloWorld.vue'
export default{
    name:'App',
    componets:{
        HelloWorld
    }
}
</script>
