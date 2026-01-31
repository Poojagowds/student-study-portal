from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Add
    path('add/', views.add_note, name='add_note'),
    path('add-activity/', views.add_activity, name='add_activity'),
    path('add-attendance/', views.add_attendance, name='add_attendance'),
    path('add-homework/', views.add_homework, name='add_homework'),

    # Edit
    path('edit-note/<int:note_id>/', views.edit_note, name='edit_note'),

    # Delete
    path('delete-note/<int:note_id>/', views.delete_note, name='delete_note'),
    path('delete-activity/<int:activity_id>/', views.delete_activity, name='delete_activity'),
    path('delete-homework/<int:homework_id>/', views.delete_homework, name='delete_homework'),
]
