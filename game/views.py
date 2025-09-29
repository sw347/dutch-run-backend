from rest_framework import generics, viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from django.utils import timezone
from .models import Game
from .serializers import GameSerializer

class GameCreateView(generics.CreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameLeaderboardViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = GameSerializer
    
    def get_queryset(self):
        return Game.objects.all().order_by('-score')[:100]

    @action(detail=False, methods=['delete'])
    def destroy_all(self, request):
        password = request.query_params.get('password')
        if password != '20250916':
            return Response(
                {"detail": "Authentication credentials were not provided or are incorrect."},
                status=status.HTTP_401_UNAUTHORIZED
            )
        Game.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class GameDeleteView(generics.DestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def destroy(self, request, *args, **kwargs):    
        password = request.query_params.get('password')
        
        if password != '20250916':
            return Response(
                {"detail": "Authentication credentials were not provided or are incorrect."},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        return super().destroy(request, *args, **kwargs)

class DailySeedView(APIView):
    
    def get(self, request):
        today_str = timezone.now().strftime('%Y%m%d')
        
        return JsonResponse({
            'status': 'success',
            'date': today_str,
            'seed': int(today_str)
        })