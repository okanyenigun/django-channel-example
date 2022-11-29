from django.shortcuts import render

# Create your views here.
def chat(request):
    return render(request, './templates/threechat.html', context={})

def room(request, room_name):
    return render(request, './templates/threeroom.html', context={'room_name': room_name})