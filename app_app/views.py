from django.shortcuts import render, get_object_or_404, redirect
from .models import BoardGame, BoardGamer, GameLoan
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import *


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

def new_board_game(request):
    # Add a new game
    if request.method != "POST":
        form = BoardGameForm
    else:
        form = BoardGameForm(data=request.POST)
        if form.is_valid():
            new_game = form.save(commit=False)
            new_game.owner = request.user
            new_game.save()
            return redirect('all_board_games')
    context = {'form': form}
    return render(request, 'new_board_game.html', context)

def edit_board_game(request, game_id):
    """Edit an existing board game."""
    game = BoardGame.objects.get(id=game_id)
    #game = get_object_or_404(BoardGame, pk=game_id, owner=request.user)

    if request.method != 'POST':
        #Initial request; pre-fill form with the current entry.
        form = BoardGameForm(instance=game)
    else:
        #POST data submitted; process data.
        form = BoardGameForm(instance=game, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('board_game_detail', game_id=game.id) 

    context = {'game': game, 'form': form}
    return render(request,'edit_board_game.html', context)

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

# Authentication views

# Registration
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# Login
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('homepage')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

# Logout
def user_logout(request):
    logout(request)
    return redirect('homepage')