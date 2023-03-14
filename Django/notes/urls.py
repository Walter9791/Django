from django.urls import path
from . import views

urlpatterns = [
    path('notes', views.NotesListView.as_view(), name = 'notes.list'), #added the name = section to link to the button on the home screeen without having to change file path this will help with production
    path('notes/<int:pk>', views.NotesDetailView.as_view(), name = 'notes.detail'),
    path('notes/<int:pk>/edit', views.NotesUpdateView.as_view(), name = 'notes.update'),
    path('notes/<int:pk>/delete', views.NotesDeleteView.as_view(), name = 'notes.delete'),
    path('notes/new', views.NotesCreateView.as_view(), name = 'notes.new'), 
    

]
