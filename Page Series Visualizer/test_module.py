import unittest
import time_series_visualizer

class Tests(unittest.TestCase):
    def test_line_plot(self):
        actual = time_series_visualizer.draw_line_plot()
        expected = None
        self.assertEqual(actual, expected, "Expected return value: None")

    def test_bar_plot(self):
        actual = time_series_visualizer.draw_bar_plot()
        expected = None
        self.assertEqual(actual, expected, "Expected return value: None")

    def test_box_plot(self):
        actual = time_series_visualizer.draw_box_plot()
        expected = None
        self.assertEqual(actual, expected, "Expected return value: None")

if __name__ == "__main__":
    unittest.main()