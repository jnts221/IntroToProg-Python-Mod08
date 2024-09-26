# ------------------------------------------------------------------------------- #
# Title: Presentation Classes Module
# # Description: A collection of presentation classes for managing the application
# ChangeLog: (Who, When, What)
# Sohail Nassiri,09.25.2024,Created Script
# ------------------------------------------------------------------------------- #

try:
    if __name__ == "__main__":
        raise Exception("Please use the main.py file to start this application.")
    else:
        import data_classes as data
except Exception as e:
    print(e.__str__())


class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    Sohail Nassiri,09.25.2024,Created Class, added menu output and input functions,added a function to display the data,
    added a function to display custom error message, and converted methods to use student objects instead of
    dictionaries
    """
    pass

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays custom error messages to the user

        ChangeLog: (Who, When, What)
        Sohail Nassiri,09.25.2024,Created function

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """

        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
         Sohail Nassiri,09.25.2024,Created function

        :return: None
        """
        print()
        print(menu)
        print()

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        Sohail Nassiri,09.25.2024,Created function

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # passing the exception object to avoid the technical message

        return choice

    @staticmethod
    def output_employee_data(employee_data: list):
        """ This function displays the review ratings to the user

        ChangeLog: (Who, When, What)
        Sohail Nassiri,09.25.2024,Created function and converted code to use student objects instead of dictionaries

        :param employee_data: list of student object data to be displayed

        :return: None
        """
        print()
        print("-" * 50)
        message = ""
        for employee in employee_data:
            if employee.review_rating == 1:
                message = " On {}, {} {} earned a rating of {} (Does Not Meet Expectations)."
            elif employee.review_rating == 2:
                message = " On {}, {} {} earned a rating of {} (Meets Some Expectations)."
            elif employee.review_rating == 3:
                message = " On {}, {} {} earned a rating of {} (Meets Expectations)."
            elif employee.review_rating == 4:
                message = " On {}, {} {} earned a rating of {} (Exceeds Expectations)."
            elif employee.review_rating == 5:
                message = " On {}, {} {} earned a rating of {} (Far Exceeds Expectations)."
            print(message.format(employee.review_date, employee.first_name, employee.last_name,
                                 employee.review_rating))

        print("-" * 50)
        print()

    @staticmethod
    def input_employee_data(employee_data: list, employee_type: object):
        """ This function gets the first name, last name, review date, and review rating from the user

        ChangeLog: (Who, When, What)
         Sohail Nassiri,09.25.2024,Created function and converted code to use student objects instead of dictionaries

        :param employee_data: list of dictionary rows to be filled with input data
        :param employee_type: list of employee objects to be filled with file data

        :return: list
        """

        try:
            # Input the data
            employee = employee_type()
            employee.first_name = input("What is the employee's first name? ")
            employee.last_name = input("What is the employee's last name? ")
            employee.review_date = input("What is the employee's review date? ")
            employee.review_rating = int(input("What is the employee's review rating? "))
            employee_data.append(employee)

        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)

        return employee_data
