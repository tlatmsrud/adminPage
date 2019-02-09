from django.shortcuts import render
from .models import Blog2
# Create your views here.

def home(request):
    blogs = Blog2.objects #쿼리셋 #메소드
    return render(request,'home.html',{'blogs':blogs})
#Blog2에 있는 객체를 blogs에 저장
#home.html 링크에 전달