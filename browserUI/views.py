from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
import browserUI.modules.timeModule
from .models import ModuleItem

# Create your views here.

def index(request):
    module_list = ModuleItem.objects.order_by('-id')[:5]
    currentTime  = browserUI.modules.timeModule.currentTime()
    context = {'module_list': module_list , 'current_time' : currentTime}
    return render(request, 'browserUI/index.html', context)

def moduleConfig(request, moduleID):
    title = get_object_or_404(ModuleItem, pk=moduleID)
    return HttpResponse("Config page for module" + moduleID)