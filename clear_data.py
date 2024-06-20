import os
import glob

def clear_directory(directory):
    files = glob.glob(f'{directory}/*')
    for file in files:
        os.remove(file)

def main():
    directories = ['monthly_sales_report/reports', 'monthly_sales_report/data']
    for directory in directories:
        clear_directory(directory)

if __name__ == "__main__":
    main()