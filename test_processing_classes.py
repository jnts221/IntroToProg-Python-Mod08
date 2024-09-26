# ------------------------------------------------------------------------------- #
# Title: Test Processing Classes Module
# # Description: A collection of tests for the processing classes module
# ChangeLog: (Who, When, What)
# Sohail Nassiri,09.25.2024,Created Script
# ------------------------------------------------------------------------------- #

import unittest
import tempfile
import json
import data_classes as data
import processing_classes as proc


class TestFileProcessor(unittest.TestCase):
    def setUp(self):
        # Create a temporary file for testing
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file_name = self.temp_file.name
        self.employee_data = []

    def tearDown(self):
        # Clean up and delete the temporary file
        self.temp_file.close()

    def test_read_data_from_file(self):
        # Create some sample data and write it to the temporary file
        sample_data = [
            {"FirstName": "John", "LastName": "Doe", "ReviewDate": "2024-03-22", "ReviewRating": 3},
            {"FirstName": "Alice", "LastName": "Smith", "ReviewDate": "2024-04-03", "ReviewRating": 5},
        ]
        with open(self.temp_file_name, "w") as file:
            json.dump(sample_data, file)

        # Call the read_data_from_file method and check if it returns the expected data
        proc.FileProcessor.read_employee_data_from_file(self.temp_file_name, self.employee_data, data.Employee)

        # Assert that the employee_data list contains the expected employee objects
        self.assertEqual(len(self.employee_data), len(sample_data))
        self.assertEqual(self.employee_data[0].first_name, "John")
        self.assertEqual(self.employee_data[1].review_rating, 5)

    def test_write_data_to_file(self):
        # Create some sample employee objects
        sample_employees = [
            data.Employee("John", "Doe", "2024-03-22", 3),
            data.Employee("Alice", "Smith", "2024-04-03",5),
        ]

        # Call the write_data_to_file method to write the data to the temporary file
        proc.FileProcessor.write_employee_data_to_file(self.temp_file_name, sample_employees)

        # Read the data from the temporary file and check if it matches the expected JSON data
        with open(self.temp_file_name, "r") as file:
            file_data = json.load(file)

        self.assertEqual(len(file_data), len(sample_employees))
        self.assertEqual(file_data[0]["FirstName"], "John")
        self.assertEqual(file_data[1]["ReviewRating"], 5)

if __name__ == "__main__":
    unittest.main()
