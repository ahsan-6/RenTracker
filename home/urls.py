from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name = 'home'),
    path('register/',views.registerUser, name = 'register'),
    path('login/',views.loginUser,name = 'login'),
    path('logout/',views.logoutUser,name = 'logout' ),
    

    path('', views.renterDetails, name = 'home'),
    path('add_renter',views.addRenter, name = 'add renter'),
    path('renter/<str:pk>/',views.renter,name = 'renter'),
    path('edit_renter/<str:pk>',views.editRenter,name = 'edit renter'),

    path('property_details/', views.propertyDetails, name = 'property details'),
    path('add_property',views.addProperty,name = 'add property'),
    path('property/<str:pk>/',views.property,name='property'),
    path('edit_property/<str:pk>',views.editProperty,name='edit property'),
    

    path('transaction_details/',views.transactionDetails, name = 'transaction details'),
    path('add_transaction', views.addTransaction, name = 'add transaction'),

    path('change_password/',views.changePassword,name='change password'),
]