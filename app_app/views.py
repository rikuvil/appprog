from django.shortcuts import render, get_object_or_404, redirect
from .models import BoardGame, BoardGamer, GameLoan

# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')

#views for BoardGame model

def all_board_games(request):
    games = BoardGame.objects.all()
    return render(request, 'all_board_games.html', {'games': games})

def board_game_detail(request, game_id):
    game = get_object_or_404(BoardGame, pk=game_id)
    return render(request, 'board_game_detail.html', {'game': game})

#views for BoardGamer model

def all_board_gamers(request):
    gamers = BoardGamer.objects.all()
    return render(request, 'all_board_gamers.html', {'gamers': gamers})

def board_gamer_detail(request, gamer_id):
    gamer = get_object_or_404(BoardGamer, pk=gamer_id)
    return render(request, 'board_gamer_detail.html', {'gamer': gamer})

#views for GameLoan model

def all_game_loans(request):
    loans = GameLoan.objects.all()
    return render(request, 'all_game_loans.html', {'loans': loans})

def loan_detail(request, loan_id):
    loan = get_object_or_404(GameLoan, pk=loan_id)
    return render(request, 'loan_detail.html', {'loan': loan})
