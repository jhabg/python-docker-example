import csv

# Define the sample data
data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 35, "Chicago"],
    ["David", 28, "Houston"]
]

# Specify the file name
file_name = "sample_data.csv"

# Write data to the CSV file
with open(file_name, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV file '{file_name}' created successfully.")
