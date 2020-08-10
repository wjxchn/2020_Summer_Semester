<template>
  <div class="showplaintext">
    <h1>Example heading <span class="badge badge-secondary">New</span></h1>
    <span v-html="htmlData">
        {{htmlData}}
    </span>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'ShowPlainText',
  data(){
    return{
      htmlData: ''
    }
  },
  mounted:function () {
    axios({
      method: 'get',
      url: 'http://localhost:8000/api/getplaintext/',
    })
    .then(response=>{
      this.htmlData = response.data.content
    })
    .catch(error=>{
      console.log(error)
      alert('出现错误')
    })
  }
}
</script>

<style>
</style>