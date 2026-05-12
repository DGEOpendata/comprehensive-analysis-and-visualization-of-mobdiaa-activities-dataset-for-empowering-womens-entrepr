python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'path_to_dataset/DL02-Mobdiaa-Activities-ADRA-OD-006-AMO_0.xlsx'
data = pd.read_excel(file_path)

# Display the first few rows of the dataset
print(data.head())

# Basic statistics of the dataset
print(data.describe())

# Grouping by activity categories
activity_counts = data['Category'].value_counts()

# Plotting the activity categories
plt.figure(figsize=(10, 6))
sns.barplot(x=activity_counts.index, y=activity_counts.values, palette='viridis')
plt.title('Distribution of Activity Categories in Mobdiaa Dataset')
plt.xlabel('Activity Categories')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Filter data for a specific activity
tailoring_data = data[data['Category'] == 'Tailoring']
print(tailoring_data)

# Save filtered data as a new Excel file
tailoring_data.to_excel('tailoring_activities.xlsx', index=False)

print("Data analysis and visualization completed. Check the generated chart and saved Excel file.")
