<template>
    <div>
        <Guider id="navBar" :class="{isFixed:istabBar}"/>
        <el-main id="TeamManagement" role="main" class="container">
            <h5>特朗普团队 的团队主页</h5>
        <el-tabs v-model="activeName" type="card" @tab-click="handleClick">
            <el-tab-pane label="团队文档" name="first">
                <el-button type="primary" style="float:right">新建</el-button>
                <el-button  style="float:right">添加</el-button>
                <el-table
                    :data="DocData.filter(data => !search || data.docname.toLowerCase().includes(search.toLowerCase()))"
                    style="width: 100%"
                    :row-class-name="tableRowClassName">
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
                    width="260">
                    <template slot="header" slot-scope="scope">
                        <el-input
                        v-model="search"
                        size="mini"
                        placeholder="输入关键字搜索"/>
                    </template>
                    <template slot-scope="scope">
                    
                        <el-button size=mini @click="handleClick(scope.row)">查看</el-button>
                        <el-button size=mini >编辑</el-button>
                        <el-button size=mini type="danger"  @click="open">删除</el-button>
                    
                    </template>
                    
                    </el-table-column>
                 </el-table>
            </el-tab-pane>
            <el-tab-pane label="团队管理" name="second">
                <el-button style="float:right" type="danger">解散团队</el-button>
                <el-button style="float:right">邀请成员</el-button>
                <el-table
                    :data="tableData.filter(data => !search || data.name.toLowerCase().includes(search.toLowerCase()))"
                    style="width: 100%"
                    max-height="450"
                    >
                    <el-table-column
                    label="姓名"
                    prop="name">
                    </el-table-column>
                    <el-table-column
                    label="权限"
                    prop="authority">
                    </el-table-column>
                    <el-table-column
                    label="身份"
                    prop="identity">
                    </el-table-column>
                    <el-table-column
                    align="right">
                    <template slot="header" slot-scope="scope">
                        <el-input
                        v-model="search"
                        size="mini"
                        placeholder="输入关键字搜索"/>
                    </template>
                    <template slot-scope="scope">
                        <el-button
                        size="mini"
                        @click="handleEdit(scope.$index, scope.row)">权限管理</el-button>
                        <el-button
                        size="mini"
                        type="danger"
                        @click="handleDelete(scope.$index, scope.row)">删除</el-button>
                    </template>
                    </el-table-column>
                </el-table>
            </el-tab-pane>
            <el-tab-pane label="分享" name="third">分享</el-tab-pane>
            <el-tab-pane label="历史记录" name="fourth">历史记录</el-tab-pane>
        </el-tabs>

       

        </el-main>
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
            activeName: 'first',
            istabBar: false,
            tableData: [{
          authority: '查看 修改 删除 增加',
          name: '特朗普',
          identity:'创建者 管理员',
          address: '白宫'
        },{
          authority: '查看 修改 删除 增加',
          name: '特朗普的口罩',
          identity:'管理员',
          address: '白宫'
        }, {
          authority: '查看 修改 删除 增加',
          name: '特朗普的儿子',
          identity:'成员',
          address: '白宫'
        }, {
          authority: '查看 修改 删除 增加',
          name: '特朗普的儿子',
          identity:'成员',
          address: '白宫'
        },
        {
          authority: '查看',
          name: '特朗普的金毛',
          identity:'成员',
          address: '白宫'
        },{
          authority: '查看',
          name: '特朗普的金毛',
          identity:'成员',
          address: '白宫'
        },{
          authority: '查看',
          name: '特朗普的金毛',
          identity:'成员',
          address: '白宫'
        },{
          authority: '查看',
          name: '特朗普的金毛',
          identity:'成员',
          address: '白宫'
        },{
          authority: '查看',
          name: '特朗普的金毛',
          identity:'成员',
          address: '白宫'
        },{
          authority: '查看',
          name: '特朗普的金毛',
          identity:'成员',
          address: '白宫'
        },{
          authority: '查看',
          name: '特朗普的金毛',
          identity:'成员',
          address: '白宫'
        }],
        search: '',
        DocData:[{
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
        handleEdit(index, row) {
            console.log(index, row);
        },
        handleDelete(index, row) {
            console.log(index, row);
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