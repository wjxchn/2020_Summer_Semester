<template>
    <div>
        <Guider id="navBar" :class="{isFixed:istabBar}"/>
        <main id="mainPart" role="main" class="container">
            <div class="personaldoc">
                <br>
                <router-link to='/PlainText_new'>
                <el-button type="primary" style="float:right" >新建 </el-button>
                </router-link>
                  
    
                <h5 fixed="right"> 我的文档 </h5>
                <span v-html="htmlData">
                    {{htmlData}}
                </span>
                <br>
                <p class="history"> 最近浏览 </p>
                
                <el-row>
                     <el-col :span="8" v-for="(o, index) in 1" :key="o" :offset="index > 0 ? 2 : 0">
                <el-card class="box-card">
                <img src="https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=2170127953,2276382196&fm=26&gp=0.jpg" class="image">
                <div class="card">
                    <span>最近的文档</span>
                    <div class="bottom clearfix">
                    <time class="time">{{ FileTime }}</time>
                    <el-button type="text" class="button">操作按钮</el-button>
                    </div>
                </div>
                </el-card>
        </el-col>
        </el-row>

                <hr>
                <el-table
                    :data="tableData"
                    style="width: 100%"
                    :row-class-name="tableRowClassName">
                    <el-table-column
                    prop="docname"
                    label="文档名"
                    >
                    </el-table-column>
                    <el-table-column
                    fixed="right"
                    prop="creator"
                    label="创建者"
                    width="180">
                    </el-table-column>
                     <el-table-column
                    fixed="right"
                    prop="belong"
                    label="所属团队"
                    width="180">
                    </el-table-column>
                    <el-table-column
                    fixed="right"
                    prop="creation_time"
                    label="最近打开"
                    width="180">
                    </el-table-column>  
                     <el-table-column
                    fixed="right"
                    label="操作"
                    width="260">
                    
                    <template slot-scope="scope">
                    
                        <el-button @click="handleClick(scope.row)" type="primary"><v class="el-icon-view"></v></el-button>
                        <el-button type="primary" ><v class="el-icon-edit"></v></el-button>
                        <el-button type="danger"  @click="open"><v class="el-icon-delete"></v></el-button>
                    
                    </template>
                    
                    </el-table-column>
                 </el-table>
            </div>
        </main>
        <BottomGuider/>
    </div>
</template>

<script>
import Guider from '../components/Guider'
import BottomGuider from '../components/BottomGuider'
export default {
    name: 'PersonalDoc',
    components: {
        Guider,
        BottomGuider
    },
    data () {
        return {
            FileTime:'2020-8-11 12:00',
            tableData:[{
                docname:'高尔夫中的治国理念',
                creator:'Trump',
                belong:'The White House',
                creation_time:'2020-8-11 12:00',
                docid:'1'
            },{
                docname:'Nobody can know better than me',
                creator:'Trump',
                belong:'The White House',
                creation_time:'2020-8-11 12:00',
                docid:'2'
            },{
                docname:'Make America Great Again!',
                creator:'Trump',
                belong:'The White House',
                creation_time:'2020-8-11 12:00',
                docid:'3'
            }],
            istabBar: false
        }
    },
    methods: {
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
        //删除文档
        open(){
            this.$confirm('删除后此文件将移入回收站，是否继续？','提示',{
                confirmButtonText:'确定',
                cancelButtonText: '取消',
                type: 'warning'
            }).then(() => {
          this.$message({
            type: 'success',
            message: '删除成功!'
          });
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          });         
        });
    },
    mounted () {
        window.addEventListener('scroll', this.handleScroll); // Dom树加载完毕
    },
    destroyed () {
        window.removeEventListener('scroll', this.handleScroll) // 销毁页面时清除
    }
    }
}
</script>

<style>

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
    background-color: rgba(255, 255, 255, 0.15);
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
</style>