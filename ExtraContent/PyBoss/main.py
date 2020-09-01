import os
import csv
from us_state_abbrev import *



# Import the employee data
csvpath = os.path.join("employee_data.csv")

with open(csvpath) as csvfile:

    employee_data = csv.reader(csvfile, delimiter=",")
    csv_header = next(employee_data)

    #Convert the csv read data to a list
    emp_data_lst = list(employee_data)

    #Find the total number of employees
    total_employees = len(emp_data_lst)

    #Create an empty list for variables
    emp_id_list = []
    emp_fname_list = []
    emp_lname_list = []
    emp_dob_list = []
    emp_ssn_list = []
    emp_state_list = []    

    #Loop through the employee records and convert fields as needed
    for i in range(total_employees):
        emp_id = emp_data_lst[i][0]
        emp_id_list.append(emp_id)

        #Split the name into first and last
        emp_name = emp_data_lst[i][1]
        name_lst = emp_name.split(" ")
        emp_first_name = name_lst[0]
        emp_last_name = name_lst[1]
        emp_fname_list.append(emp_first_name)
        emp_lname_list.append(emp_last_name)

        #Convert the employee date of birth format
        emp_dob = emp_data_lst[i][2]
        emp_dob_month = emp_dob[5:7]
        emp_dob_day = emp_dob[-2:]
        emp_dob_year = emp_dob[:4]
        emp_dob_converted = f'{emp_dob_month}/{emp_dob_day}/{emp_dob_year}'
        emp_dob_list.append(emp_dob_converted)

        #Convert the employee ssn to show only the last 4
        emp_ssn = emp_data_lst[i][3]
        emp_ssn_lastfour = emp_ssn[-4:]
        emp_ssn_converted = f'***-**-{emp_ssn_lastfour}'
        emp_ssn_list.append(emp_ssn_converted)

        #Look up the employee state code from the imported dictionary
        emp_state = emp_data_lst[i][4]
        emp_state_converted = us_state_abbrev[emp_state]
        emp_state_list.append(emp_state_converted)

        #Print the converted data to the terminal
        # print(f'{emp_id}, {emp_first_name},{emp_last_name},{emp_dob_converted},{emp_ssn_converted},{emp_state_converted}')

    #Write the reformatted results to an output csv file
    csv_save_path = os.path.join("employee_data_reformatted.csv")

    employee_data_output = open(csv_save_path, mode = "w", newline='')
    
    csv_writer = csv.writer(employee_data_output, delimiter=' ')   
    
    id = 'Emp_ID'
    fname = 'First_Name'
    lname = 'Last_Name'
    dob = 'DOB'
    ssn = 'SSN'
    state = 'State'

    csv_writer.writerow(f'{id},{fname},{lname},{dob},{ssn},{state}')


    for i in range(total_employees):
        csv_writer.writerow([f'{emp_id_list[i]},{emp_fname_list[i]},{emp_lname_list[i]},{emp_dob_list[i]},{emp_ssn_list[i]},{emp_state_list[i]}'])
        

    

    


   
    