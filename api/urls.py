from django.urls import path
from rest_framework import routers
from .views import ColorViewSet, VoteViewSet


router = routers.DefaultRouter()

router.register('colors', ColorViewSet, 'colors')
router.register('votes', VoteViewSet, 'votes')

urlpatterns = router.urls
