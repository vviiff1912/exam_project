from django.urls import path
from exam_project.common.views import bought_games, comment_game

urlpatterns = (
    path('<int:pk>/', bought_games, name='bought games'),
    path('comment/<int:game_id>/<int:user_id>/', comment_game, name='comment game'),
)
