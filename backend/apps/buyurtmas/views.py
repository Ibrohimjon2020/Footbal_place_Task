import sys
from rest_framework import generics
from .models import Buyurtma
from apps.maydons.models import Maydon
from .serializers import BuyurtmaSerializer
from apps.permissions import AdminPermission, MaydonEgasiPermission, UserPermission

class BuyurtmaListView(generics.ListAPIView):
    serializer_class = BuyurtmaSerializer
    queryset = Buyurtma.objects.all()
    permission_classes = [AdminPermission | UserPermission | MaydonEgasiPermission]

    def get_queryset(self):
        user = self.request.user

        if user.role in ['user', 'admin']:
            return Buyurtma.objects.all()
        
        elif user.role =='maydon_egasi':
            maydonlar = Maydon.objects.filter(user_id=user.id).first()
            return Buyurtma.objects.filter(maydon_id=maydonlar.id)

class BuyurtmaCreateView(generics.CreateAPIView):
    serializer_class = BuyurtmaSerializer
    queryset = Buyurtma.objects.all()
    permission_classes = [UserPermission | AdminPermission]
    
class BuyurtmaUpdateView(generics.UpdateAPIView):
    serializer_class = BuyurtmaSerializer
    queryset = Buyurtma.objects.all()
    permission_classes = [AdminPermission]

class BuyurtmaDeleteView(generics.DestroyAPIView):
    serializer_class = BuyurtmaSerializer
    queryset = Buyurtma.objects.all()
    permission_classes = [AdminPermission | MaydonEgasiPermission]

    def get_object(self):
        buyurtma_id = self.kwargs.get('pk')
        return Buyurtma.objects.get(pk=buyurtma_id)

    def get_queryset(self):
        user = self.request.user
        buyurtma_id = self.kwargs.get('pk')

        if user.role == 'maydon_egasi':
            maydon = Maydon.objects.filter(user_id=user.id).first()

            if maydon:
                # Check if the Buyurtma belongs to the correct Maydon
                buyurtma = Buyurtma.objects.filter(pk=buyurtma_id, maydon=maydon).first()

                if buyurtma:
                    return Buyurtma.objects.filter(pk=buyurtma_id)

            # Deny permission if Maydon instance doesn't exist or Buyurtma is not associated with the correct Maydon
            self.permission_denied(
                self.request,
                message='Maydon instance does not exist for the current user or the Buyurtma is not associated with the correct Maydon.'
            )
        elif user.role == 'admin':
            return Buyurtma.objects.filter(pk=buyurtma_id)

        return Buyurtma.objects.all()