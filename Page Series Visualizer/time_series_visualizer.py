import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def draw_line_plot():
    # Importar os dados
    df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'], index_col='date')

    # Filtrar os dados
    df_filtered = df[
        (df['value'] >= df['value'].quantile(0.025)) &
        (df['value'] <= df['value'].quantile(0.975))
    ]

    # Desenhar o gráfico de linhas
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df_filtered.index, df_filtered['value'], color='r')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Salvar e mostrar o gráfico
    plt.savefig('line_plot.png')
    plt.show()

def draw_bar_plot():
    # Importar os dados
    df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'], index_col='date')

    # Agrupar por ano e mês
    df['year'] = df.index.year
    df['month'] = df.index.month
    df_grouped = df.groupby(['year', 'month']).mean().unstack()

    # Desenhar o gráfico de barras
    fig = df_grouped.plot(kind='bar', figsize=(10, 6)).get_figure()
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', labels=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    plt.title('Months')
    plt.xticks(rotation=45)

    # Salvar e mostrar o gráfico
    plt.savefig('bar_plot.png')
    plt.show()

def draw_box_plot():
    # Importar os dados
    df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'], index_col='date')

    # Preparar os dados
    df['year'] = df.index.year
    df['month'] = df.index.strftime('%b')
    df['month_num'] = df.index.month

    # Desenhar o box plot
    fig, axes = plt.subplots(1, 2, figsize=(20, 6))
    sns.boxplot(x='year', y='value', data=df, ax=axes[0])
    sns.boxplot(x='month_num', y='value', data=df, ax=axes[1], order=sorted(df['month_num'].unique()))
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Salvar e mostrar o gráfico
    plt.savefig('box_plot.png')
    plt.show()

# Testando as funções
draw_line_plot()
draw_bar_plot()
draw_box_plot()