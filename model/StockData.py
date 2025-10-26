import numpy as np
import pandas as pd
import yfinance as yf


class StockData:
    """
    Encapsula a funcionalidade de importar dados de ações e realizar
    cálculos estatísticos básicos (retornos logarítmicos, volatilidade).
    """

    def __init__(self, stock_ticker, start_date='2010-1-1'):
        self.stock_ticker = stock_ticker
        self.start_date = start_date
        self.data = self._import_stock_data()
        self.log_returns = self._calculate_log_returns()
        self.daily_volatility = self._calculate_volatility()
        self.last_price = self.data['Close'].iloc[-1] if not self.data.empty else None

    def _import_stock_data(self):
        """
        Importa os dados históricos de fechamento de ações usando yfinance.
        """
        print(
            f"Importando dados para {self.stock_ticker} desde {self.start_date}...")
        try:
            ticker = yf.Ticker(self.stock_ticker)
            data = ticker.history(start=self.start_date)
            if data.empty:
                print(
                    f"Aviso: Nenhum dado encontrado para {self.stock_ticker}.")
            return data
        except Exception as e:
            print(f"Erro ao importar dados: {e}")
            return pd.DataFrame()

    def _calculate_log_returns(self):
        """
        Calcula os retornos logarítmicos diários.
        """
        if self.data.empty:
            return pd.Series(dtype=float)

        # Retornos logarítmicos: ln(1 + R)
        log_returns = np.log(1 + self.data['Close'].pct_change())
        return log_returns.dropna()  # Remove o primeiro NaN

    def _calculate_volatility(self):
        """
        Calcula a volatilidade diária (desvio padrão dos retornos logarítmicos).
        """
        if self.log_returns.empty:
            return 0.0
        return np.std(self.log_returns)


class MonteCarloSimulator:
    """
    Realiza a simulação de Monte Carlo para o preço da ação.
    """

    def __init__(self, last_price, daily_volatility, num_simulations, num_days):
        self.last_price = last_price
        self.daily_volatility = daily_volatility
        self.num_simulations = num_simulations
        self.num_days = num_days
        self.simulation_dataframe = pd.DataFrame()
        self.mean_price = 0.0
        self.lower_bound = 0.0
        self.upper_bound = 0.0

    def run_simulation(self):
        """
        Executa a simulação de Monte Carlo.
        """
        if self.daily_volatility <= 0:
            print("Erro: Volatilidade diária inválida para simulação.")
            return

        all_simulations = []

        for x in range(self.num_simulations):
            price_series = [self.last_price]

            # O modelo assume que o preço segue um caminho de passeios aleatórios
            # com base na volatilidade histórica (Movimento Browniano Geométrico simplificado)
            for y in range(1, self.num_days):
                price = price_series[-1] * \
                    (1 + np.random.normal(0, self.daily_volatility))
                price_series.append(price)

            all_simulations.append(price_series)

        self.simulation_dataframe = pd.DataFrame(all_simulations).transpose()
        self._calculate_statistics()
        print("Simulação de Monte Carlo concluída.")

    def _calculate_statistics(self):
        """
        Calcula as estatísticas de interesse a partir do resultado da simulação.
        """
        prices = self.simulation_dataframe.iloc[-1]
        self.lower_bound = np.percentile(prices, 2.5)
        self.upper_bound = np.percentile(prices, 97.5)
        self.mean_price = np.mean(prices)

    def get_statistics(self):
        """
        Retorna as estatísticas calculadas.
        """
        return {
            "mean_price": self.mean_price,
            "lower_bound": self.lower_bound,
            "upper_bound": self.upper_bound
        }
