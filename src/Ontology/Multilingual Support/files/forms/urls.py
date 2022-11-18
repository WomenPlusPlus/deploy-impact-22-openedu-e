from django.urls import path

from . import views
from .views import ListResource

app_name = 'forms'
urlpatterns = [
	path('', ListResource.as_view()),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('newresource/', views.get_newresource, name='get_newresource'),
    path('<int:pk>/newlang/', views.newlang, name='newlang'),
    path('<int:pk>/thanks/', views.Thanks.as_view(), name='thanks'),
]