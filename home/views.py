from django.shortcuts import render


def home_page(request):
    template_name = 'index.html'
    return render(request, template_name)
