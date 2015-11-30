import random


class BankAccount(object):
    """docstring for bank_account"""

    def __init__(self, bank_name, money_amount):
        self.bank_name = bank_name
        self.money_amount = money_amount

    def withdraw_money(self, withdrawn_amount):
        if self.money_amount - withdrawn_amount < 0:
            print 'Fonduri insuficiente'
        else:
            self.money_amount -= withdrawn_amount

    def deposit_money(self, deposit_amount):
        self.money_amount += deposit_amount


class Person(object):
    """docstring for ClassName"""

    def __init__(self, name, account, salary=0):
        self.name = name
        self.account = account
        self.__salary = salary

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        print 'Confidential'

    salary = property(get_salary, set_salary)

    def receive_salary(self):
        #self.account.money_amount += self.__salary
        self.account.deposit_money(self.__salary)

    def make_shopping(self, ammount):
        self.account.withdraw(ammount)


class SpecialBankAccount(BankAccount):
    """docstring for SpecialBankAccount"""

    def __init__(self, bank_name, money_amount, overdraft):
        super(SpecialBankAccount, self).__init__(bank_name, money_amount)
        self.overdraft = overdraft

    def withdraw_money(self, withdrawn_amount):
        if self.money_amount + self.overdraft < withdrawn_amount:
            print 'Creditul maxim a fost atins.'
        else:
            self.money_amount -= withdrawn_amount


class Zar(object):
    """docstring for Zar"""

    def roll(self):
        print 'zar cinstit'
        return random.randrange(1, 6)


class ZarNecinstit(Zar):
    """docstring for ZarNecinstit"""

    def roll(self):
        print 'zar necinstit'
        return 1


def main():

    # Tests for BankAccount
    # ba = BankAccount("RAlex",1000)
    # print ba.bank_name
    # print ba.money_amount
    # ba.withdraw_money(1000)
    # print ba.money_amount
    # ba.withdraw_money(10)

    # Tests for Person
    # p = Person("Gigel", BankAccount("Brd",1000),100)
    # print p.name
    # print p.account.bank_name
    # print p._Person__salary
    # print p.salary
    # p.salary = 200
    # p.receive_salary()
    # print p.account.money_amount

    # Tests for SpecialBankAccount
    # sba = SpecialBankAccount("Raif",500,500)
    # print sba.bank_name
    # print sba.money_amount, '\n'

    # p2 = Person("Eu",SpecialBankAccount("Raiffeisen",1000,500),500)
    # print p2.account.bank_name
    # print p2.account.money_amount
    # print p2.account.withdraw_money(1600)
    # print p2.account.money_amount

    # Tests for Zar
    #zar = Zar()
    # print zar.roll()

    # Tests for Zar/ZarNecinstit

    # zaruri = []
    # for i in range(3):
    #     zaruri.append(Zar())
    # for i in range(2):
    #     zaruri.append(ZarNecinstit())

    # for zar in zaruri:
    #     print zar.roll()


if __name__ == '__main__':
    main()
