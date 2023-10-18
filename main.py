import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_csv('Construction_Data_PM_Tasks_All_Projects (1).csv')
true_count = df['OverDue'].sum()

print(f"Number of 'True' entries in the 'OverDue' column: {true_count}")
#This is Question Number 1
grouped = df.groupby('Task Group')['Report Status'].value_counts().unstack(fill_value=0)

# If you want to sort by 'Task Group', you can reset the index
grouped = grouped.reset_index()
print(grouped)
#This was Question Number 2
plt.figure(figsize=(10, 6))
x = range(len(grouped))
width = 0.4
open_tasks = grouped['Open']
closed_tasks = grouped['Closed']

plt.bar(x, open_tasks, width=width, label='Open', align='center')
plt.bar(x, closed_tasks, width=width, label='Closed', align='edge')

plt.xticks(x, grouped['Task Group'], rotation=45, ha='right')

plt.xlabel('Task Group')
plt.ylabel('Total Tasks')
plt.title('Total Open and Closed Tasks by Task Group')
plt.legend()
plt.tight_layout()
plt.show()
# Filter for "overdue" tasks
# Filter for "overdue" tasks
# Filter for "overdue" tasks and group by "Project"
overdue_projects = df[df['Report Status'] == 'Open']['project'].value_counts()

# Create a bar chart
overdue_projects.plot(kind='bar', figsize=(10, 6))
plt.xlabel('Project')
plt.ylabel('Number of Overdue Tasks')
plt.title('Total Number of Overdue Tasks by Project')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()