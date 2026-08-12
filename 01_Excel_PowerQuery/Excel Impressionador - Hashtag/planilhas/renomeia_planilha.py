import os
import unicodedata

# Pasta onde fica os arquivos a serem renomeados
pasta = 'C:/Users/Pichau/Documents/Ruan/data_analytics_foundation/01_Excel_PowerQuery/Excel Impressionador - Hashtag/planilhas'

# Looping para percorrer todos os arquivos da pasta
for nome_arq in os.listdir(pasta):

    # Separa o nome do arquivo da extensão (ex: planilha / .xlsx)
    nome_base, extensao = os.path.splitext(nome_arq)

    # Transforma o nome base e a extensão para minusculo
    novo_nome = nome_base.lower()
    extensao = extensao.lower()

    # Remove acentos
    novo_nome = unicodedata.normalize('NFKD', novo_nome).encode('ASCII', 'ignore').decode('utf-8')

    # Subistitui hífen e espaços por underline
    novo_nome = novo_nome.replace(' - ', '_')
    novo_nome = novo_nome.replace(' ', '_')
    novo_nome = novo_nome.replace('-', '_')

    # Junta o nome do arquivo limpo com a extensão formatada.
    arquivo_limpo = novo_nome + extensao

    # Lista o caminho do arquivo antes da padronização e após a padronização
    caminho_antigo = os.path.join(pasta, nome_arq)
    caminho_novo = os.path.join(pasta, arquivo_limpo)

    # Renoemeia de fato no compututador o nome do arquivo.
    os.rename(caminho_antigo, caminho_novo)