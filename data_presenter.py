import csv
# import matplotlib.pyplot as plt
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

total_each_order = ""

for line in open_file:

    line = line.rstrip().split(',')

    # print(line)

    for value in line:

        total_each_order = float(line[3]) * float(line[4])

    print(total_each_order)








