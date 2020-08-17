<template>
<div class="regi">
	<div class="hed" style="text-align:center">
		<el-image style="height:120px;width:405px" :src="'http://r.photo.store.qq.com/psc?/V143D3j445iBwL/45NBuzDIW489QBoVep5mcVXyL*BsvZygoyXkXSowchA7gJ2NMBMBsOjMwY5piqegdZCDtFL6KmYG89tApO1qbCXbnAYUG9HzopHGRYUR1HI!/r'"></el-image>
		<h1 style="color:#f96332" >注册</h1>
	</div>
	<div class="bc">
		<el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="80px" class="demo-ruleForm">
			<el-form-item  label="用户名" prop="name">
				<el-input style="width:240px" v-model="ruleForm.name"></el-input></el-form-item>
			<el-form-item label="密码" prop="pass">
				<el-input type="password" style="width:240px" v-model="ruleForm.pass" auto-complete="off"></el-input></el-form-item>
			<el-form-item label="确认密码" prop="checkPass">
				<el-input type="password" style="width:240px" v-model="ruleForm.checkPass" auto-complete="off"></el-input></el-form-item>
			<el-form-item label="电子邮箱" prop="email">
				<el-input type="email" style="width:240px" v-model="ruleForm.email" auto-complete="off"></el-input></el-form-item>
			<el-form-item label-width="78px"><el-button-group >
				
				<el-button style="background-color:#f96332;color:white;width:82px" @click="submitForm('ruleForm')">注册</el-button>
				<el-button style="background-color:#f96332;color:white;width:82px" @click="resetForm('ruleForm')">重置</el-button>
				<el-button style="background-color:#f96332;color:white;width:82px" @click="Guider">返回</el-button>
				
			</el-button-group>
			
			</el-form-item>
			<i >点击[注册]按钮表示已阅读并同意福报文档服务条款</i>
		</el-form>
		<div class="tz">已有账号？点击此处登录
			<el-button style="background-color:#f96332;color:white;width:82px" @click="Login" :loading="logining">登录</el-button>
		</div>
	</div>
</div>
</template>
 
<script>
import axios from 'axios'
export default {
	data() {
		var validatePass = (rule, value, callback) => {
			if (value === '') {
				callback(new Error('请输入密码'));
			} else {
				if (this.ruleForm.checkPass !== '') {
					this.$refs.ruleForm.validateField('checkPass');
				}
				callback();
			}
		};
		var validatePass2 = (rule, value, callback) => {
			if (value === '') {
				callback(new Error('请再次输入密码'));
			} else if (value !== this.ruleForm.pass) {
				callback(new Error('两次输入密码不一致!'));
			} else {
				callback();
			}
		};
		var validateEmail = (rule, value, callback) => {
        	if (value === '') {
          		callback(new Error('请正确填写邮箱'));
       		} else {
          	if (value !== '') { 
            	var reg=/^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/;
            	if(!reg.test(value)){
              	callback(new Error('请输入有效的邮箱'));
            	}
          	}
          	callback();
        }
    };
		return {
			activeName: 'second',
			ruleForm: {
				name: '',
				pass: '',
				checkPass: '',
				email: ''
			},
			rules: {
				name: [{ required: true, message: '请输入您的名称', trigger: 'blur' }, { min: 2, max: 5, message: '长度在 2 到 5 个字符', trigger: 'blur' }],
				pass: [{ required: true, validator: validatePass, trigger: 'blur' }],
				checkPass: [{ required: true, validator: validatePass2, trigger: 'blur' }],
				email:[{ required: true, validator: validateEmail, trigger: 'blur' }]
			},
			value:1
		};
	},
 
	methods: {
		Login(){
        	this.$router.push('/Login')
      	},
		Guider(){
			this.$router.push('/')
		},
		submitForm(formName) {
			this.$refs[formName].validate(valid => {
				if (valid) {
					axios({
						method: 'post',
						url: 'http://localhost:8000/api/createuser/',
						data: {'username': this.ruleForm.name, 'password': this.ruleForm.pass, 'email': this.ruleForm.email}
					})
					.then(response => {
						console.log(response)
						if(response.data.code === 200){
							this.$router.push('/login')
						}
						else{
							alert('用户已存在')
						}
					})
					.catch(error => {
						console.log(error)
						alert('出现错误')
					})					
				} else {
					alert('注册失败');
					return false;
				}
			});
		},
		resetForm(formName) {
			this.$refs[formName].resetFields();
		}
	}
};
</script>
<style scoped>
.regi
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
.tz{
	height:70px;
	padding-top:7%;
	padding-left:35%;
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