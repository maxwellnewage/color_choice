from faker import Faker
from api.models import User

fake = Faker()


def fake_users(num_users):
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
