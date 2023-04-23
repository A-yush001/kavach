from django.urls import path,include
from . views import  FraudViewSet
from rest_framework import routers

router=routers.DefaultRouter()
router.register('fraud',FraudViewSet,basename='frauddetails')

urlpatterns = [
    path('',include(router.urls))
   

]