from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import MemberForm

def IndexView(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos guardados con éxito')
            return redirect('new_member')  # Redirige a la misma vista
    else:
        form = MemberForm()
    return render(request, 'newmembers.html', {'form': form})
