from django.urls import path

from . import views as api_views


urlpatterns = [
    path(
        'v1/playgroups',
        api_views.playgroups.as_view(),
        name='playgroups'
    ),
    path(
        'v1/playgroup/<str:playgroup_id>/players',
        api_views.playgroup_players.as_view(),
        name='playgroup_players'
    ),
    path(
        'v1/playgroup/<str:playgroup_id>/player/<str:player_id>',
        api_views.playgroup_player.as_view(),
        name='playgroup_player'
    ),
]
