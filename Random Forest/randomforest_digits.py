#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 12:25:07 2019

@author: trugilho
"""

import numpy as np
from sklearn.ensemble import RandomForestClassifier
import sklearn.datasets
import sklearn.decomposition
from sklearn.preprocessing import scale
from sklearn.metrics import accuracy_score


digitos = sklearn.datasets.load_digits()
X = digitos.data
Y = digitos.target

#redução de dimensionalidade
svd = sklearn.decomposition.TruncatedSVD(n_components = 25)
X_fit = svd.fit_transform(X)
#notmalização
X_norm = scale(X_fit)

#criar conjunto de treino e de teste aleatoriamente
idx = list(range(len(digitos.target)))
np.random.shuffle(idx)

# Cria o classificador com 2/3 do dataset para treinamento
rf = RandomForestClassifier(criterion='entropy', max_depth = 8)
rf.fit(X_norm[idx][:1198], Y[idx][:1198])

#analise da acurácia do modelo 
previsoes = rf.predict(X_norm[idx][1198:])
print(accuracy_score(Y[idx][1198:],previsoes))