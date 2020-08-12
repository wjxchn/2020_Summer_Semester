<template>
    <div>
        <Guider id="navBar" :class="{isFixed:istabBar}"/>
        <main id="mainPart" role="main" class="container">
            <div class="showplaintext_new">
                <h1>Example heading <span class="badge badge-secondary">New</span></h1>
                <span v-html="htmlData">
                    {{htmlData}}
                </span>
            </div>
        </main>
        <BottomGuider/>
    </div>
</template>

<script>
import axios from 'axios'
import Guider from '../components/Guider'
import BottomGuider from '../components/BottomGuider'
export default {
    name: 'ShowPlainText_new',
    components: {
        Guider,
        BottomGuider
    },
    data () {
        return {
            istabBar: false,
            htmlData: ''
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
    mounted:function() {
        axios({
        method: 'get',
        url: 'http://localhost:8000/api/getplaintext/',
        })
        .then(response=>{
        this.htmlData = response.data.content
        })
        .catch(error=>{
        console.log(error)
        alert('出现错误')
        })
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