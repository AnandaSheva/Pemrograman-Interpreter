#unit_test.py
import unittest
import pandas as pd
from stats import CustomStatistics

class TestCustomStatistics(unittest.TestCase):
    def setUp(self):
        # Menyiapkan DataFrame contoh untuk pengujian
        data = {'Fee': [20000, 25000, 30000, 22000, 26000],
                'Total': [18000, 22000, 27000, 19800, 25000]}
        self.df = pd.DataFrame(data)
        self.custom_stats = CustomStatistics(self.df)

    def test_mean_calculation(self):
        mean_fee = self.custom_stats.calculate_mean('Fee')
        mean_total = self.custom_stats.calculate_mean('Total')

        self.assertEqual(mean_fee, 24600.0)
        self.assertEqual(mean_total, 22360.0)

    def test_median_calculation(self):
        median_fee = self.custom_stats.calculate_median('Fee')
        median_total = self.custom_stats.calculate_median('Total')

        self.assertEqual(median_fee, 25000.0)
        self.assertEqual(median_total, 22000.0)

    def test_mode_calculation(self):
        mode_fee = self.custom_stats.calculate_mode('Fee')
        mode_total = self.custom_stats.calculate_mode('Total')

        self.assertEqual(mode_fee, 20000)
        self.assertEqual(mode_total, 18000)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            invalid_stats = CustomStatistics("bukan_dataframe")

    def test_zero_division_error(self):
        with self.assertRaises(ZeroDivisionError):
            mean_invalid = self.custom_stats.calculate_mean('KolomTidakValid')

    def test_index_error(self):
        with self.assertRaises(IndexError):
            median_invalid = self.custom_stats.calculate_median('KolomTidakValid')

if __name__ == '__main__':
    unittest.main()
