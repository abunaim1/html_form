from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    if request.method == 'POST':
        print('HEllo')
        name = request.POST.get('username')
        email = request.POST.get('email')
        return render(request, 'about.html', {'name': name, 'email' : email})
    else:
        return render(request, 'about.html', {'name': name, 'email' : email})
         

def form(request):
    return render(request, 'form.html')