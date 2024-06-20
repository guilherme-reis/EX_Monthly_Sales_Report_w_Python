import os
import subprocess
import webbrowser

def run_script(script_name):
    if not os.path.isfile(script_name):
        print(f"Script {script_name} does not exist.")
        return False

    print(f"Running {script_name}...")
    try:
        result = subprocess.run(['python3', script_name], capture_output=True, text=True)
        if result.stdout:
            print(f"Output from {script_name}:")
            print(result.stdout)
        if result.stderr:
            print(f"Errors from {script_name}:")
            print(result.stderr)
    except Exception as e:
        print(f"Failed to run {script_name}. Error: {e}")
        return False
    else:
        print(f"Finished running {script_name}.\n")
        return True

def main():
    if not os.path.exists('monthly_sales_report/data/sales_data.csv'):
        if not run_script('monthly_sales_report/scripts/create_csv_files.py'):
            return
    scripts = ['monthly_sales_report/scripts/data_processing.py', 'monthly_sales_report/scripts/visualization.py', 'monthly_sales_report/scripts/generate_report.py']
    for script in scripts:
        if not run_script(script):
            return
    webbrowser.open('file://' + os.path.realpath('monthly_sales_report/reports/monthly_sales_report.html'))

if __name__ == "__main__":
    main()