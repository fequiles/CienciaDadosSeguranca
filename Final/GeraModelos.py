'''
Author: Felipe Ribeiro Quiles    Mestrado: 40001016034P5 
'''
import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt
import csv
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error
from math import sqrt
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold, StratifiedShuffleSplit
from sklearn.metrics import roc_curve, precision_recall_curve, auc, make_scorer, recall_score, f1_score, accuracy_score, precision_score, confusion_matrix
import seaborn as sns
from sklearn.neural_network import MLPClassifier
import time
import joblib
import sys

def plot_confusionMatrix(df_confusion, clf_name):
        print ("Matriz Confusao - {}".format(clf_name))
        print (df_confusion)
        print ()
        '''ax = sns.heatmap(df_confusion, annot=True, fmt='g', cmap='Blues')

        ax.set_title('Matrix de Confusão do {}\n\n'.format(clf_name))
        ax.set_xlabel('\nPredicted Values')
        ax.set_ylabel('Actual Values ')

        ## Ticket labels - List must be in alphabetical order
        ax.xaxis.set_ticklabels(['False','True'])
        ax.yaxis.set_ticklabels(['False','True'])

        ## Display the visualization of the Confusion Matrix.
        plt.savefig("CF-{}-Complete".format(clf_name))
        plt.show()'''

def adjusted_classes(y_scores, t):
    return [1 if y >= t else 0 for y in y_scores]

def plot_ROC_Folding(skf, clf, clf_name, label):
        plt.figure(figsize=(10,10))
        plt.title('ROC Curve')
        print()
        fold = 0

        for train_index, test_index in skf.split(X, y):
                X_train_kfold, X_test_kfold = X.values[train_index], X.values[test_index]
                y_train_kfold, y_test_kfold = y.values[train_index], y.values[test_index]

                training_init = time.time()
                clf.fit(X_train_kfold, y_train_kfold)
                training_end = time.time()
                training_time = training_end - training_init
                print('Tempo de treinamento para o {}-Fold{}: {}'.format(clf_name, fold, training_time))

                y_scores = clf.predict_proba(X_test_kfold)[:,1]
                fpr, tpr, auc_thresholds = roc_curve(y_test_kfold, y_scores)
                print('Auc Fold {}: {}'.format(fold, auc(fpr, tpr)))
                plt.plot(fpr, tpr, linewidth=2, label='Fold {} - auc{}'.format(fold, auc(fpr, tpr)))

                plot_confusionMatrix(pd.DataFrame(confusion_matrix(y_test_kfold, adjusted_classes(y_scores, 0.5))), "{} - Fold {}".format(clf_name, fold))
                fold += 1 
        plt.axis([-0.005, 1, 0, 1.005])
        plt.xticks(np.arange(0,1, 0.2), rotation=90)
        plt.xlabel("False Positive Rate")
        plt.ylabel("True Positive Rate (Recall)")
        plt.legend(loc='best')
        plt.savefig("ROC-5Folds-{}".format(clf_name))
        plt.close()
        print()

def gridSearchBetter(clf_name, testSize, refit_score='precision_score'):
        skf = StratifiedShuffleSplit(n_splits=5, test_size=testSize, random_state=1)
        grid_search = GridSearchCV(clf, param_grid, scoring=scorers, refit=refit_score,
                               cv=skf, return_train_score=True, n_jobs=-1)

        plot_ROC_Folding(skf, grid_search, clf_name, "precision_optmized")

        # make the predictions
        grid_search.fit(X_train.values, y_train.values)
        y_pred = grid_search.predict(X_test.values)

        print()
        print('Melhores parametros do {} para o {}'.format(clf_name, refit_score))
        print(grid_search.best_params_)
        print('Melhor score do {} para o {}'.format(clf_name, refit_score))
        print(grid_search.best_score_)
        print()
        plot_confusionMatrix(pd.DataFrame(confusion_matrix(y_test.values, y_pred)), "MC{}".format(clf_name))

        print()
        return grid_search

file = open ("80_dataset.csv")
csvreader = csv.reader(file)
test_s = float(sys.argv[1])

matrix = []
count = 0 

for row in range (0,400001):
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

matriz_caracteristicas = pd.DataFrame(matrix, columns= header)
matriz_caracteristicas.replace([np.inf, -np.inf], np.nan, inplace=True)
matriz_caracteristicas = matriz_caracteristicas.dropna()

y = matriz_caracteristicas["Classe"]
X = matriz_caracteristicas.drop(columns=["Classe"])

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size= test_s, random_state= 1)#2564)

scorers = {
    'precision_score': make_scorer(precision_score),
    'recall_score': make_scorer(recall_score),
    'accuracy_score': make_scorer(accuracy_score), 
}

#KNeighbors
clf = KNeighborsClassifier(n_jobs=-1)

param_grid = {
    'n_neighbors': [1, 3, 5]
}

KN_gridSearch = gridSearchBetter("KNeighbors", test_s, refit_score='precision_score')
joblib.dump(KN_gridSearch, 'KNeighbors_{}.pkl'.format(test_s))

#RandomForest
clf = RandomForestClassifier(n_jobs=-1, random_state= 1)#23948)
param_grid = {
    'n_estimators' : [50, 100]
}

RF_gridSearch = gridSearchBetter("RandomForest", test_s, refit_score='precision_score')
joblib.dump(RF_gridSearch, 'RandomForest_{}.pkl'.format(test_s))

#MLPClassifier
clf = MLPClassifier(random_state=5468)
param_grid = {
    'max_iter' : [1000, 5000],
    'tol': [0.01], 
    'hidden_layer_sizes':[7]
}

MLP_gridSearch = gridSearchBetter("MLP", test_s, refit_score='precision_score')
joblib.dump(MLP_gridSearch, 'MLP_{}.pkl'.format(test_s))