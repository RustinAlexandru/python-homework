import json
import random
import re
from datetime import date
from datetime import datetime


def f(n):
    return str(n).count('1')


def guess_game():
    random_toguess_number = random.choice(range(1, 20))
    tries = 1
    number_guessed = 0
    guessed = False
    print 'Ma gandesc la un numar intre 1 si 20... Reusesti sa il ghicesti\
        din 5 incercari? '
    while tries <= 5:
        print 'Incercarea ' + str(tries)
        number_guessed = input()
        print 'Numarul ales de tine este: ' + str(number_guessed)
        if number_guessed == random_toguess_number:
            print 'Bravo, ai ghicit numarul din ' + str(tries) + ' incercari! '
            guessed = True
            break
        elif number_guessed < random_toguess_number:
            print 'Numarul la care m-am gandit este mai mare'
        else:
            print 'Numarul la care m-am gandit este mai mic'
        tries += 1
    if not guessed:
        print 'Imi pare rau, dar nu ai ghicit numarul dupa 5 incercari'


def parse_json():
    with open('input.json') as input_file:
        data = json.load(input_file)

    average_age = 0
    number_of_persons = len(data)
    list_of_years = []
    dictionary = {}

    for person in data:
        birthday_string = person['birthday']
        birthday = datetime.strptime(birthday_string, '%d.%m.%Y').date()
        # age = date.today().year - birthday.year
        age = int((date.today() - birthday).days / 365.25)
        list_of_years.append(birthday.year)
        average_age += age

        about_string = person['about']
        name_string = person['name']
        dictionary[name_string] = lookup_email(about_string)

    average_age /= number_of_persons
    list_of_years = list(set(list_of_years))

    json_dictionary = json.dumps(dictionary, indent=4, separators=(',', ': '))

    with open('output.json', 'w') as output_file:
        output_file.write(json_dictionary)


def lookup_email(string_):
    match = re.search('(\w+[.|\w])*@(\w+[.])*\w+', string_)
    if match:
        return match.group(0)
    else:
        return None


def main():
    # guess_game()
    parse_json()


if __name__ == '__main__':
    main()
