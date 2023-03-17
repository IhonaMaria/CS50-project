import csv

# Define the data to be written to the CSV file
patients = [
    ['Name', 'Age', 'Condition'],
    ['Laia', '25', 'COVID-19'],
    ['Sarah', '5', 'Broken bone'],
    ['John', '60', 'Kidney cancer'],
    ['Pol', '15', 'Leuccemia'],
    ['Marisa', '47', 'Heart attack'],
    ['Jorge', '70', 'Flu'],
]

# Specify the file name and open the file in write mode
filename = 'patients_file.csv'

with open(filename, mode='w', newline='') as file:

    # Create a CSV writer object
    writer = csv.writer(file)

    # Write the data to the CSV file
    for row in patients:
        writer.writerow(row)

print('File created successfully!')