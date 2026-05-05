# from inspect import signature
from random import randint

from faker import Faker

from random import choice


def rand_ratio():
    return randint(840, 900), randint(473, 573)


fake = Faker('pt_BR')
# print(signature(fake.random_number))

BRIAR_SKINS=[0,1,10]


def make_recipe():
    RandonSkin= choice(BRIAR_SKINS)
    UrlSkin = f'https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Briar_{RandonSkin}.jpg'
    return {
        'id' : randint(1,100),
        'title': fake.sentence(nb_words=6),
        'description': fake.sentence(nb_words=20),
        'preparation_time': fake.random_number(digits=2, fix_len=True),
        'preparation_time_unit': 'Minutos',
        'servings': fake.random_number(digits=2, fix_len=True),
        'servings_unit': 'Porção',
        'preparation_steps': fake.text(3000),
        'created_at': fake.date_time(),
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'category': {
            'name': fake.word()
        },
        'cover': {
            'url':  UrlSkin,
        }
    }


if __name__ == '__main__':
    from pprint import pprint
    pprint(make_recipe())