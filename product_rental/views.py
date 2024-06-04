from django.shortcuts import render

def index(request):
    # Add any necessary logic here
    return render(request, 'pro_rental/index.html')