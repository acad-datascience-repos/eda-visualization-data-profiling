import os
import pandas as pd
import unittest
from assignment import perform_eda
import matplotlib.pyplot as plt

class TestEDA(unittest.TestCase):
    def setUp(self):
        """Set up test data before each test"""
        self.test_file = 'test_data.csv'
        data = {
            'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
            'Salary': [50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000],
            'Department': ['IT', 'HR', 'IT', 'Finance', 'HR', 'IT', 'Finance', 'HR', 'IT', 'Finance']
        }
        pd.DataFrame(data).to_csv(self.test_file, index=False)

    def tearDown(self):
        """Clean up created files after each test"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        if os.path.exists('summary.txt'):
            os.remove('summary.txt')
        if os.path.exists('age_histogram.png'):
            os.remove('age_histogram.png')

    def test_perform_eda_creates_expected_outputs(self):
        perform_eda(self.test_file)
        self.assertTrue(os.path.exists('summary.txt'), "summary.txt not created")
        self.assertTrue(os.path.exists('age_histogram.png'), "age_histogram.png not created")

    def test_summary_content(self):
        perform_eda(self.test_file)
        with open('summary.txt', 'r', encoding='utf-8') as f:
            content = f.read()
            self.assertIn('Rows:', content)
            self.assertIn('Columns:', content)
            self.assertIn('Column Names:', content)
            self.assertIn('Age Mean:', content)

    def test_file_sizes(self):
        perform_eda(self.test_file)
        self.assertGreater(os.path.getsize('summary.txt'), 20, "summary.txt is too small")
        self.assertGreater(os.path.getsize('age_histogram.png'), 500, "Histogram file is too small")

if __name__ == '__main__':
    unittest.main()
