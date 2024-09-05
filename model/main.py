import data
import monte_carlo_simulation as mcs


def main():
    # Inicializa os dados
    data.initialize_data()

    # Escolha a série de dados
    fechamento = data.fechado_planilha_2022_2023

    # Parâmetros para a simulação
    num_simulations = 1000  # Número de simulações
    num_days = 365  # Número de dias para cada simulação

    # Executa a simulação de Monte Carlo
    simulations, final_values = mcs.monte_carlo_simulation(
        fechamento, num_simulations, num_days)

    # Plota as simulações
    mcs.plot_simulation(simulations, final_values)


if __name__ == "__main__":
    main()