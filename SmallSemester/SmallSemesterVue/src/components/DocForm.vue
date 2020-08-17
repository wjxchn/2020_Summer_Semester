<template>
    <div>
        <Guider id="navBar" :class="{isFixed:istabBar}"/>
      <el-container>
            <el-aside class="leftside" width="210px">

            <!--     ↓↓↓↓↓↓↓↓↓↓↓↓↓↓  这个default-active是指当前激活的页面，把页面对应的index写进去，例如：当前页面是我的文档，则写进去2-1 -->
            <el-menu default-active="1-1" class="el-menu-vertical-demo" :default-openeds="opend"
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

    <!-- 页面内部的内容写在main中间即可 -->
        <div class="header" style="padding:20px">
            <el-breadcrumb separator-class="el-icon-arrow-right">
            <el-breadcrumb-item :to="{ path: '/Personaldoc' }">我的文档</el-breadcrumb-item>
            <el-breadcrumb-item>新建文档</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div >
        <el-row :gutter="20">
            <el-col :span="8" v-for="item in DocFormData" :key="item.index">
                <el-card :body-style="{ padding: '0px' }" style="width:90%;margin:10px" >
                <img v-bind:src="item.url" class="image">
                <div style="padding: 14px;">
                    <p style="text-align:center;font-size:18px">{{item.name}}</p>
                    <div class="bottom clearfix">
                        <el-button type="primary" class="button" style="float:right" @click="createFile(item.index)">创建</el-button>
                    </div>
                </div>
                </el-card>
            </el-col>
        </el-row>
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
export default {
    name: 'DocForm',
    components: {
        Guider,
        BottomGuider
    },
    data () {
       return {
            currentDate: new Date(),
            opend:['1','2','3'],
            uniqueOpened:false,
            istabBar: false,
            DocFormData:[
                {
                    index:0,
                    url:"http://r.photo.store.qq.com/psc?/V50IFnJp4XxV2s3cUReP2J6k3C3FNeXZ/TmEUgtj9EK6.7V8ajmQrEMT8KH0kcT3GJdu591pDPMHvKRq6V0oZz2WYRGHa*5HDdbsK3Jtiy7R3RREPBMdTE3dyu1Vc5B3WNGtjpY.*oqM!/r",
                    name:"空白文档"
                },
                {
                    index:1,
                    url:"http://r.photo.store.qq.com/psc?/V50IFnJp4XxV2s3cUReP2J6k3C3FNeXZ/TmEUgtj9EK6.7V8ajmQrEHeIaLb1nBdjPmb.0O68t0xWJgDJuwdk3eCyySdqAhMkqFiRn5LgVaTaBxdwlXYEuIOo2nFBDj0p0WcWXeFuh8Q!/r",
                    name:"2019年终总结通用模板"
                },
                {
                    index:2,
                    url:"http://r.photo.store.qq.com/psc?/V50IFnJp4XxV2s3cUReP2J6k3C3FNeXZ/TmEUgtj9EK6.7V8ajmQrENR9RqfZdv7djXdnENnqrNUCOh2*J27vcJutVYM6RAKu74keFAYfPSFda.7p2ZsjTPQqZ0oq2Sh3O5NuILAZYoM!/r",
                    name:"个人借款协议（无居间人）"
                },
                {
                    index:3,
                    url:"http://r.photo.store.qq.com/psc?/V50IFnJp4XxV2s3cUReP2J6k3C3FNeXZ/TmEUgtj9EK6.7V8ajmQrEExUsMhEflJArhirKLG6TLQHljbfxE3ApdSkVBLjwC1jrQ0uokJSIIkU1Y0H7b70ma8We1GVl2jroX58S0b.ZTo!/r",
                    name:"外贸合同"
                }
            ]
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
        createFile(pos){
            if(pos === 0){
                this.$router.push('/plaintext_new')
            }
            else{
                this.$router.push({path: '/createfromdemo', query: {'demo_id': pos}})
            }
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
 .time {
    font-size: 13px;
    color: #999;
  }
  
  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .image {
    width: 100%;
    height: 450px;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }
  
  .clearfix:after {
      clear: both
  }
</style>