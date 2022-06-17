from faker import Faker

faker = Faker('id_ID')

print(f'name: {faker.user_name()}')
print(f'address: {faker.address()}')
print(f'text: {faker.text()}')
print(f'first name: {faker.first_name()}')
print(f'last name: {faker.last_name()}')
print(f'male name: {faker.name_male()}')
print(f'female name: {faker.name_female()}')


for _ in range(10):
    profile = faker.simple_profile('M')
    print(profile)