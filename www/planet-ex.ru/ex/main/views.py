from django.shortcuts import render, redirect
from .forms import ordersForm
from django.views import View
from bot import poptelebot



def index(request):
    return render(request, 'main/index.html', )

class ordView(View):
    def post(self, request):

        return {'status' : True}
def pop(request):

    error = ''
    if request.method == 'POST':
        form = ordersForm(request.POST)

        if form.is_valid():
            form.save()
            poptelebot()
            return redirect('home')
        else:
            error = 'Не корректные данные'

    form = ordersForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/pop.html', data,)



def polit(request):
    return render(request, 'main/polit.html')






