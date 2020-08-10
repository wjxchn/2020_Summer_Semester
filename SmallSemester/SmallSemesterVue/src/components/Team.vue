<template>
    <div>
        <Guider id="navBar" :class="{isFixed:istabBar}"/>
        <main id="mainPart" role="main" class="container">
            <el-row>
                <i class="el-icon-user-solid"></i>
                  <el-button type="text">我的团队</el-button>
            </el-row>
            <el-table
            :data="tableData"
            style="width: 100%">
            <el-table-column
                prop="name"
                label="组名"
                width="180">
            </el-table-column>
            <el-table-column
                prop="owner"
                label="组长"
                width="180">
            </el-table-column>
            <el-table-column
                prop="time"
                label="创建时间">
            </el-table-column>
            <el-table-column label="操作">
            <template slot-scope="scope">
                <el-button
                size="mini">查看</el-button>
                <el-button
                size="mini"
                type="danger">退出</el-button>
            </template>
            </el-table-column>
            </el-table>     
            <el-button type="primary">创建团队</el-button>
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
                time: '2020/8/20'
            }, {
                name: '组B',
                owner: '王小虎',
                time: '2020/8/20'
            }, {
                name: '组C',
                owner: '王小虎',
                time: '2020/8/20'
            }, {
                name: '组D',
                owner: '王小虎',
                time: '2020/8/20'
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