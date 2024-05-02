import medical_data_visualizer as mdv

def main():
    # Carregar dados
    df = mdv.load_data("exame_médico.csv")

    # Adicionar coluna "overweight"
    mdv.add_overweight_column(df)

    # Normalizar dados
    mdv.normalize_data(df)

    # Desenhar gráfico categórico
    cat_plot = mdv.draw_cat_plot(df)
    cat_plot.savefig("cat_plot.png")

    # Desenhar Mapa de Calor
    heat_map = mdv.draw_heat_map(df)
    heat_map.savefig("heat_map.png")

if __name__ == "__main__":
    main()