# Author: Felipe Ribeiro Quiles
# Curso: Mestrado em Cienia da Computacao

import joblib
import csv
import numpy  as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

def plot_confusionMatrix(df_confusion, clf_name):
    ax = sns.heatmap(df_confusion, annot=True, fmt='g', cmap='Blues')
    ax.set_title('Matrix de Confusão do {}\n\n'.format(clf_name))
    ax.set_xlabel('\nPredicted Values')
    ax.set_ylabel('Actual Values ')
    ## Ticket labels - List must be in alphabetical order
    ax.xaxis.set_ticklabels(['False','True'])
    ax.yaxis.set_ticklabels(['False','True'])
    ## Display the visualization of the Confusion Matrix.
    plt.savefig("CF-{}-Complete".format(clf_name))
    plt.show()

def KN_predict(vectors, classes):
    loaded_model = joblib.load("Modelos/KNeighbors_0.5.pkl")
    y_pred = loaded_model.predict(vectors)

    plot_confusionMatrix(pd.DataFrame(confusion_matrix(classes, y_pred)), "KN_50")

    loaded_model = joblib.load("Modelos/KNeighbors_80-20.pkl")
    y_pred = loaded_model.predict(vectors)

    plot_confusionMatrix(pd.DataFrame(confusion_matrix(classes, y_pred)), "KN_20")

def RF_predict(vectors, classes):
    loaded_model = joblib.load("Modelos/RandomForest_0.5.pkl")
    y_pred = loaded_model.predict(vectors)

    plot_confusionMatrix(pd.DataFrame(confusion_matrix(classes, y_pred)), "RF_50")

    loaded_model = joblib.load("Modelos/RandomForest_80-20.pkl")
    y_pred = loaded_model.predict(vectors)

    plot_confusionMatrix(pd.DataFrame(confusion_matrix(classes, y_pred)), "RF_20")

def MLP_predict(vectors, classes):
    loaded_model = joblib.load("Modelos/MLP_0.5.pkl")
    y_pred = loaded_model.predict(vectors)

    plot_confusionMatrix(pd.DataFrame(confusion_matrix(classes, y_pred)), "MLP_50")

    loaded_model = joblib.load("Modelos/MLP_80-20.pkl")
    y_pred = loaded_model.predict(vectors)

    plot_confusionMatrix(pd.DataFrame(confusion_matrix(classes, y_pred)), "MLP_20")


dataset_20 = open ("20_dataset.csv")

csvreader = csv.reader(dataset_20)

train = []
count = 0 

for row in range (0,100001):
    line = next(csvreader)

    if (row != 0):
        count += 1
        for x in range (0,78):
                if line[x] != '':
                        line[x] = float(line[x])
                else:
                        line[x] = 0.0
    train.append(line)

header = train.pop(0)
header[-1] = "Classe"

matriz_caracteristicas = pd.DataFrame(train, columns= header)
matriz_caracteristicas.replace([np.inf, -np.inf], np.nan, inplace=True)
matriz_caracteristicas = matriz_caracteristicas.dropna()

classes = matriz_caracteristicas["Classe"]
vectors = matriz_caracteristicas.drop(columns=["Classe"])

KN_predict(vectors, classes)
RF_predict(vectors,classes)
MLP_predict(vectors, classes)
