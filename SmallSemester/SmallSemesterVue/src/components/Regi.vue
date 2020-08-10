<template>
<div class="regi">
	<h1 align="center" style="color:white;">欢迎注册福报文档</h1>
    <el-container class="mid">
		<el-main class="bc">
			<el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="80px" class="demo-ruleForm">
				<el-form-item  label="用户名" prop="name">
					<el-input style="width:200px"  v-model="ruleForm.name"></el-input></el-form-item>
				<el-form-item label="密码" prop="pass">
					<el-input type="password" style="width:200px"  v-model="ruleForm.pass" auto-complete="off"></el-input></el-form-item>
				<el-form-item label="确认密码" prop="checkPass">
					<el-input type="password" style="width:200px"  v-model="ruleForm.checkPass" auto-complete="off"></el-input></el-form-item>
				<el-form-item label="电子邮箱" prop="checkPass">
					<el-input type="email" style="width:200px"  v-model="ruleForm.email" auto-complete="off"></el-input></el-form-item>
				<el-form-item>
					<el-button type="primary" @click="submitForm('ruleForm')">注册</el-button>
					<el-button @click="resetForm('ruleForm')">重置</el-button>
				</el-form-item>
			</el-form>
		</el-main>
	</el-container>
</div>
</template>
 
<script>
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
 
		return {
			activeName: 'second',
			ruleForm: {
				name: '',
				pass: '',
				checkPass: ''
			},
			rules: {
				name: [{ required: true, message: '请输入您的名称', trigger: 'blur' }, { min: 2, max: 5, message: '长度在 2 到 5 个字符', trigger: 'blur' }],
				pass: [{ required: true, validator: validatePass, trigger: 'blur' }],
				checkPass: [{ required: true, validator: validatePass2, trigger: 'blur' }]
			}
		};
	},
 
	methods: {
		submitForm(formName) {
			this.$refs[formName].validate(valid => {
				if (valid) {
					this.$message({
						type: 'success',
						message: '注册成功'
					});
				} else {
					console.log('注册失败');
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
	background-color:white;
	margin-left:41%;
	margin-right:40%;
	margin-top:2%;
	position: fixed;
	border-radius:15px;
}

</style>