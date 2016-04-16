__author__ = 'Jan'
import csv
import re
import datetime

filename = 'com_direckt_giro.txt'
filenameoutput= filename + '.output'
now = datetime.datetime.now()
jahr = now.year
print(jahr)
# "Buchungstag";"Verwendungszweck";"Begünstigter/Zahlungspflichtiger";"Kontonummer";"BLZ";"Betrag";"Währung";"Info"
# Date: DD/MM/YYYY
# Date,Payee,Category,Memo,Outflow,Inflow

with open(filename, newline='') as csvfilein:
    # reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    # csv.reader()
    fieldnames_com = ['Buchungsdatum', 'Valutadatum', 'Vorgang', 'Buchungstext', 'Umsatz']
    reader = csv.DictReader(csvfilein, fieldnames_com, None, None, delimiter=';', quotechar='"')
    with open(filenameoutput, 'w', newline='') as csvfileout:
        fieldnames = ['Date', 'Payee', 'Category', 'Memo', 'Outflow', 'Inflow']
        writer = csv.DictWriter(csvfileout, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            tag = str(row['Buchungstag'])[0:0 + 2]
            monat = str(row['Buchungstag'])[3:3 + 2]
            jahr2 = str(row['Buchungstag'])[6:6 + 2]
            date = tag + '/' + monat + '/' + '20' + str(jahr2)
s= "Name1=Value1;Name2=Value2;Name3=Value3"
dict(item.split("=") for item in s.split(";"))
            #payee = row['Begünstigter/Zahlungspflichtiger']
            payee = row['Zahlungspflichtiger']
            # print(tag)
            verwendungszweck = re.sub(r'(?<=[a-z])\r?\n|\u000A', ' ', row['Verwendungszweck'])
            print(monat, ',', tag, ',', verwendungszweck)
            # print(row['Begünstigter/Zahlungspflichtiger'])
            print(payee)

            # betrag
            betrag = row['Betrag']
            betrag = re.sub(r',', '.', betrag)
            print(betrag)
            betrag = float(betrag)
            inflow = 0
            outflow = 0
            if betrag > 0:
                inflow = betrag
            else:
                outflow = (betrag * -1)

            writer.writerow({'Date': date, 'Payee': payee, 'Category': '', 'Memo': verwendungszweck, 'Outflow': outflow,
                             'Inflow': inflow})




            # writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
            # writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
            # writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
