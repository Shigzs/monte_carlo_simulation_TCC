import pandas as pd
import os

# Definindo o caminho do arquivo Excel
caminho_arquivo = os.path.join(os.path.dirname(
    __file__), '..', 'Historico_BBAS3.xlsx')

# Variáveis globais para armazenar as planilhas
planilha_2022_2023 = None

# Variável global para armazenar os dados de fechamento
fechado_planilha_2022_2023 = None


def ler_planilhas():
    global planilha_2022_2023

    # Lê a planilha específica do arquivo Excel
    planilha_2022_2023 = pd.read_excel(caminho_arquivo, sheet_name='2022_2023')


def separar_coluna_em_array():
    global fechado_planilha_2022_2023

    # Extrai a coluna 'Fechado' da planilha e armazena em um array
    fechado_planilha_2022_2023 = planilha_2022_2023['Fechado'].values


def initialize_data():
    ler_planilhas()
    separar_coluna_em_array()
