<template>
    <div>
        <Guider id="navBar" :class="{isFixed:istabBar}"/>
        <main id="mainPart" role="main" class="container">
            <br>
            <el-button type="primary" style="float:right" icon="el-icon-s-flag" @click="open">创建团队</el-button>
            <!-- 
             <el-dialog title="创建团队" :visible.sync="dialogFormVisible">
            <el-form :model="form">
                <el-form-item label="团队名称" :label-width="formLabelWidth">
                    <el-input v-model="form.name" autocomplete="off"></el-input>
                </el-form-item>
            </el-form>

            <div slot="footer" class="dialog-footer">
                <el-button @click="dialogFormVisible = false">取 消</el-button>
                <el-button type="primary" @click="dialogFormVisible = false">确 定</el-button>



            </div>
            </el-dialog> -->






            <h5 fixed="right"> 我的团队 </h5>
            
            <el-table
            :data="tableData"
            style="width: 100%">
            <el-table-column
                prop="name"
                label="团队名"
                width="180"
                fixed="left"
                align="center">

            </el-table-column>
            <el-table-column
                prop="owner"
                label="管理员"
                width="180"
                fixed="left" 
                align="center">
            </el-table-column>
            <el-table-column
                prop="number"
                label="人数"
                width="180"
                align="center"
                fixed="left">
            </el-table-column>
            <el-table-column
                label="操作"
                align="center"
                width="150"
                fixed="right"
             >
           <template 
                slot-scope="scope"
                >
                    
                        <el-button @click="handleClick(scope.row)" type="primary">进入团队空间</el-button>
                    
                    </template>
            </el-table-column>
            </el-table>     
        </main>
        <BottomGuider/>
    </div>
</template>

<script>
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
            tableData: [{
                name: '组A',
                owner: '王小虎',
                number:'100'
            }, {
                name: '组B',
                owner: '王小虎',
                number:'100'
            }, {
                name: '组C',
                owner: '王小虎',
                number:'100'
            }, {
                name: '组D',
                owner: '王小虎',
                number:'1000000000000000000'
            }],
            istabBar: false,
            dialogFormVisible: false,
            dialogFormVisible2: false,
            form: {
            name: '',
            
            },
            formLabelWidth: '120px'
            }
    },
    methods: {
        open(){
            this.$prompt('请输入团队名','提示',{
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                inputPattern:/^[\u4E00-\u9FA5A-Za-z0-9_]+.{1,}$/,
                inputErrorMessage: '团队名格式错误'
            }).then(({ value }) =>{
                this.$message({
                    type:'success',
                    message:'创建成功！ 你的团队名是：' + value
                });
            }).catch(() => {
                this.$message({
                    type:'info',
                    message:'取消输入'
                });
            });
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

<style>
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
</style>