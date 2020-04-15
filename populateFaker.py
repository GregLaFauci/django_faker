import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

import django

django.setup()

# import model and Faker
from myApp.models import UserRecord
from faker import Faker

fake_generator = Faker()


def populate(N=5):
    for entry in range(N):
        # Now create fake data
        fake_name = fake_generator.name()
        fake_first_name = fake_name.split()[0]
        fake_last_name = fake_name.split()[1]
        fake_email = fake_generator.email()
        

        # now entry those data on database
        model_data = UserRecord.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]


if __name__ == '__main__':
    print('POPULATING DATABASE')
    populate(25)
    print("COMPLETE")