from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('all-board-games/', views.all_board_games, name='all_board_games'),
    path('board-game/<int:game_id>/', views.board_game_detail, name='board_game_detail'),
    
    path('all-board-gamers/', views.all_board_gamers, name='all_board_gamers'),
    path('board-gamer/<int:gamer_id>/', views.board_gamer_detail, name='board_gamer_detail'),
    
    path('all-game-loans/', views.all_game_loans, name='all_game_loans'),
    path('loan/<int:loan_id>/', views.loan_detail, name='loan_detail'),
]