<template>
    <div>
            <header class="blog-header py-3">
                <div class="row flex-nowrap justify-content-between align-items-center">
                    <div class="col-4 pt-1">
                    </div>
                    <div class="col-4 text-center">
                        <a class="blog-header-logo guider-black" href="/">福报文档</a>
                    </div>
                    <div class="col-4 d-flex justify-content-end align-items-center">
                        <a :value="showusername" v-if="play">{{showusername}}</a>
                        <a class="btn btn-sm btn-outline-secondary guider-black" href="/login" v-if="!play" >登录</a>
                        <a class="btn btn-sm btn-outline-secondary guider-black" @click="tologout" v-if="play" >退出</a>
                        <a class="btn btn-sm btn-outline-secondary guider-black" href="/regi" v-if="!play" >注册</a>
                    </div>
                </div>
            </header>
    </div>
</template>
<script>
export default {
    name: 'Guider',
    data(){
        return{
            unfoldcheck: false
        }
    },
    methods: {
        changeunfoldcheck(){
            this.unfoldcheck = !this.unfoldcheck
        },
        tologout(){
            localStorage.removeItem('playcookie');
            localStorage.removeItem('username');
            this.$router.go(0);
        }
    },
    computed: {
        play () {
            var retplay = localStorage.getItem('playcookie');
            return retplay
        },
        showusername(){
            var retusername = localStorage.getItem('username');
            return retusername
        }
    }
}
</script>

<style>
.blog-header {
  line-height: 1;
  border-bottom: 1px solid #e5e5e5;
}
.blog-header-logo {
  font-family: "Playfair Display", Georgia, "Times New Roman", serif;
  font-size: 2.25rem;
}
.blog-header-logo:hover {
  text-decoration: none;
}
.unfold-link{
  margin-top: 9px;
  margin-bottom: 9px;
}
.guider-black{
    color:black;
}
</style>
