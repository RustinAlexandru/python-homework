from datetime import datetime
from bs4 import BeautifulSoup
import requests


class Book(object):
    def function():
        pass


class BookStore(object):
    def __init__(self, url):
        self.url = url



# Functie ajutatoare folosita la testare.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '{0} got: {1}, expected: {2}'.format(prefix, got, expected)


# Functia care testeaza rezultatele.
def main():
    bs = BookStore('https://today.java.net/images/2007/04/books.xml')
    test(len(bs.books), 6)
    book = bs.books[0]
    test(book.title, 'Pride and Prejudice')
    test(book.author, 'Jane Austen')
    test(book.publisher, 'Modern Library')
    test(book.language, 'English')
    test(book.isbn, '0679601686')
    test(book.quantity, 187)
    test(book.pages, 352)
    test(book.price, 4.95)
    test(book.category, 'MMP')
    test(book.publication_date, datetime(2002, 12, 31))

    test(bs.search('affair'), None)
    test(bs.search('affair', ignore_case=True), bs.books[-1])

    book = bs.search('Height')
    test(bs.buy(book, 2), 13.16)
    test(bs.books[1].quantity, 111)
    test(bs.buy(u'Jude the Obscure', 2), 0)

    bs.order_by('title')
    test([b.title for b in bs.books],
         [u'Jude the Obscure',
          u'Pride and Prejudice',
          u"Tess of the d'Urbervilles",
          u'The Big Over Easy',
          u'The Eyre Affair',
          u'Wuthering Heights'])
    bs.order_by('publication_date')
    test([b.publication_date.year for b in bs.books],
         [1984, 1998, 2002, 2002, 2003, 2005])
    bs.order_by('pages')
    test([b.pages for b in bs.books],
         [346, 352, 384, 430, 480, 528])

    test(bs.total_cost, 6964.59)

    test(len(bs.categories), 3)
    test(bs.categories_count,
         {u'Hard Cover': 1, u'Paperback': 4, u'Mass-market Paperback': 1})

if __name__ == '__main__':
    main()
