<template>
    <div class="createteam">
        <Guider id="navBar" :class="{isFixed:istabBar}"/>
        
        <main id="mainPart" role="main" class="container">
            <div class="bc">
                <h3 align="center">创建团队</h3>
                <el-form>   
                    <el-form-item>
                        <el-input style="width:200px" type="text" auto-complete="off" placeholder="团队名"></el-input>
                    </el-form-item>
                    <el-form-item>
                        <el-button align="center" type="primary" style="background-color:#f96332;color:white;width:150px" >创建团队</el-button>
                    </el-form-item>
                </el-form>
            </div>
        </main>
        <div class="bottom">
            <BottomGuider/>
        </div>
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

<style scoped>
.isFixed {
    position: fixed;
    top: 0;
    z-index: 10;
}
.createteam {
    width:100%;
    height:100%;
    z-index:-1;
    position:fixed;
    background-image:url("../assets/cteam.png");
    position: fixed;
    background-size: 100% 100%;
    overflow-y: auto;
}
.bc{
	background-color:white; 
    margin-left:36%;
    margin-right:36%;  
	margin-top:10%;
	border-radius:15px;
}
.bottom{
    width:100%;
    position: fixed;
	bottom: 0;
}
.el-form-item{
  text-align: center;
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