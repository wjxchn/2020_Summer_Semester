<template>
    <div>
        <Guider id="navBar" :class="{isFixed:istabBar}"/>
        <el-container>
            <el-aside class="leftside" width="210px">

            <!--     ↓↓↓↓↓↓↓↓↓↓↓↓↓↓  这个default-active是指当前激活的页面，把页面对应的index写进去，例如：当前页面是我的文档，则写进去2-1 -->
            <el-menu default-active="1-5" class="el-menu-vertical-demo" :default-openeds="opend"
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
    <br>
    <el-tabs type="card">
        <el-tab-pane label="系统通知">
            <el-card class="box-card" v-for="(item) in SystemMessageData" :key="item" style="margin-bottom:20px">
            <div slot="header" class="clearfix">
                <span class="title" >{{item.MessageTitle}}</span>
                <span class="time">{{item.date}}</span>
            </div>
            <div class="text item" >
                {{ item.MessageContent }}
            </div>
        </el-card>
        </el-tab-pane>
        <el-tab-pane label="团队通知">
            <el-card class="box-card" v-for="(item) in TeamMessageData" :key="item" style="margin-bottom:20px">
            <div slot="header" class="clearfix">
                <span class="title" >{{item.MessageTitle}}</span>
                <span class="time">{{item.date}}</span>
            </div>
            <div class="text item" >
                {{ item.MessageContent }}
            </div>
            </el-card>
        </el-tab-pane>
        <el-tab-pane label="团队邀请">
            <el-card class="box-card" v-for="(item) in InvitationData" :key="item" style="margin-bottom:20px">
            <div slot="header" class="clearfix">
                <span class="title" >{{item.MessageTitle}}</span>
                <span class="time">{{item.date}}</span>
                <div v-if="item.notifytype == 4 " align="right">
                    <el-button type="primary" @click="accept(item.id)">接受</el-button>
                    <el-button type="danger" @click="ignore(item.id)">忽略</el-button>
                </div>
                <div v-if="item.notifytype == 5 " align="right">
                    <el-button type="info" disabled>已处理</el-button>
                </div>
            </div>
            <div class="text item" >
                {{ item.MessageContent }}
            </div>
            </el-card>
        </el-tab-pane>
        <el-tab-pane label="文档通知">
            <el-card class="box-card" v-for="(item) in SystemMessageData" :key="item" style="margin-bottom:20px">
                <div slot="header" class="clearfix">
                    <span class="title" >{{item.MessageTitle}}</span>
                    <span class="time">{{item.date}}</span>
                </div>
                <div class="text item" >
                    {{ item.MessageContent }}
                </div>
            </el-card>            
        </el-tab-pane>
        </el-tabs>
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
            opend:['1','2','3'],
            uniqueOpened:false,
            istabBar: false,
            SystemMessageData:[],
            TeamMessageData:[],
            DocumentMessageData:[],
            InvitationData:[]
        }
    },
    created:function(){
        axios({
            method:'post',
            url:'http://localhost:8000/api/getsystemmessage/',
            data:{'username':localStorage.getItem('username')}
        })
        .then(response => {
            console.log(response)
            if(response.data.code === 200){
                this.$set(this,'SystemMessageData',response.data.notifydata)
            }
            else{
                alert('错误')
            }
        })
        .catch(error => {
            alert('出现错误')
        });
        axios({
            method:'post',
            url:'http://localhost:8000/api/getteammessage/',
            data:{'username':localStorage.getItem('username')}
        })
        .then(response => {
            console.log(response)
            if(response.data.code === 200){
                this.$set(this,'TeamMessageData',response.data.notifydata)
            }
            else{
                alert('错误')
            }
        })
        .catch(error => {
            alert('出现错误')
        });
        axios({
            method:'post',
            url:'http://localhost:8000/api/getdocumentmessage/',
            data:{'username':localStorage.getItem('username')}
        })
        .then(response => {
            console.log(response)
            if(response.data.code === 200){
                this.$set(this,'DocumentMessageData',response.data.notifydata)
            }
            else{
                alert('错误')
            }
        })
        .catch(error => {
            alert('出现错误')
        });
        axios({
            method:'post',
            url:'http://localhost:8000/api/receiveinvitation/',
            data:{'username':localStorage.getItem('username')}
        })
        .then(response => {
            console.log(response)
            if(response.data.code === 200){
                this.$set(this,'InvitationData',response.data.notifydata)
            }
            else{
                alert('错误')
            }
        })
        .catch(error => {
            alert('出现错误')
        });
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
        accept(id){
            axios({
            method:'post',
            url:'http://localhost:8000/api/accept/',
            data:{'username':localStorage.getItem('username'),'notifyid':id}
            })
            .then(response => {
                console.log(response)
                if(response.data.code === 200){
                    this.$router.go(0)
                }
                else{
                    alert('错误')
                }
            })
            .catch(error => {
                alert('出现错误')
            });
        },
        ignore(id){
            axios({
            method:'post',
            url:'http://localhost:8000/api/ignore/',
            data:{'notifyid':id}
            })
            .then(response => {
                console.log(response)
                if(response.data.code === 200){
                    this.$router.go(0)
                }
                else{
                    alert('错误')
                }
            })
            .catch(error => {
                alert('出现错误')
            });
        }
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
.time{
    font-size: 13px;
    margin: 20px;
    color:rgb(153, 153 ,153)
}
.title{
    font-size:15px;
    font-weight:bold;
    color: rgb(51,51,51);
}
.text {
    font-size: 15px;
    color: rgb(102,102,102);
  }

  .item {
    margin-bottom: 18px;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }
  .clearfix:after {
    clear: both
  }

  .box-card {
    width: 100%;
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