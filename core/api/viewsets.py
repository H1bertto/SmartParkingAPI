from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from core.models import Status
from .serializers import StatusSerializer


class StatusViewSet(ModelViewSet):

    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    filter_backends = [filters.SearchFilter]
    http_method_names = ['get']
