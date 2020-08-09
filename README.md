# 2020_Summer_Semester

## 部分文件夹解释
|-- SmallSemester    工程文件夹

&emsp;|-- SmallSemester &emsp;Django主文件夹

&emsp;&emsp;|-- api.py &emsp;接口的python文件

&emsp;&emsp;|-- settings.py &emsp;Django设置文件

&emsp;&emsp;|-- urls.py &emsp;路径设置文件

&emsp;&emsp;|-- views.py &emsp;渲染vue页面的文件

&emsp;|-- SmallSemesterChild &emsp;Django关于数据库的相关内容的文件夹

&emsp;&emsp;|-- \_\_init\_\_.py &emsp;设置pymysql的文件

&emsp;&emsp;|-- models.py &emsp;设置表的文件

&emsp;|-- SmallSemesterVue &emsp;Vue工程文件夹

&emsp;&emsp;|--src &emsp;vue源文件夹

&emsp;&emsp;&emsp;|--components &emsp;vue组件和页面文件夹

&emsp;&emsp;&emsp;&emsp;|--Animation.vue &emsp;卡片页面

&emsp;&emsp;&emsp;&emsp;|--Article.vue &emsp;文章格式页面

&emsp;&emsp;&emsp;&emsp;|--BottomGuider.vue &emsp;底部关于组件

&emsp;&emsp;&emsp;&emsp;|--Carousel.vue &emsp;轮播图页面，该页面设为主页

&emsp;&emsp;&emsp;&emsp;|--Guider.vue &emsp;导航栏组件

&emsp;&emsp;&emsp;&emsp;|--NotFound.vue &emsp;404页面

&emsp;&emsp;&emsp;&emsp;|--PageDemo.vue &emsp;页面模板，包含导航栏组件和底部关于组件

&emsp;&emsp;&emsp;|--router &emsp;vue路由文件夹

&emsp;|-- UploadFile &emsp;上传的文件保存的文件夹

|-- README.md &emsp;解释文档

## 使用方面的一些事项：

### 调试
调试时，同时创建两个命令行，其中一个命令行位于2020_Summer_Semester/SmallSemester中，并输入以下命令：
```
python manage.py runserver 0.0.0.0:8000
```
这时，后端就运行起来了，在浏览器中输入localhost:8000，我们就可以看到我们的页面了。
另一个命令行，位于2020_Summer_Semester/SmallSemesterVue中，当该文件夹的内容有修改时，我们在这个命令行中输入以下命令：
```
npm run build
```
这时，更改的内容就会编译。当编译完成后，后端的服务器上的内容也会发生变化。
但是，这样做速度太慢了，我们怎样更快的观察页面设计的变化呢？我们打开第三个命令行，同样位于2020_Summer_Semester/SmallSemesterVue中，输入以下命令：
```
npm run dev
```
这时，我们在浏览器中输入localhost:8080，我们就可以看到页面的样子了，每次修改之后，会自动更新页面。但是这种方式，不能使用api。

当2020_Summer_Semester/SmallSemesterChild中的文件发生改变时，我们需要再新建一个命令行，在2020_Summer_Semester/SmallSemester中，输入以下命令：
```
python manage.py makemigrations SmallSemesterChild
python manage.py migrate
```
这时，表相关的东西会更新，否则，即使我们修改了代码，表也不会更新。这种更新，不仅仅是相关文件的更新，数据库中的表也会自动的创建。
迁移失败的话，就删除数据库中所有的表，因为重复迁移可能会造成这个问题。

### 创建超级用户
```
python manage.py createsuperuser
```

### Bootstrap的使用：
直接使用即可，无需引入，因为该项目已经引入。

## 参考文档
1. [Bootstrap官方文档](https://v4.bootcss.com/docs/getting-started/introduction/) 该文档内容英文内容较多，但是内容全面，也比较好理解。

2. [Runoob的Django教程](https://www.runoob.com/django/django-tutorial.html) 该教程内容简洁明了，讲述了Django的使用和Django数据库模型的使用。

3. [Django官方文档](https://docs.djangoproject.com/zh-hans/3.0/) 全英文文档，也有中文版。内容较为复杂。

## 有以下内容需要注意：
- api的最后一个字符必须为/，否则会错误。