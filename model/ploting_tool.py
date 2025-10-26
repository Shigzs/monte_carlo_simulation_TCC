# plotting_tool.py (Versão Combinada)

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
# Importar se necessário para tipagem, embora as funções não usem diretamente
import pandas as pd


class PlottingTool:
    """
    Classe utilitária para gerar gráficos a partir dos dados de ações e simulação.
    """

    # Mantendo as funções originais para referência, se necessário
    @staticmethod
    def plot_closed_price(Data, stock, start_date):
        plt.figure(figsize=(10, 6))
        plt.plot(Data['Close'], label='Close Price')
        plt.title(f'Close Price of {stock} Since {start_date}')
        plt.xlabel('Date')
        plt.ylabel('Close Price (USD)')
        plt.legend()
        plt.grid(True)
        plt.show()

    @staticmethod
    def plot_log_return(log_return, stock, start_date):
        plt.figure(figsize=(10, 6))
        plt.plot(log_return, label='Log Returns')
        plt.title(f'Log Returns of {stock} Since {start_date}')
        plt.xlabel('Date')
        plt.ylabel('Log Returns')
        plt.legend()
        plt.grid(True)
        plt.show()

    # NOVO MÉTODO COMBINADO: Plota Simulação (Caminhos) e Histograma (Distribuição Final)
    @staticmethod
    def plot_montecarlo_results(simulation_dataframe, stock, last_price, num_days, stats):

        # Cria uma figura com dois subplots: 1 linha, 2 colunas
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
        plt.suptitle(f'Simulação de Monte Carlo para: {stock}', fontsize=16)

        # --- Subplot 1: Simulação (Caminhos de Preço) ---

        # Plota todas as simulações no primeiro eixo (ax1)
        simulation_dataframe.plot(legend=False, ax=ax1)

        # Adiciona a linha horizontal do preço inicial
        ax1.axhline(y=last_price, color='r', linestyle='-', label='Last Price')

        ax1.set_title('Trajetórias de Preço Projetadas')
        ax1.set_xlabel('Dia')
        ax1.set_ylabel('Preço (USD)')
        ax1.grid(True, linestyle='--')

        # Adiciona a caixa de texto com as estatísticas
        mean_price = stats["mean_price"]
        lower_bound = stats["lower_bound"]
        upper_bound = stats["upper_bound"]

        textstr = '\n'.join((
            f"Valor esperado em {num_days} dias: {mean_price:.2f}",
            f"Intervalo de 95%: ({lower_bound:.2f}  -  {upper_bound:.2f})"
        ))

        ax1.text(
            0.05, 0.95, textstr,
            transform=ax1.transAxes,
            fontsize=10,
            verticalalignment='top',
            bbox=dict(
                facecolor='white',
                edgecolor='black',
                boxstyle='round,pad=0.5',
                alpha=0.8
            )
        )

        # --- Subplot 2: Histograma (Distribuição de Preços Finais) ---

        prices = simulation_dataframe.iloc[-1]

        # Histograma com curva de densidade (KDE) no segundo eixo (ax2)
        sns.histplot(prices, kde=True, bins=50, ax=ax2)

        ax2.set_title(f'Distribuição de Preços Finais (Dia {num_days})')
        ax2.set_xlabel('Preço Final (USD)')
        ax2.set_ylabel('Frequência das Simulações')

        # Linha da Média
        ax2.axvline(mean_price, color='g', linestyle='--', linewidth=2,
                    label=f"Média: {mean_price:.2f}")

        # Linhas do Intervalo de Segurança de 95%
        ax2.axvline(lower_bound, color='r', linestyle='-', linewidth=2,
                    label="Limite Inferior (2.5%)")
        ax2.axvline(upper_bound, color='r', linestyle='-', linewidth=2,
                    label="Limite Superior (97.5%)")

        ax2.legend()
        ax2.grid(True, axis='y', linestyle='--')

        # Ajusta o layout para evitar sobreposição
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.show()
