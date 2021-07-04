from django.urls import path
from .views import SavedGamesApi, SavedGameRetrieve

urlpatterns = [
    path('savedgames', SavedGamesApi.as_view(), name='listcreate'),
    path('savedgames/<int:pk>', SavedGameRetrieve.as_view(), name='listretrieve')
]