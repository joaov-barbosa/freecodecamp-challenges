import unittest
import sea_level_predictor

class Tests(unittest.TestCase):
    def test_plot_exists(self):
        ax = sea_level_predictor.draw_sea_level_plot()
        self.assertIsInstance(ax, plt.Axes, "Expected instance of Axes")

if __name__ == "__main__":
    unittest.main()