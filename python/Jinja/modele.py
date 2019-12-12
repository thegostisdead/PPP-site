# modele_Index.py

import csv 


with open('output.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["name"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')










# traitement 


def readCollum(collum_name):
    pass


def get_name_jobs(csv_file):
    pass
    