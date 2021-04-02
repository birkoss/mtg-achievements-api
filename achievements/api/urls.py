from django.urls import path

from . import views as api_views


urlpatterns = [
    path(
        'v1/playgroup/<str:playgroup_id>/players',
        api_views.playgroup_players.as_view(),
        name='playgroup_players'
    ),
]
