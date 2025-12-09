# Function to calculate tax based on net salary using a progressive model
def calculate_tax(net_salary):
    # Treat net_salary as taxable income (deductions are computed outside)
    tax_rate = 0
    total_tax = 0
    taxable_income = net_salary
    if taxable_income > 24000:
        tax_rate = 4  # Starting rate
        threshold = 24000  # Initial threshold
        
        while tax_rate < 32 and threshold < taxable_income:
            if taxable_income > threshold:
                total_tax = (taxable_income * tax_rate) / 100
            threshold += 8000
            tax_rate += 2
    return {'tax': total_tax, 'percentage': round(tax_rate, 1)}
