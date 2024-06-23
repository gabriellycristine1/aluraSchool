from processed_data import Data


path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

# Extract 

data_companyA = Data.read_data(path_json, 'json')
print(f'lendo dados empresa A: {data_companyA.name_columns}')
print(F'Quantidade de linhas nos dados Empresa A: {data_companyA.qtd_lines}')

data_companyB = Data.read_data(path_csv, 'csv')
print(f'lendo dados empresa B:{data_companyB.name_columns}')
print(F'Quantidade de linhas nos dados Empresa B: {data_companyB.qtd_lines}')

# Transform 

key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

data_companyB.rename_columns(key_mapping)
print(f'padronizando nome das colunas: {data_companyB.name_columns}')

data_fusion = Data.join_datas(data_companyA,data_companyB)
print(f'lendo dados pós fusão: {data_fusion.name_columns}')
print(F'Quantidade de linhas nos dados pós fusão: {data_fusion.qtd_lines}')

#Load
path_data_combined = 'data_processed/dados_combinados.csv'

data_fusion.saving_datas(path_data_combined)
print(f'novos dados salvos no caminho: {path_data_combined}')