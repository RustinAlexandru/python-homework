# -*- coding: utf-8 -*-

"""
Ex. 1
Definiți clasa DateRange care primește la inițializare o valoare start și o
valoare end, ambele fiind obiecte datetime.date.
Adăugați proprietatea:
    - days - returnează numărul de zile din intervalul [start, end]
Adăugați metoda:
    - contains - primește un obiect date și returnează True dacă data se
                  află în intervalul [start, end].
"""


class DateRange(object):

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def get_days(self):
        return (self.end_date - self.start_date).days

    days = property(get_days)

    def contains(self, date):
        return self.start_date <= date <= self.end_date


"""
Ex. 2
Definiți clasa Car cu atributele: brand, model, daily_price. Adăugați metoda:
    - get_rental_price(period) - returnează prețul de închiriere pentru
    perioada respectivă.
Permiteți afișarea informațiilor despre mașină în formatul:
    "Acesta este un brand model și prețul la închiriere este daily_price"
"""


class Car(object):

    def __init__(self, brand, model, daily_price):
        self.brand = brand
        self.model = model
        self.daily_price = daily_price

    def get_rental_price(self, period):
        return self.daily_price * period.days

    def __str__(self):
        return ('Acesta este un ' + self.brand + ' ' + self.model + ' ' +
                'și prețul la închiriere este ' + str(self.daily_price))


"""
Ex. 3
Definiți clasa Limousine care extinde clasa Car, și are în plus următoarele
atribute: driver_salary. La prețul de închiriere va adăuga salariul șoferului.
"""


class Limousine(Car):
    """docstring for Limousine"""

    def __init__(self, brand, model, daily_price, driver_salary):
        super(Limousine, self).__init__(brand, model, daily_price)
        self.driver_salary = driver_salary

    def get_rental_price(self, period):
        return self.daily_price * period.days + self.driver_salary


"""
Ex. 4
Definiți clasa Person cu atributele: first_name, last_name și birthday.
"""


class Person(object):

    def __init__(self, first_name, last_name, birthday):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday


"""
Ex. 5
Definiți clasa CarRental cu atributele: cars. Scrieți metodele:
    - add_car(car) - adaugă o mașină în centrul de închirieri
    - get_cars - returnează o listă cu mașinile filtrate după brand și preț
    maxim.
    - get_price(customer, car, period) - returnează prețul final al tranzacției.
      Dacă ziua de naștere a clientului este în intervalul închirierii, se
      aplică o reducere de 10%.
"""


class CarRental(object):

    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def get_cars(self, brand=None, max_price=None):
        if brand is None and max_price is None:
            return self.cars
        elif brand is None:
            return filter(lambda x: x.daily_price <= max_price,
                          self.cars)
        elif max_price is None:
            return filter(lambda x: x.brand == brand, self.cars)
        else:
            return filter(lambda x: x.daily_price <=
                          max_price and x.brand == brand, self.cars)

    def get_price(self, customer, car, period):
        customer_birthday_day = customer.birthday.day
        customer_birthday_month = customer.birthday.month
        customer_birthday_year = customer.birthday.year
        day_cond = customer_birthday_day > period.start_date.day and \
            customer_birthday_day < period.end_date.day
        month_cond = customer_birthday_month >= period.start_date.month and \
            customer_birthday_month <= period.end_date.month
        year_cond = customer_birthday_year <= period.start_date.year
        if day_cond and month_cond and year_cond:
            return int((car.daily_price * period.days) * 0.9)
        else:
            return car.daily_price * period.days


"""
Ex. 6
Definiti clasa Point ce primeste doua coordonate (x, y) are metode interne
pentru operatii aritmetice, definiti aceste metode astfel incat sa putem
aduna/scadea doua puncte. Sugestie __add__, __sub__.
Exemplu:
    p1 = Point(1, 2)
    p2 = Point(2, 3)
    p3 = p1 + p2
    p4 = p1 - p2
"""


class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)


# Functia ajutatoare folosita la testare.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '{0} got: {1}, expected: {2}'.format(prefix, got, expected)


# Functia care testeaza rezultatele.
def main():
    from datetime import date, timedelta
    print "\nTeste pentru clasa DateRange"
    start = date(2012, 6, 24)
    end = date(2014, 1, 1)
    dr = DateRange(start, end)

    test(dr.contains(date(2012, 6, 24)), True)
    test(dr.contains(date(2014, 1, 1)), True)
    test(dr.contains(date(2013, 6, 24)), True)
    test(dr.contains(date(2014, 6, 24)), False)
    test(dr.days, 556)

    print "\nTeste pentru clasa Car"
    c = Car('Volvo', 'S60', 500)
    dr = DateRange(date.today(), date.today() + timedelta(days=7))
    test(c.get_rental_price(dr), 3500)
    test(str(c), "Acesta este un Volvo S60 și prețul la închiriere este 500")

    print "\nTeste pentru clasa Limousine"
    l = Limousine('Mercedes', 'Diplomat Edition', 1200, 800)
    dr = DateRange(date.today(), date.today() + timedelta(days=3))
    test(l.get_rental_price(dr), 4400)

    print "\nTeste pentru clasa CarRental"
    c2 = Car('Mercedes', 'C-Class', 700)
    cr = CarRental()
    cr.add_car(c)
    cr.add_car(l)
    cr.add_car(c2)

    test(cr.get_cars(), [c, l, c2])
    test(cr.get_cars('Mercedes'), [l, c2])
    test(cr.get_cars('Mercedes', 700), [c2])
    test(cr.get_cars(max_price=600), [c])
    test(cr.get_cars(max_price=400), [])

    p = Person('Jane', 'Geller', date(1992, 12, 5))
    p2 = Person('John', 'Stain', date(1990, 12, 15))
    dr = DateRange(date(2015, 12, 1), date(2015, 12, 10))
    test(cr.get_price(p, c, dr), 4050)
    test(cr.get_price(p2, c2, dr), 6300)

    print "\nTeste pentru clasa Point"
    p1 = Point(1, 2)
    p2 = Point(3, 3)

    p3 = p1 + p2
    test(p3.x, p1.x + p2.x)
    test(p3.y, p1.y + p2.y)

    p3 = p1 - p2
    test(p3.x, p1.x - p2.x)
    test(p3.y, p1.y - p2.y)

if __name__ == '__main__':
    main()
