from django.http import JsonResponse,HttpResponse
import json
from SmallSemesterChild.models import Test,Plain,Test3
from SmallSemesterChild import models
from SmallSemester import settings,token
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db.models.query import EmptyQuerySet

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
    birthday = request_dict.get('birthday')
    address = request_dict.get('address')
    checkuser = models.User.objects.filter(username = username)
    if checkuser.exists():
        ret_dict = {'code': 400, 'msg': "用户已存在"}
        return JsonResponse(ret_dict)        
    else:       
        user = User.objects.create_user(username=username, password=password, email=email, is_active = 0)
        user.extension.birthday = birthday
        user.extension.address = address
        user.save()
        ret_dict = {'code': 200, 'msg': "创建用户成功"}
        return JsonResponse(ret_dict)
 
def login(request):
    request_data = request.body
    request_dict = json.loads(request_data.decode('utf-8'))
    username = request_dict.get('username')
    password = request_dict.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            ret_dict = {'code': 200, 'msg': "登录成功"}
            return JsonResponse(ret_dict)            
        else:
            ret_dict = {'code': 401, 'msg': "用户需要激活"}
            return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 402, 'msg': "账号或密码错误"}
        return JsonResponse(ret_dict)

def changepassword(request):
    request_data = request.body
    request_dict = json.loads(request_data.decode('utf-8'))
    username = request_dict.get('username')
    oldpassword = request_dict.get('oldpassword')
    newpassword = request_dict.get('newpassword')
    user = authenticate(username=username, password=oldpassword)
    if user is not None:
        u = User.objects.get(username = username)
        u.set_password(newpassword)
        u.save()
        ret_dict = {'code': 200, 'msg': "修改密码成功"}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "修改密码失败"}
        return JsonResponse(ret_dict)

def verifyuser(request):
    request_data = request.body
    request_dict = json.loads(request_data.decode('utf-8'))
    username = request_dict.get('username')
    password = request_dict.get('password')
    authuser = authenticate(username=username, password=password)
    if authuser is not None:
        user = models.User.objects.get(username = username)
        to_email = user.email
        mail_title = "激活邮件"
        msg='<p>您已收到激活邮件，注册账号成功，账号可以使用了。</p><a href="http://localhost:8000/home" target="_blank">点击进入首页</a>'
        send_status = send_mail(mail_title,'','2424773081@qq.com', [to_email], html_message=msg)
        if send_status:
            user.is_active = 1
            user.save()            
            ret_dict = {'code': 200, 'msg': "发送激活邮件成功"}
            return JsonResponse(ret_dict)
        else:
            ret_dict = {'code': 400, 'msg': "发送激活邮件失败"}
            return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 401, 'msg': "账号或密码错误"}
        return JsonResponse(ret_dict)

def changeuserinfo(request): 
    request_data = request.body
    request_dict = json.loads(request_data.decode('utf-8'))
    username = request_dict.get('username')
    password = request_dict.get('password')
    birthday = request_dict.get('birthday')
    address = request_dict.get('address')
    authuser = authenticate(username=username, password=password)
    if authuser is not None:
        user = models.User.objects.get(username = username)
        user.extension.birthday = birthday
        user.extension.address = address
        user.save()
        ret_dict = {'code': 200, 'msg': "修改成功"}
        return JsonResponse(ret_dict) 
    else:
        ret_dict = {'code': 400, 'msg': "账号或密码错误"}
        return JsonResponse(ret_dict)

def addageandphone(request):
    request_data = request.body
    request_dict = json.loads(request_data.decode('utf-8'))
    age = request_dict.get('age')
    phonenumber = request_dict.get('phonenumber')
    newtest3 = Test3(age = age, phonenumber = phonenumber)
    newtest3.save()
    ret_dict = {'code': 200, 'msg': "添加年龄和电话成功"}
    return JsonResponse(ret_dict)