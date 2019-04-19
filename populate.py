import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main_project.settings')

import django
django.setup()

## Fake Population script
import random

from my_app.models import User
from faker import Faker

fake = Faker()


def populateUser(N=10):

    for entry in range(N):

        full_name = fake.name()
        first_name = full_name.split()[0]
        last_name = full_name.split()[1]
        email = "{}@{}.com".format(first_name, last_name)
        print(email[0])

        user = User.objects.get_or_create(first_name=first_name, last_name=last_name, email=email)


if __name__ == "__main__":
    print("populating users")
    populateUser(50)
    print("Done!")