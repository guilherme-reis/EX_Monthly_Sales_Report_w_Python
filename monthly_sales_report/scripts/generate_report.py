import pandas as pd
from jinja2 import Environment, FileSystemLoader

def generate_html_report(df, template_path, output_path):
    env = Environment(loader=FileSystemLoader(template_path))
    template = env.get_template('report_template.html')
    html_out = template.render(table=df.to_html(index=False), 
                               summary=df.describe().to_html(classes='summary'))
    with open(output_path, 'w') as f:
        f.write(html_out)

if __name__ == "__main__":
    df = pd.read_csv('monthly_sales_report/data/sales_data.csv')
    df['Variation'] = df['Revenue'].pct_change().fillna(0) * 100
    
    generate_html_report(df, 'monthly_sales_report/templates', 'monthly_sales_report/reports/monthly_sales_report.html')
