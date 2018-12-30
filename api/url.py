from api import views
from django.urls import path, include, re_path

urlpatterns = [
    path('course/', views.CourseView.as_view({'get': 'list'})),
    re_path('^course/(?P<pk>\d+)/$', views.CourseDetailView.as_view({'get': 'retreive'})),
    path('auth/', views.AuthView.as_view()),
    path('micro/', views.MicroView.as_view({'get': 'list'})),
]
