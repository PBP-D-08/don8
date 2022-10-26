from django.shortcuts import render

# Create your views here.
def show_support(request):
    return render(request, 'support.html')