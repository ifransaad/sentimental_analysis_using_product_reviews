from django.urls import path
from . import views

urlpatterns = [
    path('user/',views.showFormData),
    # path ('machine/', views.machine_learning),
    # path('dt/', views.decision),
    # path('knn/', views.knn)
]