from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from exam_project.accounts.models import AppUser
from exam_project.common.forms import GameCommentForm
from exam_project.common.models import BoughtGame
from exam_project.games.models import GameModel


def bought_games(request, pk):
    user = AppUser.objects.filter(pk=pk).get()
    all_games = BoughtGame.objects.all()
    games = []
    for game in all_games:
        if game.user.pk == user.pk:
            games.append(game)

    context = {'all_games': games, 'user': user, }

    return render(request, 'bought_games.html', context)


@login_required
def comment_game(request, game_id, user_id):
    game = GameModel.objects.filter(pk=game_id).get()
    user = AppUser.objects.filter(pk=user_id).get()

    if request.method == 'GET':
        form = GameCommentForm()
    else:
        form = GameCommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.game = game
            comment.user = user
            comment.save()
            return redirect('index')

    context = {
        'form': form,
        'game': game,
        'user': user,
    }
    return render(request, 'comment-game.html', context, )
