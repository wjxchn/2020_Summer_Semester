import Vue from 'vue'
import Router from 'vue-router'

const routerOptions = [
  { path: '/', component: 'Firstpage' },//主页
  { path: '/aboutus' , component: 'Aboutus' },//开发者信息页面
  { path: '/animation', component: 'Animation' },//封面（暂时弃置）
  { path: '/article', component: 'Article' },//文章（暂时弃置）
  { path: '/bottomguider', component: 'BottomGuider' },//底边栏挂件
  { path: '/carousel', component: 'Carousel' },//封面（暂时弃置）
  { path: '/createfromdemo', component: 'CreateFromDemo' },//使用模板创建文档页面
  { path: '/createteam', component: 'CreateTeam' },//创建团队页面
  { path: '/editgroupdoc', component: 'EditGroupDoc'},//编辑团队文档页面
  { path: '/editperson' , component: 'EditPerson'},//编辑个人资料页面
  { path: '/editpersonaldoc', component: 'EditPersonalDoc' },//编辑个人文档页面
  { path: '/firstpage' , component: 'Firstpage'},//首页
  { path: '/findpassword' , component: 'Findpassword'},//找回密码页面
  { path: '/guider', component: 'Guider' },//顶栏挂件
  { path: '/help' , component: 'Help'},//帮助手册页面
  { path: '/login', component: 'Login' },//登录页面
  { path: '/message' , component: 'Message'},//站内信息页面
  { path: '/myfavoritedoc' , component: 'MyFavoriteDoc'},//我的收藏页面
  { path: '/newgroupdoc' , component: 'NewGroupdoc'},//新建团队文档页面 
  { path: '/pagedemo', component: 'PageDemo' },//页面模板（顶、侧、底栏）
  { path: '/person' , component: 'Person'},//个人资料页面
  { path: '/personaldoc', component:'PersonalDoc'},//个人文档页面
  { path: '/plaintext_new', component:'PlainText_new'},//创建新文档页面
  { path: '/regi', component: 'Regi' },//注册页面
  { path: '/showplaintext_new', component:'ShowPlainText_new'},//查看个人文档页面
  { path: '/team', component:'Team'},//我的团队页面
  { path: '/teammanagement', component:'TeamManagement'},//团队管理页面
  { path: '/trash' , component: 'Trash'},//回收站页面
  { path: '/docform', component:'DocForm'},//文档模板
  { path: '*', component: 'NotFound' },
]
const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () => import(`@/components/${route.component}.vue`)
  }
})

Vue.use(Router)

export default new Router({
  routes,
  mode: 'history'
})
