'''
Author: Felipe Ribeiro Quiles    Mestrado: 40001016034P5 
'''
from turtle import color
import pandas as pd
from pandas.plotting import scatter_matrix
import numpy  as np
import matplotlib.pyplot as plt
import csv

# Funcao que normatiza os dados do dataset
def normatizeMatrix(matrix):
        max_value = -1000
        min_value = 100000000
        for x in range (0,11):
                for y in range (1,100000):
                        if matrix[y][x] != '':
                                matrix[y][x] = float(matrix[y][x])
                        else:
                                matrix[y][x] = 0.0
                        if matrix[y][x] > max_value:
                                max_value = matrix[y][x]
                        if matrix[y][x] < min_value:
                                min_value = matrix[y][x]
                for y in range (1,100000):
                        if (min_value == max_value):
                                matrix[y][x] = 0.0
                        else:
                                matrix[y][x] = (float(matrix[y][x]) - min_value) / (max_value - min_value)
                max_value = -1000
                min_value = 100000000 

# Abre o dataset parcial ja filtrado
file = open ("parcial_dataset.csv")

#output = open('parcial_dataset.csv', 'w')

csvreader = csv.reader(file)
#writer = csv.writer(output)

matrix = []
count = 0 

# Retira os 50 mil primeiros dados de ddos
for row in range (0,50000):
        line = next(csvreader)
        ''' Filtra as caracteristicas
        for i in range(0,3):
                line.pop(0)
        line.pop(1)
        line.pop(2)
        line.pop(2)
        for i in range (0,10):
                line.pop(5)
        for i in range (0,20):
                line.pop(7)
        for i in range (0,14):
                line.pop(9)
        for i in range (0,24):
                line.pop(10)'''
        if (row != 0):
                line[-1] = 1
                for x in range (0,11):
                        if line[x] != '':
                                line[x] = float(line[x])
                        else:
                                line[x] = 0.0
        matrix.append(line)

# Retira os 50 mil ultimos dados benignos 
for row in csvreader:
        '''if count <= 12694627:
                count += 1
        else:
                 Filtra Caracteristicas
                for i in range(0, 3):
                        row.pop(0)
                row.pop(1)
                row.pop(2)
                row.pop(2)
                for i in range (0,10):
                        row.pop(5)
                for i in range (0,20):
                        row.pop(7)
                for i in range (0,14):
                        row.pop(9)
                for i in range (0,24):
                        row.pop(10)'''
        row[-1] = 0
        for x in range (0,11):
                if row[x] != '':
                        row[x] = float(row[x])
                else:
                        row[x] = 0.0
        matrix.append(row)

#writer.writerows(matrix)

normatizeMatrix(matrix)

header = matrix.pop(0)

teste = pd.DataFrame(matrix, columns= header)

# Geracao do scatterplot
scatter_matrix(teste, c="blue", alpha=0.2, figsize=(25,25))
plt.show()

