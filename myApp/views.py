from django.shortcuts import render
from django.http import HttpResponse
from myApp.models import UserRecord

# Create your views here.
def index(request):
    user_list = UserRecord.objects.order_by('last_name')

    context = {'user_records': user_list}

    #return HttpResponse("Hello, world from myApp.")
    return render(request, 'index.html', context=context)