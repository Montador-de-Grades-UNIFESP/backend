import json

# Função que lê um arquivo JSON e retorna um dicionário
def ler_arquivo_json(endereco_arquivo):
    with open(endereco_arquivo, 'r', encoding='utf-8') as arquivo:
        return json.load(arquivo)

# Função que recebe um dicionário e o escreve em um arquivo JSON
def dicionario_para_json(dicionario, endereco_arquivo):
    with open(endereco_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(dicionario, arquivo, ensure_ascii=False, indent=4)
    