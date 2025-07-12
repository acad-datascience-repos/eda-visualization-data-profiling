import pandas as pd
import matplotlib.pyplot as plt
import pandas_profiling

def perform_eda(file_path):
  """
  Performs an exploratory data analysis on the given dataset.

  This function demonstrates a complete EDA workflow:
  1. Data loading and inspection
  2. Automated data profiling
  3. Data visualization with histograms
  4. Relationship analysis with scatter plots

  Args:
    file_path: The path to the CSV file.
  """
  # Task 1: Load the dataset
  # Hint: Use pd.read_csv() to load the data from the file_path.
  df = pd.read_csv(file_path)
  # Your code here

  # Task 2: Generate a profile report
  # Hint: Create a ProfileReport object and use the to_file() method to save it.
  # Use pandas_profiling.ProfileReport(df, title="Pandas Profiling Report") and profile.to_file("profile_report.html")
  profile = pandas_profiling.ProfileReport(df, title="Pandas Profiling Report")
  profile.to_file("profile_report.html")
  # Your code here

  # Task 3: Create a histogram of the 'Age' column
  # Hint: Use plt.hist() and save the figure using plt.savefig().
  # Steps: plt.figure(), plt.hist(df['Age'], bins=10), add title/labels, plt.savefig('age_histogram.png'), plt.close()
  plt.figure()
  plt.hist(df['Age'], bins=10)
  plt.title('Distribution of Age')
  plt.xlabel('Age')
  plt.ylabel('Frequency')
  plt.savefig('age_histogram.png')
  plt.close()
  # Your code here

  # Task 4: Create a scatter plot of 'Age' vs 'Salary'
  # Hint: Use plt.scatter() and save the figure.
  # Steps: plt.figure(), plt.scatter(df['Age'], df['Salary']), add title/labels, plt.savefig('age_salary_scatter.png'), plt.close()
  plt.figure()
  plt.scatter(df['Age'], df['Salary'])
  plt.title('Age vs. Salary')
  plt.xlabel('Age')
  plt.ylabel('Salary')
  plt.savefig('age_salary_scatter.png')
  plt.close()
  # Your code here

  pass 