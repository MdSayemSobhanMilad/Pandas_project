import pandas as pd



# Module 2: Data Ingestion & Inspection
# Load the company_employees.csv file into a DataFrame called df.

# Display the first 5 and the last 3 rows of the DataFrame.

# Get a concise summary of the DataFrame's structure (info).

# Get the statistical summary of the numerical columns (describe).

# What is the shape of the DataFrame? (How many rows and columns?)



df = pd.read_csv('company_employees.csv') # Load the company_employees.csv file into a DataFrame called df.

print("The first 5 rows of the DataFrame: \n")
print(df.head(5))  # Display the first 5 rows of the DataFrame.
print("\nThe last 3 rows of the DataFrame: \n")
print(df.tail(3))  # Display the last 3 rows of the DataFrame.

print("Summary of the Dataframe: \n")
print(df.info())  # Get a concise summary of the DataFrame's structure (info).

print("\nStatistical summary of the numerical columns: \n")
print(df.describe())  # Get the statistical summary of the numerical columns (describe).

print("\nShape of the DataFrame: ")
print(df.shape)  # What is the shape of the DataFrame? (How many rows and columns?)




# Module 3: Selecting & Filtering Data
# Select only the first_name, department, and salary columns for all employees.

# Select the data for all employees who work in the "IT" department.

# Select the data for employees who have a performance_score greater than 90.

# Find all "Manager" titles in the "Sales" department.

# Select all employees who work in "London" OR have a salary greater than 100,000.


print("\nFirst name, department, and salary columns for all employees: \n")
print(df[['first_name', 'department', 'salary']])  # Select only the first_name, department, and salary columns for all employees.


print("\nEmployees who work in the IT department: \n")
for x in df.index:
  if df.loc[x, 'department'] == "IT":
    print(df.loc[x])  # Select the data for all employees who work in the "IT" department.

#or

print(df[df['department'] == 'IT'])


print("\nEmployees with performance_score greater than 90: \n")
for x in df.index:
  if df.loc[x, 'performance_score'] > 90:
    print(df.loc[x])  # Select the data for employees who have a performance_score greater than 90.


print("\nManagers in the Sales department: \n")
for x in df.index:
  if df.loc[x, 'title'] == "Manager" and df.loc[x, 'department'] == "Sales":
    print(df.loc[x])  # Find all "Manager" titles in the "Sales" department.


print("\nEmployees who work in London OR have a salary greater than 100,000: \n")
for x in df.index:
  if df.loc[x, 'location'] == "London" or df.loc[x, 'salary'] > 100000:
    print(df.loc[x])  # Select all employees who work in "London" OR have a salary greater than 100,000.


# Module 4: Data Cleaning
# Identify how many missing values exist in each column.

# The missing last_name for emp_id 107 is "Thompson". Fill this missing value in the DataFrame.

# The missing salary for emp_id 107 is 68,000. Fill this missing value.

# Check for any duplicate rows based on emp_id and remove them if any exist.

# Standardize the department names so any potential variations (e.g., "sales", "IT ") are corrected to "Sales" and "IT". (Hint: Use .str.strip() and .str.title()).

print("\nMissing values in each column: \n")
print(df.isnull().sum())  # Identify how many missing values exist in each column.


df.loc[df['emp_id'] == 107, 'last_name'] = "Thompson"  # The missing last_name for emp_id 107 is "Thompson". Fill this missing value in the DataFrame.

df.loc[df['emp_id'] == 107, 'salary'] = 68000  # The missing salary for emp_id 107 is 68,000. Fill this missing value.

df.drop_duplicates(subset=['emp_id'], keep='first', inplace=True)  # Check for any duplicate rows based on emp_id and remove them if any exist.

df['department'] = df['department'].str.strip().str.title()  # Standardize the department names so any potential variations (e.g., "sales", "IT ") are corrected to "Sales" and "IT". (Hint: Use .str.strip() and .str.title())


# Module 5: Transforming Data
# Create a new boolean column called is_high_performer that is True if performance_score is 90 or above.

# Create a new column called full_name by combining the first_name and last_name columns with a space in between.

# Increase everyone's salary by 3% for a cost-of-living adjustment and create a new column new_salary.


df['is_high_performancer'] = df['performance_score'] >= 90  # Create a new boolean column called is_high_performer that is True if performance_score is 90 or above.

df['full_name'] = df['first_name'] + ' ' + df['last_name']  # Create a new column called full_name by combining the first_name and last_name columns with a space in between.

df['new_salary'] = df['salary'] * 1.03  # Increase everyone's salary by 3% for a cost-of-living adjustment and create a new column new_salary.

print("\nDataFrame after transformations: \n")
print(df.to_string())  # Display the entire DataFrame after transformations.



# Module 6: Grouping and Aggregation
# What is the average salary in each department?

# What is the total number of employees in each location?

# For each department, what is the highest and lowest performance_score?

# What is the average salary for each job title?

print("\nAverage salary in each department: \n")
print(df.groupby('department')['salary'].mean())  # What is the average salary in each department? 

print("\nTotal number of employees in each location: \n")
print(df['location'].value_counts())  # What is the total number of employees in each location?

print("\nHighest and lowest performance_score in each department: \n")
print(df.groupby('department')['performance_score'].agg(['max', 'min']))  # For each department, what is the highest and lowest performance_score?


print("\nAverage salary for each job title: \n")
print(df.groupby('title')['salary'].mean())  # What is the average salary for each job title?

# Module 7: Combining Datasets (Bonus)
# Create a second CSV file called departments.csv with this data:

# csv
# department,department_budget,head_count
# Sales,500000,4
# Marketing,400000,4
# IT,700000,5
# HR,300000,2
# Operations,350000,3
# Load this new DataFrame and merge it with your main df DataFrame based on the department column. Use a left join to keep all employees.

# After merging, calculate the budget per employee for each department.

df2 = pd.read_csv('departments.csv')  # Load this new DataFrame
merged_df = pd.merge(df, df2, on = 'department', how = 'left')  # merge it with your main df DataFrame based on the department column. Use a left join to keep all employees.

print("Budget per employee: ", merged_df['department_budget'] / merged_df['head_count'])  # After merging, calculate the budget per employee for each department.


# Display the entire merged DataFrame.
print(merged_df.to_string())  # Display the entire merged DataFrame.


# Module 8: Time Series Analysis
# Convert the start_date column to a proper datetime data type.

# Set the start_date column as the index of the DataFrame.

# How many employees were hired in each year?

# What was the average salary of employees hired in 2020?

df['start_date'] = pd.to_datetime(df['start_date'])  # Convert the start_date column to a proper datetime data type.

df.set_index('start_date', inplace=True)  # Set the start_date column as the index of the DataFrame.

print("\nNumber of employees hired each year: \n")
print(df.resample('Y').size())  # How many employees were hired in each year?

# print("\nAverage salary of employees hired in 2020: \n")
# print(df['2020']['salary'].mean())  # What was the average salary of employees hired in 2020?

# Display the entire DataFrame with the datetime index.
print("\nDataFrame with datetime index: \n")
print(df.to_string())  # Display the entire DataFrame with the datetime index.

# Module 9 & 10: Advanced Techniques & Visualization
# Create a pivot table that shows the average salary for each department and title combination.

# Create a bar chart showing the total number of employees in each department.

# Create a histogram to visualize the distribution of salaries across all employees.

# Create a boxplot to show the distribution of performance_score within each department.

pivot_table = pd.pivot_table(df, values='salary', index='department', columns='title', aggfunc='mean')  # Create a pivot table that shows the average salary for each department and title combination.
print("\nPivot table showing the average salary for each department and title combination: \n")
print(pivot_table)  # Display the pivot table.

import matplotlib.pyplot as plt
import seaborn as sns
# Create a bar chart showing the total number of employees in each department.
dept_counts = df['department'].value_counts()
plt.figure(figsize=(10,6))
dept_counts.plot(kind='bar', color='skyblue')
plt.title('Total Number of Employees in Each Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.xticks(rotation=45)
plt.show()  # Show the bar chart.

# Create a histogram to visualize the distribution of salaries across all employees.
plt.figure(figsize=(10,6)) 
sns.histplot(df['salary'], bins=20, kde=True, color='green')
plt.title('Distribution of Salaries')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.show()  # Show the histogram.

# Create a boxplot to show the distribution of performance_score within each department.
plt.figure(figsize=(10,6))
sns.boxplot(x='department', y='performance_score', data=df, palette='Set3')
plt.title('Distribution of Performance Scores by Department')
plt.xlabel('Department')
plt.ylabel('Performance Score')
plt.show()  # Show the boxplot.