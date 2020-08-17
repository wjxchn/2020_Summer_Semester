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
            <div class="personaldoc" >
                <div style="padding-top:20px">
                <div style="float:right">
                <router-link to='/DocForm'>
                    <el-button style="background-color:#f96332;color:white"  >新建 </el-button>                 
                </router-link>
                </div>
    
                <h5 fixed="right"> 我的文档 </h5>
                <span v-html="htmlData">
                    {{htmlData}}
                </span>
                </div>
                <br>
                <p class="history"> 最近浏览记录 </p>
                
                <el-row>
                     <el-col :span="8" v-for="item in latestData" :key="item.divid" :offset="index > 0 ? 2 : 0">
                        <el-card class="box-card">
                        <img src="https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=2170127953,2276382196&fm=26&gp=0.jpg" class="image">
                        <div class="card">
                            <el-button type="text" class="button" v-model="item.doc_name" @click="tolatestcontent(item.doc_id)">{{item.doc_name}}</el-button>
                        </div>                    
                        </el-card>
                    </el-col>
                </el-row>

                <hr>
                <el-table
                    :data="tableData.filter(data => !search || data.docname.toLowerCase().includes(search.toLowerCase()))"
                    style="width: 100%"
                    :row-class-name="tableRowClassName"
                    >
                     <el-table-column type="index" label="序号"></el-table-column>
                    <el-table-column
                    prop="docname"
                    label="文档名"
                    >
                    </el-table-column>
                    <el-table-column
                    fixed="right"
                    prop="creator"
                    label="创建者"
                    width="200">
                    </el-table-column>
                    <el-table-column
                    fixed="right"
                    prop="createtime"
                    label="最近打开"
                    width="200">
                    </el-table-column>  
                     <el-table-column
                    fixed="right"
                    width="200px">
                     <template slot="header" slot-scope="scope">
                        <el-input
                        v-model="search"
                        size="mini"
                        placeholder="输入关键字搜索"/>
                    </template>
                    <template   slot-scope="scope">
                    <el-dropdown  split-button style="color:#f96332;float:right">
                        <v class="el-icon-folder-opened"></v>操作
                        <el-dropdown-menu slot="dropdown">
                        <el-dropdown-item><el-button @click="handleview(scope.row)" size="small" style="background-color:#f96332;color:white"><v class="el-icon-view">查看</v></el-button></el-dropdown-item>
                        <el-dropdown-item><el-button @click="handleedit(scope.row)" size="small" style="background-color:#f96332;color:white" ><v class="el-icon-edit">编辑</v></el-button></el-dropdown-item>
                        <el-dropdown-item><el-button @click="handlefavorite(scope.row)" size="small" style="background-color:#f96332;color:white" ><v class="el-icon-star-off">收藏</v></el-button></el-dropdown-item>
                        <el-dropdown-item><el-button @click="handledelete(scope.row)" size="small" type="danger"><v class="el-icon-delete">删除</v></el-button></el-dropdown-item>
                        <el-dropdown-item><el-button @click="handleshare(scope.row)" size="small" style="background-color:#f96332;color:white" ><v class="el-icon-share">分享</v></el-button>

                        </el-dropdown-item>
                        
                    </el-dropdown-menu>
                    </el-dropdown>
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
             <el-dialog title="分享文档" :visible.sync="dialogFormVisible" width="40%">
                        <el-input type="textarea" style="width:90%" readonly="true" :value="docname" id="input"></el-input>
                        <div slot="footer" class="dialog-footer">
                    <el-button @click="copyUrl()">复制到剪切板</el-button>
                    <el-button type="primary" @click="dialogFormVisible = false">确 定</el-button>
                </div>
            </el-dialog>
           
        </main>
        </el-container>
        </el-container>
        <BottomGuider/>
    </div>
</template>

<script>
import Guider from '../components/Guider'
import axios from 'axios'
import BottomGuider from '../components/BottomGuider'
export default {
    name: 'PersonalDoc',
    components: {
        Guider,
        BottomGuider
    },
    
    data () {
        return {
            total:0,
            opend:['1','2','3'],
            docname:'',
            uniqueOpened:false,
            FileTime:'2020-8-11 12:00',
            tableData:[],
            latestData: [],
            istabBar: false,
            form: {
            name: '',
            region: '',
            date1: '',
            date2: '',
            delivery: false,
            type: [],
            resource: '',
            desc: ''
            },
            search:'',
            formLabelWidth: '120px',
            dialogFormVisible: false,
            url: 'http://localhost:8000/api/showpersonaldoclist/'
        }
    },
    created:function(){
        axios({
            method: 'post',
            url: 'http://localhost:8000/api/showpersonaldoclist/',
            data: {'username': localStorage.getItem('username')}
        })
        .then(response => {
            console.log(response)
            if(response.data.code===200){
                this.$set(this,'tableData',response.data.list)
            }
            else if(response.data.code===400){
                alert('文件不存在')
                this.$router.go(0)
            }
            else{
                alert('错误')
                this.$router.go(0)
            }
        });
        axios({
            method: 'post',
            url: 'http://localhost:8000/api/latestbrowse/',
            data: {'username': localStorage.getItem('username')}
        })
        .then(response => {
            console.log(response)
            if(response.data.code===200){
                this.$set(this,'latestData',response.data.browselistdata)
            }
            else if(response.data.code===400){
            }
            else{
                alert('错误')
                this.$router.go(0)
            }
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
        //表格方法
        tableRowClassName({row,rowIndex}){
            if(rowIndex === 1){
                return 'warning-row';
            }
            else if (rowIndex === 3){
                return 'success-row';
            }
            return '';
        },

        handleedit(row){
            console.log(row.docid)//此时就能拿到整行的信息
            this.$router.push({path: '/editpersonaldoc', query: {doc_id: row.docid}})
        },
        //收藏文档
        handlefavorite(row){
            console.log(row.docid)
            axios({
                method: 'POST',
                url: 'http://localhost:8000/api/addfavoritedoc/',
                data: {'username': localStorage.getItem('username'), 'doc_id': row.docid}
            })
            .then(response =>{
                if(response.data.code === 200){
                    alert('收藏文档成功')
                }
                else if(response.data.code === 400){
                    alert('收藏文档失败')
                }
                else {
                    alert('错误')
                }

            })
            .catch(error =>{
                console.log(error)
                alert('错误')
            })
        },
        //分享文档
        handleshare(row){
            this.docname=" 【福报文档】 "+row.docname+ "  \n  " +"http://localhost:8000/showplaintext_new?doc_id="+row.docid;
            this.dialogFormVisible = true;
            return;
        },
        //删除文档
        handledelete(row){
            console.log(row);
            axios({
                method: 'post',
                url: 'http://localhost:8000/api/takedoctorecycle/',
                data: {'docid':row.docid}
            })
            .then(response => {
                console.log(response)
                if(response.data.code===200){

                    this.$confirm('删除后此文件将移入回收站，是否继续？','提示',{
                        confirmButtonText:'确定',
                        cancelButtonText: '取消',
                        type: 'warning'
                        })
                    .then(() => {
                        this.$message({type: 'success',message: '删除成功!'});
                        this.$router.go(0)
                    })
                    .catch(() => {
                        this.$message({type: 'info',message: '已取消删除'});         
                    });

                }
                else if(response.data.code===400){
                    alert('文件不存在')
                    this.$router.go(0)
                }
                else{
                    alert('错误')
                    this.$router.go(0)
                }
            })
        },
        handleview(row){
            console.log(row.docid)//此时就能拿到整行的信息
            this.$router.push({path: '/showplaintext_new', query: {doc_id: row.docid}})            
        },
        tolatestcontent(indocid){
            this.$router.push({path: '/showplaintext_new', query: {doc_id: indocid}})
        },
        copyUrl(){
            var url=document.getElementById("input");
            url.select();
            document.execCommand("Copy");
            alert("复制成坤！")
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
.time {
    font-size: 13px;
    color: #999;
  }
.box-card{
    width: 250px;
}
  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }
  
  .clearfix:after {
      clear: both
  }
 .bottom {
    margin-top: 20px;
    line-height: 20px;
  }
  .button {
    padding: 0;
    float: right;
  }
  .image {
    width: 100%;
    display: block;
  }
p.history {
    text-align: left;
    color:gray;
    font-size: 15px;
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
.el-table .warning-row {
    background: oldlace;
}
.el-table .success-row {
    background: #f0f9eb;
}
.as{
    width:20px;
}
</style>
