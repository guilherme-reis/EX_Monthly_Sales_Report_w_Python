import pandas as pd
import matplotlib.pyplot as plt
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import os

def generate_html_report(df, template_path, output_path, report_dir):
    summary_stats = df.describe().to_html(classes='summary')
    sales_plot_path, variation_plot_path, revenue_distribution_plot_path, revenue_total_plot_path, scatter_plot_path = generate_plots(df, report_dir)

    sales_plot_path = os.path.abspath(sales_plot_path)
    variation_plot_path = os.path.abspath(variation_plot_path)
    revenue_distribution_plot_path = os.path.abspath(revenue_distribution_plot_path)
    revenue_total_plot_path = os.path.abspath(revenue_total_plot_path)
    scatter_plot_path = os.path.abspath(scatter_plot_path)

    env = Environment(loader=FileSystemLoader(template_path))
    template = env.get_template('report_template.html')
    html_out = template.render(table=df.to_html(index=False, classes='data-table'),
                               summary=summary_stats,
                               sales_plot_path=sales_plot_path,
                               variation_plot_path=variation_plot_path,
                               revenue_distribution_plot_path=revenue_distribution_plot_path,
                               revenue_total_plot_path=revenue_total_plot_path,
                               scatter_plot_path=scatter_plot_path)

    with open(output_path, 'w') as f:
        f.write(html_out)

    HTML(output_path).write_pdf(output_path.replace('.html', '.pdf'))

def generate_plots(df, report_dir):
    sales_plot_filename = plot_monthly_sales(df, report_dir)
    variation_plot_filename = plot_monthly_variation(df, report_dir)
    revenue_distribution_plot_filename = plot_revenue_distribution(df, report_dir)
    revenue_total_plot_filename = plot_revenue_total(df, report_dir)
    scatter_plot_filename = plot_scatter(df, report_dir)

    return sales_plot_filename, variation_plot_filename, revenue_distribution_plot_filename, revenue_total_plot_filename, scatter_plot_filename

def plot_monthly_sales(df, report_dir):
    plt.figure(figsize=(8, 6))
    plt.plot(df['Month'], df['Revenue'], marker='o', color='b', label='Revenue')
    plt.title('Monthly Sales')
    plt.xlabel('Month')
    plt.ylabel('Revenue ($)')
    plt.grid(True)
    plt.legend()
    filename = report_dir + '/monthly_sales.png'
    plt.savefig(filename)
    plt.close()
    return filename

def plot_monthly_variation(df, report_dir):
    plt.figure(figsize=(8, 6)) 
    plt.bar(df['Month'], df['Variation'], color='g', label='Variation (%)')
    plt.title('Monthly Sales Variation')
    plt.xlabel('Month')
    plt.ylabel('Variation (%)')
    plt.grid(True)
    plt.legend()
    filename = report_dir + '/monthly_variation.png'
    plt.savefig(filename)
    plt.close()
    return filename

def plot_revenue_distribution(df, report_dir):
    plt.figure(figsize=(8, 6))
    df['Revenue'].plot(kind='pie', autopct='%1.1f%%')
    plt.title('Revenue Distribution')
    filename = report_dir + '/revenue_distribution.png'
    plt.savefig(filename)
    plt.close()
    return filename

def plot_revenue_total(df, report_dir):
    plt.figure(figsize=(8, 6))
    df.groupby('Month')['Revenue'].sum().plot(kind='bar')
    plt.title('Total Revenue by Month')
    plt.xlabel('Month')
    plt.ylabel('Total Revenue ($)')
    filename = report_dir + '/revenue_total.png'
    plt.savefig(filename)
    plt.close()
    return filename

def plot_scatter(df, report_dir):
    plt.figure(figsize=(8, 6))
    plt.scatter(df['Revenue'], df['Variation'])
    plt.title('Scatter Plot of Revenue and Variation')
    plt.xlabel('Revenue ($)')
    plt.ylabel('Variation (%)')
    filename = report_dir + '/scatter_plot.png'
    plt.savefig(filename)
    plt.close()
    return filename

if __name__ == "__main__":
    df = pd.read_csv('monthly_sales_report/data/sales_data.csv')
    df['Variation'] = df['Revenue'].pct_change().fillna(0) * 100
    report_dir = 'monthly_sales_report/reports'
    generate_html_report(df, 'monthly_sales_report/templates', report_dir + '/monthly_sales_report.html', report_dir)