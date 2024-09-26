# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08
# # Description: A collection of classes for managing the application
# ChangeLog: (Who, When, What)
# Sohail Nassiri,09.25.2024,Created Script
# ------------------------------------------------------------------------------------------------- #

try:
    if __name__ == "__main__":
        import processing_classes as proc
        import presentation_classes as pres
        import data_classes as data
    else:
        raise Exception("This file starts the application and should not be imported.")
except Exception as e:
    print(e.__str__())


# Beginning of the main body of this script
employees = proc.FileProcessor.read_employee_data_from_file(file_name=data.FILE_NAME, employee_data=data.employees,
                                                            employee_type=data.Employee)

# Repeat the follow tasks
while True:
    pres.IO.output_menu(menu=data.MENU)
    menu_choice = pres.IO.input_menu_choice()

    if menu_choice == "1":  # Display current data
        pres.IO.output_employee_data(employee_data=employees)
        continue

    elif menu_choice == "2":  # Get new data (and display the change)
        employees = pres.IO.input_employee_data(employee_data=employees, employee_type=data.Employee)
        pres.IO.output_employee_data(employee_data=employees)
        continue

    elif menu_choice == "3":  # Save data in a file
        proc.FileProcessor.write_employee_data_to_file(file_name=data.FILE_NAME, employee_data=employees)
        pres.IO.output_employee_data(employee_data=employees)
        continue

    elif menu_choice == "4":  # End the program
        break  # out of the while loop
