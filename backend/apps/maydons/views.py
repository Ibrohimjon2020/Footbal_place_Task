import sys
from rest_framework import generics
from rest_framework.response import Response
from datetime import datetime
from .models import Maydon
# from models Buyurtma
from apps.buyurtmas.models import Buyurtma
from .serializers import MaydonSerializer
from apps.permissions import AdminPermission, MaydonEgasiPermission, UserPermission

class MaydonListView(generics.ListAPIView):
    serializer_class = MaydonSerializer
    queryset = Maydon.objects.all()
    permission_classes = [AdminPermission | UserPermission | MaydonEgasiPermission]

    def filter_by_time(self, request):
        date = request.GET.get('date')
        start_time = request.GET.get('start_time')
        end_time = request.GET.get('end_time')

        start_datetime = datetime.strptime(f'{date} {start_time}', '%Y-%m-%d %H:%M:%S')
        end_datetime = datetime.strptime(f'{date} {end_time}', '%Y-%m-%d %H:%M:%S')

        filtered_buyurtma = Buyurtma.objects.filter(created_at__range=[start_datetime, end_datetime])

        maydon_ids = filtered_buyurtma.values_list('maydon_id', flat=True).distinct()

        other_maydonlar = Maydon.objects.exclude(id__in=maydon_ids)

        serializer = MaydonSerializer(other_maydonlar, many=True)
        
        return Response(serializer.data)

class MaydonCreateView(generics.CreateAPIView):
    serializer_class = MaydonSerializer
    queryset = Maydon.objects.all()
    permission_classes = [AdminPermission | MaydonEgasiPermission]
    
class MaydonUpdateView(generics.UpdateAPIView):
    serializer_class = MaydonSerializer
    queryset = Maydon.objects.all()
    permission_classes = [AdminPermission | MaydonEgasiPermission]

class MaydonDeleteView(generics.DestroyAPIView):
    serializer_class = MaydonSerializer
    queryset = Maydon.objects.all()
    permission_classes = [AdminPermission | MaydonEgasiPermission]