<template>
  <div class="login">
    <div class="bc">
        <h3 align="center" >登录</h3>
        <div class="loginbody">
          <el-image style="height:120px;width:350px" :src="'http://r.photo.store.qq.com/psc?/V143D3j445iBwL/45NBuzDIW489QBoVep5mcSvMd8hkV3G1vEW70bFpO7JTUQ723yi1Jhbhp1hlQxNVY0eXGtq17lrGf0NKyfp9YeeeHqL9wN2L3Mqqu7lECW8!/r'"></el-image>
          <el-form :model="ruleForm2" :rules="rules2" status-icon ref="ruleForm2">
            <el-form-item label-width="40px" style="width:310px" prop="username">
                <el-input type="text" v-model="ruleForm2.username" auto-complete="off" placeholder="用户名"></el-input>
            </el-form-item>
            <el-form-item label-width="40px" style="width:310px" prop="password">
                <el-input type="password" v-model="ruleForm2.password" auto-complete="off" placeholder="密码"></el-input>
            </el-form-item >
            <el-form-item label-width="100px">
              <el-button type="primary" @click="handleSubmit" :loading="logining">登录</el-button>
              <el-button type="primary" @click="Guider" :loading="logining">返回</el-button>
            </el-form-item>
            <el-form-item label-width="105px" >
                <el-checkbox v-model="checked" class="rememberme">记住密码</el-checkbox>
                <el-button type="text" @click="forgetpassword">忘记密码</el-button>
            </el-form-item>
            <el-form-item label="还未注册？点击此处注册" label-width="270px">
                <el-button type="primary" @click="Regi" :loading="logining">注册</el-button>
            </el-form-item>
            
          </el-form>
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
        logining: false,
        ruleForm2: {
          username: '',
          password: ''
        },
        rules2: {
          account: [
            { required: true, message: '请输入账号', trigger: 'blur' },
          ],
          checkPass: [
            { required: true, message: '请输入密码', trigger: 'blur' },
          ]
        },
        checked: true
      };
    },
    methods: {
      Regi(){
        this.$router.push('/Regi')
      },
      Guider(){
        this.$router.push('/')
      },
      handleReset2() {
        this.$refs.ruleForm2.resetFields();
      },
      handleSubmit(ev) {
        this.$refs.ruleForm2.validate((valid) => {
          if (valid) {
            this.logining = true;
            axios({
                method: 'post',
                url: 'http://localhost:8000/api/login/',
                data: {'username': this.ruleForm2.username, 'password': this.ruleForm2.password}
            })
            .then(response => {
                console.log(response)
                if(response.data.code===200){
                    localStorage.setItem('username', this.ruleForm2.username);
                    this.$router.push('/')
                }
                else if(response.data.code===400){
                    alert('账号或密码错误')
                    this.$router.go(0)
                }
                else{
                    alert('错误')
                    this.$router.go(0)
                }
            })
            .catch(error => {
                console.log(error)
                alert('出现错误')
                this.$router.go(0)
            })
          } else {
            alert('登录失败');
            return false;
          }
        });
      },
      forgetpassword(){
          this.$alert( '提示', {
          confirmButtonText: '确定',
          type: 'warning'
        })
      }
    }
  }
</script>

<style>
.login
{
    width:100%;
    height:100%;
    z-index:-1;
    position:fixed;
    background-image:url("../assets/login.png");
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
	border-radius:15px;
  margin: 50px auto;
  width: 350px;
}
</style>