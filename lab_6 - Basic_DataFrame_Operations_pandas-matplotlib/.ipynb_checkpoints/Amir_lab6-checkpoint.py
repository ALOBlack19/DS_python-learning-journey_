import pandas as pd
import matplotlib.pyplot as plt

# import numpy as np

#                                           Questions for Dataset 1:
#                                        1. Basic DataFrame Operations:

print("# 1. Basic DataFrame Operations:")
# Load the dataset into a Pandas DataFrame.

students = pd.read_csv("students_grades.csv")
print(students)
# Display the first 5 rows of the DataFrame.
print("Dataframe head\n",students.head())
print()

# Display the summary statistics of the DataFrame.
print(students.describe())
print()

# Display the column names of the DataFrame.
print(students.columns)
print()

# Count the number of male and female students.
print(students["Gender"].value_counts())
print()

#                                            2. Filtering and Subsetting:
print("2. Filtering and Subsetting:")

# Filter the DataFrame to show only students who are 16 years old.
age_16 = students[["Name", "Age"]]

print("Students with age 16:\n", age_16[age_16["Age"] == 16])
print()

# Filter the DataFrame to show only female students.
female = students[["Name", "Gender"]]

print("Female Students:\n",female[female["Gender"] == "F"])
print()

# Filter the DataFrame to show students with Math scores above 85.
stu_math = students[["Name", "Math"]]

print("Students with Math Score above 85:\n", stu_math[stu_math["Math"] > 85])
print()

# Select the Name and Total_Grades columns for all students.
tg = students[["Name", "Math", "Science", "English", "History", "Physical_Education"]]

print("Total student's grades:\n",tg)
print()

# Calculate the average Math score for male and female students.
stu = students[["Name", "Gender", "Math"]]

female_stu = stu[stu["Gender"] == "F"]
print(female_stu)
print()
male_stu = stu[stu["Gender"] == "M"]
print(male_stu)
print()
'''
print("Average Math score for FEMALE students:\n", female_stu["Math"].mean())
print()

print("Average Math score for MALE students:\n", male_stu["Math"].mean())
print()
'''
print("Math average per gender:\n",students.groupby("Gender")[["Math"]].mean())
print()

#                                        3. Aggregation and Grouping:

# Calculate the average grade for each subject.
stu_subject = students[["Math", "Science", "English", "History", "Physical_Education"]]
print(stu_subject.mean())
print()

# Calculate the average grade for each gender.
stu_gen_mean = students.groupby("Gender")[["Math", "Science", "English", "History", "Physical_Education"]].mean()
print("Average grade per students gender:\n",stu_gen_mean)
print()

# Calculate the total grades for each student (sum of all subjects).
subjects = ["Math", "Science", "English", "History", "Physical_Education"]
students["stu_sub_sum"] = students[subjects].sum(axis = 1) # students["stu_sub_sum"] is a new column name to receive the sum of all selected columns.
print("total grades for each student:\n", students[["Name", "stu_sub_sum"]])
print()
# axis=0 Rows go UP & DOWN (affects rows)
# axis=1 → Columns go LEFT & RIGHT (affects columns)

# Find the student with the highest total grade.
Max_grade = students[["Name", "stu_sub_sum"]].max()
print("Student with the highest total grade:\n", Max_grade)
print()

# Calculate the average age of the students.
avg_age = students[["Age"]].mean()
print("Average age of the students:\n", avg_age)
print()

#                                            4. Data Visualization:

# Create a bar plot showing the average grade for each subject.
subject_avg = students[subjects]
sub_avg = subject_avg.mean()
print("Average subject grades:\n",sub_avg)
print()
sub_avg.plot(kind = "bar", color = "y", x = sub_avg, y = subjects, rot = 10)
plt.xlabel("Subjects")
plt.ylabel("Average Grade")
plt.title("Average Grade per Subject")
plt.show()

# Create a bar plot showing the total grades of each student.
tot_grades = students[["Name","stu_sub_sum"]]
tot_grades.plot(kind = "bar", y = "stu_sub_sum", x = "Name", label = "stu_sub_sum", rot = 13)
plt.title("Total Grades")
plt.ylabel("Grades")
plt.xlabel("Students")
plt.show()

# Create a histogram showing the distribution of Math scores.
stu_math.plot(y = "Math", x = "Name", kind = "hist", edgecolor = "black")
plt.title("Math Distribution")
plt.ylabel("Number of students")
plt.xlabel("Math grades")
plt.show()

# Create a box plot to show the distribution of grades for each subject.
stu_subject.plot(kind = "box")
plt.title("Distribution of Grades", weight = 'bold')
plt.ylabel("Grades", weight = 'bold')
plt.xlabel("Subjects", weight = 'bold')
plt.show()

# Create a scatter plot showing the relationship between Math and Science
# scores.
math_science = students[["Name","Math","Science"]]
m_s_sort = math_science.sort_values(["Math","Science"])
m_s_sort.plot(kind = "scatter", x = "Math", y = "Science")
plt.title("Relationship - Math and Science")
plt.show()
# print(m_s_sort)


