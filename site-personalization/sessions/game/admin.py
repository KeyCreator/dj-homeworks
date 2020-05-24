from django.contrib import admin

from .models import Game, Player, PlayerGameInfo


class PlayerInline(admin.TabularInline):
    model = PlayerGameInfo


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    inlines = [PlayerInline]


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    inlines = [PlayerInline]

@admin.register(PlayerGameInfo)
class PlayerGameInfoAdmin(admin.ModelAdmin):
    fields = ('player', 'game', 'is_author', 'attempts')