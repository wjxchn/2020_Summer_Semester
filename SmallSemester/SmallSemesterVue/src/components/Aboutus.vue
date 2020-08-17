<template>
    <div>
        <Guider id="navBar" :class="{isFixed:istabBar}"/>
        <el-container>
            <el-aside class="leftside" width="210px">

            <!--     ↓↓↓↓↓↓↓↓↓↓↓↓↓↓  这个default-active是指当前激活的页面，把页面对应的index写进去，例如：当前页面是我的文档，则写进去2-1 -->
            <el-menu default-active="" class="el-menu-vertical-demo" :default-openeds="opend"
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
        <main  id="mainPart" role="main" class="container" color="black">
            <div class="backgroundsize" :style="note">
                <h5 style="padding:15px">开发者信息</h5>

            <h2 style="padding:15px;text-align:center;">小组简介</h2>
            <p style="font-size:20px">
                小车正穿行在落基山脉蜿蜒曲折的盘山公路上。克里斯朵夫·李维静静地望着窗外，发现每当车子即将行驶到无路的关头，
                路边都会出现一块交通指示牌‘前方转弯’或‘注意！急转弯’。而拐过每一道弯之后，前方照例又是一片柳暗花明，豁然开朗。
                山路弯弯，峰回路转，‘前方转弯’几个大字一次次地冲击着他的眼球，也渐渐叩醒了他的心扉：
                原来，不是路已到了尽头，而是该转弯了。路在脚下，更在心中，心随路转，心路常宽。
                学会转弯也是人生的智慧，因为挫折往往是转折，危机同时是转机。
            </p>
            <h2 style="padding:15px;text-align:center;">分工简介</h2>
            <el-table
            :data="tableData"
            style="width:100%;">
            
            <el-table-column
                prop="developer_name"
                label="开发者"
                width="280">
            </el-table-column>
            <el-table-column
                prop="group"
                label="分工"
                width="280">
            </el-table-column>
            <el-table-column
                prop="time"
                label="开发时间">
            </el-table-column>
            
            </el-table>




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
    name: 'PageDemo',
    components: {
        Guider,
        BottomGuider
    },
    data () {
       return {
           note: {
            backgroundImage: "url(" + require("../assets/background.png") + ")",
            backgroundRepeat: "no-repeat",
            backgroundSize: "1000px auto",
            marginTop: "5px",
            },
            opend:['1','2','3'],
            tableData: [
                {developer_name:"wjx",group:"组长",time:"8.10-2.20"},
                {developer_name:"zxw",group:"前端",time:"8.10-2.20"},
                {developer_name:"wjq",group:"前端",time:"8.10-2.20"},
                {developer_name:"gly",group:"前端",time:"8.10-2.20"},
                {developer_name:"myl",group:"后端",time:"8.10-2.20"},
                {developer_name:"lyy",group:"后端",time:"8.10-2.20"},

            ],
            uniqueOpened:false,
            istabBar: false
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
.backgroundsize {
    height: 100%;
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