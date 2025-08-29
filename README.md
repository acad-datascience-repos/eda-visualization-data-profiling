# EDA, Visualization, and Data Profiling Assignment

## Problem Description

In this assignment, you will perform a very lightweight exploratory data analysis (EDA) on a small dataset. Your tasks are to load the data, generate a short text summary, and create a single histogram to understand the distribution of ages.

## Learning Objectives

By completing this assignment, you will learn:
- How to load CSV data using pandas
- How to compute and write a minimal summary
- How to create and save a basic histogram with matplotlib
- How to export simple analysis results to disk

## Setup Instructions

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. This project uses only:
   - pandas (>=1.3.0)
   - matplotlib (>=3.5.0)
   - numpy (>=1.21.0)

## Instructions

1. Open the `assignment.py` file.
2. Implement the function `perform_eda(file_path)`.
3. The function takes a file path to a CSV file as input.
4. Your tasks are to:
   - Load the CSV file into a pandas DataFrame.
   - Create a brief text summary and save it as `summary.txt` containing:
     - Number of rows and columns
     - Column names
     - Mean of the `Age` column
   - Create a histogram of the `Age` column and save it as `age_histogram.png`.

## Hints

- Use `pd.read_csv(file_path)` to load the data.
- Use `df.shape`, `df.columns`, and `df['Age'].mean()` for the summary.
- Use `open('summary.txt', 'w')` to write the summary text.
- For plotting, use `matplotlib.pyplot`: `plt.figure()`, `plt.hist(df['Age'], bins=10)`, add labels/title, `plt.savefig('age_histogram.png')`, then `plt.close()`.

## Testing Your Solution

Run the tests to verify your implementation:
```bash
python -m unittest test.py
```

The tests will check that:
- `summary.txt` and `age_histogram.png` are created
- `summary.txt` contains the expected lines (Rows, Columns, Column Names, Age Mean)
- The generated files are not empty and have reasonable sizes

## Expected Output

Your function should create two files:
- `summary.txt`: A small text file with dataset shape, column names, and mean age
- `age_histogram.png`: A histogram showing the distribution of ages

Example `summary.txt` content:
```
Rows: 10
Columns: 3
Column Names: Age, Salary, Department
Age Mean: 45.00
```

## Sample Data Format

Your CSV file should have at least these columns:
- `Age`: Numerical values representing ages
- `Salary`: Numerical values representing salaries

Example:
```csv
Age,Salary,Department
25,50000,IT
30,60000,HR
35,70000,IT
```

## Troubleshooting

- Ensure the CSV has an `Age` column.
- If plots are not saved, confirm `plt.savefig(...)` is called before `plt.close()`.
- If files are empty, check that you write content to `summary.txt` and that the DataFrame is loaded correctly.

## Further Exploration (Optional)

- Add a scatter plot of `Age` vs `Salary`.
- Write an HTML report summarizing more statistics.
- Add basic error handling for missing files or columns.

## Resources

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/)
