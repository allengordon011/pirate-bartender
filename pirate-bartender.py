questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

preferences = {
    "strong": False,
    "salty": False,
    "bitter": False,
    "sweet": False,
    "fruity": False,
}


def customer_prefs():
    strong = input(questions["strong"])
    salty = input(questions["salty"])
    bitter = input(questions["bitter"])
    sweet = input(questions["sweet"])
    fruity = input(questions["fruity"])
    if strong == ('yes') or strong == ('y'):
        preferences["strong"] = True
    if salty == ('yes') or salty == ('y'):
        preferences["salty"] = True
    if bitter == ('yes') or bitter == ('y'):
        preferences["bitter"] = True
    if sweet == ('yes') or sweet == ('y'):
        preferences["sweet"] = True
    if fruity == ('yes') or fruity == ('y'):
        preferences["fruity"] = True
    # print (preferences)

import random

def make_drink(prefs):
    drink = []
    if preferences["strong"] == True:
        drink.append(random.choice(ingredients["strong"]))
    if preferences["salty"] == True:
        drink.append(random.choice(ingredients["salty"]))
    if preferences["bitter"] == True:
        drink.append(random.choice(ingredients["bitter"]))
    if preferences["sweet"] == True:
        drink.append(random.choice(ingredients["sweet"]))
    if preferences["fruity"] == True:
        drink.append(random.choice(ingredients["fruity"]))
    return drink

if __name__ == '__main__':
    customer_prefs()
    drink = make_drink(preferences)
    if drink == []:
        print('Yer too picky! Get ye lost!')
    print('Yer drink is served! Arrr... it consists of {}'.format(drink))
