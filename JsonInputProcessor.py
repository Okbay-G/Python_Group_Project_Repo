import json
import TaxPrinter
import TaxCalculator
import re
import os

#file_path = 'D:/Desktop/LocalRepo/Python_Group_Project_Repo/Python_Code/tax_data.json'

def validate_input(person):
    """Validate a person record for required fields and correct data types.

    This function checks that a person dictionary contains all required fields
    with valid values. It validates that name fields contain only alphabetic
    characters, spaces, hyphens, and apostrophes. It also ensures that numeric
    fields contain valid numbers and that gross_salary is non-negative.
    Args:
        person (dict): A dictionary containing person data with the following keys:
            - first_name (str): The person's first name
            - last_name (str): The person's last name
            - sex (str): The person's sex
            - address (str): The person's address
            - gross_salary (float): The person's gross salary (must be non-negative)
            - social_deduction (float): The person's social deduction amount
            - expenses (float): The person's expenses amount
    Returns:
        bool: True if the person record is valid, False otherwise.
    Side Effects:
        Prints error messages to stdout for each validation failure encountered.
    """
    required_fields = ['first_name', 'last_name', 'sex', 'address', 'gross_salary', 'social_deduction', 'expenses']
    name_pattern = re.compile(r"^[A-Za-z\s'\-]+$")
    numeric_fields = ['gross_salary', 'social_deduction', 'expenses']
    
    for field in required_fields:
        if field not in person or person[field] is None or (isinstance(person[field], str) and person[field].strip() == ""):
            print(f"Error: Missing or invalid value for {field} in record: {person}")
            return False
        elif not name_pattern.match(str(person['first_name'])):
            print(f"Error: Invalid first_name (contains special characters or digits): {person['first_name']}")
            return False
        elif not name_pattern.match(str(person['last_name'])):
            print(f"Error: Invalid last_name (contains special characters or digits): {person['last_name']}")
            return False
        else:
            for nf in numeric_fields:
                try:
                    val = float(person[nf])
                except (TypeError, ValueError):
                    print(f"Error: {nf} must be a number in record: {person}")
                    return False
                
                if nf == 'gross_salary' and val < 0:
                    print(f"Error: gross_salary must be non-negative in record: {person}")
                    return False
                else:
                    return True

# Prompts user for a valid JSON file path and returns it after validation
def get_file_path():
    while True:
        path = input("Enter path to JSON file: ").strip().strip('"').strip("'")
        if not path:
            print("No path entered. Please provide a path to a .json file.")
            continue
        if not path.lower().endswith('.json'):
            print("The file must have a .json extension. Please try again.")
            continue
        if not os.path.exists(path):
            print(f"File not found: {path}. Please provide a valid file path.")
            continue
        if not os.path.isfile(path):
            print(f"Path is not a file: {path}. Please provide a valid file path.")
            continue
        return path

# Reads and parses a JSON file, handling errors gracefully
def load_json_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File not found: {path}. Please try again.")
    except PermissionError:
        print(f"Permission denied when opening: {path}. Choose another file or adjust permissions.")
    except json.JSONDecodeError as e:
        print(f"Invalid JSON in file: {path}. Error: {e}. Please provide a valid JSON file.")
    except OSError as e:
        print(f"Error opening file: {e}. Please try again.")
    return None

# Processes a single person record by extracting data, validating it, and generating tax letter
def process_person(person):
    try:
        first_name = str(person.get('first_name', '')).strip().capitalize()
        last_name = str(person.get('last_name', '')).strip().capitalize()
        sex = person.get('sex', '')
        address = person.get('address', '')
        gross_salary = float(person.get('gross_salary', 0))
        social_deduction = float(person.get('social_duction', 0))
        expenses = float(person.get('expenses', 0))
    except Exception as e:
        print(f"Skipping record due to read/convert error: {e}. Record: {person}")
        return

    if validate_input(person):
        try:
            total_deductions = social_deduction + expenses
            net_salary = gross_salary - total_deductions
            tax_info = TaxCalculator.calculate_tax(net_salary)
            TaxPrinter.create_tax_letter(
                first_name,
                last_name,
                sex,
                address,
                gross_salary,
                total_deductions,
                net_salary,
                tax_info.get('percentage'),
                tax_info.get('tax')
            )
        except Exception as e:
            print(f"Error processing record for {first_name} {last_name}: {e}")

# Main entry point that loads JSON file and processes all person records
def processJSON():
    path = get_file_path()
    data = load_json_file(path)
    if data is None or not isinstance(data, list):
        print(f"Expected a JSON array of person records, but root is {type(data).__name__}. Please provide a JSON array.")
        return

    for person in data:
        process_person(person)
