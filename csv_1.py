# Importar biblioteca pandas para trabalhar com arquivos CSV
import pandas as pd

arquivo_entrada = "votacao_secao_2012_SP.csv"
arquivo_saida = "itapevi_12.csv"

# Ler o arquivo CSV de entrada e armazenar em um DataFrame
dados = pd.read_csv(arquivo_entrada, encoding='cp1252', sep=';')
print(dados.columns)
print(dados)
# Filtrar apenas as linhas que possuem a coluna "nm_municipio" com o valor nome da cidade EM MAIUSUCULO e o cargo em DS_CARGO
dados_osasco = dados[(dados['NM_MUNICIPIO'] == 'ITAPEVI') & (dados['DS_CARGO'] == 'Prefeito')]
print(dados_osasco)
# Salvar as linhas filtradas em um novo arquivo CSV
dados_osasco.to_csv(arquivo_saida, encoding='utf-8', sep=';')
# Exibir mensagem de sucesso
print(f"O arquivo {arquivo_saida} foi criado com sucesso!")
