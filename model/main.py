import plot
import data

# Definindo a ação (Stock) a ser utilizada
stock = "BBAS3.SA"

# Definindo a data de início dos dados a serem recolhidos
start_date = '2025-1-1'

# Inicializando o data frame com os dados recolhidos
Data = data.import_stock_data(stock, start=start_date)

# Definindo o número de simulações a serem realizadas
num_simulations = 1000

# Definindo o número de dias a serem simulados
num_days = 100

# Definindo o último valor conhecido da ação escolhida
last_price = Data['Close'].iloc[-1]

# Definindo o retorno logarítmico dos dados
log_return = data.log_returns(Data)

# Carregando um data frame com os dados simulados
simulation_dataframe = data.run_monteCarlo(
    num_simulations, num_days, last_price, log_return)


def main():
    # plot.plot_closed_price(Data, stock, start_date)
    # plot.plot_log_return(log_return, stock, start_date)
    plot.plot_simulation(simulation_dataframe, stock, last_price, num_days)


if __name__ == "__main__":
    main() in ()
