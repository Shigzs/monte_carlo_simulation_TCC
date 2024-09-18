import numpy as np
import pandas as pd


def monte_carlo_simulation(fechamento, num_simulations, num_days):
    # Converte o array numpy de fechamento para uma pandas Series
    fechamento_series = pd.Series(fechamento)

    # Verifica se os dados são strings e substitui vírgulas por pontos
    if fechamento_series.dtype == object:
        fechamento_series = fechamento_series.str.replace(
            ',', '.', regex=False).astype(float)

    # Calcula os retornos logarítmicos diários
    log_returns = np.log(1 + fechamento_series.pct_change().dropna())

    # Média e variância dos retornos logarítmicos
    mean_log_return = log_returns.mean()
    variance_log_return = log_returns.var()

    # Gerando simulações de Monte Carlo
    simulations = np.zeros((num_simulations, num_days))
    final_values = np.zeros(num_simulations)

    # Adiciona um ajuste para a média se ela for negativa
    adjusted_mean = mean_log_return if mean_log_return > 0 else 0

    for i in range(num_simulations):
        random_shocks = np.random.normal(
            loc=adjusted_mean, scale=np.sqrt(variance_log_return), size=num_days)
        simulations[i] = fechamento_series.iloc[-1] * \
            np.exp(np.cumsum(random_shocks))
        final_values[i] = simulations[i][-1]

    return simulations, final_values
