#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys
import csv
import sys
import xlrd
import xlwt
import sys
import json
from bs4 import BeautifulSoup
from datetime import *
import inspect
import pprint
from unidecode import unidecode
import requests

# ex1
# does not parse everything correctly (valoarea de tipul 'zzzz.zzzz.zzz')


def convert_from_xls_to_csv(xls_, csv_):

    workbook = xlrd.open_workbook(xls_, formatting_info=True)
    sheet = workbook.sheet_by_index(0)
    your_csv_file = open(csv_, 'w')
    writer = csv.writer(your_csv_file, delimiter=' ')

    for rownum in range(1, sheet.nrows):

        date = sheet.row_values(rownum)[2]
        row = map(lambda x: x.encode('utf8') if isinstance(
            x, basestring) else x, sheet.row_values(rownum))
        if isinstance(date, float) or isinstance(date, int):
            year, month, day, hour, minute, sec = xlrd.xldate_as_tuple(date, 0)
            py_date = "%02d/%02d/%04d" % (day, month, year)
            writer.writerow(row[0:2] +
                            [py_date] +
                            row[3:])
        else:
            writer.writerow(row)

    your_csv_file.close()


def read_csv_file(csv_):
    with open(csv_, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        # row[5] = Judet
        # row[10] = valoare
        # row[11] = moneda
        dict_ = {}
        reader.next()

        for row in reader:
            judet = row[5]
            val = float(row[10].replace(',', ''))
            if judet in dict_:
                dict_[judet] += val
            else:
                dict_[judet] = val
        return dict_


def write_to_csv_file(csv_):
    with open(csv_, 'w') as writefile:
        dict_ = read_csv_file(
            '/Users/alexandrurustin/Desktop/Python/python-homework/anunturibun.csv')
        writer = csv.writer(writefile)
        writer.writerow(['Judet', 'Valorea estimata'])
        for key in dict_:
            writer.writerow([key, str(dict[key])])


def write_to_json_file(csv_, json_):
    with open(csv_, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        reader.next()
        dict_ = {}

        # row[2] = data publicare
        # row[10] = valoare
        # row[11] = moneda
        for row in reader:
            month = datetime.strptime(row[2], "%d.%m.%Y %M:%S").month
            value = float(row[10].replace(',', ''))
            if row[11] != 'RON':
                converted_value = currency_convertor(value, row[11], 'http://www.bnr.ro/nbrfxrates.xml')
            else:
                if month in dict:
                    dict_[month] += value
                else:
                    dict_[month] = value

    with open(json_, 'w') as writefile:
        json.dump(dict_, writefile, indent=4)


def currency_convertor(sum_to_convert, currency_, url):
    request = requests.get(url)
    data = request.content
    soup = BeautifulSoup(data, 'xml')

    currency = soup.find('Rate', {'currency': currency_.upper()})
    currency_value = float(currency.string)
    return sum_to_convert / currency_value

# printing doesn't work, problems with unicode/encoding
def population_dictionary(url):
    r = requests.get(url)
    data = r.content
    soup = BeautifulSoup(data, 'html.parser')

    table = soup.find('table')
    rows = table.findAll('tr')
    dict_ = {}

    for row in rows[1:]:
        column = row.findAll('td')
        # column[9] populatie pe ultimul an
        # column[1] judetul / <a> judet
        population = str(column[9].find(text=True, recursive=False)).replace('.','')
        if population != 'None':
            population = float(population)
        if row.a != None:
            county = row.a.string
            if county == 'Municipiul București':
                county = county.split('')[1]
        if county not in dict_:
                dict_[county] = population
    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(dict)
    # print str(dict)
    return dict_

# doesn't work, problems with unicode/encoding
def contract_value_per_head_of_population():
    dictionary_population = population_dictionary('https://ro.wikipedia.org/wiki/Lista_județelor_României_după_populație')
    dictionary_contracts_value = read_csv_file('/Users/alexandrurustin/Desktop/Python/python-homework/anunturibun.csv')
    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(dictionary_contracts_value)
    # pp.pprint(dictionary_population)
    # dict_ = {}
    # for county in dictionary_population.keys():
    #     dict_[county] = dictionary_population[county] / dictionary_contracts_value[county]
    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(dict_)



def main():
    # convert_from_xls_to_csv(
    # '/Users/alexandrurustin/Desktop/Python/python-homework/Anunturi-participare-2015-S1.xls', '/Users/alexandrurustin/Desktop/Python/python-homework/MyAnunturi.csv')
    # read_csv_file('/Users/alexandrurustin/Desktop/Python/python-homework/anunturibun.csv')
    # write_to_csv_file('/Users/alexandrurustin/Desktop/Python/python-homework/csvfile.csv')
    # write_to_json_file('/Users/alexandrurustin/Desktop/Python/python-homework/anunturibun.csv', '/Users/alexandrurustin/Desktop/Python/python-homework/anunturi.json')
    # print currency_convertor(1234, 'eur', 'http://www.bnr.ro/nbrfxrates.xml')
    # population_dictionary(
    #      'https://ro.wikipedia.org/wiki/Lista_județelor_României_după_populație')
    # contract_value_per_head_of_population()

if __name__ == '__main__':
    main()
