from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from game.views import GameCreateView, GameLeaderboardViewSet, GameDeleteView, DailySeedView, GameTopLankView

router = DefaultRouter()
router.register(r'games', GameLeaderboardViewSet, basename='game')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('game/create/', GameCreateView.as_view(), name='game-create'),
    path('game/delete/<int:pk>/', GameDeleteView.as_view(), name='game-delete'),
    path('game/top-rank/', GameTopLankView.as_view(), name='game-top-rank'),
    path('api/daily_seed/', DailySeedView.as_view(), name='daily-seed'),
    path('', include(router.urls)),
]