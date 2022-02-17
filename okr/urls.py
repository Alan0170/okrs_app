from django.urls import path
from . import views
urlpatterns = [
    path('okr/', views.okr_register, name='okr_register'),
    path('okr/list/', views.okr_list, name='okr_list'),
    path('okr/<int:id>/', views.okr_view, name='okr_view')
]
