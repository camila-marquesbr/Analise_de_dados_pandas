import pandas as pd

df = pd.read_csv('base_de_dados_olimpiadas.csv')

#idade máxima
max_idade= df['idade'].max()

#idade mínima
df1 = df
df1.drop(df1.loc[df1['idade'] == 0].index, inplace=True)
min_idade = df1['idade'].min()

#média das idades
med_idade = df['idade'].mean()
med_idade1 = round(med_idade, 2)

#Liste todos os registros da atleta Serena Williams.
selecionar_serena = df.loc[df['atleta'] == 'Serena Williams']

#Liste o nome de todos os países distintos que participaram das olimpíadas.
data_columns = [col_name for col_name in df1.columns if col_name.startswith('pais')]
filtered_df = df.loc[:,data_columns]

#Liste os atletas que receberam mais de 3 medalhas de ouro.
atletas_ouro = df.query('ouro > 3').head()

#Liste todos os atletas do esporte natação e do país Brasil.
atletas_brasil = df.query('pais == "Brazil" & esporte == "Swimming"')



