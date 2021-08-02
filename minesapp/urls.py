from django.urls import path
from .views import SavedGamesApi, PlayedGamesApi, loginView, retrieveView, signupView

urlpatterns = [
    path('savedgames', SavedGamesApi.as_view(), name='listcreate'),
    path('savedgames/<int:id>',retrieveView),
    path('savedgames/<int:id>/<int:gid>', retrieveView),
    path('playedgames', PlayedGamesApi.as_view(), name='playedcreate'),
    path('login', loginView),
    path('signup',signupView)
]