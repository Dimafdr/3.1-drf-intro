from django.urls import path
from .views import ProjectList, ProjectRetrieve, ProjectCreate, ProjectUpdate, ProjectMeasurement


urlpatterns = [
    path('create/', ProjectCreate.as_view()),
    path('update/', ProjectUpdate.as_view()),
    path('measurement/', ProjectMeasurement.as_view()),
    path('list/', ProjectList.as_view()),
    path('retrieve/<pk>/', ProjectRetrieve.as_view())
]