from django.urls import path

from . import views

app_name = 'myblog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('posts/<int:pk>/', views.detail, name='detail'),
    # path('categories/<int:pk>/', views.category, name='category'),
    path('categories/<int:pk>/', views.CategoryView.as_view(), name='category'),
    path('tag/<int:pk>/', views.tag, name='tag'),
    path('archives/<int:year>/<int:month>/', views.archive, name='archive'),
    path('about.html', views.about, name='about'),
    path('search/', views.search, name='search')
]