from django.urls import path
from rest_framework import routers
from .views import ColorViewSet, VoteViewSet, user_auth, is_voted


router = routers.DefaultRouter()

router.register('colors', ColorViewSet, 'colors')
router.register('votes', VoteViewSet, 'votes')

urlpatterns = router.urls

urlpatterns += [
    path('auth', user_auth, name='api-auth'),
    path('votes/voted', is_voted, name='api-votes-voted')
]
