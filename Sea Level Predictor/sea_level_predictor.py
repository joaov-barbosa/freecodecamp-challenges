import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_sea_level_plot():
    file_path = "epa-sea-level.csv"
    df = pd.read_csv(file_path)

    # Criar o gráfico de dispersão
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], c='b', label='Data')

    # Obter a linha de melhor ajuste para todos os dados
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Prever o aumento do nível do mar em 2050
    x_future = list(range(1880, 2051))
    y_future = [intercept + slope * year for year in x_future]
    plt.plot(x_future, y_future, 'r', label='Best Fit Line (1880-2050)')

    # Obter a linha de melhor ajuste para os dados desde o ano 2000
    recent_years_df = df[df['Year'] >= 2000]
    recent_slope, recent_intercept, _, _, _ = linregress(recent_years_df['Year'], recent_years_df['CSIRO Adjusted Sea Level'])
    y_recent_future = [recent_intercept + recent_slope * year for year in x_future]
    plt.plot(x_future, y_recent_future, 'g', label='Best Fit Line (2000-recent)')

    # Configurar o título e os rótulos dos eixos
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

    # Adicionar legenda
    plt.legend()

    # Salvar e mostrar o gráfico
    plt.savefig('sea_level_plot.png')
    plt.show()

    return plt.gca()

draw_sea_level_plot()