import pandas as pd
import os

# Definindo o caminho do arquivo Excel
caminho_arquivo = os.path.join(os.path.dirname(
    __file__), '..', 'Historico_BBAS3.xlsx')

# Variáveis globais para armazenar as planilhas
planilha_2004_2024 = None
planilha_2004_2005 = None
planilha_2022_2023 = None

# Variáveis globais para armazenar os dados de fechamento
fechado_planilha_2004_2024 = None
fechado_planilha_2004_2005 = None
fechado_planilha_2022_2023 = None


def ler_planilhas():
    global planilha_2004_2024, planilha_2004_2005, planilha_2022_2023

    # Lê as planilhas específicas do arquivo Excel
    planilha_2004_2024 = pd.read_excel(caminho_arquivo, sheet_name='2004_2024')
    planilha_2004_2005 = pd.read_excel(caminho_arquivo, sheet_name='2004_2005')
    planilha_2022_2023 = pd.read_excel(caminho_arquivo, sheet_name='2022_2023')


def separar_coluna_em_array():
    global fechado_planilha_2004_2024, fechado_planilha_2004_2005, fechado_planilha_2022_2023

    # Extrai a coluna 'Fechado' de cada planilha e armazena em arrays
    fechado_planilha_2004_2024 = planilha_2004_2024['Fechado'].values
    fechado_planilha_2004_2005 = planilha_2004_2005['Fechado'].values
    fechado_planilha_2022_2023 = planilha_2022_2023['Fechado'].values


def initialize_data():
    ler_planilhas()
    separar_coluna_em_array()
