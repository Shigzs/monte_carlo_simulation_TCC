# main_oo.py (Versão Simplificada)

from StockData import StockData, MonteCarloSimulator
from ploting_tool import PlottingTool

# --- Parâmetros de Configuração ---
stock_ticker = "BBAS3.SA"  # Banco do Brasil
# stock_ticker = "^BVSP"  # IBOVESPA
# stock_ticker = "PETR4.SA"  # Petrobrás
start_date = '2025-1-1'
num_simulations = 100000
num_days = 15
# -----------------------------------


def main_oo():
    # 1. Obter e processar dados
    stock_data_handler = StockData(stock_ticker, start_date)

    if stock_data_handler.data.empty or stock_data_handler.last_price is None:
        print("Não foi possível continuar devido à falta de dados.")
        return

    # 2. Executar a simulação de Monte Carlo
    mc_simulator = MonteCarloSimulator(
        last_price=stock_data_handler.last_price,
        today_price=stock_data_handler.today_price,
        daily_volatility=stock_data_handler.daily_volatility,
        num_simulations=num_simulations,
        num_days=num_days
    )
    mc_simulator.run_simulation()

    # Obter estatísticas para plotagem
    simulation_stats = mc_simulator.get_statistics()

    # 3. Plotar Resultados

    # Chamada única para o novo método combinado
    PlottingTool.plot_montecarlo_results(
        mc_simulator.simulation_dataframe,
        stock_ticker,
        stock_data_handler.last_price,
        stock_data_handler.today_price,
        num_days,
        simulation_stats
    )


if __name__ == "__main__":
    main_oo()
