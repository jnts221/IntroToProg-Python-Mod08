# ------------------------------------------------------------------------------- #
# Title: Processing Classes Module
# # Description: A collection of processing classes for managing the application
# ChangeLog: (Who, When, What)
# Sohail Nassiri,09.25.2024,Created Script
# ------------------------------------------------------------------------------- #

try:
    if __name__ == "__main__":
        raise Exception("Please use the main.py file to start this application.")
    else:
        import json
        import data_classes as data
        import presentation_classes as pres
except Exception as e:
    print(e.__str__())


class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    Sohail Nassiri,09.25.2024,Created Class and converted code to use employee objects instead of dictionaries
    """

    @staticmethod
    def read_employee_data_from_file(file_name: str, employee_data: list, employee_type: object):
        """ This function reads data from a json file and loads it into a list of employee objects

        ChangeLog: (Who, When, What)
        Sohail Nassiri,09.25.2024,Created function and converted list of dictionaries to list of employee objects

        :param file_name: string data with name of file to read from
        :param employee_data: list of dictionary rows to be filled with file data
        :param employee_type: list of employee objects to be filled with file data

        :return: list
        """
        try:
            with open(file_name, "r") as file:
                list_of_dictionary_data = json.load(file)  # the load function returns a list of dictionary rows.
                for employee in list_of_dictionary_data:
                    employee_object = employee_type(first_name=employee["FirstName"],
                                                    last_name=employee["LastName"],
                                                    review_date=employee["ReviewDate"],
                                                    review_rating=employee["ReviewRating"])
                    employee_data.append(employee_object)
        except FileNotFoundError as e:
            pres.IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            pres.IO.output_error_messages("There was a non-specific error!", e)
        return employee_data

    @staticmethod
    def write_employee_data_to_file(file_name: str, employee_data: list):
        """ This function writes data to a json file with data from a list of dictionary rows

        ChangeLog: (Who, When, What)
        Sohail Nassiri,09.25.2024,Created function and converted code to use employee objects instead of dictionaries

        :param file_name: string data with name of file to write to
        :param employee_data: list of dictionary rows to be writen to the file

        :return: None
        """
        try:
            list_of_dictionary_data: list = []
            for employee in employee_data:  # Convert List of Employee objects to list of dictionary rows.
                employee_json: dict = {"FirstName": employee.first_name,
                                       "LastName": employee.last_name,
                                       "ReviewDate": str(employee.review_date),
                                       "ReviewRating": employee.review_rating}
                list_of_dictionary_data.append(employee_json)

            with open(file_name, "w") as file:
                json.dump(list_of_dictionary_data, file)
            print("The following data has been saved to the file:")
        except TypeError as e:
            pres.IO.output_error_messages("Please check that the data is a valid JSON format", e)
        except Exception as e:
            pres.IO.output_error_messages("There was a non-specific error!", e)
