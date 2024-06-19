import matplotlib.pyplot as plt

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
