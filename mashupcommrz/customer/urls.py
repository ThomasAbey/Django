from django.urls import path

from . import views


urlpatterns = [
     path('registercustomer', views.registercustomer, name='registercustomer'),
     path('logout', views.logoutcustomer, name='logoutcustomer'),
     path('logincustomer', views.logincustomer, name='logincustomer'),
     path('products', views.homepage, name='products'),
     path('addtocart', views.addproducttocart, name='addtocart'),
     path('removefromcart', views.removeproductfromcart, name='removefromcart'),
     path('viewcustomercart', views.viewcustomercart, name='viewcustomercart'),
     path('removefromcartpage/', views.removeproductcartpage, name='removeproductcartpage'),
     path('checkoutcustomer', views.checkoutcustomer, name='checkoutcustomer'),
     path('markpaymentsuccess', views.markpaymentsuccess, name='markpaymentsuccess'),
     ]