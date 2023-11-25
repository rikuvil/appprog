from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class BoardGame(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, default='none')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    date_added = models.DateTimeField(default=timezone.now)
    #last_modified = models.DateTimeField(default=timezone.now)
    # Add other fields as needed

    def __str__(self):
        return self.name

class BoardGamer(models.Model):
    name = models.CharField(max_length=100)
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    #borrowed_games = models.ManyToManyField(BoardGame, through='GameLoan')
    # Add other fields as needed

    def __str__(self):
        return self.name

class GameLoan(models.Model):
    board_game = models.ForeignKey(BoardGame, on_delete=models.CASCADE)
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    #borrower = models.ForeignKey(BoardGamer, on_delete=models.CASCADE)
    loan_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.board_game} - {self.borrower} - {self.loan_date}"
    
    #Display the most recent loan first
    class Meta:
        ordering = ['-loan_date']
