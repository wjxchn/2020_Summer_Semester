<template>
  <div class="login">
    <el-container class="mid">
      <el-main class="bc">
        <h3 align="center" >登录</h3>
      <el-image style="height:100px;width:300px" :src="'http://r.photo.store.qq.com/psc?/V143D3j445iBwL/45NBuzDIW489QBoVep5mcSvMd8hkV3G1vEW70bFpO7JTUQ723yi1Jhbhp1hlQxNVY0eXGtq17lrGf0NKyfp9YeeeHqL9wN2L3Mqqu7lECW8!/r'"></el-image>
        <el-form :model="ruleForm2" :rules="rules2" status-icon ref="ruleForm2" label-width="50px" >
            <el-form-item prop="username">
                <el-input style="width:200px" type="text" v-model="ruleForm2.username" auto-complete="off" placeholder="用户名"></el-input>
            </el-form-item>
            <el-form-item style="width:250px" prop="password">
                <el-input type="password" v-model="ruleForm2.password" auto-complete="off" placeholder="密码"></el-input>
            </el-form-item>
            <el-form-item style="width:200px">
                <el-button type="primary" style="width:200px" @click="handleSubmit" :loading="logining">登录</el-button>
            </el-form-item>
            <el-form-item style="width:200px">
                <el-button type="primary" style="width:200px" @click="Regi" :loading="logining">注册</el-button>
            </el-form-item>
            <el-form-item style="width:200px">
                <el-button type="primary" style="width:200px" @click="Guider" :loading="logining">返回</el-button>
            </el-form-item>
            <el-form-item >
                <el-checkbox v-model="checked" class="rememberme">记住密码</el-checkbox>
                <el-button type="text" @click="forgetpassword">忘记密码</el-button>
            </el-form-item>
      </el-form>
    </el-main>
  </el-container>
</div>
</template>

<script>
export default {
  data() {
    return {
        logining: false,
        ruleForm2: {
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
            var loginParams = { username: this.ruleForm2.username, password: this.ruleForm2.password, identifycode: this.ruleForm2.identifycode };
            requestLogin(loginParams).then(data => {
              this.logining = false;
              let { msg, code, user } = data;
             
            });
          } else {
            console.log('error submit!!');
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
	background-color:white;
	margin-left:41%;
	margin-right:40%;
	margin-top:2%;
	position: fixed;
	border-radius:15px;
}

</style>