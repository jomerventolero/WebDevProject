from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    my_context = {
        'my_name': "Jomer",
        'my_list': [123, 456, 789]
    }
    return render(request, 'test.html', my_context)
