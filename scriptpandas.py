# Importar biblioteca Pandas
import pandas as pd 

# Ler o arquivo CSV
df = pd.read_csv(r"C:\Users\aline\OneDrive\Desktop\Azure\PowerBi\Desafio1\stocks_prediction.csv")

# Renomear colunas
df.rename(columns={'Date': 'Data'},inplace=True)
df.rename(columns={'Open': 'Abertura'},inplace=True)
df.rename(columns={'High': 'Máxima'},inplace=True)
df.rename(columns={'Low': 'Mínima'},inplace=True)
df.rename(columns={'Close': 'Fechamento'},inplace=True)
df.rename(columns={'Stock Name': 'Ação'},inplace=True)

# Transformar os valores da coluna data em tipo datetime
df['Data'] = pd.to_datetime(df['Data'])

# Adicionar uma nova coluna 'Empresa' com base na coluna de ação
df['Empresa'] = 'Empresa' 
df.loc[df['Ação'] == 'PETR4.SA' , 'Empresa'] = 'Petrobras'
df.loc[df['Ação'] == 'MGLU3.SA' , 'Empresa'] = 'Magazine Luiza'
df.loc[df['Ação'] == 'VALE3.SA' , 'Empresa'] = 'Vale'
df.loc[df['Ação'] == 'ABEV3.SA' , 'Empresa'] = 'Ambev'
df.loc[df['Ação'] == 'BBDC4.SA' , 'Empresa'] = 'Banco Bradesco'
df.loc[df['Ação'] == 'ITUB4.SA' , 'Empresa'] = 'Itaú Unibanco'
df.loc[df['Ação'] == 'RAIZ4.SA' , 'Empresa'] = 'Raizen'

# Imprimir dataframe
print(df)
