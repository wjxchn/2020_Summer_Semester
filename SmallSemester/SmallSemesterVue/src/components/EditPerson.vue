<template>
    <div>
        <Guider id="navBar" :class="{isFixed:istabBar}"/>
        <el-container>
            <el-aside class="leftside" width="210px">

            <!--     ↓↓↓↓↓↓↓↓↓↓↓↓↓↓  这个default-active是指当前激活的页面，把页面对应的index写进去，例如：当前页面是我的文档，则写进去2-1 -->
            <el-menu default-active="2-1" class="el-menu-vertical-demo" :default-openeds="opend"
            @open="handleOpen" @close="handleClose" background-color="#fff"
            text-color="#000000" active-text-color="#f96332" >
            <el-submenu index="1">
                <template slot="title">
                    <i class="el-icon-menu"></i>
                    <span>工作台</span>
                </template>
                    <el-menu-item index="1-1" @click="Mywork" :loading="logining"><i class="el-icon-notebook-2" style="color:black"></i>我的文档</el-menu-item>
                    <el-menu-item index="1-2" @click="Myteam" :loading="logining"><i class="el-icon-set-up" style="color:black"></i>我的团队</el-menu-item>
                    <el-menu-item index="1-3" @click="MyFavorite" :loading="logining"><i class="el-icon-star-off" style="color:black"></i>我的收藏</el-menu-item>
                    <el-menu-item index="1-4" @click="Trash" :loading="logining"><i class="el-icon-delete" style="color:black"></i>回收站</el-menu-item>
                    <el-menu-item index="1-5" @click="Message" :loading="logining"><i class="el-icon-chat-dot-round" style="color:black"></i>收件箱</el-menu-item>
            </el-submenu>
            <el-submenu index="2">
                <template slot="title">
                    <i class="el-icon-s-home"></i>
                    <span>个人信息</span>
                </template>
                    <el-menu-item index="2-1" @click="Person" :loading="logining"><i class="el-icon-user" style="color:black"></i>个人资料</el-menu-item>
            </el-submenu>
            <el-submenu index="3">
                <template slot="title">
                    <i class="el-icon-s-opportunity"></i>
                    <span>其他</span>
                </template>
                    <el-menu-item index="3-1" @click="Help" :loading="logining"><i class="el-icon-view" style="color:black"></i>帮助</el-menu-item>
                    <el-menu-item index="3-2" @click="Aboutus" :loading="logining"><i class="el-icon-link" style="color:black"></i>开发者信息</el-menu-item>
            </el-submenu>
            </el-menu>
            </el-aside>
        <el-container>
        <main id="mainPart" role="main" class="container" color="black">

    <!-- 页面内部的内容写在main中间即可 -->
        <div class="header">
            <el-breadcrumb separator-class="el-icon-arrow-right">
            <el-breadcrumb-item :to="{ path: '/Person' }">个人资料</el-breadcrumb-item>
            <el-breadcrumb-item>编辑个人信息</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="block">
            <el-row >
                <el-col  span="4" >
                    <el-avatar shape="square" :size="150" :src="circleUrl"></el-avatar>
                </el-col> 
                <el-col class="eman" span="6" > 
                    <h2 :value="showusername">{{showusername}}</h2>
                </el-col>
            </el-row>
        </div>
        <el-card>
            <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" style="width:500px" class="demo-ruleForm">
            <el-form-item label="姓名" prop="name" >
                <el-input v-model="ruleForm.name" clearable></el-input>
            </el-form-item>
            <el-form-item label="性别" prop="region">
                <el-select v-model="ruleForm.region" placeholder="请选择性别">
                <el-option label="男" value="男"></el-option>
                <el-option label="女" value="女"></el-option>
                <el-option label="不公开" value="不公开"></el-option>
                </el-select>
            </el-form-item>
            <el-form-item label="生日" required>
                <el-form-item prop="date1">
                <el-date-picker type="date" placeholder="选择日期" v-model="ruleForm.date1" format="yyyy 年 MM 月 dd 日" value-format="yyyy-MM-dd" style="width: 100%;"></el-date-picker>
            </el-form-item>
            </el-form-item>
            <el-form-item label="邮箱" prop="email" >
                <el-input v-model="ruleForm.email" clearable></el-input>
            </el-form-item>
            <el-form-item label="个人简介" prop="desc">
                <el-input type="textarea" v-model="ruleForm.desc" clearable></el-input>
            </el-form-item>
            <el-form-item>
                <el-button style="background-color:#f96332;color:white" @click="submitForm">保存</el-button>
                <el-button style="background-color:#f96332;color:white" @click="Return">返回</el-button>
            </el-form-item>
</el-form>
        </el-card>
        </main>
        </el-container>
        </el-container>
        <BottomGuider/>
    </div>
</template>

<script>
import Guider from '../components/Guider'
import BottomGuider from '../components/BottomGuider'
import axios from 'axios'
export default {
    name: 'PageDemo',
    components: {
        Guider,
        BottomGuider
    },
    data () {
       return {
            showusername: '',
            circleUrl: "http://r.photo.store.qq.com/psc?/V143D3j445iBwL/ubiEST8aMMlZjEEUGVmWIvQRktHhz2iAdR3J.A4nqij8aa0.iu6BoAsF9QicJOl2HSbaNWgM8nnAiFqjhgVj6jpHhRfm2MRX08O2SAq4NIQ!/r",
            opend:['1','2','3'],
            uniqueOpened:false,
            istabBar: false,
            ruleForm: {
                name: '',
                region: '',
                date1: '',
                email: '',
                delivery: false,
                type: [],
                desc: ''
            },
            rules: {
                name: [
                    { required: true, message: '请输入姓名', trigger: 'blur' },
                    { min: 3, max: 5, message: '长度在 3 到 5 个字符', trigger: 'blur' }
                ],
                region: [
                    { required: true, message: '请选择性别', trigger: 'change' }
                ],
                date1: [
                    { required: true, message: '请选择日期', trigger: 'change' }
                ],
                email:[
                    { type:'email',required:true,message:'请输入邮箱',trigger:'blur'}
                ],
                desc: [
                    { required: true, message: '请填写个人简介', trigger: 'blur' }
                ]
            }
        }
    },
    methods: {
        //
        Return(){
            this.$router.push('/Person');
        },
        //侧边栏的跳转
        handleOpen(key, keyPath) {
            console.log(key, keyPath);
        },
        handleClose(key, keyPath) {
            console.log(key, keyPath);
        },
        Home(){
            this.$router.push('/');
        },
        Person(){
            this.$router.push('/Person');
        },
        Mywork(){
            this.$router.push('/Personaldoc');
        },
        Myteam(){
            this.$router.push('/Team');
        },
        MyFavorite(){
            this.$router.push('/MyFavoriteDoc');
        },
        TeamM(){
            this.$router.push('/TeamManagement');
        },
        Trash(){
            this.$router.push('/Trash');
        },
        Message(){
            this.$router.push('/Message');
        },
        Help(){
            this.$router.push('/Help');
        },
        Aboutus(){
            this.$router.push('/Aboutus');
        },
        // 添加一个方法 兼容
        handleScroll () {
            let scrollTop = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop;
                    
                // 固定导航栏
                let navBar = document.querySelector("#navBar");
                let mainPart = document.querySelector("#mainPart");
                if (scrollTop > 0){
                    this.istabBar = true
                    mainPart.style.paddingTop = navBar.offsetHeight + "px";
                } else {
                    this.istabBar = false
                    mainPart.style.paddingTop = "0px";
                }
        },
        submitForm () {
            axios({
                method: 'POST',
                url: 'http://localhost:8000/api/changepersonalintro/',
                data: {'username': localStorage.getItem('username'), 'email': this.ruleForm.email, 'sex': this.ruleForm.region, 'birthday': this.ruleForm.date1,
                        'intro': this.ruleForm.desc, 'name': this.ruleForm.name}
            })
            .then(response =>{
                if(response.data.code === 400){
                    alert('修改个人资料失败')
                    this.$router.go(0)
                }
                else if(response.data.code === 200){
                    alert('修改个人资料成功')
                    this.$router.push('/person')
                }
                else{
                    alert('错误')
                    this.$router.go(0)
                }

            })
            .catch(error =>{
                alert('错误')
                this.$router.go(0)
            })
        }
    },
    created: function(){
        axios({
            method: 'post',
            url: 'http://localhost:8000/api/showpersonalintro/',
            data: {'username': localStorage.getItem('username')}
        })
        .then(response => {
            console.log(response)
            if(response.data.code === 400){
                alert('加载个人资料失败')
                this.$router.go(0)                
            }
            else if(response.data.code === 200){
                this.$set(this, 'showusername', response.data.username)
                this.ruleForm.name = response.data.name
                this.ruleForm.region = response.data.sex
                this.ruleForm.date1 = response.data.birthday
                this.ruleForm.email = response.data.email
                this.ruleForm.desc = response.data.intro
            }
            else{
                alert('错误')
                this.$router.go(0)
            }
        })
        .catch(error => {
            console.log(error)
            alert('错误')
            this.$router.go(0)
        })             
    },
    mounted () {
        window.addEventListener('scroll', this.handleScroll); // Dom树加载完毕
    },
    destroyed () {
        window.removeEventListener('scroll', this.handleScroll) // 销毁页面时清除
    }
}
</script>

<style scoped>
.header{
    margin-top:10px;
}
.block{
    margin-top:10px;
}
.isFixed {
    position: fixed;
    top: 0;
    z-index: 10;
}
#navBar {
    width: 100%;
    background-color: #f96332;
    backdrop-filter: blur(30px);
}
#mainPart {
    width: 100%;
}

</style>