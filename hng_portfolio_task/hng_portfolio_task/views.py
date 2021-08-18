from core.forms import ContactMessageForm
from django.http import JsonResponse
from django.shortcuts import render

ROOT_URL = 'https://dratapp-media.s3.us-west-2.amazonaws.com/extras'
MAIN_IMG = f'{ROOT_URL}/business.png'
DEV_IMG = f'{ROOT_URL}/web-dev.png'
DESIGN_IMG = f'{ROOT_URL}/design.png'

def homepage(request):
    form = ContactMessageForm()
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status':'success'})
        else:
            return JsonResponse({'status':'error'})
    return render(request,'portfolio.html',{
        'form':form,'main':MAIN_IMG,'dev':DEV_IMG,
        'design':DESIGN_IMG
        })