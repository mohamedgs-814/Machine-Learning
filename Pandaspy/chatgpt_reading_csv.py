from pathlib import Path

import pandas as pd


# The data files are in the parent folder of this script. Using paths based on
# __file__ means the script works no matter which folder the terminal is in.
COURSE_DIR = Path(__file__).resolve().parent.parent
CSV_FILE = COURSE_DIR / "data_students.csv"
EXCEL_FILE = COURSE_DIR / "monthly_sales_tracker.xlsx"


data_frame = pd.read_csv(CSV_FILE)
print(data_frame)


data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": ["25", "48", "23"],
    "Country": ["USA", "Canada", "UK"],
}

df = pd.DataFrame(data)
print(df)

# Loading dataframes
csv_dataframe = pd.read_csv(CSV_FILE)
excel_dataframe = pd.read_excel(EXCEL_FILE)
dictionary_dataframe = pd.DataFrame(data)
print(excel_dataframe)