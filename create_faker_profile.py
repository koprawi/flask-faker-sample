import sys
from faker import Faker
from profile import db, Profile

def create_fake_profile(n):
    """Generate fake profile"""
    faker = Faker(['id_ID'],  use_weighting=True)
    for _ in range(n):
        
        profil = Profile(username=faker.user_name(),
                        name=faker.name(),
                        address=faker.address().replace('\n', ', '),
                        email=faker.email())

        db.session.add(profil)
    db.session.commit()

    print(f'Added {n} fake profile to database')


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('Pass the number of users you want to create as an argument.')
        sys.exit(1)
    create_fake_profile(int(sys.argv[1]))