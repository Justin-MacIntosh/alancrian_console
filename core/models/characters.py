from core.models.users import Player

from django.db import models


class Campaign(models.Model):
    dungeon_masters = models.ManyToManyField(Player)

    name = models.CharField(max_length=100)


class Character(models.Model):
    player = models.ManyToManyField(Player)

    name = models.CharField(max_length=100)
    health = models.IntegerField()


class Ability(models.Model):
    character = models.ForeignKey(Character)

    description = models.CharField(max_length=200)
