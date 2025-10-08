from rest_framework import generics, viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from django.utils import timezone
from .models import Game
from .serializers import GameSerializer, GameRankSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

class GameCreateView(generics.CreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

@method_decorator(cache_page(60 * 5), name='list')
class GameTopLankView(generics.ListAPIView):
    serializer_class = GameSerializer

    def get_queryset(self):
        today = timezone.now().date()
        
        queryset = Game.objects.filter(
            date__date=today
        ).order_by('-score')[:10]
        
        return queryset

@method_decorator(cache_page(60 * 5), name='list')
class GameLeaderboardViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = GameRankSerializer
    
    def get_queryset(self):
        today = timezone.now().date()
        
        queryset = Game.objects.filter(
            date__date=today
        ).order_by('-score')[:100]
        
        return queryset

    @action(detail=False, methods=['delete'])
    def destroy_all(self, request):
        password = request.query_params.get('password')
        if password != '20250916':
            return Response(
                {"detail": "Authentication credentials were not provided or are incorrect."},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        today_date = timezone.localtime().date()    
        
        deleted_count, _ = self.get_queryset().filter(
            created_at__date=today_date # 오늘 날짜와 일치하는 레코드만 필터링합니다.
        ).delete()
    
        if deleted_count > 0:
            message = f"{deleted_count} records for today ({today_date}) have been successfully deleted."
            return Response({"detail": message}, status=status.HTTP_204_NO_CONTENT)
        else:
            message = f"No records found for today ({today_date}) to delete."
            return Response({"detail": message}, status=status.HTTP_200_OK)
    
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

@method_decorator(cache_page(60 * 5), name='list')
class DailySeedView(APIView):
    
    def get(self, request):
        today_str = timezone.now().strftime('%Y%m%d')
        
        return JsonResponse({
            'status': 'success',
            'date': today_str,
            'seed': int(today_str)
        })