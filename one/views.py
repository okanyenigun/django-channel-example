from django.shortcuts import render

def one(request):
    return render(request, './templates/one.html', context={'one_text': "ASD"})