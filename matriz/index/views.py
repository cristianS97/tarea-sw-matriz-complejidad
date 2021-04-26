from django.views.generic import TemplateView
from .utils import get_plot


# Create your views here.
class IndexView(TemplateView):
    x, y, chart = None, None, None
    template_name = "index.html"

    def change_chart(self):
        try:
            self.x = int(self.x)
            self.y = int(self.y)
            self.chart = get_plot(int(self.x), int(self.y))
        except:
            self.chart = None

    def get(self, request, *args, **kwargs):
        print('Valor, request', )
        self.x = request.GET.get('x', None)
        self.y = request.GET.get('y', None)
        self.change_chart()

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['chart'] = self.chart

        return context
