from django.contrib import messages
from django.shortcuts import redirect, render
from. forms import *
from django.views import generic

# Create your views here.
def home(request):
    return render(request,'dashboard/home.html')

def notes_view(request):
    if request.method == "POST":
        form = NotesForm(request.POST)
        
        #checking if form is valid or not
        if form.is_valid():
            user_notes = notes(user=request.user,title=request.POST['title'],desc=request.POST['desc'])
            user_notes.save()
        messages.success(request,f"Notes added from {request.user.username} Sucessfully!!")
    else:
        form = NotesForm()
    user_notes = notes.objects.filter(user=request.user)
    context = {'notes':user_notes,'form':form}
    return render(request,'dashboard/notes.html',context)

def delete_note(request,pk=None):
    notes.objects.get(id=pk).delete()
    return redirect("notes")

def NotesDetailView(generic.DetailView):
    models = notes