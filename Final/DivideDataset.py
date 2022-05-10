"""
Author: Felipe Ribeiro Quiles    Mestrado: 40001016034P5 
"""
from turtle import color
import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt
import csv

# Abre o dataset parcial ja filtrado
file = open ("../parcial_dataset.csv")

output_80 = open('80_dataset.csv', 'w')
output_20 = open('20_dataset.csv', 'w')

csvreader = csv.reader(file)
writer_80 = csv.writer(output_80)
writer_20 = csv.writer(output_20)

train = []
tests = []
count = 0 

for row in range (0,250001):
    line = next(csvreader)

    if (row != 0):
        count += 1
        for x in range (0,78):
                if line[x] != '':
                        line[x] = float(line[x])
                else:
                        line[x] = 0.0
        if count <= 200000:
            train.append(line)
        else:
            tests.append(line)
    else:
        train.append(line)
        tests.append(line)

count = 0
for row in csvreader:
    count += 1
    for x in range (0,78):
            if row[x] != '':
                    row[x] = float(row[x])
            else:
                    row[x] = 0.0
    if count <= 50000:
        tests.append(row)
    else:
        train.append(row)

header = train[0]

writer_80.writerows(train)
writer_20.writerows(tests)

print(len(train))
print(len(tests))

