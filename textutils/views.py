# I have created this file - sush
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # params = {'name': 'sush', 'place': 'Mars'}
    return render(request, 'index.html')
    # return HttpResponse('''<h1>Home</h1''')


def analyze(request):
    # Get the text
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    analyzed = djtext
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif fullcaps == 'on':
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'change to uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse('Error')

# def capfirst(request):
#     return HttpResponse('capitalize first')
# def newlineremove(request):
#     return HttpResponse('newlineremove')
# def spaceremove(request):
#     return HttpResponse("spaceremove <a href = '/'>back</a>")
# def charcount(request):
#     return HttpResponse('charcount')
