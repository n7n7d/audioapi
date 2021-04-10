from django.urls import path
from audioFile import views

urlpatterns = [
    path('<str:audioFileType>/', views.AudioList.as_view()),
    path('<str:audioFileType>/<int:pk>/',views.AudioDetail.as_view())
]