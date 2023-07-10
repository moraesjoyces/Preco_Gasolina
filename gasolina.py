
import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#transforma o arquivo .csv em dataframe
gasolina_df = pd.read_csv('gasolina.csv', sep=',')

#cria o grafico com base no dataframe e salva no formato .png
sns.set_style('whitegrid')
grafico = sns.lineplot(x='dia',y='venda', data=gasolina_df)
plt.title('Preço Médio Gasolina em São Paulo', fontsize =12, fontweight ="bold")
plt.xlabel('Dia de Junho/2021')
plt.ylabel('Preço Médio')
plt.savefig(fname='gasolina.png', bbox_inches ="tight")
