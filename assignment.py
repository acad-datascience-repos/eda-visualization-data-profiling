import pandas as pd
import matplotlib.pyplot as plt

def perform_eda(file_path):
  """


  Your tasks (keep it super simple):
  1) Load the CSV into a DataFrame using pd.read_csv(file_path).
  2) Create a small text summary and save it as "summary.txt" containing:
     - Number of rows and columns
     - Column names
     - Mean of the 'Age' column (assume it exists)
  3) Plot a histogram of the 'Age' column and save it as "age_histogram.png".

  That's it. No HTML report, no scatter plots.
  """
  # Task 1: Load the dataset
  # Hint: Use pd.read_csv(file_path)
  # Your code here

  # Task 2: Write a minimal summary to "summary.txt"
  # Hint: Use df.shape, df.columns, df['Age'].mean(), and open(..., 'w')
  # Your code here

  # Task 3: Create a histogram of the 'Age' column and save to "age_histogram.png"
  # Hint: plt.figure(); plt.hist(...); add labels/title; plt.savefig('age_histogram.png'); plt.close()
  # Your code here

  pass
