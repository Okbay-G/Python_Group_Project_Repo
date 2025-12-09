from TaxPrinter import create_tax_letter
from TaxCalculator import calculate_tax
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

# Main function to process console input
def processConsoleInput():
    print("Welcome to Tax Data Processor")
    
    while True:
        person = requestInput()
        formatted_name = format_name(person['first_name'], person['last_name'])
        sex = format_sex(person['sex'])
        address = person['address'] 
        gross_salary = person['gross_salary']
        social_deduction = person['social_deduction']
        expenses = person['expenses']

        net_salary, total_deductions = calculate_financials(gross_salary, social_deduction, expenses)
        tax_info = calculate_tax(net_salary)
        create_tax_letter(formatted_name['first_name'], formatted_name['last_name'], sex, address,
                          gross_salary, total_deductions, net_salary,
                          tax_info['percentage'], tax_info['tax'])

        if not continue_prompt():
            print("Thank you. Exiting.")
            return

def format_name(first_name, last_name):
    return {
        "first_name": first_name[0].upper() + first_name[1:].lower(),
        "last_name": last_name[0].upper() + last_name[1:].lower()
    }

def format_sex(sex):
    return sex[0].upper()  # Take first letter and uppercase it

def calculate_financials(gross_salary, social_deduction, expenses):
    total_deductions = social_deduction + expenses
    net_salary = gross_salary - total_deductions
    return net_salary, total_deductions

def continue_prompt():
    while True:
        cont = input("Do you want to add another record? (y/n): ").strip().lower()
        if cont in ('y', 'yes'):
            return True  # continue outer loop to add another record
        if cont in ('n', 'no'):
            return False
        print("Please enter 'y' or 'n'.")

