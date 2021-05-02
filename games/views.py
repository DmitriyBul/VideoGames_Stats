from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .models import Category, Game, Wishlist
from account.models import Profile


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


@login_required
def add_game(request, id):
    game = get_object_or_404(Game, id=id)
    user = User.objects.get(id=request.user.id)
    profile = Profile.objects.filter(user=user).get()
    profile.games.add(game)
    wished_item = Wishlist.objects.get_or_create(wished_item=game, user=request.user)
    return render(request, 'games/game/success.html', {'game': game})



