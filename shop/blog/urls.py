from django.urls import path
from .views import index , singlePost , sum2

app_name = 'blog'

urlpatterns = [
    path('index/' , index , name = 'index'),
    path('singlePost/<str:slug>' , singlePost , name="singlePost"),
    path('test/<int:number>', sum2 , name = "sum"),
]
