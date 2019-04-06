# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 10:03:20 2019

@author: Adenir
"""
def visualize_correlation_matrix(data, hurdle = 0.0):
    R = np.corrcoef(data, rowvar = 0)
    R[np.where(np.abs(R) < hurdle)] = 0.0
    heatmap = plt.pcolor(R, cmap = mpl.cm.coolwarm, alpha = 0.8)
    heatmap.axes.set_frame_on(False)
    heatmap.axes.set_yticks(np.arange(R.shape[0]) + 0.5, minor = False)
    heatmap.axes.set_xticks(np.arange(R.shape[1]) + 0.5, minor = False)
    heatmap.axes.set_xticklabels(variables, minor = False)
    plt.xticks(rotation=90)
    heatmap.axes.set_yticklabels(variables, minor = False)
    plt.tick_params(axis = 'both', which = 'both', bottom = 'off', top = 'off', left = 'off', right = 'off') 
    plt.colorbar()
    plt.show()
    
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.datasets import load_boston
from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
import statsmodels.api as sm
import statsmodels.formula.api as smf
import warnings
import seaborn as sns
warnings.filterwarnings("ignore")

# Gerando o dataset
boston = load_boston() 
descricao = boston.DESCR
dataset = pd.DataFrame(boston.data, columns = boston.feature_names)
dataset['target'] = boston.target
    
# Gerando número de observações e variáveis
observations = len(dataset)
variables = dataset.columns[:-1]

# Coletando x e y
X = dataset.iloc[:,:-1]
y = dataset['target'].values

# Usando Múltiplos Atributos com StatsModels
Xc = sm.add_constant(X) #no pacote statsmodel é necessario essa add de constante em X   
modelo_v1 = sm.OLS(y, Xc)
modelo_v2 = modelo_v1.fit()
modelo_v2.summary()
# R-squared -> quanto da variabilidade de y é explicada pelo menos por uma variavel preditora (0, 1)
# R-squared -> considera a complexidade do modelo ( melhor quando existem muitas variaveis para interpretar o modelo )
# P>|t\ -> Essa coluna representa o Valor-p, se o valor for > 0,05 a a variavel não tem significancia para ser usada

# matriz de correlação usando seaborn
correlation_matrix = dataset.corr().round(2)
matrix = sns.heatmap(data=correlation_matrix, annot=True)
#matriz de coreelação sem o target usando a funação criada
visualize_correlation_matrix(X, hurdle=0.5)

# Avaliando a Multicolinearidade
# Autovalores (Eigenvalues) e Autovetores (Eigenvectors)
# Gerando eigenvalues e eigenvectors
corr = np.corrcoef(X, rowvar = 0)
eigenvalues, eigenvectors = np.linalg.eig(corr)

# O menor valor está na posição 8. Valor buscar a posição 8 no autovetor.
print (eigenvalues)

# Os valores nas posições de índice 2, 8 e 9 estão em destaque 
print (eigenvectors[:,8])

# Imprimimos os nomes das variáveis para saber quais contribuem mais com a multicolinearidade
print (variables[2], variables[8], variables[9])
# Removemos as variáveis INDUS RAD e TAX de nossa análise


 













































