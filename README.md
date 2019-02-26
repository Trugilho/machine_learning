# Machine Learning

  Neste exemplo, queremos saber se dinheiro faz as pessoas felizes. Para isso fizemos o download dos dados de índices de satisfação de vida em diversos países no site https://stats.oecd.org/index.aspx?DataSetCode=BLI e fizemos o download dos dados de renda per capta em outros países em http://goo.gl/j1MSKe. Após tratarmos os dados, fizemos o merge nas duas tabelas, onde é possível ver num determinado país os índices de "Renda per Capta" e "Life Satisfaction". Ao plotarmos o gráfico dessas duas variáveis encontramos o seguinte: 
  
  ![plot1](https://user-images.githubusercontent.com/12522815/53444287-80f33b80-39ec-11e9-906c-be3af502b371.png)

  Vemos que não parece haver nenhuma relação de linearidade entre os dois parâmetros, então vamos investigar mais a fundo.
  Utilizamos primeiramente o pacote stats para encontrar o Coeficiente de Determinação (R²), esse coeficiente varia entre 0 e 1, e quanto mais próximo de 1, melhor as previsões do modelo. Encontramos R² = 0.594, o que confirma a suspeita de que a regressão linear não é um bom modelo para nosso conjunto de dados. 
  
  
  
