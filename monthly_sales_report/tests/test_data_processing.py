import unittest
import pandas as pd
from scripts.data_processing import process_sales_data

class TestDataProcessing(unittest.TestCase):

    def test_process_sales_data(self):
        data = {
            'Month': ['Jan', 'Feb'],
            'Revenue': [15000, 18000],
            'Quantity': [150, 180],
            'New_Customers': [10, 15],
            'Returning_Customers': [50, 55]
        }
        df = pd.DataFrame(data)
        processed_df = process_sales_data(df)
        self.assertEqual(processed_df['Variation'].iloc[1], 20.0)

if __name__ == '__main__':
    unittest.main()
