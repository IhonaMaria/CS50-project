import re
import csv

infections = ['COVID19', 'Flu', 'SIDA', 'Aspergillus', 'Crpytococcus', 'Mucor']
cardiopatologies=['Heart attack', 'Heart failure', 'Arrythmia', 'High blood pressure', 'Valve disease']
cancers=['Kidney cancer', 'lung cancer', 'breast cancer', 'colon caner', 'brain cancer']
traumas=['Broken bone', 'Broken joint', 'Dislocated bone', 'Bone ache']

def main():
    if validate(input("Introduce your working credential: ")):
        # Open the first CSV file
        with open('patients_file.csv', mode='r') as file1:
            reader1 = csv.reader(file1)
            file1_data = list(reader1)

        # Open the second CSV file
        with open('doctors_file.csv', mode='r') as file2:
            reader2 = csv.reader(file2)
            file2_data = list(reader2)

        # Extract information from both CSV files
        with open('matches.csv', mode='w', newline='') as matches_file:
            writer = csv.writer(matches_file)
            writer.writerow(['Patient', 'Doctor associated'])

            for row1 in file1_data:
                for row2 in file2_data:
                    if row1[2] in infections and row2[2] == 'Infection':
                        writer.writerow([row1[0], row2[0]])
                    elif row1[2] in cardiopatologies and row2[2] == 'Cardiology':
                        writer.writerow([row1[0], row2[0]])
                    elif row1[2] in cancers and row2[2] == 'Oncology':
                        writer.writerow([row1[0], row2[0]])
                    elif row1[2] in traumas and row2[2] == 'Traumatology':
                        writer.writerow([row1[0], row2[0]])
            print('File created succesfully!')


def validate(s):
    if re.search(r"^([a-z]+)_([a-z]+)([0-9][0-9])([A-Z]{1})$",s):
        return True
    else:
        return False




if __name__ == '__main__':
    main()
