import time_series_visualizer

def main():
    # Chamando as funções para desenhar os gráficos
    time_series_visualizer.draw_line_plot()
    time_series_visualizer.draw_bar_plot()
    time_series_visualizer.draw_box_plot()

if __name__ == "__main__":
    main()