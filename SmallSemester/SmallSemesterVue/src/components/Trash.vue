<template>
    <div>
        <div class="sidebar sidebar-shrink">
            <div class="nano">
                <div class="nano-content">
                <ul>
					<li class="label">首页</li>
                    <li><a href="index.html"><i class="ti-home"></i> 主页 </a></li>	
                    <li><a href="index.html"><i class="ti-user"></i> 个人资料 </a></li>
					<li class="label">功能</li>
					<li><a href="index.html"><i class="ti-home"></i> 文档 </a></li>	
					<li><a href="index.html"><i class="ti-home"></i> 我的团队 </a></li>	
					<li class="active"><a href="./trash"><i class="ti-home"></i> 回收站 </a></li>	
					<li><a href="index.html"><i class="ti-home"></i> 消息 </a></li>
					<li class="label">开发者</li>
					<li><a href="form-basic.html"><i class="ti-view-list-alt"></i> 开发信息</a></li>
                </ul>
            </div>
        </div>
    </div><!-- /# sidebar -->

    <div class="header">
        

        <div class="pull-right p-r-15">
                <li class="header-icon dib" @click="bell"><i class="ti-bell"></i></li>
                <li class="header-icon dib" @click="message"><i class="ti-email"></i></li>
        </div>
    </div>
	<!-- /# header -->

    <div class="content-wrap">
        <div class="main">
            <div class="container-fluid">
                <div class="row">
                    <div class="col-lg-12 p-0">
                        <div class="page-header">
                            <div class="page-title">
                                <h1>回收站</h1>
                            </div>
                        </div>
                    </div><!-- /# column -->
                    
                </div><!-- /# row -->
                <div class="main-content">
                    <div class="row">
                        <div class="col-lg-12">
                            <div class="card alert">
                                <div id="dellist">
                                <h1>列表</h1>
                                <li v-for="(item,index) in 10" :key='index'>
                                    <span>{{item}}</span>
                                </li>
                                </div>
                                
							</div><!-- /# card -->
						</div><!-- /# column -->
					</div><!-- /# row -->     </div>
     
            </div><!-- /# container-fluid -->
        </div><!-- /# main -->
    </div><!-- /# content wrap -->
    
	
	
    









</div>
</template>
<script>

var vm = {
    data(){
        return {
            list:["1","2","3"]
        }
    }
}
export default vm;
</script>

<style src="../assets/css/lib/font-awesome.min.css" scoped></style>
<style src="../assets/css/lib/themify-icons.css" scoped></style>
<style src="../assets/css/lib/sidebar.css" scoped></style>
<style src="../assets/css/lib/simdahs.css" scoped></style>
<style src="../assets/css/style.css" scoped></style>
