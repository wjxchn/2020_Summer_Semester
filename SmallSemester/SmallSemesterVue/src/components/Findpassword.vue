<template>
  <div class="login">
    <div class="hed" style="text-align:center">
      <el-image style="height:120px;width:405px" :src="'http://r.photo.store.qq.com/psc?/V143D3j445iBwL/45NBuzDIW489QBoVep5mcVXyL*BsvZygoyXkXSowchA7gJ2NMBMBsOjMwY5piqegdZCDtFL6KmYG89tApO1qbCXbnAYUG9HzopHGRYUR1HI!/r'"></el-image>
      <h1 style="color:#f96332" >找回密码</h1>
    </div>
    <div class="bc">
          <el-form :model="ruleForm2" :rules="rules2" status-icon ref="ruleForm2">
            <el-form-item label-width="40px" style="width:310px" prop="username">
                <el-input v-model="ruleForm2.username" type="text" auto-complete="off" placeholder="用户名"></el-input>
            </el-form-item>
            <el-form-item label-width="40px" style="width:310px" prop="email">
                <el-input v-model="ruleForm2.email" style="width:60%;float:left" type="email" auto-complete="off" placeholder="邮箱"></el-input>
                <el-button style="background-color:#f96332;color:white;width:40%;float:left" @click="sendverifycode">发送验证码</el-button>
            </el-form-item>
            <el-form-item label-width="40px" style="width:310px" prop="verifycode">
                <el-input v-model="ruleForm2.verifycode" type="text" auto-complete="off" placeholder="验证码"></el-input>
            </el-form-item>
            <el-form-item label-width="40px" style="width:310px" prop="newpassword">
                <el-input v-model="ruleForm2.newpassword" type="password" auto-complete="off" placeholder="新密码"></el-input>
            </el-form-item > 
            <el-form-item label-width="40px" style="width:310px" prop="checkpassword">
                <el-input v-model="ruleForm2.checkpassword" type="password2"  auto-complete="off" placeholder="重复密码"></el-input>
            </el-form-item > 
            <el-form-item label-width="20px" style="width:400px">
              <el-button style="background-color:#f96332;color:white;" @click="changepassword">确认更改</el-button>
              <el-button style="background-color:#f96332;color:white;" @click="Return" >返回</el-button>
              <el-button style="background-color:#f96332;color:white;" @click="Login" >直接登录</el-button>
            </el-form-item>
          </el-form>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      logining: false,
      checked: true,
      ruleForm2: {
        username: '',
        email: '',
        verifycode: '',
        newpassword: '',
        checkpassword: ''
      },
      rules2: {
        username: [
          { required: true, message: '请输入用户名', trigger: 'blur' },
        ],
        email: [
          { required: true, message: '请输入邮箱', trigger: 'blur' },
        ],
        verifycode: [
          { required: true, message: '请输入验证码', trigger: 'blur' },
        ],
        newpassword: [
          { required: true, message: '请输入新密码', trigger: 'blur' },
        ],
        checkpassword: [
          { required: true, message: '请输入验证密码', trigger: 'blur' },
        ]
      }
    };
  },
  methods: {
    Return(){
      this.$router.push('/')
    },
    Login(){
      this.$router.push('/Login')
    },
    sendverifycode(){
      axios({
        method: 'post',
        url: 'http://localhost:8000/api/sendverifycode/',
        data:{ 'username': this.ruleForm2.username, 'email': this.ruleForm2.email}
      })
      .then(response => {
        if(response.data.code === 200){
          alert('发送验证码成功')
        }
        else if(response.data.code === 400){
          alert('发送验证码失败')
        }
        else{
          alert('发送验证码错误')
        }
      })
      .catch(error => {
        alert('错误')
      })
    },
    changepassword(){
      axios({
        method: 'post',
        url: 'http://localhost:8000/api/changepassword/',
        data:{ 'username': this.ruleForm2.username, 'email': this.ruleForm2.email, 'verifycode': this.ruleForm2.verifycode, 'newpassword': this.ruleForm2.newpassword, 'checkpassword': this.ruleForm2.checkpassword}
      })
      .then(response => {
        if(response.data.code === 200){
          alert('修改密码成功')
          this.$router.push('/login')
        }
        else if(response.data.code === 401){
          alert('两次密码不相同')
        }
        else if(response.data.code === 402){
          alert('输入信息有误')
        }
        else if(response.data.code === 403){
          alert('验证码错误')
        }
        else if(response.data.code === 410){
          alert('验证码超时')
        }
        else{
          alert('发送验证码错误')
        }
      })
      .catch(error => {
        alert('错误')
      })
    }
  }
}
</script>

<style scoped>
.el-checkbox__input is checked{
  fill:#f96332;
  border-color:#f96332;
  color:#f96332;
}
.login
{
    width:100%;
    height:100%;
    z-index:-1;
    position:fixed;
	  background-color:#f7f7f7;
    position: fixed;
    background-size: 100% 100%;
    overflow-y: auto;
}
.mid
{
	height:100%;
}
.bc
{
 background-color: rgba(255, 255, 255, 0.7);
    border-radius:50px;
	padding-top:2%;
	padding-bottom:1%;
	padding-left:3.5%;
    margin: 3% auto;
    width: 500px;
}
</style>
