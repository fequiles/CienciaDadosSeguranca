'''
Author: Felipe Ribeiro Quiles    Mestrado: 40001016034P5 
'''
import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt
import csv
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import sklearn.metrics as skm
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error
from math import sqrt
import seaborn as sns

# Funcao que normatiza os dados do dataset
def normatizeMatrix(matrix):
        max_value = -1000
        min_value = 100000000
        for x in range (0,78):
                for y in range (1,len(matrix)):
                        if matrix[y][x] != '':
                                matrix[y][x] = float(matrix[y][x])
                        else:
                                matrix[y][x] = 0.0
                        if matrix[y][x] > max_value:
                                max_value = matrix[y][x]
                        if matrix[y][x] < min_value:
                                min_value = matrix[y][x]
                for y in range (1,len(matrix)):
                        if (min_value == max_value):
                                matrix[y][x] = 0.0
                        else:
                                matrix[y][x] = (float(matrix[y][x]) - min_value) / (max_value - min_value)
                max_value = -1000
                min_value = 100000000 

# Abre o dataset parcial ja filtrado
file = open ("../parcial_dataset.csv")

csvreader = csv.reader(file)

matrix = []
count = 0 

# Retira os 50 mil primeiros dados de ddos
for row in range (0,50001):
        line = next(csvreader)

        if (row != 0):
                for x in range (0,78):
                        if line[x] != '':
                                line[x] = float(line[x])
                        else:
                                line[x] = 0.0
        matrix.append(line)


header = matrix.pop(0)
header[-1] = "Classe"
normatizeMatrix(matrix)

matriz_caracteristicas = pd.DataFrame(matrix, columns= header)
matriz_caracteristicas.replace([np.inf, -np.inf], np.nan, inplace=True)
matriz_caracteristicas = matriz_caracteristicas.dropna()


#Filtra DataFrame de acordo com o valor do rotulo
cond = (matriz_caracteristicas["Classe"] == 0)
benign = matriz_caracteristicas.loc[cond,:]
cond = (matriz_caracteristicas["Classe"] == 1)
ddos = matriz_caracteristicas.loc[cond,:]


#Seleciona aleatoriamente 500 amostras de cada classe
benign_frame = benign.sample(n=5000)
ddos_frame = ddos.sample(n=5000)

frames = [benign_frame, ddos_frame]

#Concatena os frames de benignos e ddos
amostragem = pd.concat(frames)

train_y = amostragem["Classe"]
#train_x = PCA(n_components=2).fit_transform(amostragem.drop(columns=["Classe"]))
train_x = amostragem.drop(columns=["Classe"])
#trainX_Df = pd.DataFrame(data = train_x, columns = ['Component_1', 'Component_2'])

indexNames = amostragem.index
matriz_caracteristicas.drop(indexNames, inplace=True)
dataTest = matriz_caracteristicas

tests_y = dataTest["Classe"]
#tests_x = PCA(n_components=2).fit_transform(dataTests.drop(columns=["Classe"]))
tests_x = dataTest.drop(columns=["Classe"])
#testX_Df = pd.DataFrame(data = tests_x, columns = ['Component_1', 'Component_2'])


clf = KNeighborsRegressor(n_neighbors=1)
clf.fit(train_x, train_y)

#clf=RandomForestClassifier(n_estimators=100)
#clf.fit(trainX_Df, train_y)

print ("Tamanho dos testes: "+str(len(tests_x)))

test_preds = clf.predict(tests_x)
mse = mean_squared_error(tests_y, test_preds)
rmse = sqrt(mse)
print("Erro teste: " + str(rmse))

df_confusion = pd.crosstab(tests_y, test_preds)

print ("Accuracy: " + str(skm.accuracy_score(tests_y, test_preds)))
print ("Recall: " + str(skm.recall_score(tests_y, test_preds)))
print ("Precision: " + str(skm.precision_score(tests_y, test_preds)))
print ("F1: " + str(skm.f1_score(tests_y, test_preds)))

ax = sns.heatmap(df_confusion, annot=True, fmt='g', cmap='Blues')

ax.set_title('Seaborn Confusion Matrix with labels\n\n')
ax.set_xlabel('\nPredicted Values')
ax.set_ylabel('Actual Values ')

## Ticket labels - List must be in alphabetical order
ax.xaxis.set_ticklabels(['False','True'])
ax.yaxis.set_ticklabels(['False','True'])

## Display the visualization of the Confusion Matrix.
plt.show()
