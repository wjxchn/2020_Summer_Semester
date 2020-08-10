<template>
    <div class="login">
        <el-form :model="ruleForm2" :rules="rules2"
         status-icon
         ref="ruleForm2" 
         label-position="left" 
         label-width="0px" 
         class="demo-ruleForm login-page">
            <h3 class="title">登录平台</h3>
            <el-form-item prop="username">
                <el-input style="width:200px" type="text" 
                    v-model="ruleForm2.username" 
                    auto-complete="off" 
                    placeholder="用户名"></el-input>
            </el-form-item>
            <el-form-item style="width:200px" prop="password">
                <el-input type="password" 
                    v-model="ruleForm2.password" 
                    auto-complete="off" 
                    placeholder="密码"></el-input>
            </el-form-item>
            <el-form-item style="width:200px">
                <el-button type="primary" style="width:200px" @click="handleSubmit" :loading="logining">登录</el-button>
            </el-form-item>
            <el-form-item >
                <el-checkbox 
                    v-model="checked"
                    class="rememberme">记住密码</el-checkbox>
                <el-button type="text" @click="forgetpassword">忘记密码</el-button>
            </el-form-item>
            
        </el-form>
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
              if (code !== 200) {
                this.$message({
                  message: msg,
                  type: 'error'
                });
              } else {
                if (user.type === "admin"){
                    sessionStorage.setItem('user', JSON.stringify(user));
                    this.$router.push({ path: '/homepage' });
                } else if (user.type === "advert") {
                    sessionStorage.setItem('user', JSON.stringify(user));
                    this.$router.push({ path: '/table' });
                }
              }
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
    label.el-checkbox.rememberme {
        margin: 0px 0px 15px;
        text-align: left;
    }
    label.el-button.forget {
        margin: 0;
        padding: 0;
        border: 1px solid transparent;
        outline: none;
    }
</style>