
import pandas as pd 
import random 
from datetime import datetime, timedelta
# Função para gerar dados de vendas ficticios

def gerar_dados(num_linhas, in_min, in_max):
    produtos = ['Tupperware', 'Bombril', 'Xerox', 'Kodac']
    cidades = ['Orlando', 'Anahein', 'Franco da Rocha', 'Poá']
    dados = []
    #in_min = 0
    #in_max = 365
    for _ in range(num_linhas):
        produto = random.choice(produtos)
        cidade = random.choice(cidades)
        valor = round(random.uniform(50,500),2)
        data = datetime.today() - timedelta(days=random.randint(in_min,in_max)) #para dar datas aleatorias (hoje-365 dias)
        dados.append([produto, cidade, valor, data])
    return dados 
#gerar 100 linhas de dados com intervalos de dats de 1 a 365 dias
dados_prontos = gerar_dados(100, 1, 365)

#criar dataframe (efetivamente a tabela)
df_vendas = pd.DataFrame(dados_prontos,columns=['Produto','Cidade', 'Valor', 'Data'])

#salvando em csv
df_vendas.to_excel('vendas.xlsx',index=False,engine='openpyxl')

print("Deu tudo certo! arquivo foi salvo!")
