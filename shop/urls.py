from django.urls import path
from  .import views
urlpatterns=[
    path('',views.home,name="home"),
    path('register',views.register,name="register"),
    path('login',views.login_page,name="login"),
    path('logout',views.logout_page,name="logout"),
    path('cart',views.cart_page,name="cart"),
    path('fav',views.fav_page,name="fav"),
    path('favviewpage',views.favviewpage,name="favviewpage"),
    path('remove_cart/<str:cid>/',views.remove_cart,name="remove_cart"),
    path('remove_fav/<str:fid>/',views.remove_fav,name="remove_fav"),
    path('PlotType',views.PlotType,name="PlotType"),
    path('PlotType/<str:name>/',views.PlotTypeviews,name="PlotTypeViews"),
    path('PlotDetails/<str:cname>/<str:pname>/',views.plot_details,name="plot_details"),
    path('addtocart',views.add_to_cart,name="addtocart"),
    
]
