from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import NameForm
from .ml.predict import prediction


class IndexView(TemplateView):
    template_name = 'herokunlp/index.html'

    def get(self, request):
        form = NameForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = NameForm(request.POST)
        if form.is_valid():
            sl = form.cleaned_data['sl']
            sv = form.cleaned_data['sv']
            pl = form.cleaned_data['pl']
            pw = form.cleaned_data['pw']
            # choice = form.cleaned_data['choice']
        values = [sl, sv, pl, pw]
        names, pics = prediction(values)

        args = {'form': form,
                'res': names,
                'pic': pics}
        # return HttpResponseRedirect('/polls/home_2', args)
        # return HttpResponseRedirect('polls:home_2', args=args)
        return render(request, 'herokunlp/home_2.html', args)


class ResView(TemplateView):
    template_name = 'herokunlp/home_2.html'
