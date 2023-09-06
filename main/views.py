from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Arya Wijaya Kusuma',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
# Create your views here.
