import pandas as pd
import matplotlib.pyplot as plt
from jinja2 import Environment, FileSystemLoader

def generate_html_report(df, template_path, output_path):
    summary_stats = df.describe().to_html(classes='summary')
    generate_plots(df)

    env = Environment(loader=FileSystemLoader(template_path))
    template = env.get_template('report_template.html')
    html_out = template.render(table=df.to_html(index=False, classes='data-table'),
                               summary=summary_stats)

    with open(output_path, 'w') as f:
        f.write(html_out)

def generate_plots(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df['Month'], df['Revenue'], marker='o', color='b', label='Revenue')
    plt.title('Monthly Sales')
    plt.xlabel('Month')
    plt.ylabel('Revenue ($)')
    plt.grid(True)
    plt.legend()
    plt.savefig('monthly_sales_report/reports/monthly_sales.png')
    plt.close()

    plt.figure(figsize=(10, 6))
    plt.bar(df['Month'], df['Variation'], color='g', label='Variation (%)')
    plt.title('Monthly Sales Variation')
    plt.xlabel('Month')
    plt.ylabel('Variation (%)')
    plt.grid(True)
    plt.legend()
    plt.savefig('monthly_sales_report/reports/monthly_variation.png')
    plt.close()

if __name__ == "__main__":
    df = pd.read_csv('monthly_sales_report/data/sales_data.csv')
    df['Variation'] = df['Revenue'].pct_change().fillna(0) * 100

    generate_html_report(df, 'monthly_sales_report/templates', 'monthly_sales_report/reports/monthly_sales_report.html')
