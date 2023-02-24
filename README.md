# Integração Python com PowerBI

## Descrição

* Exercício desenvolvido na Academia Mulheres em Tech Data Engineer (Accenture e GamaAcademy) com a proposta de integrar python com PowerBI.
* Utilizar a biblioteca pandas em python para ler e transformar arquivo CSV e abrir o arquivo transformado diretamento no PowerBi Desktop através do *scripts python.*

## Exercício

### Arquivo CSV

Para realização do exercício, foi utilizado um arquivo do tipo csv chamado "stocks_prediction.csv" obtido no site [Brazilian stock exchange shares for forecast | Kaggle](https://www.kaggle.com/datasets/marcosgois07/brazilian-stock-exchange-shares-for-forecast).

Nesse arquivo, há dados históricos de 7 ações negociadas na bolsa de valores brasileira (PETR4.SA, MGLU3.SA, ABEV3.SA, BBDC4.SA, ITUB4.SA, RAIZ4.SA, VALE3.SA), que incluem: preços de abertura, variação máxima e mínima, preços de fechamento e volumes de negociação. Os dados foram coletados do Yahoo Finance e possui registros atualizados até 17/01/2023.

---

### Script Python

```
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
```

---

### Abrindo o CSV transformado no PowerBI pelo python script

! (https://github.com/alinetsbarreto/python-powerbi/blob/main/pythonscript.png) 

---

### Preview da tabela no PowerBI

![1677270761752](image/readme/1677270761752.png)

---

### Dashboard das Ações

Dashboard das ações, podendo filtrar os valores de cotação e volume de negociação pelo nome da empresa e periodo.

![1677272352852](image/readme/1677272352852.png)

![1677272365731](image/readme/1677272365731.png)

![1677272380214](image/readme/1677272380214.png)
