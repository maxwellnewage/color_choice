from faker import Faker
from api.models import User, Color, Vote
from random import choice


def fake_users(num_users):
    fake = Faker()
    user_list = []
    for i in range(num_users):
        username = fake.user_name()
        email = fake.email()
        password = fake.password()
        first_name = fake.first_name()
        last_name = fake.last_name()
        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        user.save()
        user_list.append(user)

    return user_list


def fake_votes(num_votes):
    vote_list = []
    colors = Color.objects.all()
    users = User.objects.all()

    while len(vote_list) < num_votes:
        random_color = choice(colors)
        random_user = choice(users)

        old_vote = Vote.objects.filter(user=random_user).first()
        if old_vote is None:
            vote = Vote.objects.create(user=random_user, color=random_color)
            vote.save()
            vote_list.append(vote)

    return vote_list
