from django.urls import path
from . import views

urlpatterns = [
    path('', views.project, name='projects'),
    path('index/<int:pk>/', views.projectView, name='project'),
    path('forms/', views.createView, name='create-project'),
    path('update-forms/<int:pk/>', views.UpdateView, name='Update-project'),
    path('delete-forms/<int:pk/>', views.deleteView, name='delete-project'),
]
