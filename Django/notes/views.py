from django.shortcuts import render
from .models import Notes
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import NotesForm
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect



class NotesDeleteView(LoginRequiredMixin, DeleteView):
    model = Notes
    success_url = '/notes'
    template_name = 'notes/notes_delete.html'
    login_url = "/admin"

class NotesUpdateView(LoginRequiredMixin, UpdateView):
    model = Notes
    #instead of fields from Notes, we can use a form class like below //fields = ['title', 'text']
    form_class = NotesForm
    success_url = '/notes'
    login_url = "/admin"

#this is some test after i installed Git


class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    #instead of fields from Notes, we can use a form class like below //fields = ['title', 'text']
    form_class = NotesForm
    success_url = '/notes'
    login_url = "/admin"

    def form_valid(self, form):
        self.object = form.save(commit = False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())



class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html" #another way to call notes_list.html for this list view
    login_url = '/admin'

    def get_queryset(self):
        return self.request.user.notes.all() #this is how to show user specific entries. needs to be overridden so see the notes create view def


#the class above handles what is below as a class function easily   
#def list(request):
 #   all_notes = Notes.objects.all()
 #   return render(request, 'notes/notes_list.html', {'notes':all_notes})



class NotesDetailView(LoginRequiredMixin, DetailView):
    model = Notes
    context_object_name = "note"
    login_url = "/admin"

# the above code handles how this below function works with the DETAILVIEW. It even throws the error without have to type out the try loop as we have below. 
#
#def detail(request, pk):
 #   try:
  #      note = Notes.objects.get(pk=pk)
   # except Notes.DoesNotExist:
    #    raise Http404("Note DNE")
    #return render(request, 'notes/notes_detail.html', {'note': note})

