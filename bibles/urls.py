from django.urls import path
from . import views # 현재 같은 경로에 있는 views파일 참조

app_name = 'bibles'

urlpatterns = [
    path("", views.index, name="index"),
    path("verse", views.verse, name="verse"),
    path("love", views.love, name="love"),
    path("wisdom", views.wisdom, name="wisdom"),
    path("comfort", views.comfort, name="comfort"),
]