__author__ = 'Jan'
import csv
import re
import datetime


filename = '20160410-2007227-umsatz.CSV'
filenameoutput = 'output_' + filename
now = datetime.datetime.now()
jahr = now.year
print(jahr)
# "Buchungstag";"Verwendungszweck";"Begünstigter/Zahlungspflichtiger";"Kontonummer";"BLZ";"Betrag";"Währung";"Info"
# Date: DD/MM/YYYY
# Date,Payee,Category,Memo,Outflow,Inflow

with open(filename, newline='') as csvfilein:
    # reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    # csv.reader()
    reader = csv.DictReader(csvfilein, None, None, None, delimiter=';', quotechar='"')
    with open(filenameoutput, 'w', newline='') as csvfileout:
        fieldnames = ['Date', 'Payee', 'Category', 'Memo', 'Outflow', 'Inflow']
        writer = csv.DictWriter(csvfileout, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            tag = str(row['Valutadatum'])[0:0 + 2]
            monat = str(row['Valutadatum'])[3:3 + 2]
            jahr2 = str(row['Valutadatum'])[6:6 + 2]
            date = tag + '/' + monat + '/' + '20' + str(jahr2)

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
