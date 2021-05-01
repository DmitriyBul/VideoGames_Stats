from django.shortcuts import render, get_object_or_404
from .models import Category, Game


def game_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    games = Game.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        games = games.filter(category=category)
    return render(request, 'games/game/list.html',
                  {'category': category,
                   'categories': categories,
                   'games': games})


def game_detail(request, id, slug):
    game = get_object_or_404(Game, id=id, slug=slug)
    return render(request, 'games/game/detail.html', {'game': game})
