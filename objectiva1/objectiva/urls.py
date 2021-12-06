from django.conf import settings
from django.conf.urls.static import  static
from django.urls import path
from . import views


urlpatterns=[
    path('',views.home1,name='home_index1'),
    path('activity',views.home2,name='activity'),
    path('done_activity',views.done_a,name='done_activity'),
    path('not_done',views.not_d,name='not_done'),
    path('manage_page',views.manage_p,name='manage_page'),
    path('activity_form', views.activity_frm1, name='activity_form'),
    path('about',views.about1,name='about'),
    path('contact',views.contact1,name='contact'),
    path('reference',views.reference1,name='references'),
    path('sign_up',views.sign_up1,name='sign_up'),
    path('login_page',views.login1,name='login_page'),
    path('logout',views.logout1,name='logout'),
    path('change_account',views.change_account,name='change_account'),
    path('notify_page',views.notify_user,name='notify_page')

]
static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)