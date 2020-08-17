<template>
    <div>
        <Guider id="navBar" :class="{isFixed:istabBar}"/>
        <el-container>
            <el-aside class="leftside" width="210px">

            <!--     ↓↓↓↓↓↓↓↓↓↓↓↓↓↓  这个default-active是指当前激活的页面，把页面对应的index写进去，例如：当前页面是我的文档，则写进去2-1 -->
            <el-menu default-active="1-1" class="el-menu-vertical-demo" :default-openeds="opend"
            @open="handleOpen" @close="handleClose" background-color="#fff"
            text-color="#000000" active-text-color="#f96332" >
            <el-submenu index="1">
                <template slot="title">
                    <i class="el-icon-menu"></i>
                    <span>工作台</span>
                </template>
                    <el-menu-item index="1-1" @click="Mywork" :loading="logining"><i class="el-icon-notebook-2" style="color:black"></i>我的文档</el-menu-item>
                    <el-menu-item index="1-2" @click="Myteam" :loading="logining"><i class="el-icon-set-up" style="color:black"></i>我的团队</el-menu-item>
                    <el-menu-item index="1-3" @click="MyFavorite" :loading="logining"><i class="el-icon-star-off" style="color:black"></i>我的收藏</el-menu-item>
                    <el-menu-item index="1-4" @click="Trash" :loading="logining"><i class="el-icon-delete" style="color:black"></i>回收站</el-menu-item>
                    <el-menu-item index="1-5" @click="Message" :loading="logining"><i class="el-icon-chat-dot-round" style="color:black"></i>收件箱</el-menu-item>
            </el-submenu>
            <el-submenu index="2">
                <template slot="title">
                    <i class="el-icon-s-home"></i>
                    <span>个人信息</span>
                </template>
                    <el-menu-item index="2-1" @click="Person" :loading="logining"><i class="el-icon-user" style="color:black"></i>个人资料</el-menu-item>
            </el-submenu>
            <el-submenu index="3">
                <template slot="title">
                    <i class="el-icon-s-opportunity"></i>
                    <span>其他</span>
                </template>
                    <el-menu-item index="3-1" @click="Help" :loading="logining"><i class="el-icon-view" style="color:black"></i>帮助</el-menu-item>
                    <el-menu-item index="3-2" @click="Aboutus" :loading="logining"><i class="el-icon-link" style="color:black"></i>开发者信息</el-menu-item>
            </el-submenu>
            </el-menu>
            </el-aside>
        <el-container>
        <main id="mainPart" role="main" class="container">
        <div class="a4">
            <div class="plaintext_new">
            <br>
                <el-form ref="form" :model="form" label-width="80px">
                <el-form-item label="文档名">
                    <el-col :span="22">
                    <el-input v-model="form.doc_name"></el-input>
                    </el-col>
                </el-form-item>
                <el-form-item label="简介">
                    <el-col :span="22">
                    <el-input type="textarea" :rows="4"  v-model="form.introduction"></el-input>
                    </el-col>
                </el-form-item>
                <el-form-item label="文件位置">
                    <el-col :span="20">
                    <el-input v-model="form.address" value="/个人文档" :disabled=true></el-input>
                    </el-col>
                    <el-col class="line" :span="2"></el-col>
                    <el-col :span="3">
                    <el-button>更改</el-button>
                    </el-col>
                </el-form-item>
                </el-form>
                <quill-editor class="editor"
                ref="myTextEditor"
                v-model="content"
                style="height:800px"
                :options="editorOption"
                @blur="onEditorBlur($event)"
                @focus="onEditorFocus($event)"
                @ready="onEditorReady($event)"
                @change="onEditorChange($event)">
                </quill-editor>

                <br><br><br>
                 
                 <el-button class="btn btn-primary" style="background-color:#f96332;color:white;float:right" @click="submitPlainText" plain>提交修改</el-button>
            </div>
        </div>
        </main>
        </el-container>
        </el-container>
        <BottomGuider/>
    </div>
</template>

<script>
import Guider from '../components/Guider'
import BottomGuider from '../components/BottomGuider'
import axios from 'axios'
export default {
    components: {
        Guider,
        BottomGuider
    },
    data () {
        return {
            opend:['1','2','3'],
            uniqueOpened:false,
            isUnmodifiable:true,
            istabBar: false,
            content: null,
            form:null,
            editorOption: {

                modules: {
                toolbar: [
                    ["bold", "italic", "underline", "strike"], // 加粗 斜体 下划线 删除线
                    ["blockquote", "code-block"], // 引用  代码块
                    [{ header: 1 }, { header: 2 }], // 1、2 级标题
                    [{ list: "ordered" }, { list: "bullet" }], // 有序、无序列表
                    [{ script: "sub" }, { script: "super" }], // 上标/下标
                    [{ indent: "-1" }, { indent: "+1" }], // 缩进
                    // [{'direction': 'rtl'}],                         // 文本方向
                    [{ size: ["small", false, "large", "huge"] }], // 字体大小
                    [{ header: [1, 2, 3, 4, 5, 6, false] }], // 标题
                    [{ color: [] }, { background: [] }], // 字体颜色、字体背景颜色
                    [{ font: [] }], // 字体种类
                    [{ align: [] }], // 对齐方式
                    ["clean"], // 清除文本格式
                    ["link", "image"] // 链接、图片、视频
                ], //工具菜单栏配置
                },
                placeholder: '请在此输入正文', //提示
                readyOnly: false, //是否只读
                theme: 'snow', //主题 snow/bubble
                syntax: true, //语法检测
        },
            form: {
                doc_name: '',
                introduction:'',
                address:''
            }
        }
    },
    created:function(){
        axios({
            method: 'post',
            url: 'http://localhost:8000/api/showpersonaldoc/',
            data: {'doc_id':this.$route.query.doc_id,'username': localStorage.getItem('username')}
        })
        .then(response => {
            console.log(response)
            if(response.data.code===200){
                this.content=response.data.doc_content
                this.form.doc_name = response.data.doc_name
                this.form.introduction = response.data.doc_intro
            }
            else if(response.data.code===400){
                alert('文件不存在')
                this.$router.go(0)
            }
            else{
                alert('错误')
                this.$router.go(0)
            }
        })
        .catch(error => {
            alert('有错误')
            this.$router.go(0)                
        })
    },
    methods: {
        //侧边栏的跳转
        handleOpen(key, keyPath) {
            console.log(key, keyPath);
        },
        handleClose(key, keyPath) {
            console.log(key, keyPath);
        },
        Person(){
            this.$router.push('/Person');
        },
        Mywork(){
            this.$router.push('/Personaldoc');
        },
        Myteam(){
            this.$router.push('/Team');
        },
        MyFavorite(){
            this.$router.push('/MyFavoriteDoc');
        },
        TeamM(){
            this.$router.push('/TeamManagement');
        },
        Trash(){
            this.$router.push('/Trash');
        },
        Message(){
            this.$router.push('/Message');
        },
        Help(){
            this.$router.push('/Help');
        },
        Aboutus(){
            this.$router.push('/Aboutus');
        },
         // 失去焦点
        ChangeModifiable() {
            if(this.isUnmodifiable==false)
                this.isUnmodifiable=true;
            else
                this.isUnmodifiable=false;
            return;
        },
        onEditorBlur(editor) {},
        // 获得焦点
        onEditorFocus(editor) {},
        // 开始
        onEditorReady(editor) {},
        // 值发生变化
        onEditorChange(editor) {
            this.content = editor.html;
            console.log(editor);
        },
        submitPlainText(){
            console.log(this.content);
            axios({
                method: 'post',
                url: 'http://localhost:8000/api/changepersonaldoc/',
                data: {'doc_id':this.$route.query.doc_id, 'content': this.content, 'doc_name': this.form.doc_name, 'introduction': this.form.introduction}
            })
            .then(response => {
                console.log(response)
                if(response.data.code===200){
                    this.$router.push({path: '/teammanagement', query: {group_id: this.$route.query.group_id, group_name: this.$route.query.group_name}});
                }
                else if(response.data.code===400){
                    alert('编辑失败')
                }
                else{
                    alert('错误')
                }
            })
            .catch(error => {
                console.log(error)
                alert('出现错误')
            })
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
    computed: {
        editor() {
            return this.$refs.myTextEditor.quillEditor;
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
.a4{
    width:800px;
    margin:auto;
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
