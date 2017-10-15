from django.conf.urls import url
from django.shortcuts import render
from django.views.generic import View

from core.models import Ability, Character


class ViewerHomeView(View):
    def get(self, request):
        chars = Character.objects.all()
        return render(
            request,
            'character_viewer/viewer_home.html',
            {'chars': chars}
        )

    def post(self, request):
        pass

    @staticmethod
    def urls():
        return [
            url(
                r'^viewer_home/',
                ViewerHomeView.as_view(),
                name='viewer_home'
            )
        ]


class CharacterViewerView(View):
    def get(self, request, character_id):
        character = Character.objects.get(id=character_id)
        abilities = Ability.objects.filter(character=character)

        return render(
            request,
            'character_viewer/character.html',
            {
                'character': character,
                'abilities': abilities
            }
        )

    def post(self, request):
        pass

    @staticmethod
    def urls():
        return [
            url(
                r'^character/(?P<character_id>[\w-]+)',
                CharacterViewerView.as_view(),
                name='character'
            )
        ]
