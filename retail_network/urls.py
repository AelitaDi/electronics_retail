from django.urls import path

from retail_network.apps import RetailNetworkConfig
from retail_network.views import (LinkCreateAPIView, LinkDestroyAPIView,
                                  LinkListAPIView, LinkRetrieveAPIView,
                                  LinkUpdateAPIView)

app_name = RetailNetworkConfig.name

urlpatterns = [
    path("links/", LinkListAPIView.as_view(), name="link_list"),
    path("links/<int:pk>/", LinkRetrieveAPIView.as_view(), name="link_retrieve"),
    path("links/create/", LinkCreateAPIView.as_view(), name="link_create"),
    path("links/update/<int:pk>/", LinkUpdateAPIView.as_view(), name="link_update"),
    path("links/delete/<int:pk>/", LinkDestroyAPIView.as_view(), name="link_delete"),
]
