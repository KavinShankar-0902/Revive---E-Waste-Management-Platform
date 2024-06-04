from django.shortcuts import render, redirect
from .forms import EWasteCollectionForm
from .models import EWasteCollection

def index(request):
    if request.method == 'POST':
        form = EWasteCollectionForm(request.POST, request.FILES)
        if form.is_valid():
            ewaste = form.save(commit=False)
            # Check if the checkbox is checked (True) or not (False)
            ewaste.visible = request.POST.get('visible', False) == 'on'
            ewaste.save()
            return redirect('ewaste_collection_success')
    else:
        form = EWasteCollectionForm()
    return render(request, 'index.html', {'form': form})

def ewaste_collection_success(request):
    return render(request, 'ewaste_collection_success.html')

def show_ewaste(request):
    visible_ewastes = EWasteCollection.objects.filter(visible=True)
    return render(request, 'show_ewaste.html', {'ewastes': visible_ewastes})
