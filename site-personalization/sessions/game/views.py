from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from .models import Game, Player, PlayerGameInfo
from .forms import GameForm


class GameView(View):
    form_class = GameForm
    # initial = {'key': 'value'}
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(request.GET)
        player = create_player(request)
        context = {}
        context['form'] = form

        new_game = request.GET.get('new')
        if new_game:
            finish_game(player, Game.objects.get(is_over=False))
            return redirect('/')

        if form.is_valid():
            form_data = form.cleaned_data
            context['is_game'] = game_found()

            if context['is_game']:
                game = Game.objects.get(is_over=False)
                join_game(player, game)
                context['is_author'] = player_is_author(player, game)
                if context['is_author']:
                    context['statistic'] = get_statistic(Game.objects.get(is_over=False))
                    context['is_true_answer'] = \
                        True if PlayerGameInfo.objects.filter(game=game, is_true_answer=True).count() else False
                else:
                    join_game(player=player, game=game)
                    if form_data.get('riddle'):
                        increase_attempts(player=player, game=game)
                        if form_data['riddle'] < game.riddle:
                            context['message'] = 'Ваше число меньше'
                        elif form_data['riddle'] > game.riddle:
                            context['message'] = 'Ваше число больше'
                        else:
                            context['message'] = 'Вы угадали заданное число'
                            stop_game(player, game)

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        context = {}

        if Game.objects.filter(is_over=False).count():
            return redirect('/')

        if form.is_valid():
            # <process form cleaned data>
            data = form.cleaned_data
            create_game(request, data['riddle'])
            context['form'] = form
            context['is_author'] = True
            context['is_game'] = True
            context['riddle'] = data['riddle']
            context['statistic'] = get_statistic(Game.objects.get(is_over=False))
            return render(request, self.template_name, context)

        return render(request, self.template_name, {'form': form})


def create_game(request, riddle):
    player = create_player(request)

    game_id = request.session.get('game_id')
    if not game_id or not Game.objects.filter(id=game_id, is_over=False).count():
        game = Game()
        game.riddle = riddle
        game.save()
        request.session['game_id'] = game.id

        join_game(player, game, is_author=True)


def game_found():
    count = Game.objects.filter(is_over=False).count()
    return count == 1


def join_game(player, game, is_author=False):
    if not PlayerGameInfo.objects.filter(player=player, game=game).count():
        game.player.add(player)
        info = PlayerGameInfo.objects.get(player=player, game=game)
        info.is_author = is_author
        info.save()


def create_player(request):
    player_id = request.session.get('player_id')
    if not player_id:
        player = Player()
        if not request.session.session_key:
            request.session.save()
        player.name = player.id
        player.save()
        request.session['player_id'] = player.id
    else:
        player = Player.objects.get(id=player_id)

    return player


def increase_attempts(player, game):
    info = PlayerGameInfo.objects.get(player=player, game=game)
    info.attempts += 1
    info.save()


def get_statistic(game):
    info = PlayerGameInfo.objects.filter(game=game, is_author=False)
    statistic = list()
    statistic.append(f'Вы загадали число {game.riddle}')

    if PlayerGameInfo.objects.filter(game=game, is_true_answer=True).count():
        statistic.append('Ваше число угадали')
    else:
        statistic.append('Игра продолжается')

    for bar in info:
        statistic.append(f'Игрок {bar.player.name} сделал {bar.attempts} попыток')

    return statistic


def stop_game(player, game):
    info = PlayerGameInfo.objects.get(player=player, game=game)
    info.is_true_answer = True
    info.save()


def finish_game(player, game):
    stop_game(player, game)
    game.is_over = True
    game.save()

def player_is_author(player, game):
    return PlayerGameInfo.objects.get(player=player, game=game).is_author