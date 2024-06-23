from processed_data import Data


path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

# Extract 

data_companyA = Data.read_data(path_json, 'json')
print(160*'=')
print(f'|  Reading Company A data: {data_companyA.name_columns}{28*" "}{"|"}') 
print(160*'=')
print(F'|  Number of rows in Company A data: {data_companyA.qtd_lines}{117*" "}{"|"}')
print(160*'=')

data_companyB = Data.read_data(path_csv, 'csv')
print(f'|  Reading Company B data:{data_companyB.name_columns}{7*" "}{"|"}')
print(160*'=')
print(F'|  Number of rows in Company B data: {data_companyB.qtd_lines}{117*" "}{"|"}')
print(160*'=')

# Transform 

key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

data_companyB.rename_columns(key_mapping)
print(f'| Standardizing column names B: {data_companyB.name_columns}{6*" "}{"|"}')
print(160*'=')

data_fusion = Data.join_datas(data_companyA,data_companyB)
print(f'| reading data after data fusion: {data_fusion.name_columns}{4*" "}{"|"}')
print(160*'=')
print(F'| Number of lines in the data after fusion: {data_fusion.qtd_lines}{110*" "}{"|"}')
print(160*'=')

#Load
path_data_combined = 'data_processed/dados_combinados.csv'

data_fusion.saving_datas(path_data_combined)
print(f'| New data saved in the path: {path_data_combined}{93*" "}{"|"}')
print(160*'=')