from django.shortcuts import render
import pickle
from ranking_list.models import Ranking

# Create your views here.
def  welcome_main(request):


    return render(request,'aa.html')
def  welcome_list(request):
    k = request.COOKIES  # 获取所有cookie

    client=k.get('client')
    grade=k.get('grade')
    #return HttpResponse(k)
    r=Ranking.objects.all().order_by("-grade")
    for i in r:
        if client==i.client:
            b=list(r)
            n=b.index(i)+1
            print(n)

    return render(request,'index.html',{'client':client,'grade':grade,'r':r,'n':n})

def  bb(request):
    return render(request,'bb.html')
def  cc(request):

    client=request.GET.get('c')
    grade=request.GET.get('f')
    if Ranking.objects.filter(client=client):
        c = Ranking.objects.get(client=client)
        c.grade = grade
        c.save()
    else:
        r=Ranking(client=client,grade=grade)
        r.save()

    response = render(request, 'cc.html')
        # 设置cookie
    response.set_cookie("client", client)
    response.set_cookie("grade", grade)
        # 给出响应，并写出cookie
    #return response

    return response