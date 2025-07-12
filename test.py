import os
import pandas as pd
import unittest
from assignment import perform_eda
import matplotlib.pyplot as plt

class TestEDA(unittest.TestCase):
    def setUp(self):
        """Set up test data before each test"""
        # Create a dummy csv file for testing
        self.test_file = 'test_data.csv'
        data = {
            'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
            'Salary': [50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000],
            'Department': ['IT', 'HR', 'IT', 'Finance', 'HR', 'IT', 'Finance', 'HR', 'IT', 'Finance']
        }
        pd.DataFrame(data).to_csv(self.test_file, index=False)

    def tearDown(self):
        """Clean up created files after each test"""
        # Clean up the created files
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        if os.path.exists('profile_report.html'):
            os.remove('profile_report.html')
        if os.path.exists('age_histogram.png'):
            os.remove('age_histogram.png')
        if os.path.exists('age_salary_scatter.png'):
            os.remove('age_salary_scatter.png')

    def test_perform_eda_creates_all_files(self):
        """Test that the function creates all expected output files"""
        perform_eda(self.test_file)
        
        # Check that all expected files are created
        self.assertTrue(os.path.exists('profile_report.html'), "Profile report HTML file not created")
        self.assertTrue(os.path.exists('age_histogram.png'), "Age histogram PNG file not created")
        self.assertTrue(os.path.exists('age_salary_scatter.png'), "Age-Salary scatter plot PNG file not created")

    def test_profile_report_content(self):
        """Test that the profile report contains expected content"""
        perform_eda(self.test_file)
        
        # Check that the HTML file contains expected content
        with open('profile_report.html', 'r', encoding='utf-8') as f:
            content = f.read()
            # Check for basic HTML structure and data statistics
            self.assertIn('Data Profiling Report', content, "Profile report title not found")
            self.assertIn('Age', content, "Age column not found in profile report")
            self.assertIn('Salary', content, "Salary column not found in profile report")
            self.assertIn('Mean:', content, "Basic statistics not found in profile report")

    def test_data_loading(self):
        """Test that the data loading functionality works correctly"""
        # Test that the CSV file can be loaded
        df = pd.read_csv(self.test_file)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertGreater(len(df), 0)
        self.assertIn('Age', df.columns)
        self.assertIn('Salary', df.columns)

    def test_file_sizes(self):
        """Test that the generated files have reasonable sizes"""
        perform_eda(self.test_file)
        
        # Check that files are not empty
        self.assertGreater(os.path.getsize('profile_report.html'), 100, "Profile report file is too small")
        self.assertGreater(os.path.getsize('age_histogram.png'), 1000, "Histogram file is too small")
        self.assertGreater(os.path.getsize('age_salary_scatter.png'), 1000, "Scatter plot file is too small")

if __name__ == '__main__':
    unittest.main()