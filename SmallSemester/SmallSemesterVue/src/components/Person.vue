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
        <main id="mainPart" role="main" class="container">
            <div class="div1">
                <div class="div2">
                        <div class="block" v-for="fit in fits" :key="fit">
                            <el-image
                            style="width: 100%;height:200px"
                            :src="backgroundurl"
                            :fit="fit"></el-image>
                        </div>
                       
                        <el-dialog title="上传封面照片" :visible.sync="sendCoverVisible">
                            <ImgCutter
                                ref="imgCutterModal"
                                label="Crop local pictures"
                                :crossOrigin="true"
                                crossOriginHeader="*"
                                rate=""
                                toolBgc="none"
                                :isModal="false"
                                :showChooseBtn="true"
                                :lockScroll="true"
                                :boxWidth="545"
                                :boxHeight="458"
                                :cutWidth="250"
                                :cutHeight="250"
                                :sizeChange="true"
                                :moveAble="true"
                                :originalGraph="false"
                                @cutDown="cutDownCover">
                                <div class="btn btn-primary" slot="open">剪裁本地背景图片</div>
                            </ImgCutter>
                        </el-dialog>
                        <el-dialog title="上传头像照片" :visible.sync="sendProfileVisible">
                            <ImgCutter
                                ref="imgCutterModal"
                                label="Crop local pictures"
                                :crossOrigin="true"
                                crossOriginHeader="*"
                                rate=""
                                toolBgc="none"
                                :isModal="false"
                                :showChooseBtn="true"
                                :lockScroll="true"
                                :boxWidth="545"
                                :boxHeight="458"
                                :cutWidth="250"
                                :cutHeight="250"
                                :sizeChange="true"
                                :moveAble="true"
                                :originalGraph="false"
                                @cutDown="cutDownProfile">
                                <div class="btn btn-primary" slot="open">剪裁本地背景图片</div>
                            </ImgCutter>
                        </el-dialog>
                    <div class="block1">
                    <el-row >
                            <el-col  span="4" >
                                <el-avatar shape="square" :size="150" :src="circleUrl"></el-avatar>
                            </el-col> 
                            <el-col class="eman" span="10" > 
                                <h2 :value="showusername">{{showusername}}</h2>
                            </el-col>
                            <el-col class="edit" span="3" > 
                                <el-button style="background-color:#f96332;color:white"  round @click="EditPerson" :loading="logining">编辑个人信息</el-button>
                            </el-col>
                            <el-col class="edit" span="3.5" > 
                                <el-button style="background-color:#f96332;color:white"  round @click="sendCoverVisible = true" plain ><i class="el-icon-camera" style="color:white" ></i>上传封面图片</el-button>
                            </el-col>
                            <el-col class="edit" span="3.5" >    
                                <el-button style="background-color:#f96332;color:white"  round @click="sendProfileVisible = true" plain ><i class="el-icon-camera" style="color:white" ></i>上传头像图片</el-button>
                            </el-col>
                            
                        </el-row>
                    </div>
                </div>
                <div class="div3" >
                     <el-card class="box-card" style="width:100%;box-shadow:0px 0px  10px 5px #aaa;">
                        <div slot="header" >
                            <span>个人简介</span>
                         </div>   
                                <div style="height:10px;background-color:transparent"></div>

                                <el-input clearable v-model="input" :disabled="true" placeholder="请输入内容"></el-input>
                        
                        
                    </el-card>
                </div>
                 <div class="div4">
                    <el-card class="box-card" style="width:100%;box-shadow:0px 0px  10px 5px #aaa;">
                        <div slot="header">
                            <span>个人信息</span>
                        </div>
                        <div style="width:30%;height:100%;float:left">
                            <el-table :data="tableData1" style="width: 100%">
                                <el-table-column prop="info" label=""></el-table-column>
                            </el-table>
                        </div>

                        <div style="width:70%;height:100%;float:right">
                            <el-table :data="tableData2" style="width: 100%">
                                <el-table-column prop="info" label=""></el-table-column>
                            </el-table>
                        </div>
                   
                    </el-card>
                </div>

            </div>
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
import ImgCutter from 'vue-img-cutter'
export default {
    name: 'PageDemo',
    components: {
        Guider,
        BottomGuider,
        ImgCutter
    },
    data () {
        return {
            input: '',
            opend:['1','2','3'],
            uniqueOpened:false,
            tableData: [],
            tableData1: [{info:"姓名"},{info:"性别"},{info:"生日"},{info:"电子邮箱"}],
            tableData2: [],
            circleUrl: "http://r.photo.store.qq.com/psc?/V143D3j445iBwL/ubiEST8aMMlZjEEUGVmWIvQRktHhz2iAdR3J.A4nqij8aa0.iu6BoAsF9QicJOl2HSbaNWgM8nnAiFqjhgVj6jpHhRfm2MRX08O2SAq4NIQ!/r",
            showusername:"这里是用户昵称",
            istabBar: false,
            sendCoverVisible: false,
            sendProfileVisible: false,
            fits: ['fill'],
            backgroundurl: "http://r.photo.store.qq.com/psc?/V52Qutst1Ze0TP0BqSlg0Ogc8N1lTYZp/45NBuzDIW489QBoVep5mcWCQKX9WHhAARbvjDHbE5p080qFMB3PE9EKYZm4ixFpGpOz2LgI6LvNURNSZH29x.*XMFGLDpA3riSY4BnJRS8k!/r"
        }
        
    },
    methods: {
        //侧边栏的跳转
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
        //
        EditPerson(){
            this.$router.push('/EditPerson');
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
        cutDownCover(res){
            let imgSrc = res.dataURL;
            console.log(imgSrc);//输出为base64数据
            axios({
                method: 'post',
                url: 'http://localhost:8000/api/addbackgroundphoto/',
                data: { 'username': localStorage.getItem('username'), 'backgroundphotodata': imgSrc}
            })
            .then(response => {
                if(response.data.code === 200){
                    alert('添加背景图片成功，请手动刷新')
                }
                else if(response.data.code === 400){
                    alert('添加背景图片失败')
                }
                else{
                    alert('错误')
                }
            })
            .catch(error => {
                alert('出现错误')
            })
            this.sendCoverVisible = false                       
        },
        cutDownProfile(res){
            let imgSrc = res.dataURL;
            console.log(imgSrc);//输出为base64数据
            axios({
                method: 'post',
                url: 'http://localhost:8000/api/addprofilephoto/',
                data: { 'username': localStorage.getItem('username'), 'profilephotodata': imgSrc}
            })
            .then(response => {
                if(response.data.code === 200){
                    alert('添加头像图片成功，请手动刷新')
                }
                else if(response.data.code === 400){
                    alert('添加头像图片失败')
                }
                else{
                    alert('错误')
                }
            })
            .catch(error => {
                alert('出现错误')
            })
            this.sendProfileVisible = false                       
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
                this.$set(this, 'tableData', response.data)
                this.$set(this, 'showusername', localStorage.getItem('username'))
                this.$set(this, 'input', response.data.intro)
                this.tableData2 = [{'info': response.data.name}, {'info': response.data.sex}, {'info': response.data.birthday}, {'info': response.data.email}]
                console.log(this.tableData)
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
        });
        axios({
            method: 'post',
            url: 'http://localhost:8000/api/showbackgroundphoto/',
            data: {'username': localStorage.getItem('username')}
        })
        .then(response => {
            console.log(response)
            if(response.data.code === 400){
                alert('加载背景图片失败')
                this.$router.go(0)                
            }
            else if(response.data.code === 200){
                this.$set(this, 'backgroundurl', response.data.backgroundphotodata)
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
        });
        axios({
            method: 'post',
            url: 'http://localhost:8000/api/showprofilephoto/',
            data: {'username': localStorage.getItem('username')}
        })
        .then(response => {
            console.log(response)
            if(response.data.code === 400){
                alert('加载背景图片失败')
                this.$router.go(0)                
            }
            else if(response.data.code === 200){
                this.$set(this, 'circleUrl', response.data.profilephotodata)
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
        });          
    },
    mounted () {
        window.addEventListener('scroll', this.handleScroll); // Dom树加载完毕
    },
    destroyed () {
        window.removeEventListener('scroll', this.handleScroll) // 销毁页面时清除
    }
        
}
</script>

<style>
.block1{
    margin-top:-100px;
    padding-left:20px;
}
.eman{
    padding-top:105px;
}
.edit{
    padding-top:100px;
    float:right;
}

*{
    margin:0;
}
.div1{
    border:20px solid transparent;
    width:100%;
    height:1000px;
    background-color: transparent;
}
.div2{
    margin-top: 10px;
    width:100%;
    height:280px;
    background-color: transparent;
}
.div3{
    float:left;
    margin-top: 10px;
    width:69%;
    height:720px;
    background-color:transparent;
}
.div4{
    float:right;
    margin-top: 10px;
    width:30%;
    height:720px;
    background-color: transparent;
}

.picture{

    background-image: url("../assets/timg.jpg");
    background-size: 100% 100%;

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
