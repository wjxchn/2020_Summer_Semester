<template>
    <div>
        <Guider id="navBar" :class="{isFixed:istabBar}"/>
        <main id="mainPart" role="main" class="container" color="black">
            <div>
                <div class="main-box">
                    <div class="g-of-h">
                        <div class="g-f-l" style="width:700px;height:100%;">
                            <div style="width:700px;height:100px"></div>
                            <div class="g-f-l box-l animated"><img src="../assets/Firstpage-bg3.png" style="pointer-events:none;width:700px">
                            <i class="by">云端办公 · 高效便捷 · 协同管理</i>
                            <i class="by">996 IS A BLESSING ! </i>
                            </div>
                            <div class="g-f-l box-b animated"><img src="../assets/Firstpage-bg1.png" style="pointer-events:none;height:300px">
                            </div>
                        </div>
                        <div class="g-f-l" style="width:470px;height:100%;">
                            <div class="g-f-l box-r animated"><img src="../assets/Firstpage-bg2.png" style="pointer-events:none;height:600px;float:right">
                            <br><br><br><br><br><br>
                            <br>■多人在线协作编辑文档，告别通过社交软件多次传输文件的繁琐过程<br>
                            <br>■多端同步，随时随地开展工作，满足多场景办公使用需求<br>
                            <br>■云端数据存储，避免文档丢失的业务风险<br>
                            <br>■团队可通过链接、二维码等形式共享文档<br>
                            </div>
                        </div>
                    </div> 
                </div>
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
.g-of-h{
  overflow: hidden;
}
.g-f-l{
  float: left;
}
.g-f-r{
  float: right;
}
.main-box{
  width: 1200px;
  margin: 0 auto;
}
.box-l{
    width: 400px;
    height: 280px;
    background-color: transparent;
    animation-name: fadeLeftIn;
    -webkit-animation-name: fadeLeftIn;
}
.box-r{
    float:right;
    margin-left: 20px;
    width: 450px;
    height: 600px;
    background-color: transparent;
    animation-name: fadeRightIn;
    -webkit-animation-name: fadeRightIn;
}
.box-b{
    width: 400px;
    height: 300px;
    animation-name: fadeBottomIn;
    -webkit-animation-name: fadeBottomIn;
    background-color: transparent;
    margin-top: 20px;
}
.animated {
  -webkit-animation-duration: 1s;
  animation-duration: 1s;
  -webkit-animation-fill-mode: both;
  animation-fill-mode: both;
}
@keyframes fadeLeftIn {
  0%{
    opacity: 0;
    transform: translate3d(-100%,0,0);
  }
  100%{
    opacity: 1;
    transform: none;
  }
}
@keyframes fadeRightIn {
  0%{
    opacity: 0;
    transform: translate3d(100%,0,0);
  }
  100%{
    opacity: 1;
    transform: none;
  }
}
@keyframes fadeBottomIn {
  0%{
    opacity: 0;
    transform: translate3d(0,100%,0);
    -webkit-transform: translate3d(0,100%,0);
  }
  100%{
    opacity: 1;
    transform: none;
    -webkit-transform: none;
  }
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
.by{
    padding-left:30%;
}
</style>