from django.shortcuts import render
from django.views.generic import TemplateView
from .utils import get_plot
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
class IndexView(TemplateView):
    x, y = None, None
    template_name="index/index.html"
    def get(self, request, *args, **kwargs):
        print('Valor, request', )
        self.x = request.GET.get('x', None)
        self.y = request.GET.get('y', None)
        try:
            self.x = int(self.x)
            self.y = int(self.y)
            chart = get_plot(int(self.x), int(self.y))
        except:
            chart = None
        return render(request, template_name=self.template_name, context={'chart': chart})



