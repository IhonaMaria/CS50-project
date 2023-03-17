# A DAY IN THE HOSPITAL

#Introduction
This is a small project I did for the CS50 introduction to programming with Python. Since I study biomedical engineering, I decided to create a program related to the healthcare field.
The program, after validating your supposed hospital "working credential", takes the information of two csv files previously created and outputs another csv file with a list of the patient and the doctor that should be assigned to the patient according to his or her medical condition. 

#Validate working credential
Imagine you are a hospital worker and want to access the database to check which new patient needs to be assigned to which doctor. For security reasons, there must be a way to prove that you are indeed a hospital employee to have the right to access that information. I decided to check the worker credential first using Python regular expressions, which are really useful to check if a string contains the specified search pattern. The search pattern I decided to implement was name_surnameXXY, XX being two numbers and Y being a capital letter. 
Only if the string that the user introduces matches the pattern (meaning that indeed the user is a hospital employee properly indentified) the output csv file will be created.  


#patients_file.csv and doctors_file.csv

Patients_file.csv is a csv file I created with Python through the code patients.py that contains information of the incoming patients (name, age and medical condition).
Doctors_file.csv, on the other hand, is a csv file I created with Python through the code doctors.py that contains information of doctors that are in that hospital (name, credential and specialization).


#project.py

After validating the working credential through regular expressions as it was previously mentioned, the program opens and reads both csv files and creates a new csv file called matches.csv with a first row named 'Patient', 'Doctor associated'. Then, through a for loop it iterates through the csv files and with a conditional it compares the medical condition of each patient with a list of different contitions. If the condition of the patient is in the list and the name of the list matches with the specialization of the doctor in doctors_file.csv, then the program appends a new row in matches.csv with the name of that patient and the doctor. 


#Conclusion

This program provides a file with the name of the patient and the name of the doctor that has to take care of the patient. The case has been simplified (it has a small quantity of patients and doctors and the list of medical conditions is also short) but it exemplifies a situation that could happen nowadays. This program could be helpful to reduce the time that the employees spend searching for available doctors to assign to a patient. 

A possible improvement could be to extract the information from an API with real-time patients and also to erase the doctor from the list of available doctors once it has been assigned to several patients. 

Hope you like it!




