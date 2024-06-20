import subprocess

def run_script(script_name):
    print(f"Running {script_name}...")
    result = subprocess.run(['python3', script_name], capture_output=True, text=True)
    if result.stdout:
        print(f"Output from {script_name}:")
        print(result.stdout)
    if result.stderr:
        print(f"Errors from {script_name}:")
        print(result.stderr)
    print(f"Finished running {script_name}.\n")

def main():
    scripts = ['monthly_sales_report/scripts/data_processing.py', 'monthly_sales_report/scripts/visualization.py', 'monthly_sales_report/scripts/generate_report.py']
    for script in scripts:
        run_script(script)

if __name__ == "__main__":
    main()