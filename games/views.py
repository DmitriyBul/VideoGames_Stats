from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

from games.forms import SearchForm, GameCreationForm
from .models import Category, Game, Wishlist
from account.models import Profile
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank


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


def games_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            search_vector = SearchVector('title')
            search_query = SearchQuery(query)
            results = Game.objects.annotate(
                search=search_vector,
                rank=SearchRank(search_vector, search_query)
            ).filter(search=search_query).order_by('-rank')
    return render(request, 'games/game/search.html', {'form': form,
                                                      'query': query,
                                                      'results': results})


@login_required
def game_create(request):
    if request.method == 'POST':
        # Форма отправлена.
        form = GameCreationForm(request.POST, request.FILES)
        if form.is_valid():
            # Данные формы валидны.
            # img = form.cleaned_data.get("image")
            cd = form.cleaned_data
            new_item = form.save(commit=True)

            form.save()
            # Добавляем пользователя к созданному объекту.
            new_item.save()
            messages.success(request, 'Game added successfully')
            # Перенаправляем пользователя на страницу сохраненного изображения.
            return redirect(new_item.get_absolute_url())
    else:
        # Заполняем форму данными из GET-запроса.
        form = GameCreationForm(data=request.GET)
    return render(request,
                  'games/game/create.html',
                  {'section': 'images', 'form': form})
