<template>
    <div>
        <Guider id="navBar" :class="{isFixed:istabBar}"/>
        <main id="mainPart" role="main" class="container" color="black">
        <div class="nopage">
            <img class="four" src="../assets/nopage.png">
        </div>
        <div class="but">
            <el-button style="width:100px;background-color:#f96332;color:white" @click="Guider" :loading="logining">返回首页</el-button>
        </div>
        </main>
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
            istabBar: false
        }
    },
    methods: {
        Guider(){
            this.$router.push('/');
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
.nopage{
    text-align:center;
    height:550px;
}
.four{
    padding-top:10%;
}
.but{
    text-align:center;
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