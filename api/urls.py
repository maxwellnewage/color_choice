from django.urls import path
from rest_framework import routers
from .views import ColorViewSet, VoteViewSet, user_auth, \
    is_voted, generate_fake_users, generate_fake_votes, votes_stats


router = routers.DefaultRouter()

router.register('colors', ColorViewSet, 'colors')
router.register('votes', VoteViewSet, 'votes')

urlpatterns = router.urls

urlpatterns += [
    path('auth', user_auth, name='api-auth'),
    path('votes/voted', is_voted, name='api-votes-voted'),
    path('votes/stats', votes_stats, name='api-votes-stats'),
    path('users/generate/<int:amount>', generate_fake_users),
    path('votes/generate/<int:amount>', generate_fake_votes),
]
