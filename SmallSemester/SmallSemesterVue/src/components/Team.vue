<template>
    <div>
        <Guider id="navBar" :class="{isFixed:istabBar}"/>
      <el-container>
            <el-aside class="leftside" width="210px">

            <!--     ↓↓↓↓↓↓↓↓↓↓↓↓↓↓  这个default-active是指当前激活的页面，把页面对应的index写进去，例如：当前页面是我的文档，则写进去2-1 -->
            <el-menu default-active="1-2" class="el-menu-vertical-demo" :default-openeds="opend"
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
        <main id="mainPart" role="main" class="container">
            <h5 style="padding:15px">我的团队</h5>
            <el-table
            :data="tableData"
            style="width: 100%">
            <el-table-column
                prop="group_name"
                label="组名"
                width="180">
            </el-table-column>
            <el-table-column
                prop="group_creator"
                label="组长"
                width="180">
            </el-table-column>
            <el-table-column
                prop="time"
                label="创建时间">
            </el-table-column>
            <el-table-column label="操作">
            <template slot-scope="scope">
                <el-button style="width:70px;background-color:#f96332;color:white"
                size="mini"  @click="toteam(scope.row)">管理</el-button>
                <el-button
                size="mini"
                type="danger" @click="leave(scope.row)">退出</el-button>
            </template>
            </el-table-column>
            </el-table>     
            <el-button style="width:100px;background-color:#f96332;color:white" @click="dialogFormVisible = true">创建团队</el-button>
            <el-dialog title="创建团队" :visible.sync="dialogFormVisible">
            <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
                <el-form-item label="团队名称" :label-width="formLabelWidth" prop="name" required>
                <el-input v-model="ruleForm.name"></el-input>
                </el-form-item>
                <el-form-item label="团队简介" :label-width="formLabelWidth" prop="introduction" required>
                <el-input type="textarea" v-model="ruleForm.introduction"></el-input>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button style="width:70px;background-color:#f96332;color:white" @click="dialogFormVisible = false">取 消</el-button>
                <el-button style="width:70px;background-color:#f96332;color:white" @click="submitForm('ruleForm',ruleForm),dialogFormVisible = false">确 定</el-button>
            </div>
            </el-dialog>

        </main>
        </el-container>
        </el-container>
        <BottomGuider/>
    </div>
</template>

<script>
import axios from 'axios'
import Guider from '../components/Guider'
import BottomGuider from '../components/BottomGuider'
export default {
    owner: 'PageDemo',
    components: {
        Guider,
        BottomGuider
    },
    data () {
        return {
            opend:['1','2','3'],
            uniqueOpened:false,
            dialogFormVisible:false,
            tableData: [],
            ruleForm:{
                name:'',
                introduction:''
            },
            rules:{
                name: [
                { required: true, message: '请输入团队名称', trigger: 'blur' },
                { min: 2, max: 15, message: '长度在 2 到 15 个字符', trigger: 'blur' }
            ],
                introduction:[
                    {required:true, message:'请输入团队简介', trigger:'blur'},
                    {min:5,max:50,message:'长度在 5 到 50 个字符',trigger:'blur'}
                ]
            },
            istabBar: false
        }
    },
    created:function(){
            axios({
                method: 'post',
                url: 'http://localhost:8000/api/showgrouplist/',
                data: {'username': localStorage.getItem('username')}
            })
            .then(response => {
                console.log(response)
                if(response.data.code===200){
                    this.$set(this,'tableData',response.data.grouplist)
                }
                else if(response.data.code===400){
                    alert('服务器错误')
                    this.$router.go(0)
                }
                else{
                    alert('错误')
                    this.$router.go(0)
                }
            })
    },
    methods: {
        handleOpen(key, keyPath) {
            console.log(key, keyPath);
        },
        handleClose(key, keyPath) {
            console.log(key, keyPath);
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
        toteam(row){
            console.log(row.group_id)//此时就能拿到整行的信息
            this.$router.push({path: '/teammanagement', query: {group_id: row.group_id, group_name: row.group_name}})
        },
        leave(row){
            console.log(row.group_id)
            axios({
                method: 'post',
                url: 'http://localhost:8000/api/leavegroup/',
                data: {'username': localStorage.getItem('username'),
                       'groupid':row.group_id}
            })
            .then(response => {
                console.log(response)
                if(response.data.code===200){
                    alert('退出团队成功')
                    this.$router.go(0)
                }
                else if(response.data.code===400){
                    alert('小组创建者无法退出团队')
                    this.$router.go(0)
                }
                else{
                    alert('错误')
                    this.$router.go(0)
                }
            })
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
        getNowDate(){
            let strTime=new Date();
            return strTime.getFullYear()+'/'+strTime.getMonth()+'/'+strTime.getDate()+' '+strTime.getHours()+':'+strTime.getMinutes()+':'+strTime.getSeconds();
        },
        addTeam(item){
            axios({
                method: 'post',
                url: 'http://localhost:8000/api/creategroup/',
                data: {'creater': localStorage.getItem('username'), 'name': this.ruleForm.name, 'introduction': this.ruleForm.introduction}
            })
            .then(response => {
                console.log(response)
                if(response.data.code===200){
                    alert('创建团队成功')
                    this.$router.go(0)
                }
                else if(response.data.code===400){
                    alert('创建团队失败')
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
            });            
        },
        getTeamList(){
            axios({
                method: 'post',
                url: 'http://localhost:8000/api/showgrouplist/',
                data: {'creater': localStorage.getItem('username')}
            })
            .then(response => {
                console.log(response)
                if(response.data.code===200){
                    this.tableData = response.data.grouplist
                }
                else if(response.data.code===400){
                    alert('加载团队列表失败')
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
            });
        },
        submitForm(formName,item){
            this.$refs[formName].validate((valid) => {
            if (valid) {
                this.addTeam(item);
                alert('提交成功');
            } else {
                console.log('提交失败');
                return false;
            }
            this.getTeamList();
            }); 

        },
        
    },
    mounted () {
        window.addEventListener('scroll', this.handleScroll); // Dom树加载完毕
    },
    destroyed () {
        window.removeEventListener('scroll', this.handleScroll) // 销毁页面时清除
    },
}
</script>

<style scoped>
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