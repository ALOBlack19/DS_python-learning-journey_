import pandas as pd
import matplotlib.pyplot as plt

#                                            Questions for Dataset 2:

#                                         1. Basic DataFrame Operations:

# Load the dataset into a Pandas DataFrame.
employees = pd.read_csv("employee_data.csv")

# Display the first 5 rows of the DataFrame.
print("First 5 rows:\n", employees.head())
print()

# Display the summary statistics of the DataFrame.
print("Summary statistics:\n", round(employees.describe()))
print()

# Display the column names of the DataFrame.
print("Column names:\n",employees.columns)
print()

# Count the number of employees in each department.
print("Number of employees per department:\n", employees["Department"].value_counts())
print()

#                                         2. Filtering and Subsetting:

# Filter the DataFrame to show only employees who are older than 40.
emp_40 = employees[employees["Age"] > 40]
print("Employees who are older than 40:\n",emp_40[["Name", "Age"]])
print()

# Filter the DataFrame to show only employees in the 'IT' department.
emp_it = employees[employees["Department"] == "IT"]
print("Employees in the 'IT' department:\n", emp_it[["Name", "Department"]])
print()

# Filter the DataFrame to show employees with a salary above 75000.
emp_salary = employees[employees["Salary"] > 75000]
print("Employees with a salary above 75000:\n", emp_salary[["Name", "Salary"]])
print()

# Select the Name and Salary columns for all employees.
print("Name and Salary:\n", employees[["Name", "Salary", "Department"]])
print()

# Calculate the average salary for each department.
avg_dep_salary = employees.groupby("Department")[["Salary"]].mean()
print("Average salary for each department:\n\n", avg_dep_salary)
print()

#                                           3. Aggregation and Grouping:

# Calculate the average salary of all employees.
avg_emp_salary = employees[["Salary"]].mean()
print("Average salary of all employees:\n", avg_emp_salary)
print()

# Calculate the average age of employees in each department.
avg_age_dep = employees.groupby("Department")["Age"].mean()
print("Average age of employees in each department:\n", round(avg_age_dep))
print()

# Calculate the total years worked at the company for all employees.
t_y_w_e = employees[["YearsAtCompany"]].sum()
print("Total years worked at the company for all employees:\n", t_y_w_e)
print()

# Find the employee with the highest salary.

print("Employee with the highest salary:\n",employees[employees["Salary"] == employees["Salary"].max()])
print()

sort_salary = employees.sort_values('Salary', ascending = False)
print(sort_salary.iloc[0])
print()

# Calculate the average years at the company for each department.
avg_years_dep = employees.groupby("Department")["YearsAtCompany"].mean()

print("Average years at the company for each department:\n\n", avg_years_dep)

#                                             4. Data Visualization:

# Create a bar plot showing the average salary for each department.
avg_dep_salary.plot(kind = "bar", rot = 10)
plt.title("Average Salary per Department", weight = "bold")
plt.ylabel("Salaries", weight = "bold")
plt.xlabel("Department", weight = "bold")
plt.show()

# Create a bar plot showing the total years at the company for each employee.
employees[["Name","YearsAtCompany"]].plot(kind = "bar",rot = 45, y = "YearsAtCompany", x = "Name")
plt.title("Total Years per Employee", weight = "bold")
plt.ylabel("Years", weight = "bold")
plt.xlabel("Employees", weight = "bold")
plt.show()

# Create a histogram showing the distribution of employee ages.
employees["Age"].plot(kind = "hist", edgecolor = "black")
plt.title("Distribution of Employee Ages", weight = "bold")
plt.xlabel("Employees age", weight = "bold")
plt.ylabel("Number of employees", weight = "bold")
plt.show()

# Create a box plot to show the distribution of salaries for each department.
piv_dep_sal = employees.pivot_table("Salary",index = "Name", columns = "Department") #Also tried ".fillna(0)", but ruined the box plot visualization.
piv_dep_sal.plot(kind = "box")
plt.show()
print()
print(piv_dep_sal)

# Create a scatter plot showing the relationship between age and salary.
age_sal = employees[["Age","Salary"]].sort_values("Age")
age_sal.plot(kind = "scatter", x = "Age", y = "Salary")
plt.title("Relationship - Age and salary", weight = "bold")
plt.xlabel("Employees age", weight = "bold")
plt.ylabel("Salaries", weight = "bold")
print(age_sal)
plt.show()