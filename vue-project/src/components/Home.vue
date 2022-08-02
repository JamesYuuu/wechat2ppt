<script lang="ts" setup>
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  
  const link=ref([{}])
  const text=ref('')
  const router=useRouter()

  function fetch_link(){
    router.push({name:'select',params:{url:text.value}})
  }

  function reset(){
    text.value=''
  }
  
</script>

<template>
<div class="Input">
  <el-header> 请输入微信公众号网址 </el-header>

  <el-input v-model="text" clearable> </el-input>
  <el-row>
    <el-col :span="5"> </el-col> 
    <el-col :span="7"> <el-button @click="fetch_link" type="primary"> 确认 </el-button> </el-col>
    <el-col :span="5"> </el-col>
    <el-col :span="7"> <el-button @click="reset" type="danger"> 重置 </el-button> </el-col>
  </el-row>
</div>
</template>

<style>
.Input{
  position: absolute;
  left: 50%;
  top: 40%;
  transform: translate(-50%, -50%);
}
.el-input{
  width:800px;
  height:40px;
  font-size: large;
}
.el-header{
  font-size:xx-large;
  font-weight: bold;
  text-align:center;
}
.el-button{
  height: 40px;
  margin-top: 10px;
  font-size: large;
}
</style>