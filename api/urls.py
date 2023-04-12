from django.urls import path
from rest_framework import routers
from .views import ColorViewSet, VoteViewSet, user_auth, is_voted, generate_fake_users


router = routers.DefaultRouter()

router.register('colors', ColorViewSet, 'colors')
router.register('votes', VoteViewSet, 'votes')

urlpatterns = router.urls

urlpatterns += [
    path('auth', user_auth, name='api-auth'),
    path('votes/voted', is_voted, name='api-votes-voted'),
    path('users/generate/<int:amount>', generate_fake_users),
]
