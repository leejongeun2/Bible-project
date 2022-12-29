from django.urls import path
from . import views # 현재 같은 경로에 있는 views파일 참조

app_name = 'bibles'

urlpatterns = [
    path("", views.index, name="index"),
]