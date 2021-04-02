from django.contrib import admin

from .models import (
    Achievement, Playgroup, PlaygroupAchievement,
    PlaygroupPlayer, PlayerAchievement, PlayerRole
)


admin.site.register(Achievement)
admin.site.register(Playgroup)
admin.site.register(PlaygroupAchievement)
admin.site.register(PlaygroupPlayer)
admin.site.register(PlayerAchievement)
admin.site.register(PlayerRole)
