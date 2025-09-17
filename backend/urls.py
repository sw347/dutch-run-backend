from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from game.views import GameCreateView, GameLeaderboardViewSet, GameDeleteView

router = DefaultRouter()
router.register(r'games', GameLeaderboardViewSet, basename='game')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('game/create/', GameCreateView.as_view(), name='game-create'),
    path('game/delete/<int:pk>/', GameDeleteView.as_view(), name='game-delete'),    
    path('', include(router.urls)),
]