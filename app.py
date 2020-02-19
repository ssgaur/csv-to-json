from voluptuous import Schema
from datetime import datetime
from voluptuous import Url
import csv

def validate_email(email):
    if not "@" in email:
        raise Invalid("This email is invalid.")
    return email

def Date1(fmt='%d %B %Y'): #7 January 2020
    return lambda v: datetime.strptime(v, fmt)    

def Date2(fmt='%Y-%m-%d'): #1997-07-20
    return lambda v: datetime.strptime(v, fmt)      

def Date3(fmt='%d/%m/%Y'): #07/01/2020
    return lambda v: datetime.strptime(v, fmt)      

def Time1(fmt='%H:%M'): #23:59
    return lambda v: datetime.strptime(v, fmt)  

schemaObj =  {
    "provincie" : str,
    "candidatura" : str,
    "nome" : str,
    "cognome" : str,
    "email" : validate_email,
    "city" : str,
    "height" : int,
    "lead_score" : float,
    "applied_before" : bool,
    "genere" : str,
    "nascita" : Date2,
    "_time" : Time1,
    "_date" : Date1,
    "_url" : str,
    "last_applies" : Date3,
}

schemaCheck  = Schema(schemaObj)

with open('csv-icsv-importer-input.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            rowObj =  {
                "provincie" : row[0],
                "candidatura" : row[1],
                "nome" : row[2],
                "cognome" : row[3],
                "email" : row[4],
                "city" : row[5],
                "height" : row[6],
                "lead_score" : row[7],
                "applied_before" : row[8],
                "genere" : row[9],
                "nascita" : row[10],
                "_time" : row[11],
                "_date" : row[12],
                "_url" : row[13],
                "last_applies" : row[14],
            }
            #print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            schemaCheck(rowObj)
            line_count += 1
    print(f'Processed {line_count} lines.')
