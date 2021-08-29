from django.urls import path, include
from rest_framework import routers
from workapp_api.views import CreateUserView, ItemListView, ItemRetrieveView, ItemViewSet

# modelViewSetを継承した場合の設定
router = routers.DefaultRouter()
router.register('items', ItemViewSet, basename = 'items')

urlpatterns = [
    path('item-list/', ItemListView.as_view(), name='item-list'),
    path('item-list/<str:pk>/', ItemRetrieveView.as_view(), name = 'detail-item'),
    path('register/', CreateUserView.as_view(), name = 'register'),
    path('auth/', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]