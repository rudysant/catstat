from django.urls import path
from . import views
from .views import SearchResultsView

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('detail_pubyear/<int:publish_year>/', views.detail_pubyear, name='detail_pubyear'),
    path('detail_publisher/<str:publisher_type>/', views.detail_publisher, name='detail_publisher'),
    path('detail_language/<str:language>/', views.detail_language, name='detail_language'),
    path('detail_genre/<str:genre>/', views.detail_genre, name='detail_genre'),
    path('detail_subject/<str:subject>/', views.detail_subject, name='detail_subject'),
    path('detail_authorship/<str:authorship_type>/', views.detail_authorship, name='detail_authorship'),
]