from django.contrib.auth import get_user_model
from django.db import models
from exam_project.games.models import GameModel

UserModel = get_user_model()


class BoughtGame(models.Model):
    game = models.ForeignKey(
        GameModel,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = ('game', 'user')


class GameComment(models.Model):
    text = models.CharField(max_length=200, null=False, blank=False,)
    publication_date_and_time = models.DateTimeField(auto_now_add=True, blank=True, null=False,)
    game = models.ForeignKey(GameModel, on_delete=models.RESTRICT, null=False, blank=True,)
    user = models.ForeignKey(UserModel, on_delete=models.RESTRICT, null=False, blank=True,)

    def __str__(self):
        return self.text
