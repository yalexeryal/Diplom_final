from rest_framework.routers import DefaultRouter
from django.urls import path

from app.views import PartnerPriceLoad, CategoryView, ShopView, UserLogin, UserRegister, ProductInfoView, \
    PartnerOrdersView, BasketView, ContactView, OrderView


app_name = 'app'

urlpatterns = [
    path('user/login', UserLogin.as_view(), name='user-login'),
    path('user/register', UserRegister.as_view(), name='user-register'),
    path('user/contact', ContactView.as_view(), name='user-contact'),
    path('user/basket', BasketView.as_view(), name='user-basket'),
    path('user/orders', OrderView.as_view(), name='user-orders'),
    path('partner/load', PartnerPriceLoad.as_view(), name='partner-load'),
    path('partner/orders', PartnerOrdersView.as_view(), name='partner-orders'),
    # path('category', CategoryView.as_view(), name='category-view'),
    # path('shop', ShopView.as_view(), name='shop-view'),
    # path('product', ProductInfoView.as_view(), name='product-view'),
]

router = DefaultRouter()
router.register('category', CategoryView, basename='category-view')
router.register('shop', ShopView, basename='shop-view')
router.register('product', ProductInfoView, basename='product-view')

urlpatterns += router.urls

