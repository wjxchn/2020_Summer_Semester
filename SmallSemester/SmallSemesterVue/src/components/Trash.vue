<template>
    <div>
        <Guider id="navBar" :class="{isFixed:istabBar}"/>
     <el-container>
            <el-aside class="leftside" width="210px">

            <!--     ↓↓↓↓↓↓↓↓↓↓↓↓↓↓  这个default-active是指当前激活的页面，把页面对应的index写进去，例如：当前页面是我的文档，则写进去2-1 -->
            <el-menu default-active="1-4" class="el-menu-vertical-demo" :default-openeds="opend"
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
        <div class="th"> 
            <h5 fixed="right" style="float:left"> 回收站 </h5>
        </div>
            <el-button type="danger" icon="el-icon-delete" style="float:right" @click="Deleteall">全部删除</el-button>

          <div class="recycler">         


            <el-table
                :data="tableData"
                style="width: 100%"
                :row-class-name="tableRowClassName">
                <el-table-column type="index" label="序号"></el-table-column>
                
                <el-table-column
                  prop="docname"
                  label="文档名">
                </el-table-column>
                <el-table-column
                  fixed="right"
                  prop="createtime"
                  label="创建时间"
                  width="180">
                </el-table-column>  
                <el-table-column
                  fixed="right"
                  label="操作"
                  width="260">
                <template slot-scope="scope">
                <el-button style="background-color:#f96332;color:white" class="el-icon-refresh" @click="Recoverdoc(scope.row)"></el-button>
                <el-button type="danger"  @click="Deletedoc(scope.row)"><v class="el-icon-delete"></v></el-button>
                </template>
                </el-table-column>
            </el-table>
              <el-pagination
                @size-change="handleSizeChange"
                @current-change="handleCurrentChange"
                :current-page="1"
                :page-sizes="[5, 10, 15, 20]"
                :page-size="1"
                layout="total, sizes, prev, pager, next, jumper"
                :total="total">
              </el-pagination>
              
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
export default {
    name: 'PageDemo',
    components: {
        Guider,
        BottomGuider
    },
    data () {
        return {
            total:0,
            opend:['1','2','3'],
            uniqueOpened:false,
            FileTime:'2020-8-11 12:00',
            tableData:[],
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
        Recoverdoc(row){
            axios({
                method: 'post',
                url: 'http://localhost:8000/api/recoverfromrecycle/',
                data: {'docid': row.docid}
            })
            .then(response =>{
                console.log(response)
                if(response.data.code === 200){
                    alert("恢复文档成功")
                    this.$router.go(0)   
                }
                else if(response.data.code === 400){
                    alert("恢复文档失败")
                    this.$router.go(0)                     
                }
                else{
                    alert("错误")
                    this.$router.go(0)
                }
            })
            .catch(error => {
                alert("错误")
                this.$router.go(0)
            })
        },
        Deletedoc(row){
            axios({
                method: 'post',
                url: 'http://localhost:8000/api/deletepersonaldoc/',
                data: {'docid': row.docid}
            })
            .then(response =>{
                console.log(response)
                if(response.data.code === 200){
                    alert("删除文档成功")
                    this.$router.go(0)   
                }
                else if(response.data.code === 400){
                    alert("删除文档失败")
                    this.$router.go(0)                     
                }
                else{
                    alert("错误1")
                    this.$router.go(0)
                }
            })
            .catch(error => {
                alert("错误2")
                this.$router.go(0)
            })
        },
        Deleteall(item){
            axios({
                method: 'post',
                url: 'http://localhost:8000/api/deleteallpersonaldoc/',
                data: {'list': this.tableData}
            })
            .then(response =>{
                console.log(response)
                if(response.data.code === 200){
                    alert("清空回收站成功")
                    this.$router.go(0)   
                }
                else if(response.data.code === 400){
                    alert("清空回收站失败")
                    this.$router.go(0)                     
                }
                else if(response.data.code === 300){
                    alert("回收站为空")
                    this.$router.go(0)
                }
                else{
                    alert("错误")
                    this.$router.go(0)
                }
            })
            .catch(error => {
                console.log(error)
                alert('出现错误')
                this.$router.go(0)
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
        }
    },
    created: function(){
        axios({
            method: 'post',
            url: 'http://localhost:8000/api/showrecycledoclist/',
            data: {'username': localStorage.getItem('username')}
        })
        .then(response => {
            console.log(response)
            if(response.data.code === 400){
                alert('查看文档失败')
                this.$router.go(0)                
            }
            else if(response.data.code === 200){
                this.$set(this, 'tableData', response.data.list)
                console.log(this.tableData)
            }
        })
        .catch(error => {
            console.log(error)
            alert('出现错误')
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
.th{
    margin-top:2%;
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
