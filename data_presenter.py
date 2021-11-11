import csv

open_file = open("CupcakeInvoices.csv")
for row in open_file:
    print(row)
open_file.close() 

open_file = open("CupcakeInvoices.csv")
reader = csv.DictReader(open_file)
data = [row for row in reader]
for row in data:
    print(row["Chocolate"])

open_file.close()

open_file = open("CupcakeInvoices.csv")
total_each_order=""
for line in open_file:
        line = line.rstrip('/n').split(',')

        









