import time
from processamento_dados import Dados

path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

print("Iniciando processo de ETL...")
time.sleep(1)

# Extract
print("\n[EXTRACT] Extraindo dados da Empresa A (JSON)")
dados_empresaA = Dados('data_raw/dados_empresaA.json', 'json')
print(f"Colunas encontradas: {dados_empresaA.nome_colunas}")
print(f"Total de registros: {dados_empresaA.qtd_linhas}")
time.sleep(1)

print("\n[EXTRACT] Extraindo dados da Empresa B (CSV)")
dados_empresaB = Dados('data_raw/dados_empresaB.csv', 'csv')
print(f"Colunas encontradas: {dados_empresaB.nome_colunas}")
print(f"Total de registros: {dados_empresaB.qtd_linhas}")
time.sleep(1)

# Transform
print("\n[TRANSFORM] Renomeando colunas da Empresa B para padronizar")
key_mapping = {
    'Nome do Item': 'Nome do Produto',
    'Classificação do Produto': 'Categoria do Produto',
    'Valor em Reais (R$)': 'Preço do Produto (R$)',
    'Quantidade em Estoque': 'Quantidade em Estoque',
    'Nome da Loja': 'Filial',
    'Data da Venda': 'Data da Venda'
}

dados_empresaB.rename_columns(key_mapping)
print(f"Colunas após padronização: {dados_empresaB.nome_colunas}")
time.sleep(1)

print("\n[TRANSFORM] Realizando fusão dos dados")
dados_fusao = Dados.join(dados_empresaA, dados_empresaB)
print(f"Total de registros após fusão: {dados_fusao.qtd_linhas}")
print(f"Colunas finais: {dados_fusao.nome_colunas}")
time.sleep(1)

# Load
path_dados_combinados = 'data_processed/dados_combinados.csv'
print("\n[LOAD] Salvando dados combinados em CSV...")
dados_fusao.salvando_dados(path_dados_combinados)
print(f"Arquivo salvo em: {path_dados_combinados}")
time.sleep(1)

print("\nProcesso de ETL finalizado com sucesso.\nBy: Duffes")
