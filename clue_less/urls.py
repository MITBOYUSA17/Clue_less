"""
URL configuration for clue_less project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from Backend.Authentication.views import RegisterView, LoginView, LogoutView
from Backend.MessageTranslator.views import MessageView
from Backend.GameManagement.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('register/', RegisterView.as_view(), name='register'),

    #Example Custom method in view.
    #path('my-view/jamari/', MyView.as_view({'get': 'jamari'}), name='jamari'),  # Handles GET for jamari
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('messages/', MessageView.as_view(), name='messages'),
    path('games/', GameView.as_view(), name='games'),
    path('create_game/', CreateGameView.as_view(), name='create_game'),
    path('leave_game/', JoinGameView.as_view(), name='leave_game'),
    path('join_game/', LeaveGameView.as_view(), name='join_game'),
    path('start_game/', StartGameView.as_view(), name='start_game'),
    path('choose_character/', ChooseCharacterView.as_view(), name='choose_character'),
    path('player_move/', PlayerMoveView.as_view(), name='player_move'),
    path('make_suggestion/', MakeSuggestionView.as_view(), name='make_suggestion'),
    path('make_accusation/', MakeAccusationView.as_view(), name='make_accusation'),
    path('end_turn/', EndTurnView.as_view(), name='end_turn'),
    path('end_game_early_request/', EndGameEarlyRequestView.as_view(), name='end_game_early_request'),
    path('end_game_early_vote/', EndGameEarlyVoteView.as_view(), name='end_game_early_vote'),
]
