# EDA, Visualization, and Data Profiling Assignment

## Problem Description

In this assignment, you will perform an exploratory data analysis (EDA) on a small dataset. Your tasks are to load the data, generate a comprehensive profile report, and create two different visualizations to understand the data's characteristics. This assignment introduces fundamental data analysis techniques used in real-world data science projects.

## Learning Objectives

By completing this assignment, you will learn:
- How to load and inspect CSV data using pandas
- How to generate automated data profiling reports
- How to create basic visualizations (histograms and scatter plots)
- How to save and export analysis results
- Best practices for exploratory data analysis

## Setup Instructions

### Option 1: Using ydata-profiling (Recommended)
1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Make sure you have the following packages installed:
   - pandas (>=1.3.0)
   - matplotlib (>=3.5.0)
   - ydata-profiling (==4.6.3)
   - numpy (>=1.21.0)
   - scipy (>=1.9.0,<1.12.0)

### Option 2: Using pandas-profiling (Alternative)
If you encounter compatibility issues with ydata-profiling and Python 3.12, use this alternative:

1. Install the alternative dependencies:
   ```bash
   pip install -r requirements_alternative.txt
   ```

2. Use the alternative sample submission:
   ```bash
   cp sample_submission_alternative.py sample_submission.py
   ```

## Instructions

1. Open the `assignment.py` file.
2. You will find a function definition: `perform_eda(file_path)`.
3. The function takes a file path to a CSV file as input.
4. Your tasks are to:
   *   **Task 1**: Load the CSV file into a pandas DataFrame.
   *   **Task 2**: Use the profiling library to generate a profile report of the DataFrame and save it as `profile_report.html`.
   *   **Task 3**: Create a histogram of the 'Age' column and save it as `age_histogram.png`.
   *   **Task 4**: Create a scatter plot showing the relationship between 'Age' and 'Salary' and save it as `age_salary_scatter.png`.

## Hints

*   Use `pd.read_csv()` to load the data.
*   Use `ProfileReport(df, title="Pandas Profiling Report")` to create the report and `profile.to_file("profile_report.html")` to save it.
*   Use `matplotlib.pyplot` for plotting. `plt.hist()` for the histogram and `plt.scatter()` for the scatter plot.
*   Remember to add titles and labels to your plots!
*   Don't forget to call `plt.close()` after saving each plot to free up memory.

## Testing Your Solution

Run the test file to verify your implementation:
```bash
python test.py
```

The tests will check:
- That your function creates all expected output files
- That the profile report contains expected content
- That the data loading functionality works correctly
- That the generated files have reasonable sizes

## Expected Output

Your function should create three files:
- `profile_report.html`: An interactive HTML report with comprehensive data analysis
- `age_histogram.png`: A histogram showing the distribution of ages
- `age_salary_scatter.png`: A scatter plot showing the relationship between age and salary

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

### Compatibility Issues
If you encounter errors with ydata-profiling and Python 3.12, try:
1. Using the alternative requirements file with pandas-profiling
2. Downgrading to Python 3.11
3. Using a virtual environment with specific package versions

### Common Errors
- `AttributeError: 'float' object has no attribute 'ndim'`: This is a known issue with ydata-profiling and newer scipy versions. Use the alternative solution.
- `ModuleNotFoundError`: Make sure all dependencies are installed correctly.

## Further Exploration (Optional)

*   Try creating other types of plots, such as a box plot (`plt.boxplot()`) to see the distribution of salaries.
*   Explore the `seaborn` library, which is built on top of matplotlib and can create more aesthetically pleasing plots with less code.
*   Look into the `ProfileReport` object. What other information can you extract from it besides saving it to a file?
*   How would you modify the function to accept different column names?
*   Can you add error handling for cases where the CSV file doesn't exist or has missing columns?

## Resources

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/)
- [YData Profiling Documentation](https://ydata-profiling.ydata.ai/)
- [Pandas Profiling Documentation](https://pandas-profiling.ydata.ai/)
- [Exploratory Data Analysis Guide](https://towardsdatascience.com/exploratory-data-analysis-8fc1cb20fd15)
