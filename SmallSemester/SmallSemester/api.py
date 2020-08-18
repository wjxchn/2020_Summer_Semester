from django.http import JsonResponse,HttpResponse
import json
from SmallSemesterChild.models import Test, Plain, Test3, Group, Document, Comment, Demo, Browse, Belong, Docbelong, Favorite, Verifycode, Notify
from SmallSemesterChild import models
from SmallSemester import settings,token
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db.models.query import EmptyQuerySet
from django.db.models import Max
from django.utils import timezone
import random
import datetime

def ajax_list(request):
    a = list(range(100))
    return JsonResponse(a, safe=False)

def ajax_dict(request):
    name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    return JsonResponse(name_dict)

def addname(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))
        postname = request_dict.get('inname')
        print(postname)
        test1 = Test(name = postname)
        test1.save()
        ret_dict = {'code': 200, 'msg': "填写信息成功"}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "填写信息失败"}
        return JsonResponse(ret_dict)

def getname(request):
    if request.method == 'POST':
        request_data_get = request.body
        print(request_data_get)
        request_dict_get = json.loads(request_data_get.decode('utf-8'))
        getpostname = request_dict_get.get('queryname')
        print(getpostname)
        test2 = models.Test.objects.filter(name__contains = getpostname)
        print(test2)
        for item in test2:
            print(item.name)
        ret_getdict = {'code': 200, 'msg': "查询成功"}
        return JsonResponse(ret_getdict)
    else:
        ret_getdict = {'code': 400, 'msg': "查询失败"}
        return JsonResponse(ret_getdict)        

def addplaintext(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))
        postname = request_dict.get('content')
        print(postname)
        test3 = Plain(plainname = postname)
        test3.save()
        ret_dict = {'code': 200, 'msg': "填写富文本成功"}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "填写富文本失败"}
        return JsonResponse(ret_dict)

def getplaintext(request):
    if request.method == 'GET':
        test4 = models.Plain.objects.last()
        print(test4.plainname)
        ret_dict = {'code': 200, 'msg': "显示富文本成功", 'content': test4.plainname}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "显示富文本失败", 'content': ''}
        return JsonResponse(ret_dict)

def uploadfile(request):
    #获取文件
    infile = request.FILES.get("file")
    #创建文件
    save_path ="%s/%s" % (settings.MEDIA_ROOT,infile.name)
    print(save_path)
    with open(save_path, "wb") as f:
        #将文件以二进制形式写入到指定路径
        for temp in infile.chunks():
            f.write(temp)
    ret_dict = {'code': 200, 'msg': "上传成功"}
    return JsonResponse(ret_dict)

def downloadfile(request):
    save_path ="%s/%s" % (settings.MEDIA_ROOT,'testphoto.jpg')
    file = open(save_path, 'rb')
    response = HttpResponse(file)
    response['Content-Type'] = 'application/octet-stream' #设置头信息，告诉浏览器这是个文件
    response['Content-Disposition'] = 'attachment;filename="testphoto.jpg"'
    return response

def sendemail(request):
    msg='<a href="http://localhost:8000/home" target="_blank">点击激活</a>'
    send_mail('注册激活','','2424773081@qq.com', ['14798065468@163.com'], html_message=msg)
    ret_dict = {'code': 200, 'msg': "发送邮件成功"}
    return JsonResponse(ret_dict)

def createuser(request):
    request_data = request.body
    request_dict = json.loads(request_data.decode('utf-8'))
    username = request_dict.get('username')
    password = request_dict.get('password')
    email = request_dict.get('email')
    checkuser = models.User.objects.filter(username = username)
    if checkuser.exists():
        ret_dict = {'code': 400, 'msg': "用户已存在"}
        return JsonResponse(ret_dict)        
    else:       
        user = User.objects.create_user(username=username, password=password, email=email)
        user.extension.backgroundphoto = "http://r.photo.store.qq.com/psc?/V52Qutst1Ze0TP0BqSlg0Ogc8N1lTYZp/45NBuzDIW489QBoVep5mcWCQKX9WHhAARbvjDHbE5p080qFMB3PE9EKYZm4ixFpGpOz2LgI6LvNURNSZH29x.*XMFGLDpA3riSY4BnJRS8k!/r"
        user.extension.userphoto = "http://r.photo.store.qq.com/psc?/V143D3j445iBwL/ubiEST8aMMlZjEEUGVmWIvQRktHhz2iAdR3J.A4nqij8aa0.iu6BoAsF9QicJOl2HSbaNWgM8nnAiFqjhgVj6jpHhRfm2MRX08O2SAq4NIQ!/r"
        user.save()
        content = "欢迎使用福报文档，您可以使用福报文档创建属于自己的团队，以更简洁的方式互相分享文档，共同完成项目，有使用问题请移步帮助"
        notify_object = Notify(username = username, title="尊敬的"+username+"，您已完成注册", notifytype=1,content=content)
        notify_object.save()        
        ret_dict = {'code': 200, 'msg': "创建用户成功"}
        return JsonResponse(ret_dict)
 
def login(request):
    request_data = request.body
    request_dict = json.loads(request_data.decode('utf-8'))
    username = request_dict.get('username')
    password = request_dict.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        ret_dict = {'code': 200, 'msg': "登录成功"}
        return JsonResponse(ret_dict)            
    else:
        ret_dict = {'code': 400, 'msg': "账号或密码错误"}
        return JsonResponse(ret_dict)

def changepassword(request):
    request_data = request.body
    request_dict = json.loads(request_data.decode('utf-8'))
    username = request_dict.get('username')
    email = request_dict.get('email')
    verifycode = request_dict.get('verifycode')
    newpassword = request_dict.get('newpassword')
    checkpassword = request_dict.get('checkpassword')
    user = User.objects.filter(username = username, email = email).first()
    if user:
        if newpassword == checkpassword:
            verify_obj = Verifycode.objects.filter(email = email, verify_code = verifycode).first()
            if verify_obj:
                if verify_obj.verify_time >= timezone.now()- datetime.timedelta(minutes=3):
                    u = User.objects.get(username = username)
                    u.set_password(newpassword)
                    u.save()
                    ret_dict = {'code': 200, 'msg': "修改密码成功"}
                    return JsonResponse(ret_dict)
                else:
                    ret_dict = {'code': 410, 'msg': "验证码超时"}
                    return JsonResponse(ret_dict)                    
            else:
                ret_dict = {'code': 403, 'msg': "验证码错误"}
                return JsonResponse(ret_dict)                 
        else:
            ret_dict = {'code': 401, 'msg': "两次密码不相同"}
            return JsonResponse(ret_dict)            
    else:
        ret_dict = {'code': 402, 'msg': "输入信息有误"}
        return JsonResponse(ret_dict)            

def show_personalintro(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))

        username = request_dict.get('username')
        user = models.User.objects.get(username = username)
        user_dict = {'code': 200, 'username': user.username, 'email': user.email, 'name': user.extension.name, 'sex': user.extension.sex,
                    'birthday': user.extension.birthday, 'intro': user.extension.selfintro}
        return JsonResponse(user_dict)
    else:
        ret_dict = {'code': 400, 'msg': "查看个人信息失败"}
        return JsonResponse(ret_dict)

def change_personalintro(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))

        username = request_dict.get('username')
        name = request_dict.get('name')
        email = request_dict.get('email')
        sex = request_dict.get('sex')
        birthday = request_dict.get('birthday')
        print(birthday)
        intro = request_dict.get('intro')

        user = models.User.objects.get(username = username)

        user.email = email
        user.extension.sex = sex
        user.extension.name = name
        user.extension.birthday = birthday
        user.extension.selfintro = intro
        user.save()

        ret_dict = {'code': 200, 'msg': "修改个人信息成功"}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "修改个人信息失败"}
        return JsonResponse(ret_dict)    

def show_personal_doc(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))
        
        docid = request_dict.get('doc_id')
        username = request_dict.get('username')
        doc_list = Document.objects.filter(doc_id = int(docid))
        if doc_list.exists() :
            doc = doc_list.first()
            browse_object = Browse.objects.filter()
            if browse_object.exists():
                browse_same_object = Browse.objects.filter(doc_id = docid, username = username)
                if browse_same_object:
                    browse_same_object.delete()
                browse_obj = Browse.objects.filter()
                if browse_obj:
                    res = Browse.objects.all().aggregate(Max('browse_id'))
                    browse_id = int(res['browse_id__max'])+1
                else:
                    browse_id = 0
                browse = Browse(browse_id = browse_id, username = username, doc_id = docid)
                browse.save()                
            else:
                browse_id = 0
                browse = Browse(browse_id = browse_id, username = username, doc_id = docid)
                browse.save()
            ret_dict = {'code':200, 'msg':"查看文档成功", 'docid': doc.doc_id, 'doc_name': doc.doc_name, 'doc_creater': doc.doc_creater, 'doc_intro': doc.introduction, 'doc_content': doc.doc_content}
            return JsonResponse(ret_dict)
        else:
            ret_dict = {'code': 401, 'msg': "查看文档失败"}
            return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "查看文档失败"}
        return JsonResponse(ret_dict)

def change_personal_doc(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))
        docid = request_dict.get('doc_id')
        content = request_dict.get('content')
        doc_name = request_dict.get('doc_name')
        introduction = request_dict.get('introduction')
        doc = Document.objects.get(doc_id = docid)
        doc.doc_content = content
        doc.doc_name = doc_name
        doc.introduction = introduction
        doc.islock = False
        doc.save()
        ret_dict = {'code': 200, 'msg': "修改文档成功"}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "修改文档失败"}
        return JsonResponse(ret_dict)

def add_personal_doc(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))
        print(request_dict)
        doc_content = request_dict.get('content')
        doc_name = request_dict.get('doc_name')
        introduction = request_dict.get('introduction')
        doc_creater = request_dict.get('doc_creater')
        isin_recycle = False
        findeddoc = Document.objects.filter()
        if findeddoc.exists():
            res = Document.objects.all().aggregate(Max('doc_id'))
            doc_id = int(res['doc_id__max'])+1
        else:
            doc_id = 0         
        doc = Document(doc_name=doc_name, doc_id=doc_id, doc_content=doc_content, introduction=introduction, doc_creater=doc_creater, isin_recycle=isin_recycle)
        doc.save()
        
        ret_dict = {'code': 200, 'msg': "上传个人文档成功"}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "上传个人文档失败"}
        return JsonResponse(ret_dict)

def new_group_doc(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))
        print(request_dict)
        doc_content = request_dict.get('content')
        doc_name = request_dict.get('doc_name')
        introduction = request_dict.get('introduction')
        doc_creater = request_dict.get('doc_creater')
        groupid = request_dict.get('group_id')
        isin_recycle = False
        findeddoc = Document.objects.filter()
        if findeddoc.exists():
            res = Document.objects.all().aggregate(Max('doc_id'))
            doc_id = int(res['doc_id__max'])+1
        else:
            doc_id = 0         
        doc = Document(doc_name=doc_name, doc_id=doc_id, doc_content=doc_content, introduction=introduction, doc_creater=doc_creater, isin_recycle=isin_recycle)
        doc.save()
        
        db = Docbelong(group_id = groupid, doc_id = doc_id)
        db.save()
        
        ret_dict = {'code': 200, 'msg': "新建团队文档成功"}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "新建团队文档失败"}
        return JsonResponse(ret_dict)

def create_group(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))

        creater = request_dict.get('creater')
        name = request_dict.get('name')
        introduction = request_dict.get('introduction')
        browse_object = Browse.objects.filter()
        group_object = Group.objects.filter()
        if group_object.exists():
            res = Group.objects.all().aggregate(Max('groupid'))
            groupid = int(res['groupid__max'])+1
        else:
            groupid = 0
        group = Group(group_name = name, creater = creater, groupid = groupid, introduction = introduction)
        group.save()
        belong = Belong(username = creater, group_id = groupid, authority = 2)
        belong.save()
        ret_dict = {'code': 200, 'msg': "创建团队成功"}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "创建团队失败"}
        return JsonResponse(ret_dict)

def add_group_doc(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))

        groupid = request_dict.get('groupid')
        item = request_dict.get('item')
        docid = item['docid']
        res = Docbelong.objects.filter(group_id = groupid, doc_id = docid)
        if res.exists():
            ret_dict = {'code': 200, 'msg': "添加团队文档成功"}
            return JsonResponse(ret_dict)
        else:
            db = Docbelong(group_id = groupid, doc_id = docid)
            db.save()
            ret_dict = {'code': 200, 'msg': "添加团队文档成功"}
            return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "添加团队文档失败"}
        return JsonResponse(ret_dict)

def delete_personal_doc(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))

        docid = request_dict.get('docid')
        Document.objects.filter(doc_id = docid).delete()
        Comment.objects.filter(doc_id = docid).delete()
        Browse.objects.filter(doc_id = docid).delete()
        Favorite.objects.filter(doc_id = docid).delete()
        Docbelong.objects.filter(doc_id = docid).delete()
        ret_dict = {'code': 200, 'msg': "删除个人文档成功"}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "删除个人文档失败"}
        return JsonResponse(ret_dict)

def delete_all_personal_doc(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))

        alist = request_dict.get('list')
        if len(alist) > 0:
            for item in alist:
                print(item)
                docid = item['docid']
                Document.objects.filter(doc_id = docid).delete()
                Comment.objects.filter(doc_id = docid).delete()
                Browse.objects.filter(doc_id = docid).delete()
                Favorite.objects.filter(doc_id = docid).delete()
                Docbelong.objects.filter(doc_id = docid).delete()
            ret_dict = {'code': 200, 'msg': "清空回收站成功"}
        else:
            ret_dict = {'code': 300, 'msg': "回收站为空"}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "清空回收站失败"}
        return JsonResponse(ret_dict)

def delete_group_doc(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))

        docid = request_dict.get('docid')
        groupid = request_dict.get('groupid')
        username = request_dict.get('username')
        doc = Document.objects.get(doc_id = docid)
        db = Docbelong.objects.filter(doc_id = docid, group_id = groupid)
        belongdb = Belong.objects.get(username = username, group_id = groupid)
        if belongdb.authority > 1:
            ret_dict = {'code': 200, 'msg': "删除团队文档成功"}
            db.delete()
        else:
            if doc.doc_creater == username:
                ret_dict = {'code': 200, 'msg': "删除团队文档成功"}
                db.delete()
            else:
                ret_dict = {'code': 300, 'msg': "权限不足"}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "删除团队文档失败"}
        return JsonResponse(ret_dict)

def take_doc_to_recycle(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))

        docid = request_dict.get('docid')
        document_object = Document.objects.filter(doc_id = docid).first()
        if document_object :
            document_object.isin_recycle = True
            document_object.save()
            ret_dict = {'code': 200, 'msg': "删除个人文档成功"}
            return JsonResponse(ret_dict)
        else :
            ret_dict = {'code': 404, 'msg': "删除个人文档失败"}
            return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "删除个人文档失败"}
        return JsonResponse(ret_dict)
    
def recover_from_recycle(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))
        
        docid = request_dict.get('docid')
        document_object = Document.objects.get(doc_id = docid)
        document_object.isin_recycle = False
        document_object.save()
        ret_dict = {'code': 200, 'msg': "恢复文件成功"}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "恢复失败"}
        return JsonResponse(ret_dict)

def show_personal_doclist(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))

        username = request_dict.get('username')
        doclist = Document.objects.filter(doc_creater=username)

        alist = []
        for doc in doclist:
            if doc.isin_recycle == False:
                alist.append({'docid':doc.doc_id,'docname':doc.doc_name,'createtime':doc.time,'creator':doc.doc_creater,'islock':doc.islock})
        ret_dict = {'code': 200, 'msg': "个人文档页面加载成功",'list':alist}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "个人文档页面加载失败"}
        return JsonResponse(ret_dict)
    
def show_recycle_doclist(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))

        username = request_dict.get('username')
        doclist = Document.objects.filter(doc_creater=username)

        alist = []
        for doc in doclist:
            if doc.isin_recycle == True:
                alist.append({'docid':doc.doc_id,'docname':doc.doc_name,'createtime':doc.time, 'creator':doc.doc_creater})
        ret_dict = {'code': 200, 'msg': "回收站页面加载成功", 'list': alist}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "回收站页面加载失败"}
        return JsonResponse(ret_dict)

def show_favorite_doclist(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))

        username = request_dict.get('username')
        doclist = Favorite.objects.filter(username = username)

        alist = []
        for doct in doclist:
            doc = Document.objects.get(doc_id = doct.doc_id)
            if doc.isin_recycle == False:
                alist.append({'doc_id': doc.doc_id, 'docname': doc.doc_name, 'creator':doc.doc_creater,'createtime': doc.time}) 
        ret_dict = {'code': 200, 'msg': "收藏文档页面加载成功", 'alist': alist}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "收藏文档页面加载失败"}
        return JsonResponse(ret_dict)

def leave_group(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))

        username = request_dict.get('username')
        groupid =  request_dict.get('groupid')
        belong = Belong.objects.filter(username=username,group_id=groupid).first()
        group = Group.objects.filter(groupid=groupid).first()

        if username!=group.creater:
            belong.delete()
            ret_dict = {'code': 200, 'msg': "退出团队成功"}
            return JsonResponse(ret_dict)
        else:
            ret_dict = {'code': 400, 'msg': "该用户为小组创建者，不可退出"}
            return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 405, 'msg': "退出团队失败"}
        return JsonResponse(ret_dict)
        
def dismiss_group(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))

        username = request_dict.get('username')
        groupid =  request_dict.get('group_id')
        group = Group.objects.filter(groupid=groupid).first()
        belonglist = Belong.objects.filter(group_id=groupid)
        docbelonglist = Docbelong.objects.filter(group_id = groupid)
        content = group.group_name+"团队已解散，请确认"
        if username==group.creater:
            for belong in belonglist:
                username = belong.username
                notify_object = Notify(username = belong.username, title="团队解散通知", notifytype=2,content=content)
                notify_object.save()
            group.delete()
            belonglist.delete()
            docbelonglist.delete()
            ret_dict = {'code': 200, 'msg': "解散团队成功"}
            return JsonResponse(ret_dict)
        else:
            ret_dict = {'code': 400, 'msg': "该用户不是小组创建者，不可解散团队"}
            return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "退出团队失败"}
        return JsonResponse(ret_dict)

def join_group(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))

        username = request_dict.get('username')
        groupid =  request_dict.get('groupid')

        belong = Belong(username=username, group_id=groupid)
        belong.save()
        ret_dict = {'code': 200, 'msg': "加入团队成功"}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "加入团队失败"}
        return JsonResponse(ret_dict)

def show_grouplist(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))

        username = request_dict.get('username')
        belong_list = Belong.objects.filter(username=username)
        group_name_list=[]
        for belong in belong_list:
            group = Group.objects.get(groupid=belong.group_id)
            group_name_list.append({'group_name':group.group_name,'group_creator':group.creater,'introduction':group.introduction, 'group_id':group.groupid, 'time':group.time})
        print(group_name_list)
        ret_dict = {'code':200, 'msg':"显示团队列表", 'grouplist':group_name_list}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "显示团队失败"}
        return JsonResponse(ret_dict)

def show_group_doclist(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))

        groupid = request_dict.get('doc_groupid')
        doc_list = Docbelong.objects.filter(group_id = groupid)
        alist = []
        for item in doc_list:
            doc = Document.objects.filter(doc_id = item.doc_id).first()
            if doc:
                if doc.isin_recycle == False:
                    alist.append({'docid': doc.doc_id, 'docname': doc.doc_name, 'creator': doc.doc_creater, 'createtime': doc.time,'islock':doc.islock})
        ret_dict = {'code': 200, 'list': alist} 
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': '400', 'msg': '加载团队文档失败'}
        return JsonResponse(ret_dict)

def add_favorite_doc(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))

        username = request_dict.get('username')
        doc_id = request_dict.get('doc_id')
        favorite = Favorite(doc_id=doc_id, username=username)
        favorite.save()
        ret_dict = {'code': 200, 'msg': "收藏成功"}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "收藏失败"}
        return JsonResponse(ret_dict)

def delete_group_member(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))

        usernameA = request_dict.get('usernameA')  #团队创建者
        usernameB = request_dict.get('usernameB')  #被删除者
        groupid = request_dict.get('groupid')
        group = Group.objects.filter(groupid=groupid).first()
        user = Belong.objects.get(username = usernameA, group_id = groupid)
        tuser = Belong.objects.get(username = usernameB, group_id = groupid)
        content = "您已被"+group.group_name+"团队删除，请确认"
        notify_object = Notify(username = usernameB, title="离开团队通知", notifytype=2,content=content)
        if user.authority == 2:
            if tuser.authority < 2:
                tuser.delete()
                notify_object.save()
                ret_dict = {'code': 200, 'msg': "删除团队成员成功"}
            else:
                if usernameA == group.creater and usernameB != group.creater:
                    tuser.delete()
                    notify_object.save()
                    ret_dict = {'code': 200, 'msg': "删除团队成员成功"}
                else:
                    ret_dict = {'code': 402, 'msg': "无法删除团队管理员或团队创建者"}
        else:
            ret_dict = {'code': 401, 'msg': "没有权限删除团队成员"}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "删除团队成员失败"}
        return JsonResponse(ret_dict)

def add_comment(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))

        username = request_dict.get('username')
        content = request_dict.get('content')
        doc_id = request_dict.get('doc_id')
        comment_object = Comment.objects.filter()
        
        if comment_object.exists():
            comment_id_obj = Comment.objects.all().aggregate(Max('com_id'))
            comment_id = int(comment_id_obj['com_id__max']) + 1
        else:
            comment_id = 0
        comment = Comment(com_content=content, com_author=username, doc_id=doc_id, com_id=comment_id)
        comment.save()
        
        doc = Document.objects.get(doc_id = doc_id)
        content = '您的' + doc.doc_name + '文档被人评论。'
        notify = Notify(username = doc.doc_creater, title = '评论通知', content = content, notifytype = 3)
        notify.save()
        ret_dict = {'code': 200, 'msg': "添加评论成功"}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "添加评论失败"}
        return JsonResponse(ret_dict)

def return_demo(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))

        demo_id = request_dict.get('demo_id')
        demo = Demo.objects.get(demo_id=demo_id)
        ret_dict = {'code': 200, 'msg': "返回模板成功", 'content':demo.demo_content}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "返回模板失败"}
        return JsonResponse(ret_dict)

def latest_browse(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))
        username = request_dict.get('username')
        browse = Browse.objects.filter(username = username).order_by('-browse_time')
        if browse.exists():
            checknum = 0
            browselist = []
            for item in browse:
                checknum = checknum+1
                doc = Document.objects.get(doc_id=item.doc_id)
                browselist.append({'content':doc.doc_content, 'doc_id':doc.doc_id, 'doc_time':doc.time, 'doc_name':doc.doc_name, 'doc_creater':doc.doc_creater, 'browse_time': item.browse_time})
                if checknum == 8:
                    break
            ret_dict = {'code': 200, 'msg': "返回最后浏览成功", 'browselistdata': browselist}
            return JsonResponse(ret_dict)
        else:
            ret_dict = {'code': 400, 'msg': "无最后浏览信息"}
            return JsonResponse(ret_dict)            
    else:
        ret_dict = {'code': 401, 'msg': "返回最后浏览失败"}
        return JsonResponse(ret_dict)

def remove_favorite_doc(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))

        username = request_dict.get('username')
        doc_id = request_dict.get('doc_id')
        Favorite.objects.filter(doc_id=doc_id, username=username).delete()

        ret_dict = {'code': 200, 'msg': "移除收藏成功"}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "移除收藏失败"}
        return JsonResponse(ret_dict)

def show_groupmember_list(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))

        group_id = request_dict.get('group_id')
        thisgroup = Group.objects.filter(groupid = group_id).first()
        belong_list = Belong.objects.filter(group_id = group_id)
        memberlist = []
        for belong in belong_list:
            memberlist.append({'name':belong.username,'authority':belong.authority})
        print(memberlist)
        ret_dict = {'code': 200, 'msg': "返回成员列表成功", 'memberlist': memberlist}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "返回成员列表失败"}
        return JsonResponse(ret_dict)

def show_comment(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))

        doc_id = request_dict.get('doc_id')
        commentquery = Comment.objects.filter(doc_id = doc_id)
        commentlist = []
        if commentquery.exists():  
            for item in commentquery:
                commentlist.append({'com_id': item.com_id, 'com_content': item.com_content, 'time': item.time, 'com_author': item.com_author, 'doc_id': item.doc_id})
            ret_dict = {'code': 200, 'msg': "获取到评论内容", 'commentlist': commentlist}
            return JsonResponse(ret_dict)
        else:
            ret_dict = {'code': 401, 'msg': "无评论内容", 'commentlist': commentlist}
            return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "获取评论失败"}
        return JsonResponse(ret_dict)

def del_comment(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))

        com_id = request_dict.get('com_id')
        comment_object = Comment.objects.get(com_id = com_id)
        comment_object.delete()
        ret_dict = {'code': 200, 'msg': "获取到评论内容"}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "获取评论失败"}
        return JsonResponse(ret_dict)

def sendverifycode(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))

        username = request_dict.get('username')
        email= request_dict.get('email')

        u = User.objects.filter(username = username, email = email)
        if u:
            H = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
            salt = ''
            for i in range(6):
                salt += random.choice(H)
            msg='您的验证码为'+salt
            send_mail('注册激活','','2424773081@qq.com', [email], html_message=msg)
            v = Verifycode.objects.filter()
            if v:
                res = Verifycode.objects.all().aggregate(Max('verify_id'))
                v_id = int(res['verify_id__max'])+1
                verify_object = Verifycode(username = username, verify_id = v_id+1, email = email, verify_code = salt)
                verify_object.save()
            else:
                verify_object = Verifycode(username = username, verify_id = 0, email = email, verify_code = salt)
                verify_object.save()
            ret_dict = {'code': 200, 'msg': "发送验证邮件成功"}
            return JsonResponse(ret_dict)
        else:
            ret_dict = {'code': 401, 'msg': "用户名或邮箱错误"}
            return JsonResponse(ret_dict)            
    else:
        ret_dict = {'code': 400, 'msg': "发送验证邮件成功"}
        return JsonResponse(ret_dict)

def addbackgroundphoto(request):
    if request.method == 'POST':
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))
        username = request_dict.get('username')
        backgroundphotodata = request_dict.get('backgroundphotodata')
        user = models.User.objects.get(username = username)
        user.extension.backgroundphoto =backgroundphotodata
        user.save()

        ret_dict = {'code': 200, 'msg': "上传背景图片成功"}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "上传背景图片失败"}
        return JsonResponse(ret_dict)

def addprofilephoto(request):
    if request.method == 'POST':
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))
        username = request_dict.get('username')
        profilephotodata = request_dict.get('profilephotodata')
        user = models.User.objects.get(username = username)
        user.extension.userphoto =profilephotodata
        user.save()
        ret_dict = {'code': 200, 'msg': "上传头像图片成功"}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "上传头像图片失败"}
        return JsonResponse(ret_dict)

def showbackgroundphoto(request):
    if request.method == 'POST':
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))
        username = request_dict.get('username')
        user = models.User.objects.get(username = username)
        ret_dict = {'code': 200, 'msg': "显示背景图片成功", 'backgroundphotodata': user.extension.backgroundphoto}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "显示背景图片失败"}
        return JsonResponse(ret_dict)

def showprofilephoto(request):
    if request.method == 'POST':
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))
        username = request_dict.get('username')
        user = models.User.objects.get(username = username)
        ret_dict = {'code': 200, 'msg': "显示头像图片成功", 'profilephotodata': user.extension.userphoto}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "显示头像图片失败"}
        return JsonResponse(ret_dict)    

def getsystemmessage(request):
    if request.method == 'POST':
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))
        username = request_dict.get('username')
        notify = Notify.objects.filter(username = username, notifytype = 1)
        notifylist = []
        if notify:
            for item in notify:
                notifylist.append({'MessageTitle': item.title, 'date':item.time, 'MessageContent':item.content})
        ret_dict = {'code': 200, 'msg': "显示系统通知列表成功", 'notifydata': notifylist}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "显示系统通知列表失败"}
        return JsonResponse(ret_dict)

def getteammessage(request):
    if request.method == 'POST':
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))
        username = request_dict.get('username')
        notify = Notify.objects.filter(username = username, notifytype = 2)
        notifylist = []
        if notify:
            for item in notify:
                notifylist.append({'MessageTitle': item.title, 'date':item.time, 'MessageContent':item.content})
        ret_dict = {'code': 200, 'msg': "显示团队通知列表成功", 'notifydata': notifylist}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "显示团队通知列表失败"}
        return JsonResponse(ret_dict)

def getdocumentmessage(request):
    if request.method == 'POST':
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))
        username = request_dict.get('username')
        notify = Notify.objects.filter(username = username, notifytype = 3)
        notifylist = []
        if notify:
            for item in notify:
                notifylist.append({'MessageTitle': item.title, 'date':item.time, 'MessageContent':item.content})
        ret_dict = {'code': 200, 'msg': "显示文件通知列表成功", 'notifydata': notifylist}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "显示文件通知列表失败"}
        return JsonResponse(ret_dict)

def changeauthority(request):
    if request.method == 'POST':
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))
        username = request_dict.get('username')
        tusername = request_dict.get('targetusername')
        authority = request_dict.get('authority')
        group_id = request_dict.get('group_id')
        group = Group.objects.get(groupid = group_id)
        user = Belong.objects.get(username = username, group_id = group_id)
        tuser = Belong.objects.get(username = tusername, group_id = group_id)
        if user.authority == 2:
            if username == group.creater:
                if tusername == group.creater:
                    ret_dict = {'code': 402, 'msg': "无法修改团队创建者权限"}
                else:
                    tuser.authority = authority
                    tuser.save()
                    ret_dict = {'code': 200, 'msg': "修改权限成功"}
            else:
                if tusername == group.creater:
                    ret_dict = {'code': 402, 'msg': "无法修改团队创建者权限"}
                else:
                    if tuser.authority == 2:
                        ret_dict = {'code': 403, 'msg': "无法修改管理员权限"}
                    else:
                        tuser.authority = authority
                        tuser.save()
                        ret_dict = {'code': 200, 'msg': "修改权限成功"}
        else:
            ret_dict = {'code': 401, 'msg': "无法修改团队成员权限"}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "修改权限失败"}
        return JsonResponse(ret_dict)   

def check_authority(request):
    if request.method == 'POST':
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))

        username = request_dict.get('username')
        groupid = request_dict.get('group_id')      
        belongdb = Belong.objects.get(username = username, group_id = groupid)
        ret_dict = {'code': 200, 'authority': belongdb.authority, 'msg': "查看权限成功"}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "查看权限失败"}
        return JsonResponse(ret_dict)

def return_user_name(request):
    if request.method == 'POST':
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))
        keyword = request_dict.get('keyword')
        groupid = request_dict.get('groupid')
        userlist =  models.User.objects.filter(username__icontains=keyword)
        relist = []
        for user in userlist:
            isbelong = Belong.objects.filter(group_id=groupid,username=user.username)
            if isbelong:
                a = []
            else :
                relist.append({'username':user.username})
        ret_dict = {'code': 200, 'msg': "根据关键字查询成功", 'userlist': relist}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "查询失败"}
        return JsonResponse(ret_dict)
        
def invite(request):
    if request.method == 'POST':
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))
        username = request_dict.get('username')
        groupid = request_dict.get('groupid')
        groupname = Group.objects.filter(groupid=groupid).first().group_name
        isbelong = Belong.objects.filter(group_id=groupid,username=username)
        content = groupname+"团队邀请您加入，点击确认按钮加入团队，点击拒绝按钮拒绝加入"
        if isbelong:
            ret_dict = {'code': 401, 'msg': "该用户已经是团队成员"}
            return JsonResponse(ret_dict)
        else:
            notify_object = Notify(username = username, title=groupname+"团队的邀请", notifytype=4,content=content, groupid=groupid)
            notify_object.save()
            ret_dict = {'code':200, 'msg': "发送通知成功"}
            return JsonResponse(ret_dict)

def receive_invitation(request): 
    if request.method == 'POST':
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))
        username = request_dict.get('username')
        notify = Notify.objects.filter(username = username, notifytype__in =[4,5])
        notifylist = []
        if notify:
            for item in notify:
                notifylist.append({'MessageTitle': item.title, 'date':item.time, 'MessageContent':item.content,'notifytype':item.notifytype,'id':item.id})
        ret_dict = {'code': 200, 'msg': "显示团队通知列表成功", 'notifydata': notifylist}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "显示团队通知列表失败"}
        return JsonResponse(ret_dict)


def accept(request):
    if request.method == 'POST':
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))
        username = request_dict.get('username')
        notifyid = request_dict.get('notifyid')
        groupid = Notify.objects.filter(id=notifyid).first().groupid
        belong = Belong(group_id=groupid,username=username)
        belong.save()
        notify = Notify.objects.filter(id=notifyid).first()
        notify.notifytype=5
        notify.save()
        ret_dict = {'code': 200, 'msg': "接受邀请成功"}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "接受邀请失败"}
        return JsonResponse(ret_dict)
    
def ignore(request):
    if request.method == 'POST':
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))
        notifyid = request_dict.get('notifyid')
        notify = Notify.objects.filter(id=notifyid).first()
        notify.delete()
        ret_dict = {'code': 200, 'msg': "接受邀请成功"}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "接受邀请失败"}
        return JsonResponse(ret_dict)

def showgroupintro(request):
    if request.method == 'POST':
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))
        group_id = request_dict.get('group_id')
        groupobj = Group.objects.get(groupid = group_id)
        ret_dict = {'code': 200, 'msg': "显示团队介绍成功", 'introduction': groupobj.introduction}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "显示团队介绍失败"}
        return JsonResponse(ret_dict)

def changegroupintro(request):
    if request.method == 'POST':
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))
        group_id = request_dict.get('group_id')
        introduction = request_dict.get('introduction')
        groupobj = Group.objects.get(groupid = group_id)
        groupobj.introduction = introduction
        groupobj.save()
        ret_dict = {'code': 200, 'msg': "修改团队介绍成功"}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "修改团队介绍失败"}
        return JsonResponse(ret_dict)

def lock_doc(request):
    if request.method == 'POST':
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))
        doc_id = request_dict.get('doc_id')
        doc = Document.objects.filter(doc_id=doc_id).first()
        doc.islock=True
        doc.save()
        ret_dict = {'code': 200, 'msg': "文件锁定成功"}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "文件锁定失败"}
        return JsonResponse(ret_dict)

def return_lock_status(request):
    if request.method == 'POST':
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))
        doc_id = request_dict.get('doc_id')
        doc = Document.objects.filter(doc_id=doc_id).first()
        ret_dict = {'code': 200, 'msg': "返回锁定状态成功",'islock':doc.islock}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "返回锁定状态失败"}
        return JsonResponse(ret_dict)

def unlock(request):
    if request.method == 'POST':
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))
        
        doc_id = request_dict.get('doc_id')
        doc = Document.objects.filter(doc_id=doc_id).first()
        doc.islock=False
        doc.save()
        ret_dict = {'code': 200, 'msg': "解锁成功"}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "解锁失败"}
        return JsonResponse(ret_dict)            