import csv

# Define the data to be written to the CSV file
doctors = [
    ['Name', 'Credential', 'specialization'],
    ['Maria', 'maria_correa98L', 'Infection'],
    ['Catalina', 'cata_liliana34R', 'Cardiology'],
    ['Angel', 'angel_cabo23P', 'Oncology'],
    ['Boni', 'boni_martin56F', 'Traumatology'],

]

# Specify the file name and open the file in write mode
filename = 'doctors_file.csv'

with open(filename, mode='w', newline='') as file:

    # Create a CSV writer object
    writer = csv.writer(file)

    # Write the data to the CSV file
    for row in doctors:
        writer.writerow(row)

print('File created successfully!')