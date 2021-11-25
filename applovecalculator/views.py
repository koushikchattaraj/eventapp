from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic.base import View


# Create your views here.

class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)
    def post(self, request):
            wish_by = request.POST.get('name').title()
            link = "http://127.0.0.1:8000/event"

            msg = f"Hi friends here your new year gift {link}"
            whatsapp = f'<a href= "whatsapp://send?text={msg}" data-action="share/whatsapp/share" target="_blank"></a>'

            return render (request, self.template_name)



class EventView(View):
    template_name = 'wish.html'
    
    def get(self, request):
        return render(request, self.template_name)