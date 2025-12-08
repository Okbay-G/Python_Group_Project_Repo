import json
import TaxPrinter
import TaxCalculator
import re
import os

# Validates that a person record contains all required fields with valid formats and values
def validate_input(person):
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


def process_person(person):
    # TODO: validate record, calculate tax and create letter
    pass

# Main entry point that loads JSON file and processes all person records
def processJSON():
    # TODO: load JSON file and process all person records
    pass

