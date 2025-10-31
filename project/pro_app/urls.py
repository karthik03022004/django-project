from django.urls import path
from . import views
urlpatterns=[
    path('create/',view=views.create_data),
    path('read/',view=views.read_user),
    path('update/<int:id>',view=views.update_user),
    path('delete/<int:id>',view=views.delete_user),
    path('welcome/',view=views.welcome)
]