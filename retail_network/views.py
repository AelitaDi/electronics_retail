from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import IsAuthenticated

from retail_network.models import Link
from retail_network.serializers import (LinkListSerializer, LinkSerializer,
                                        LinkUpdateSerializer)
from users.permissions import IsActiveUser, IsStaffUser


class LinkListAPIView(ListAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkListSerializer
    permission_classes = (
        IsAuthenticated,
        IsActiveUser,
    )


class LinkCreateAPIView(CreateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = (
        IsAuthenticated,
        IsActiveUser,
    )


class LinkRetrieveAPIView(RetrieveAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = (
        IsAuthenticated,
        IsActiveUser,
    )


class LinkUpdateAPIView(UpdateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkUpdateSerializer
    permission_classes = (
        IsAuthenticated,
        IsActiveUser,
    )


class LinkDestroyAPIView(DestroyAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = (
        IsAuthenticated,
        IsStaffUser,
    )
