from django.conf.urls.static import static
from django.urls import path, include
from site_app.views import BaseView, DeviseMenu, DeviceDetail
from testsite import settings

urlpatterns = [

    path('', BaseView.as_view(), name='menu-main'),
    path('/<str:device>', DeviseMenu.as_view(), name='menu-device'),
    path('/detail/<str:category>', DeviceDetail.as_view(), name='menu-detail'),
]