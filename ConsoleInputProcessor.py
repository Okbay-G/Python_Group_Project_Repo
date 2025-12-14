"""Console input processor for tax information collection and processing.

This module handles user input validation, data collection, and coordination
with tax calculation and letter generation modules.
"""

from TaxPrinter import create_tax_letter
from TaxCalculator import calculate_tax
import re


def requestInput():
    """Collect and validate tax information from user input.
    
    Prompts user for personal and financial information with validation
    for each field according to specific format requirements.
    
    Returns:
        dict: Dictionary containing validated user information with keys:
            first_name, last_name, sex, address, gross_salary,
            social_deduction, expenses.
    """

    print("=== Enter Tax Information ===")

    def get_name(prompt):
        """Validate and return a name input.
        
        Allows Unicode letters (including accented characters), spaces,
        apostrophes, and hyphens. Rejects digits and special characters.
        """
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
        """Validate and return a Swiss address in format: Street Number Zipcode City."""
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
        """Validate and return sex as 'male' or 'female'.
        
        Accepts variations: male, female, m, f, man, woman.
        Normalizes man/woman to male/female.
        """
        valid = {"male", "female", "m", "f", "man", "woman"}
        while True:
            val = input(prompt).strip().lower()
            if val not in valid:
                print(f"Error: enter one of: male, female, man, woman, m, f.")
                continue
            if val == "man":
                return "male"
            elif val == "woman":
                return "female"
            return val

    def get_number(prompt):
        """Validate and return a non-negative decimal number."""
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
    """Process tax information in a loop until user exits.
    
    Collects user input, calculates financials and taxes, generates
    tax letters, and prompts for additional records.
    """
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
    """Format name with proper capitalization.
    
    Args:
        first_name: First name string.
        last_name: Last name string.
    
    Returns:
        dict: Dictionary with capitalized first_name and last_name.
    """
    return {
        "first_name": first_name[0].upper() + first_name[1:].lower(),
        "last_name": last_name[0].upper() + last_name[1:].lower()
    }


def format_sex(sex):
    """Return uppercase first letter of sex designation."""
    return sex[0].upper()


def calculate_financials(gross_salary, social_deduction, expenses):
    """Calculate net salary and total deductions.
    
    Args:
        gross_salary: Gross salary amount.
        social_deduction: Social security deduction amount.
        expenses: Expenses amount.
    
    Returns:
        tuple: (net_salary, total_deductions)
    """
    total_deductions = social_deduction + expenses
    net_salary = gross_salary - total_deductions
    return net_salary, total_deductions


def continue_prompt():
    """Prompt user whether to process another record.
    
    Returns:
        bool: True to continue, False to exit.
    """
    while True:
        cont = input("Do you want to add another record? (y/n): ").strip().lower()
        if cont in ('y', 'yes'):
            return True
        if cont in ('n', 'no'):
            return False
        print("Please enter 'y' or 'n'.")

