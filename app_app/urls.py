from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('all-board-games/', views.all_board_games, name='all_board_games'),
    path('board-game/<int:game_id>/', views.board_game_detail, name='board_game_detail'),
    path('new_board_game', views.new_board_game, name='new_board_game'),
    path('edit_board_game/<int:game_id>/',  views.edit_board_game, name='edit_board_game'),
    path('delete_board_game/<int:game_id>/', views.delete_board_game, name='delete_board_game'),

    path('board_game_review/<int:game_id>/', views.board_game_review, name='board_game_review'),
    path('edit_board_game_review/<int:review_id>/', views.edit_board_game_review, name='edit_board_game_review'),
    path('delete_review/<int:review_id>/', views.delete_review, name='delete_review'),
    
    path('loan_board_game/<int:game_id>', views.loan_board_game, name='loan_board_game'),
    path('return_board_game/<int:game_id>/', views.return_board_game, name='return_board_game'),
    path('loaned_games/', views.loaned_games, name='loaned_games'),
    path('error/', views.more_than_3_games_error, name='more_than_3_games_error'),


    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('account', views.account, name='account'),
]
