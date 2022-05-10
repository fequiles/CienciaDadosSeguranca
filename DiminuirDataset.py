"""
Author: Felipe Ribeiro Quiles    Mestrado: 40001016034P5 
"""
from turtle import color
import pandas as pd
from pandas.plotting import scatter_matrix
import numpy  as np
import matplotlib.pyplot as plt
import csv

# Funcao que normatiza os dados do dataset
def normatizeMatrix(matrix):
        """Normatiza a Matriz de Caracteristicas"""
        max_value = -1000
        min_value = 100000000
        for x in range (0,78):
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
file = open ("final_dataset.csv")

output = open('parcial_dataset.csv', 'w')

csvreader = csv.reader(file)
writer = csv.writer(output)

matrix = []
count = 0 

# Retira os 50 mil primeiros dados de ddos
for row in range (0,250001):
        line = next(csvreader)

        for i in range(0,3):
                line.pop(0)
        line.pop(1)
        line.pop(3)
        for i in range(0,2):
                line.pop(0)
        if (row != 0):
                line[-1] = 1
                for x in range (0,78):
                        if line[x] != '':
                                line[x] = float(line[x])
                        else:
                                line[x] = 0.0
        matrix.append(line)

# Retira os 50 mil ultimos dados benignos 
for row in csvreader:
        if count < 12294627:
                count += 1
        else:
                for i in range(0,3):
                        row.pop(0)
                row.pop(1)
                row.pop(3)
                for i in range(0,2):
                        row.pop(0)
                row[-1] = 0
                for x in range (0,78):
                        if row[x] != '':
                                row[x] = float(row[x])
                        else:
                                row[x] = 0.0
                matrix.append(row)

writer.writerows(matrix)

header = matrix.pop(0)
header[-1] = "Classe"

matriz_caracteristicas = pd.DataFrame(matrix, columns= header)
matriz_caracteristicas.replace([np.inf, -np.inf], np.nan, inplace=True)
matriz_caracteristicas = matriz_caracteristicas.dropna()


#Filtra DataFrame de acordo com o valor do rotulo
cond = (matriz_caracteristicas["Classe"] == 0)
benign = matriz_caracteristicas.loc[cond,:]
print(len(benign))
cond = (matriz_caracteristicas["Classe"] == 1)
ddos = matriz_caracteristicas.loc[cond,:]
print(len(ddos))


