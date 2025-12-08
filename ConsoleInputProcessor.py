from TaxPrinter import create_tax_letter  # not used yet
from TaxCalculator import calculate_tax   # not used yet
import re

# Request input from user with validation for required fields.
def requestInput():

    print("=== Enter Tax Information ===")

    def get_name(prompt):
        # Allow Unicode letters (including German/French accents), spaces, apostrophes and hyphens
        pattern = re.compile(r"^[^\W\d_]+(?:[ '\-][^\W\d_]+)*$", re.UNICODE)
        while True:
            val = input(prompt).strip()
            if not val:
                print("Error: value cannot be empty.")
                continue
            if not pattern.fullmatch(val):
                print("Error: name must contain only letters (including accented), spaces, apostrophes or hyphens (no digits or special characters).")
                continue
            return val

    def get_address(prompt):
        # Allow Unicode letters (including ä, ö, ü, è, etc.), spaces, apostrophes and hyphens.
        # Expected format: StreetName StreetNumber ZipCode(4 digits) City
        # Examples: "Bahnhofstrasse 12 8001 Zürich", "General Weberstrasse 12 8001 Zürich", "Main-Street 5 1003 Lausanne"
        pattern = re.compile(
            r"^[^\W\d_]+(?:[ '\-\.][^\W\d_]+)*\s+\d+[A-Za-z]?\s+\d{4}\s+[^\W\d_]+(?:[ '\-][^\W\d_]+)*$",
            re.UNICODE,
        )
        while True:
            val = input(prompt).strip()
            if not val:
                print("Error: value cannot be empty.")
                continue
            if not pattern.fullmatch(val):
                print("Error: address must be in Swiss format (Street_name street_number Zipcode City). Street names can include multiple words with spaces or hyphens (e.g., 'General Weberstrasse', 'Main-Street').")
                continue
            return val

    def get_sex(prompt):
        valid = {"male", "female", "m", "f", "man", "woman"}
        valid_input = {"male", "female", "m", "f"}
        while True:
            val = input(prompt).strip().lower()
            if val not in valid:
                print(f"Error: enter one of: male, female, man, woman, m, f.")
                continue
            # Convert man/woman to male/female
            if val == "man":
                return "male"
            elif val == "woman":
                return "female"
            return val

    def get_number(prompt):
        # Accept only non-negative decimal numbers (digits and optional single dot)
        pattern = re.compile(r"^\d+(\.\d+)?$")
        while True:
            s = input(prompt).strip()
            if not s:
                print("Error: value cannot be empty.")
                continue
            if not pattern.fullmatch(s):
                print("Error: enter a numeric value (digits and optional single decimal point).")
                continue
            try:
                return float(s)
            except ValueError:
                print("Error: invalid number format.")

    person = {
        "first_name": get_name("Enter first name: "),
        "last_name": get_name("Enter last name: "),
        "sex": get_sex("Enter sex (male/female): "),
        "address": get_address("Enter address: "),
        "gross_salary": get_number("Enter gross salary: "),
        "social_deduction": get_number("Enter social deduction: "),
        "expenses": get_number("Enter expenses: "),
    }

    return person


def processConsoleInput():
    # TODO: use requestInput(), calculate tax and print letter
    pass
#commit message:add input validation for console and JSON processingg