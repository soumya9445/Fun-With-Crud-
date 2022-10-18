from django.contrib import admin
from django.urls import path
from crudapp import views
from django.conf.urls.static import static
from CRUDProject import settings

urlpatterns = [
    path('',views.index,name='index'),
    path('create/',views.create,name='create'),
    path('save/',views.save,name='save'),
    path('read/',views.read,name='read'),
    path('update/',views.update,name='update'),
    path('update_record/',views.update_record,name='update_record'),
    path('delete/',views.delete,name='delete'),
    path('single_record/',views.single_record,name='single_record'),
    path('search_one/',views.search_one,name='search_one'),
    path('login/',views.login,name='login'),
    path('student_login/',views.student_login,name='student_login'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
