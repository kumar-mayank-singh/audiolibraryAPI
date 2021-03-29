from django.urls import path, include
from . import views
urlpatterns = [
    path('create/', views.CreateAPI.as_view(),name='create'),
    path('view/<str:audiotype>/<int:id>/', views.GetRecordsAPI.as_view(),name='create'),
    path('update/<str:audiotype>/<int:id>/', views.UpdateRecordAPI.as_view(),name='update'),
    path('delete/<str:audiotype>/<int:id>/', views.DeleteRecordAPI.as_view(),name='delete'),
]
