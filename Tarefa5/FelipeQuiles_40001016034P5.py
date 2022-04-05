'''
Author: Felipe Ribeiro Quiles    Mestrado: 40001016034P5 
'''
import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt
import csv
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import confusion_matrix

# Funcao que normatiza os dados do dataset
def normatizeMatrix(matrix):
        max_value = -1000
        min_value = 100000000
        for x in range (0,78):
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
file = open ("../final_dataset.csv")

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
        if count < 12792627:
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


normatizeMatrix(matrix)

header = matrix.pop(0)
header[-1] = "Classe"

matriz_caracteristicas = pd.DataFrame(matrix, columns= header)
matriz_caracteristicas = matriz_caracteristicas.dropna()

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

reduced_data = PCA(n_components=2).fit_transform(amostragem)
reduced_data_Df = pd.DataFrame(data = reduced_data, columns = ['principal component 1', 'principal component 2'])

kmeans = KMeans(n_clusters=2, init='k-means++', max_iter=300, n_init=10, random_state=0)
pred_y = kmeans.fit_predict(reduced_data)#[["Dst Port", "Pkt Size Avg"]])

h = 0.02  # point in the mesh [x_min, x_max]x[y_min, y_max].

# Plot the decision boundary. For that, we will assign a color to each
x_min, x_max = reduced_data[:, 0].min() - 1, reduced_data[:, 0].max() + 1
y_min, y_max = reduced_data[:, 1].min() - 1, reduced_data[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# Obtain labels for each point in mesh. Use last trained model.
Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
Z = Z.reshape(xx.shape)
plt.figure(1)
plt.clf()
plt.imshow(
    Z,
    interpolation="nearest",
    extent=(xx.min(), xx.max(), yy.min(), yy.max()),
    cmap=plt.cm.Paired,
    aspect="auto",
    origin="lower",
)

plt.scatter(reduced_data_Df['principal component 1'].head(500)
               , reduced_data_Df['principal component 2'].head(500), c = "blue", s = 100)
plt.scatter(reduced_data_Df['principal component 1'].tail(500)
               , reduced_data_Df['principal component 2'].tail(500), c = "red", s = 100)


# Plot the centroids as a white X
centroids = kmeans.cluster_centers_
plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    marker="x",
    s=169,
    linewidths=3,
    color="w",
    zorder=10,
)
plt.title(
    "K-means clustering"
)
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
plt.show()

df_confusion = pd.crosstab(amostragem["Classe"], pred_y)
print (df_confusion)
