import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import data


def monte_carlo_simulation(fechamento, num_simulations, num_days):
    # Converte o array numpy de fechamento para uma pandas Series
    fechamento_series = pd.Series(fechamento)

    # Verifica se os dados são strings e substitui vírgulas por pontos
    if fechamento_series.dtype == object:
        fechamento_series = fechamento_series.str.replace(
            ',', '.', regex=False).astype(float)

    # Calcula os retornos logarítmicos diários a partir da variação percentual dos preços de fechamento. Isso ajuda a normalizar os retornos e capturar melhor a volatilidade dos preços.
    log_returns = np.log(1 + fechamento_series.pct_change().dropna())

    # Calcula a média e a variância dos retornos logarítmicos, que serão usados para gerar as simulações aleatórias.
    mean_log_return = log_returns.mean()
    variance_log_return = log_returns.var()

    # Inicializa matrizes para armazenar os resultados das simulações (preços simulados ao longo dos dias) e os valores finais (preço ao final de cada simulação).
    simulations = np.zeros((num_simulations, num_days))
    final_values = np.zeros(num_simulations)

    # Ajusta a média dos retornos para evitar a influência de uma média negativa que poderia enviesar as simulações para baixo.
    adjusted_mean = mean_log_return if mean_log_return > 0 else 0

    for i in range(num_simulations):
        random_shocks = np.random.normal( #gera números randômicos que seguem a distribuição gaussiana
            loc=adjusted_mean, scale=np.sqrt(variance_log_return), size=num_days)
        simulations[i] = fechamento_series.iloc[-1] * \ #último preço de fechamento do ativo na série histórica
            np.exp(np.cumsum(random_shocks)) #soma cumulativa dos choques aleatórios ao longo dos dias
        final_values[i] = simulations[i][-1]

    return simulations, final_values


def plot_simulation(simulations, final_values):
    plt.figure(figsize=(12, 8))

    # Plota as simulações
    for i in range(simulations.shape[0]):
        color = 'green' if final_values[i] > simulations[i][0] else 'red'
        plt.plot(simulations[i], color=color, alpha=0.6, linewidth=1.5)

    # Adiciona uma linha mostrando a média dos valores finais
    mean_final_value = np.mean(final_values)
    plt.axhline(y=mean_final_value, color='blue', linestyle='--',
                label=f'Média Final: {mean_final_value:.2f}')

    # Adiciona rótulos e título
    plt.title('Simulação de Monte Carlo - Fechamento BBAS3', fontsize=16)
    plt.xlabel('Dias', fontsize=14)
    plt.ylabel('Preço Simulado', fontsize=14)

    # Adiciona a legenda
    plt.legend()

    # Adiciona uma grade
    plt.grid(True, linestyle='--', alpha=0.6)

    # Exibe o gráfico
    plt.show()
