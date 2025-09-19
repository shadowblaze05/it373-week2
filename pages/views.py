from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'title': 'Home Page',
        'features': ['Django', 'Templates', 'Static Files']
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html', {'title': 'About Us'})

def hello(request, name):
    return render(request, 'hello.html', {'name': name})

def gallery(request):
    images = [
        'gallery/downoad.jpg',
        'gallery/download (5).jpg',
        'gallery/download (6).jpg',
    ]
    return render(request, 'gallery.html', {'images': images})