from django.http import HttpResponse

def HomePageView(request):
    return HttpResponse('Hello Django')
