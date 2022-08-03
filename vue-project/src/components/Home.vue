<script lang="ts" setup>
  import { ref } from 'vue'
  import API from '../axios'
  import { ElLoading } from 'element-plus'
  import { ElMessageBox } from 'element-plus'
  
  const text=ref('')

  function fetch_link(){
    const loading = ElLoading.service({ fullscreen: true })
    API({method:'POST',url:'/download',data:{'url':text.value},responseType:'blob'})
    .then((res)=>{
      loading.close()
      const blob = new Blob([res.data]);
      const fileName = 'Result.pptx';
      const down = document.createElement('a');
      down.download = fileName;
      down.style.display = 'none';
      down.href = URL.createObjectURL(blob);
      document.body.appendChild(down);
      down.click();
      URL.revokeObjectURL(down.href);
      document.body.removeChild(down);
      ElMessageBox.alert('下载成功！','提示',{center:true})
      })
    .catch((error)=>{
      loading.close()
      ElMessageBox.alert('请输入正确的微信公众号网址', '错误',{center:true})
      });
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
  position: fixed;
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