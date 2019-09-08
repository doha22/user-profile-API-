from django.conf.urls import url
from django.conf.urls import include

# defaultroute used only in django rest framework
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('hello_viewset',views.helloViewSet , base_name='hello_viewset')

router.register('profile',views.UserProfileViewSet)
router.register('login',views.loginViewSet , base_name='login')

urlpatterns = [
    # it renders api (helloapiview) and .as_view() , it will return as obj
    url(r'^hello_view/',views.HelloApiView.as_view()),
    url(r'',include(router.urls))

]

# urlpatterns = [
#     url(r'^hello-view/', views.HelloApiView.as_view()),
#     url(r'', include(router.urls))
# ]