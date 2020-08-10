<template>
    <div>
        <div class="container">
            <header class="blog-header py-3">
                <div class="row flex-nowrap justify-content-between align-items-center">
                    <div class="col-4 pt-1">
                        <a class="guider-black" data-toggle="collapse" data-target="#collapseExample" aria-expanded="false" aria-controls="collapseExample" @click="changeunfoldcheck">
                            <svg width="1.5em" height="1.5em" viewBox="0 0 16 16" class="bi bi-chevron-down" fill="currentColor" xmlns="http://www.w3.org/2000/svg" v-show="!unfoldcheck">
                                <path fill-rule="evenodd" d="M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708z"/>
                            </svg>
                            <svg width="1.5em" height="1.5em" viewBox="0 0 16 16" class="bi bi-chevron-up" fill="currentColor" xmlns="http://www.w3.org/2000/svg" v-show="unfoldcheck">
                                <path fill-rule="evenodd" d="M7.646 4.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1-.708.708L8 5.707l-5.646 5.647a.5.5 0 0 1-.708-.708l6-6z"/>
                            </svg>
                        </a>
                    </div>
                    <div class="col-4 text-center">
                        <a class="blog-header-logo guider-black" href="/">金刚石文档</a>
                    </div>
                    <div class="col-4 d-flex justify-content-end align-items-center">
                        <a class="guider-black" href="#" aria-label="Search">
                            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="mx-3" role="img" viewBox="0 0 24 24" focusable="false"><title>Search</title><circle cx="10.5" cy="10.5" r="7.5"/><path d="M21 21l-5.2-5.2"/></svg>
                        </a>
                        <a class="btn btn-sm btn-outline-secondary guider-black" href="/login">登录</a>
                        <a class="btn btn-sm btn-outline-secondary guider-black" href="/regi">注册</a>
                    </div>
                </div>
            </header>
            <div class="collapse" id="collapseExample">
                <div class="row">
                    <div class="col-6 col-sm-3 col-md-2 col-lg-2 col-xl-2 unfold-link"><a href="/workplat" class="guider-black">工作台</a></div>
                    <div class="col-6 col-sm-3 col-md-2 col-lg-2 col-xl-2 unfold-link"><a href="/message" class="guider-black">收件箱（附加内容）</a></div>
                    <div class="col-6 col-sm-3 col-md-2 col-lg-2 col-xl-2 unfold-link"><a href="/mydesktop" class="guider-black">我的桌面</a></div>
                    <div class="col-6 col-sm-3 col-md-2 col-lg-2 col-xl-2 unfold-link"><a href="/team" class="guider-black">我的团队</a></div>
                    <div class="col-6 col-sm-3 col-md-2 col-lg-2 col-xl-2 unfold-link"><a href="/recycler" class="guider-black">回收站</a></div>
                    <div class="col-6 col-sm-3 col-md-2 col-lg-2 col-xl-2 unfold-link"><a href="/help" class="guider-black">使用帮助</a></div>
                    <div class="col-6 col-sm-3 col-md-2 col-lg-2 col-xl-2 unfold-link"><a href="/article" class="guider-black">文章</a></div>
                    <div class="col-6 col-sm-3 col-md-2 col-lg-2 col-xl-2 unfold-link"><a href="/animation" class="guider-black">卡片</a></div>
                    <div class="col-6 col-sm-3 col-md-2 col-lg-2 col-xl-2 unfold-link"><a href="/pagedemo" class="guider-black">页面模板</a></div>
                    <div class="col-6 col-sm-3 col-md-2 col-lg-2 col-xl-2 unfold-link"><a href="/uploadfile2" class="guider-black">上传文件</a></div>
                    <div class="col-6 col-sm-3 col-md-2 col-lg-2 col-xl-2 unfold-link"><a href="/helloworld" class="guider-black">数据库测试</a></div>
                    <div class="col-6 col-sm-3 col-md-2 col-lg-2 col-xl-2 unfold-link"><a href="/downloadfile" class="guider-black">下载文件</a></div>
                    <div class="col-6 col-sm-3 col-md-2 col-lg-2 col-xl-2 unfold-link"><a href="/localstorage" class="guider-black">本地存储</a></div>
                    <div class="col-6 col-sm-3 col-md-2 col-lg-2 col-xl-2 unfold-link"><a href="/plaintext_new" class="guider-black">富文本编辑</a></div>
                    <div class="col-6 col-sm-3 col-md-2 col-lg-2 col-xl-2 unfold-link"><a href="/showplaintext_new" class="guider-black">显示富文本</a></div>
                    <div class="col-6 col-sm-3 col-md-2 col-lg-2 col-xl-2 unfold-link"><a href="/sendemail" class="guider-black">发送邮件</a></div>
                </div>
            </div>
        </div>
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