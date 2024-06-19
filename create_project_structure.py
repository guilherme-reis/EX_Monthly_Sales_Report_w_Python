import os

# Estrutura de pastas
folders = [
    'monthly_sales_report',
    'monthly_sales_report/data',
    'monthly_sales_report/notebooks',
    'monthly_sales_report/reports',
    'monthly_sales_report/scripts',
    'monthly_sales_report/tests',
    'monthly_sales_report/templates'
]

# Arquivos e seus conteúdos iniciais
files = {
    'monthly_sales_report/.gitignore': '',
    'monthly_sales_report/README.md': '''# Monthly Sales Report with Python

This project generates a monthly sales report using Python. It includes data processing, visualization, and report generation.

## Project Structure

- `data/`: Contains the sales data in CSV format.
- `notebooks/`: Jupyter notebook for exploratory data analysis.
- `reports/`: Directory for generated reports.
- `scripts/`: Contains Python scripts for data processing, visualization, and report generation.
- `tests/`: Contains tests for the data processing script.
- `requirements.txt`: Lists the project dependencies.
- `README.md`: Project documentation.

## Setup

1. Clone the repository.
2. Install the dependencies:
    ```
    pip install -r requirements.txt
    ```
3. Run the data processing script:
    ```
    python scripts/data_processing.py
    ```
4. Generate visualizations:
    ```
    python scripts/visualization.py
    ```
5. Generate the final report:
    ```
    python scripts/generate_report.py
    ```

## Usage

- Add your sales data to the `data/` directory in CSV format.
- Modify the scripts in the `scripts/` directory as needed.
- Run the scripts to generate the report.
''',
    'monthly_sales_report/requirements.txt': '''pandas
matplotlib
jinja2
''',
    'monthly_sales_report/scripts/data_processing.py': '''import pandas as pd

def load_sales_data(filepath):
    return pd.read_csv(filepath)

def process_sales_data(df):
    df['Variation'] = df['Revenue'].pct_change().fillna(0) * 100
    return df

if __name__ == "__main__":
    df = load_sales_data('../data/sales_data.csv')
    df = process_sales_data(df)
    print(df.head())
''',
    'monthly_sales_report/scripts/visualization.py': '''import matplotlib.pyplot as plt

def plot_monthly_sales(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df['Month'], df['Revenue'], marker='o')
    plt.title('Monthly Sales')
    plt.xlabel('Month')
    plt.ylabel('Revenue ($)')
    plt.grid(True)
    plt.savefig('../reports/monthly_sales.png')

def plot_variation(df):
    plt.figure(figsize=(10, 6))
    plt.bar(df['Month'], df['Variation'])
    plt.title('Monthly Sales Variation')
    plt.xlabel('Month')
    plt.ylabel('Variation (%)')
    plt.grid(True)
    plt.savefig('../reports/monthly_variation.png')
''',
    'monthly_sales_report/scripts/generate_report.py': '''import pandas as pd
from jinja2 import Environment, FileSystemLoader

def generate_html_report(df, template_path, output_path):
    env = Environment(loader=FileSystemLoader(template_path))
    template = env.get_template('report_template.html')
    html_out = template.render(table=df.to_html(index=False))
    
    with open(output_path, 'w') as f:
        f.write(html_out)

if __name__ == "__main__":
    df = pd.read_csv('../data/sales_data.csv')
    df['Variation'] = df['Revenue'].pct_change().fillna(0) * 100
    
    generate_html_report(df, '../templates', '../reports/monthly_sales_report.html')
''',
    'monthly_sales_report/templates/report_template.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Monthly Sales Report</title>
</head>
<body>
    <h1>Monthly Sales Report</h1>
    <p>Below is the summary of the monthly sales data:</p>
    {{ table | safe }}
    <h2>Sales Visualizations</h2>
    <img src="monthly_sales.png" alt="Monthly Sales">
    <img src="monthly_variation.png" alt="Monthly Sales Variation">
</body>
</html>
''',
    'monthly_sales_report/tests/test_data_processing.py': '''import unittest
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
'''
}

# Criação das pastas
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Criação dos arquivos com conteúdos iniciais
for filepath, content in files.items():
    with open(filepath, 'w') as f:
        f.write(content)

print("Project structure created successfully!")
