from django.db import models


class Player(models.Model):
    name = models.CharField(verbose_name='Имя игрока', max_length=64)

    class Meta:
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'

    def __str__(self):
        return self.name


class Game(models.Model):
    riddle = models.IntegerField(verbose_name='Загаданное число')
    player = models.ManyToManyField(Player,
                                     through='PlayerGameInfo',
                                     through_fields=('game', 'player'))
    is_over = models.BooleanField(verbose_name='Игра закончена',
                                  default=False,
                                  blank=False,
                                  null=False)

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'

    def __str__(self):
        return str(self.riddle)


class PlayerGameInfo(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='games')
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    is_author = models.BooleanField(verbose_name='Основной',
                                    default=False,
                                    null=False)
    attempts = models.IntegerField(verbose_name='Количество попыток отгадывающего игрока',
                                   default=0,
                                   null=False)
