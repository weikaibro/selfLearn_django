from django.shortcuts import render, HttpResponse
# import json
from django.http import JsonResponse
# input data from fe to db
from django.db import connection

# Create your views here.
# 1. request: 前端傳資料給後端
# 2. return HttpResponse: 後端傳畫面回前端
def index(request):
    # GET 後面是接一個字典，因此就會獲得值，再把值透過參數來儲存，因此在網址後面加上"?f2b=123"即可傳值
    f2b = request.GET["f2b"]
    return HttpResponse("Wayne, <a href='https://www.google.com'>"+f2b+"</a>")

# method1: 使用 python 中的 json 庫
# def getNews(request):
#     list1 = [
#         {
#             'title': 'You are handsome',
#             'time': '23:11:43'
#         },
#         {
#             'title': 'You are gay',
#             'time': '05:12:16'
#         }
#     ]
#     str1 = json.dumps(list1)
#     return HttpResponse(str1)

# method2: 使用 django 框架中的 JsonResponse
def getNews(request):
    list1 = [
        {
            'title': 'You are handsome',
            'time': '23:11:43'
        },
        {
            'title': 'You are gay',
            'time': '05:12:16'
        }
    ]
    # django 框架中的 response.py 會將 safe 設定成 True，故無法傳遞 json data
    return JsonResponse(list1, safe = False)


# 以下為 template page 的渲染 (rendering)
def homepage(request):
    # 可以針對 render 點擊 f12，即可發現其本質還是在【調用 HttpResponse】
    # 第 3 個參數為【將數據傳遞給 template】，是以【字典】的形式來傳遞的。若沒有值，則會在 template 中採用 filter default 技術
    context = {
        "blog_name": "Wayne's Blog",
        # "blog_name": "",
        "articleList": [
            {
                'title': 'Today news',
                'time': '2022-10-11 23:11:43',
                'author': 'Wayne'
            },
            {
                'title': 'Oscar is gay',
                'time': '2023-04-22 05:12:16',
                'author': 'Oscar'
            }
        ]
    }
    return render(request, "index.html", context)

def about(request):
    context = {
        "blog_name": "About me",
    }
    return render(request, "about.html", context)

def register(request):
    return render(request, "register.html")

def addReg(request):
    userID = request.POST['userID']
    username = request.POST['username']
    password = request.POST['password']
    truename = request.POST['truename'] 
    sex = request.POST['sex']
    age = request.POST['age']
    mycursor = connection.cursor()
    # connect to db
    mycursor.execute('insert into userinfo(userID, username, password, truename, sex, age) values(%s, %s, %s, %s, %s, %s)', (userID, username, password, truename, sex, age))
    print(userID, username, password, truename, sex, age)
    return HttpResponse("Success!")