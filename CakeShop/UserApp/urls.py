from django.urls import path
from . import views
urlpatterns =[
    path('',views.homepage),
    path('signup',views.signup),
    path('login',views.login),
    path('viewdetails/<did>',views.viewdetails),
    path('showcakes/<did>',views.showcakes),
    path('signout',views.signout),
    path('cart',views.cart),
    path('delete/<did>',views.delete),
    path('showallrecord',views.showallrecord),
    path('Makepayment',views.Makepayment),

] 