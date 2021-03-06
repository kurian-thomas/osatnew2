from django.conf.urls import url,include
from rest_framework import routers
from django.contrib import admin
from osat import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^osat/', include('osat.urls'),name='osat'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
