import matplotlib.pyplot as plt
import numpy as np


def plotar(fechamento, simulations, final_values):
    # Configura os subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 12))

    # Plota o gráfico de fechamento histórico
    plot_fechamento(fechamento, ax1)

    # Plota o gráfico da simulação de Monte Carlo
    plot_simulation(simulations, final_values, ax2)

    # Ajuste de layout para não sobrepor os gráficos
    plt.tight_layout(pad=3)
    plt.show()


def plot_fechamento(fechamento, ax):
    # Substitui vírgulas por pontos e converte para float
    fechamento = [float(str(valor).replace(',', '.')) for valor in fechamento]

    # Inverte os valores de fechamento para mostrar na ordem correta
    fechamento = fechamento[::-1]

    # Plota o gráfico de fechamento histórico
    ax.plot(fechamento)

    # Título estilizado com espaçamento ajustado
    ax.set_title("Valores Reais - Fechamento BBAS3", fontsize=22,
                 color='#333333', pad=20)

    # Rótulos dos eixos com maior espaçamento e formatação
    ax.set_xlabel('Dias', fontsize=16, labelpad=15, color='#333333')
    ax.set_ylabel('Valor de Fechamento (R$)', fontsize=16,
                  labelpad=15, color='#333333')

    # Personalização da grade para melhor estética
    ax.grid(True, linestyle='--', alpha=0.5)

    # Melhorias na legenda com mais detalhes
    ax.legend(loc='upper left', fontsize=14,
              frameon=True, shadow=True, borderpad=1.5)

    # Ajuste das margens para uma melhor visualização
    ax.margins(x=0)

    # Ajusta os ticks para uma visualização mais clara
    ax.tick_params(axis='both', which='major', labelsize=12, colors='#333333')

    # Adiciona uma linha horizontal no valor médio do fechamento
    mean_value = np.mean(fechamento)
    ax.axhline(mean_value, color='purple', linestyle='-.',
               linewidth=1.5, alpha=0.7, label=f'Média: {mean_value:.2f}')

    # Adiciona a legenda
    ax.legend(loc='upper left', fontsize=14,
              frameon=True, shadow=True, borderpad=1.5)


def plot_simulation(simulations, final_values, ax):
    # Plota as simulações
    for i in range(simulations.shape[0]):
        color = 'green' if final_values[i] > simulations[i][0] else 'red'
        ax.plot(simulations[i], color=color, alpha=0.6, linewidth=1.5)

    # Adiciona uma linha mostrando a média dos valores finais
    mean_final_value = np.mean(final_values)
    ax.axhline(y=mean_final_value, color='blue', linestyle='--',
               label=f'Média Final: {mean_final_value:.2f}')

    # Adiciona rótulos e título
    ax.set_title('Simulação de Monte Carlo - Fechamento BBAS3', fontsize=16)
    ax.set_xlabel('Dias', fontsize=14)
    ax.set_ylabel('Preço Simulado', fontsize=14)

    # Adiciona a legenda
    ax.legend()

    # Adiciona uma grade
    ax.grid(True, linestyle='--', alpha=0.6)

    # Ajuste das margens
    ax.margins(x=0)
