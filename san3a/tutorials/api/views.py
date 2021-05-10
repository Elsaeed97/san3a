from rest_framework import viewsets

from ..models import Tutorial
from .permissions import IsTutorialOwnerOrReadOnly
from .serializers import TutorialSerializer, TutorialSerializerWriter


class TutorialViewSet(viewsets.ModelViewSet):
    queryset = Tutorial.objects.all()
    permission_classes = [IsTutorialOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return TutorialSerializer
        return TutorialSerializerWriter