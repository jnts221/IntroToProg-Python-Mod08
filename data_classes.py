# ------------------------------------------------------------------------------- #
# Title: Data Classes Module
# # Description: A collection of data classes for managing the application
# ChangeLog: (Who, When, What)
# Sohail Nassiri,09.25.2024,Created Script
# ------------------------------------------------------------------------------- #

try:
    if __name__ == "__main__":
        raise Exception("Please use the main.py file to start this application.")
    else:
        from datetime import date
except Exception as e:
    print(e.__str__())

# Data -------------------------------------------- #
FILE_NAME: str = 'EmployeeRatings.json'

MENU: str = '''
---- Employee Ratings ------------------------------
  Select from the following menu:
    1. Show current employee rating data. 
    2. Enter new employee rating data.
    3. Save data to a file.
    4. Exit the program.
--------------------------------------------------
'''

employees: list = []  # a table of employee data
menu_choice = ''


class Person:
    """
    A class representing person data.

    Properties:
        first_name (str): The employee's first name.
        last_name (str): The employee's last name.

    ChangeLog:
    Sohail Nassiri,09.25.2024: Created the class.
    """

    def __init__(self, first_name: str = '', last_name: str = ''):
        self.first_name = first_name
        self.last_name = last_name

    @property  # (Use this decorator for the getter or accessor)
    def first_name(self):
        return self.__first_name.title()  # formatting code

    @first_name.setter
    def first_name(self, value: str):
        if value.isalpha() or value == "":  # is character or empty string
            self.__first_name = value
        else:
            raise ValueError("The last name should not contain numbers.")

    @property
    def last_name(self):
        return self.__last_name.title()  # formatting code

    @last_name.setter
    def last_name(self, value: str):
        if value.isalpha() or value == "":  # is character or empty string
            self.__last_name = value
        else:
            raise ValueError("The last name should not contain numbers.")

    def __str__(self):
        return f'{self.first_name},{self.last_name}'


class Employee(Person):
    """
    A class representing employee data.

    Properties:
        first_name (str): The employee's first name.
        last_name (str): The employee's last name.
        review_date (str): The employee's review date.
        review_rating (int): The review rating of the employee.

    ChangeLog: (Who, When, What)
   Sohail Nassiri,09.25.2024,Created Class, added properties and private attribute, moved first_name and last_name into
   a parent class
    """

    def __init__(self, first_name: str = '', last_name: str = '', review_date: str = '1900-01-01',
                 review_rating: int = 3):
        super().__init__(first_name=first_name, last_name=last_name)
        self.review_date = review_date
        self.review_rating = review_rating

    @property
    def review_date(self):
        return self.__review_date

    @review_date.setter
    def review_date(self, value: str):
        try:  # using a try block to capture when an input cannot be changed to format other than ISO 8601
            date.fromisoformat(value)
            self.__review_date = value

        except ValueError:
            raise ValueError("Review date must be in ISO 8601 format (YYYY-MM-DD).")

    @property
    def review_rating(self):
        return self.__review_rating

    @review_rating.setter
    def review_rating(self, value: int):
        try:  # using a try block to capture when an input cannot be changed to a float
            self.__review_rating = value
            if value not in (1, 2, 3, 4, 5):
                raise ValueError("Review rating must be between 1 and 5.")
        except ValueError:
            raise ValueError("Review rating must be a numeric integer value between 1 - 5.")

    def __str__(self):
        return f'{self.first_name},{self.last_name},{self.review_date},{self.review_rating}'
