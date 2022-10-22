from django.contrib import admin
from django.urls import path
from app1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("muolif/<int:pk>/",single_yozuvchi),
    path("muolif/",all_yozuvchilar),
    path("student/",talaba),
    path("bitta_talaba/<int:pk>/",single_talaba),
    path("Kitob/",kitoblar),
    path("kitoblar/<int:pk>/",single_kitoblar),
    path("delete-student/<int:pk>/",delete_talaba),
    path("delete-muolif/<int:pk>/",delete_muolif),
    path("delete-kitob/<int:pk>/",delete_kitob),
    path("add-talaba/",create_talaba),
    path("add-muolif/",create_muolif),
    path("add-kitob/",create_kitob),
    path("record/",RECORDS),
    path("login/",login_now),
    path('logout/',logout_s)

]
