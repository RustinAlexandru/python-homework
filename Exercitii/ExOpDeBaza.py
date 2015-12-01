import random
import time
from datetime import date
from datetime import datetime
import re


def ex1():
    length = 0
    with open('input.txt', 'r') as f, open('output.txt', 'w') as output:
        for line in f:
            length += 1
        output.write(str(length))


def ex2():
    with open('output.txt', 'w') as output:
        randLineNum = random.choice(range(1, 10, 2))
        for i in range(1, crandLineNum + 1):
            randNum = random.choice(range(100, 1000, 2))
            output.write(str(randNum) + '\n')


# ex3
def ex3():
    with open('input.txt', 'r') as f:
        birthday_string = f.read()
        birthday = datetime.strptime(birthday_string, '%Y %m %d').date()
        timeElapsed = date.today() - birthday
    print timeElapsed


# ex4
def ex4():
    cards = [
        'ace',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '10',
        'jack',
        'queen',
        'king', ]
    suits = ['clubs',
             'diamonds',
             'hearts',
             'spades', ]
    random_card = random.choice(cards)
    random_suit = random.choice(suits)
    rand_card = random_card + ' ' + random_suit
    return rand_card

# ex5


def ex5():
    rand_hand = []
    while len(rand_hand) != 5:
        rand_card = ex4()
        if rand_card not in rand_hand:
            rand_hand.append(rand_card)
    print rand_hand


# ex6
def ex6():
    # v1
    # extragere = []
    # while len(extragere) != 6:
    #     numar = random.randint(1,50)
    #     if numar not in extragere:
    #         extragere.append(numar)
    # print extragere

    # v2
    extragere = random.sample(range(1, 50), 6)
    print extragere


def ex7():
    n = input('Dati un n: ')
    sum = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            sum += i**2
    print sum


def ex8(number):
    regexp = re.compile(r'021([0-9]{7})')
    match = regexp.search(number)
    if match:
        print 'true'
    else:
        print 'false'


# ex9
def ex9(arg='default'):
    now = datetime.now()
    if arg == 'america' or arg == 'USA' or arg == 'US':
        print now.strftime('%B %d, %Y - %H:%M')
    else:
        print now.strftime('%H:%M / %d.%m')


def main():
    # ex1()
    # ex2()
    # ex3()
    # ex4()
    # ex5()
    # ex6()
    # ex7()
    # ex8('noul meu numar este 0218822555, este scris in clar')
    # ex8(testNumber('noul meu numar este 0218822sss, dar este codificat')
    # ex8('Din numarul meu 021882255 lipseste o cifra')
    # ex9()
    # ex9('US')

if __name__ == '__main__':
    main()
