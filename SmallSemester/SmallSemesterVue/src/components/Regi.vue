<template>
<div class="regi">
    <div class="bc">
		<h3 align="center" >加入我们</h3>
		<el-image style="height:120px;width:350px" :src="'http://r.photo.store.qq.com/psc?/V143D3j445iBwL/45NBuzDIW489QBoVep5mcSvMd8hkV3G1vEW70bFpO7JTUQ723yi1Jhbhp1hlQxNVY0eXGtq17lrGf0NKyfp9YeeeHqL9wN2L3Mqqu7lECW8!/r'"></el-image>
		<el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="80px" class="demo-ruleForm">
			<el-form-item  label="用户名" prop="name">
				<el-input style="width:240px" v-model="ruleForm.name"></el-input></el-form-item>
			<el-form-item label="密码" prop="pass">
				<el-input type="password" style="width:240px" v-model="ruleForm.pass" auto-complete="off"></el-input></el-form-item>
			<el-form-item label="确认密码" prop="checkPass">
				<el-input type="password" style="width:240px" v-model="ruleForm.checkPass" auto-complete="off"></el-input></el-form-item>
			<el-form-item label="电子邮箱" prop="email">
				<el-input type="email" style="width:240px" v-model="ruleForm.email" auto-complete="off"></el-input></el-form-item>
			<el-form-item label-width="50px"><el-button-group >
		
				<el-button type="primary" style="width:82px" @click="submitForm('ruleForm')">注册</el-button>
				<el-button type="primary" style="width:82px" @click="resetForm('ruleForm')">重置</el-button>
				<el-button type="primary" style="width:82px" @click="Guider">返回</el-button>
			</el-button-group></el-form-item>
		</el-form>
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
    background-image:url("../assets/regi.png");
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