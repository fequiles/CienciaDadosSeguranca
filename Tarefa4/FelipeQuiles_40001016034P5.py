'''
Author: Felipe Ribeiro Quiles    Mestrado: 40001016034P5 
'''
import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt
import csv

# Funcao que normatiza os dados do dataset
def normatizeMatrix(matrix):
        max_value = -1000
        min_value = 100000000
        for x in range (0,80):
                for y in range (1,2001):
                        if matrix[y][x] != '':
                                matrix[y][x] = float(matrix[y][x])
                        else:
                                matrix[y][x] = 0.0
                        if matrix[y][x] > max_value:
                                max_value = matrix[y][x]
                        if matrix[y][x] < min_value:
                                min_value = matrix[y][x]
                for y in range (1,2001):
                        if (min_value == max_value):
                                matrix[y][x] = 0.0
                        else:
                                matrix[y][x] = (float(matrix[y][x]) - min_value) / (max_value - min_value)
                max_value = -1000
                min_value = 100000000 

# Abre o dataset parcial ja filtrado
file = open ("final_dataset.csv")

csvreader = csv.reader(file)

matrix = []
count = 0 

# Retira os 50 mil primeiros dados de ddos
for row in range (0,1001):
        line = next(csvreader)

        for i in range(0,3):
                line.pop(0)
        line.pop(1)
        line.pop(3)
        if (row != 0):
                line[-1] = 1
                for x in range (0,80):
                        if line[x] != '':
                                line[x] = float(line[x])
                        else:
                                line[x] = 0.0
        matrix.append(line)

# Retira os 50 mil ultimos dados benignos 
for row in csvreader:
        if count < 12792627:
                count += 1
        else:
                for i in range(0,3):
                        row.pop(0)
                row.pop(1)
                row.pop(3)
                row[-1] = 0
                for x in range (0,80):
                        if row[x] != '':
                                row[x] = float(row[x])
                        else:
                                row[x] = 0.0
                matrix.append(row)


normatizeMatrix(matrix)

header = matrix.pop(0)
header[-1] = "Classe"

matriz_caracteristicas = pd.DataFrame(matrix, columns= header)


#Filtra DataFrame de acordo com o valor do rotulo
cond = (matriz_caracteristicas["Classe"] == 0)
benign = matriz_caracteristicas.loc[cond,:]
cond = (matriz_caracteristicas["Classe"] == 1)
ddos = matriz_caracteristicas.loc[cond,:]


#Seleciona aleatoriamente 500 amostras de cada classe
benign_frame = benign.sample(n=500)
ddos_frame = ddos.sample(n=500)

frames = [benign_frame, ddos_frame]

#Concatena os frames de benignos e ddos
amostragem = pd.concat(frames)

#Geracao do grafico de Benigno X DDoS
x=[1,2]
plt.title('Benigno x DDoS')
plt.bar(x,height=[len(benign_frame["Classe"]),len(ddos_frame["Classe"])] )
plt.xticks(x, ('Benigno','DDoS'))
plt.show()
