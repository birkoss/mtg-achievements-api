from django.contrib import admin

from .models import Achievement, Game, GameAchievement, GamePlayer, PlayerAchievement, PlayerRole


admin.site.register(Achievement)
admin.site.register(Game)
admin.site.register(GameAchievement)
admin.site.register(GamePlayer)
admin.site.register(PlayerAchievement)
admin.site.register(PlayerRole)
