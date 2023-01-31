from django.urls import path
from .views import Home, addCart, cartdetail, loginform, Promo, orderHistory, partner, partner_info, preorder, register, contact, registerParner, removeCart, search, showproduct, signOutView, thankyou, viewOrder

urlpatterns = [
    path('', Home, name="Home"),
    path('login', loginform, name="login"),
    path('logout', signOutView, name="signOut"),
    path('Promo', Promo, name="Promotion"),
    path('register', register, name="register"),
    path('partner', partner, name="partner"),
    path('contact', contact, name="contact"),
    path('thankyou', thankyou, name="thankyou"),
    path('registerPartner', registerParner, name="registerParner"),
    #หน้ารายละเอียด
    path('preorder', preorder, name="preorder"),
    path('showproduct/<slug:category_slug>/<slug:product_slug>', showproduct, name="showproduct"),
    path('addCart<int:product_id>',addCart, name="addCart"),
    path('remove<int:product_id>',removeCart, name="removeCart"),
    path('cartdetail',cartdetail, name="cartdetail"),
    path('orderHistory/',orderHistory, name="orderHistory"),
    path('order/<int:order_id>',viewOrder, name="orderDetails"),
    path('partnerinfo',partner_info, name="partnerinfo"),
    path('search',search, name="search"),
]
