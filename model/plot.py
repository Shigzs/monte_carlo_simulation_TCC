import matplotlib.pyplot as plt
import numpy as np


def plot_closed_price(Data, stock, start_date):
    plt.figure(figsize=(10, 6))
    plt.plot(Data['Close'], label='Close Price')
    plt.title(f'Close Price of {stock} Since {start_date}')
    plt.xlabel('Date')
    plt.ylabel('Close Price (USD)')
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_log_return(log_return, stock, start_date):
    plt.figure(figsize=(10, 6))
    plt.plot(log_return, label='Log Returns')
    plt.title(f'Log Returns of {stock} Since {start_date}')
    plt.xlabel('Date')
    plt.ylabel('Log Returns')
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_simulation(simulation_dataframe, stock, last_price, num_days):
    simulation_dataframe.plot(legend=False)
    plt.suptitle(f'Monte Carlo Simulation for: {stock}')
    plt.axhline(y=last_price, color='r', linestyle='-')
    plt.xlabel('Day')
    plt.ylabel('Price')

    prices = simulation_dataframe.iloc[-1]
    lower_bound = np.percentile(prices, 2.5)
    upper_bound = np.percentile(prices, 97.5)
    mean_price = np.mean(prices)

    textstr = '\n'.join((
        f"Valor esperado em {num_days} dias: {mean_price:.2f}",
        f"Intervalo de segurança de 95%: ({lower_bound:.2f}  -  {upper_bound:.2f})"
    ))

    plt.text(
        0.02, 0.95, textstr,
        transform=plt.gca().transAxes,   # Usa coordenadas relativas ao gráfico
        fontsize=10,                     # Tamanho da fonte
        verticalalignment='top',         # Alinha no topo
        bbox=dict(                       # Caixa de destaque
            facecolor='white',           # Cor de fundo
            edgecolor='black',           # Cor da borda
            boxstyle='round,pad=0.5',    # Caixa arredondada
            alpha=0.8                    # Transparência
        )
    )
    plt.tight_layout()
    plt.show()
