from django.shortcuts import render, get_object_or_404, redirect
from .models import BoardGame, BoardGamer, GameLoan
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseForbidden
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


## Doesnt work
def edit_board_game(request, game_id):
    game = BoardGame.objects.get(id=game_id)

    if request.method == 'POST':
        # POST data submitted; process data.
        form = BoardGameForm(instance=game, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('board_game_detail', game_id=game.id)
    else:
        # Initial request; pre-fill form with the current entry.
        form = BoardGameForm(instance=game)
    
    print(form.errors)

    context = {'game': game, 'form': form}
    return render(request, 'edit_board_game.html', context)

#views for BoardGamer model

def all_board_gamers(request):
    gamers = BoardGamer.objects.all()
    return render(request, 'all_board_gamers.html', {'gamers': gamers})

def board_gamer_detail(request, gamer_id):
    gamer = get_object_or_404(BoardGamer, pk=gamer_id)
    return render(request, 'board_gamer_detail.html', {'gamer': gamer})

#views for GameLoan model
# Function for user to see the games they have loaned in loaned_games
@login_required
def loaned_games(request):
    user = request.user # Get user
    user_loaned = BoardGame.objects.filter(loaned_to = user) # Get games loaned to user
    return render(request, 'loaned_games.html', {'user_loaned': user_loaned})

# Function for a user loaning the board game from board_game_details
@login_required
def loan_board_game(request, game_id):
    game = BoardGame.objects.get(id=game_id) # Get boardgame
    user = request.user # Get users info

    # Check if there are 3 games loaned already to the user
    check_loaned_count = BoardGame.objects.filter(loaned_to = user).count()
    if check_loaned_count >= 3:
        return HttpResponseForbidden('Cannot loan more than 3 games')
    # If not loan game to user
    if game.available:
        game.available = False
        game.loaned_to = user
        game.save()
    return redirect('board_game_detail', game_id=game.id)

# Function to return loaned board game
@login_required
def return_board_game(request, game_id):
    game = BoardGame.objects.get(id=game_id)
    user = request.user
    if request.method == "POST":
        game.available = True
        game.loaned_to = None
        game.save()
        return redirect('loaned_games')
    
    return render(request, 'return_board_game.html', {'game': game})


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