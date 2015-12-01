def ex1():
    for i in range(100):
        print 'Hello world'


def ex2():
    string_ = ''
    for i in range(100):
        string_ += 'hello'
    print string_

a = [1, 3, 20, 1024, 53, 12, 102, 1, 4, 43, 32]


def ex3():
    for elem in a:
        if elem % 3 == 0:
            print str(elem) + ' numar divizil cu 3!'


def ex4():
    b = []
    for i in range(len(a)):
        if i % 2 == 0:
            b.append(a[i])
    print b


def ex5():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print 'fizz buzz ' + str(num)
        elif num % 3 == 0:
            print 'fizz ' + str(num)
        elif num % 5 == 0:
            print 'buzz ' + str(num)
        else:
            print num


def ex6():
    lista = {
        "tastatura": 70,
        "mouse": 50,
        "casti": 50,
    }
    sum = 0
    for elem in lista:
        tva = 0.24 * lista[elem]
        lista[elem] += tva
        sum += lista[elem]
        print elem + ' ' + str(lista[elem])
    print 'Suma totala a cumparaturilor: ' + str(sum)


# ex7
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def ex8():
    resultString = ''
    for num in range(2000, 3001):
        if num % 5 == 0 and num % 7 == 0:
            resultString += str(num) + ', '
    print resultString

# ex9


def is_palindrome(arg):
    reversed = ''
    for i in range(len(arg) - 1, -1, -1):
        reversed += arg[i]
    if reversed == arg:
        print 'Palindrome!'
    else:
        print 'Not a palindrome'

# ex10


def equalLists(list1, list2):
    for l1 in list1:
        for l2 in list2:
            if l1 == l2:
                return True
    return False

# ex11


def find_longest_word(listOfWords):
    max = ''
    for word in listOfWords:
        if len(word) > max:
            max = word
    print word

# ex12


def filter_long_words(listOfWords, n):
    resultList = []
    for word in listOfWords:
        if len(word) > n:
            resultList.append(word)
    return resultList


# ex13
def sum(*args):
    sum = 0
    for arg in args:
        sum += arg
    print sum

# sum(1,2,3)

# ex14


def decipher(list):
    result = ""
    for letter in list:
        if letter >= 'b' and letter <= 'z':
            result += chr(ord(letter) - 1)
        elif letter == 'a':
            result += 'z'
        else:
            result += letter

    return result


def main():
        # ex1()
        # ex2()
        # ex3()
        # ex4()
        # ex5()
        # ex6()
        # print factorial(5)
        # ex8()
        # is_palindrome('radar')
        # is_palindrome('ana')
        # is_palindrome('costel')
        # print(equalLists([1,2,3],[4,2,6]))
        # find_longest_word(["gigi",'ana',"gegegegegegegege"])
        # print filter_long_words(['gige', 'mere', 'perere', 'apa'], 4)
        # sum(1, 2, 3)
        # print decipher("j mjlf cjh cvuut boe j dboopu mjf\nzpv puifs cspuifst
        # dbo'u efoz")

if __name__ == '__main__':
    main()
