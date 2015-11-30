#!/usr/bin/env python
# -*- coding: utf-8 -*-
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


def citeste_achizitii_xls(xls):

    wb = xlrd.open_workbook(xls, formatting_info=True)
    sheet = wb.sheet_by_index(0)
    your_csv_file = open(
        '/Users/alexandrurustin/Desktop/Python.anunturibun.csv', 'w')
    wr = csv.writer(your_csv_file, delimiter=' ')

    cell = sheet.cell(6, 10)  # gets a Cell object
    cell.ctype = 1
    print cell.value

    for rownum in range(1, sheet.nrows):

        date = sheet.row_values(rownum)[2]
        row = map(lambda x: x.encode('utf8') if isinstance(
            x, basestring) else x, sheet.row_values(rownum))
        if isinstance(date, float) or isinstance(date, int):
            year, month, day, hour, minute, sec = xlrd.xldate_as_tuple(date, 0)
            py_date = "%02d/%02d/%04d" % (day, month, year)
            wr.writerow(row[0:2] +
                        [py_date] +
                        row[3:])
        else:
            wr.writerow(row)

    your_csv_file.close()


def citeste_achizitii_csv(csv_):
    with open(csv_, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        # row[5] = Judet
        # row[10] = valoare
        # row[11] = moneda
        dict = {}
        reader.next()

        for row in reader:
            judet = row[5]
            val = float(row[10].replace(',', ''))
            if judet in dict:
                dict[judet] += val
            else:
                dict[judet] = val
        return dict


def scrie_csv():
    with open('csvfile.csv', 'w') as writefile:
        dict = citeste_achizitii_csv(
            '/Users/alexandrurustin/Desktop/Python/anunturibun.csv')
        writer = csv.writer(writefile)
        writer.writerow(['Judet', 'Valorea estimata'])
        for key in dict:
            writer.writerow([key, str(dict[key])])


def scrie_json():
    with open('/Users/alexandrurustin/Desktop/Python/anunturibun.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        reader.next()
        dict = {}

        # row[2] = data publicare
        # row[10] = valoare
        # row[11] = moneda
        for row in reader:
            month = datetime.strptime(row[2], "%d.%m.%Y %M:%S").month
            val = float(row[10].replace(',', ''))
            if row[11] != 'RON':
                val_convertita = convertor_valutar(val, row[11])
            else:
                if month in dict:
                    dict[month] += val
                else:
                    dict[month] = val

    with open('anunturi.json', 'w') as writefile:
        json.dump(dict, writefile, indent=4)


def convertor_valutar(suma_convert, moneda):
    soup = BeautifulSoup(
        open('/Users/alexandrurustin/Desktop/Python/nbrfxrates.xml'),
        'xml')
    currency = soup.find('Rate', {'currency': moneda.upper()})
    currency_value = float(currency.string)
    return suma_convert / currency_value


def dictionar_populatie(url):
    r = requests.get(url)
    data = r.content
    soup = BeautifulSoup(data, 'html.parser')

    table = soup.find('table')
    rows = table.findAll('tr')
    dict = {}

    for row in rows[1:]:
        column = row.findAll('td')
        # cells[9] populatie pe ultimul an
        # cells[1] judetul
        populatie = str(column[9].find(text=True, recursive=False))
        judet = unidecode(column[1].text)
        if judet not in dict:
            if populatie:
                dict[judet] = populatie
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(dict)
    return dict

def valoare_contract_cap_locuitor():
    dictionar_populatie = dictionar_populatie()
    dictionar_valori_contracte = citeste_achizitii_csv('anunturibun.csv')
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint((dictionar_populatie))
    for judet in dictionar_populatie.keys()

def main():

    # citeste_achizitii_xls('Anunturi-participare-2015-S1.xls')
    # citeste_achizitii_csv('anunturibun.csv')
    # scrie_csv()
    scrie_json()
    convertor_valutar(1234, 'eur')
    dictionar_populatie(
        'https://ro.wikipedia.org/wiki/Lista_județelor_României_după_populație')
    valoare_contract_cap_locuitor()

if __name__ == '__main__':
    main()
