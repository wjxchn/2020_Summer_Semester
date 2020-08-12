from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from . import api

urlpatterns = [
    url(r'^api/ajax_list/$', api.ajax_list),
    url(r'^api/ajax_dict/$', api.ajax_dict),
    url(r'^api/addname/$', api.addname),
    url(r'^api/getname/$', api.getname),
    url(r'^api/addplaintext/$', api.addplaintext),
    url(r'^api/getplaintext/$', api.getplaintext),
    url(r'^api/uploadfile/$', api.uploadfile),
    url(r'^api/downloadfile/$', api.downloadfile),
    url(r'^api/sendemail/$', api.sendemail),
    url(r'^api/createuser/$', api.createuser),
    url(r'^api/login/$', api.login),
    url(r'^api/changepassword/$', api.changepassword),
    url(r'^api/verifyuser/$', api.verifyuser),
    url(r'^admin/', admin.site.urls),
    url(r'^', TemplateView.as_view(template_name="index.html")),
]
