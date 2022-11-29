from django.shortcuts import render

def two(request):
    return render(request, './templates/two.html')