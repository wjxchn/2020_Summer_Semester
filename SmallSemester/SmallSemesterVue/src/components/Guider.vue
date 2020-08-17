<template>
    <div>
            <header class="blog-header py-3">
                <div class="row flex-nowrap justify-content-between align-items-center">
                    <div class="col-4 pt-1">
                    </div>
                    <div class="col-4 text-center">
                         <el-image style="height:70px;width:270px" :src="'http://r.photo.store.qq.com/psc?/V143D3j445iBwL/45NBuzDIW489QBoVep5mcQPgG0kiB0YEcveF4w7BTYDb1y3jx**7F0Oz1D6j66zTAfIVP2tCVMnKXZbFu9y*Mj6sMhTrGjUqDQl9CPJzItA!/r'"></el-image>
                    </div>
                    <div class="lori col-4 d-flex justify-content-end align-items-center">
                        <a :value="showusername" style="color:white" href="/personaldoc" v-if="play">{{showusername}}</a>
                        <a style="width:70px;background-color:#f96332;color:white" class="btn btn-sm btn-outline-secondary guider-black" href="/login" v-if="!play" >登录</a>
                        <i style="width:20px"></i>
                        <a style="width:70px;background-color:#f96332;color:white" class="btn btn-sm btn-outline-secondary guider-black" href="/" @click="tologout" v-if="play" >退出</a>
                        <a style="width:70px;background-color:#f96332;color:white" class="btn btn-sm btn-outline-secondary guider-black" href="/regi" v-if="!play" >注册</a>
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

<style scoped>
.lori{
    padding-right:5%;
}
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

</style>
