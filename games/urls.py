from django.urls import path
from . import views

app_name = 'games'
urlpatterns = [
    path('', views.game_list, name='game_list'),
    path('add-game/<int:id>/', views.add_game, name='add_game'),
    path('<slug:category_slug>/', views.game_list,
         name='game_list_by_category'),
    path('<int:id>/<slug:slug>/', views.game_detail, name='game_detail'),
]
