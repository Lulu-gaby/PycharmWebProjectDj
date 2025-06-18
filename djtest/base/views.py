from django.http import HttpResponse

# Create your views here.

def data(request):
    return HttpResponse('<h1>Ура!!! Все получилось на Django!</h1>')
def test(request):
    return HttpResponse('<h1>Ура!!! Это вторая страница моего проекта на Django</h1>')