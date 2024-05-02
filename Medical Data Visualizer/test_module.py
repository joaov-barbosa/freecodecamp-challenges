import unittest
import medical_data_visualizer as mdv

class TestMedicalDataVisualizer(unittest.TestCase):
    
    def test_draw_cat_plot(self):
        df = mdv.load_data("exame_médico.csv")
        mdv.add_overweight_column(df)
        mdv.normalize_data(df)
        fig = mdv.draw_cat_plot(df)
        self.assertIsInstance(fig, plt.Figure, "A função draw_cat_plot não retorna uma figura.")

    def test_draw_heat_map(self):
        df = mdv.load_data("exame_médico.csv")
        mdv.add_overweight_column(df)
        mdv.normalize_data(df)
        fig = mdv.draw_heat_map(df)
        self.assertIsInstance(fig, plt.Figure, "A função draw_heat_map não retorna uma figura.")

if __name__ == "__main__":
    unittest.main()