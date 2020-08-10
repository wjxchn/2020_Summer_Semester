<template>
  <div class="plaintext">
    <h1>富文本编辑器 <span class="badge badge-secondary">测试</span></h1>
    <quill-editor class="editor"
      ref="myTextEditor"
      v-model="content"
      :options="editorOption"
      @blur="onEditorBlur($event)"
      @focus="onEditorFocus($event)"
      @ready="onEditorReady($event)"
      @change="onEditorChange($event)">
    </quill-editor>
    <button type="button" class="btn btn-primary" @click="submitPlainText">Primary</button>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'PlainText',
    data () {
        return {
        content: null,
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
                ["link", "image", "video"] // 链接、图片、视频
            ], //工具菜单栏配置
            },
            placeholder: '请在这里添加产品描述', //提示
            readyOnly: false, //是否只读
            theme: 'snow', //主题 snow/bubble
            syntax: true, //语法检测
        }
        }
    },
    methods: {
        // 失去焦点
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
                url: 'http://localhost:8000/api/addplaintext/',
                data: {'content': this.content}
            })
            .then(response => {
                console.log(response)
                if(response.data.code===200){
                    alert('添加富文本成功')
                }
                else if(response.data.code===400){
                    alert('添加富文本失败')
                }
                else{
                    alert('错误')
                }
            })
            .catch(error => {
                console.log(error)
                alert('出现错误')
            })
        }
    },
    computed: {
        editor() {
            return this.$refs.myTextEditor.quillEditor;
        }
    },
    mounted() {
        // console.log('this is my editor',this.editor);
    } 
}
</script>

<style>
</style>