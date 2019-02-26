# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from scipy import stats

satisfacao_vida = pd.read_csv("satisfacao.csv", thousands=',')
renda = pd.read_csv("renda.xls",thousands=',',delimiter='\t',encoding='latin1', na_values="n/a")
#pega os headers de cada tabela
#colunas_qualidade = list(qualidade.head(0))
#colunas_renda = list(renda.head(0))
satisfacao_vida = satisfacao_vida[satisfacao_vida["INEQUALITY"]=="TOT"]
satisfacao_vida = satisfacao_vida.pivot(index="Country", columns="Indicator", values="Value")
renda.rename(columns={"2015": "Renda per capita"}, inplace=True)
renda.set_index("Country", inplace=True)
tabela_renda_satisfacao = pd.merge(left=satisfacao_vida, right=renda, left_index=True, right_index=True)
tabela_renda_satisfacao.sort_values(by="Renda per capita", inplace=True)


remove_indices = [0, 1, 6] # removido para teste 
keep_indices = list(set(range(36)) - set(remove_indices))
tabelaFinal = tabela_renda_satisfacao[["Renda per capita", 'Life satisfaction']].iloc[keep_indices]
tabelaFinal.plot(kind="scatter", x="Renda per capita", y="Life satisfaction")


X = np.c_[tabelaFinal["Renda per capita"]]
Y = np.c_[tabelaFinal["Life satisfaction"]]

coefAng, coefLin, r, p, std_err = stats.linregress(X[:,0], Y[:,0])
r ** 2 
# Pelo valor de r² distante de 1, vemos que regressão linear não é um bom modelo 
# para o conjunto de dados
lin_reg_model = LinearRegression()
lin_reg_model.fit(X, Y)
# Teste
tabela_renda_satisfacao[["Renda per capita", 'Life satisfaction']].iloc[1]
print(lin_reg_model.predict(8669.998))
# Erro de 6.6 para 5.71

###########################################################################################
# testando regressão polinomial de grau 2

p = np.poly1d(np.polyfit(X[:,0], Y[:,0],2))
plt.scatter(X,Y)
plt.plot(X, p(X), c='r')
plt.show()
from sklearn.metrics import r2_score
r2 = r2_score(Y,p(X))
print(r2)












