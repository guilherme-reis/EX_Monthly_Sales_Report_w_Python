# Monthly Sales Report

This project generates a monthly sales report from sales and product data. The report includes various plots for visualizing the data.

## Project Structure

- `data/`: This directory contains the sales and product data in CSV format.
- `reports/`: This directory is where the generated reports are saved.
- `templates/`: This directory contains the HTML templates for the reports.
- `scripts/generate_report.py`: This is the main script that generates the report.

## How to Run

1. Ensure you have Python 3.6 or later installed.
2. Install the required packages with `pip install -r requirements.txt`.
3. Run the script with `python run_pipeline.py`.

## Report Details

The report includes the following plots:

- Monthly sales
- Monthly variation
- Revenue distribution
- Total revenue
- Scatter plot of revenue and variation
- Sales by product (new)
- Stock by product (new)
- Profit by product (new)

The report is saved as an HTML file in the `reports/` directory.
