def calculate_tax(net_salary):
    """Calculate income tax based on progressive tax brackets.

    This function computes the total tax owed on a given net salary using a
    progressive tax rate system. Tax rates increase in 2% increments for every
    8000 units of taxable income above the initial 24000 threshold, up to a
    maximum rate of 32%.
    Args:
        net_salary: The net salary amount to calculate tax on (numeric value).
    Returns:
        A dictionary containing:
            - 'tax': The calculated total tax amount.
            - 'percentage': The final tax rate percentage applied (rounded to 1 decimal place).
    Note:
        - No tax is calculated if net_salary is 24000 or less.
        - The function assumes net_salary represents taxable income with
          deductions already applied.
    """
    tax_rate = 0
    total_tax = 0
    taxable_income = net_salary
    
    if taxable_income > 24000:
        tax_rate = 4
        threshold = 24000
        applied_rate = tax_rate  # track the real applied rate

        while tax_rate < 32 and threshold < taxable_income:
            if taxable_income > threshold:
                applied_rate = tax_rate  # store rate used in calculation
                total_tax = (taxable_income * tax_rate) / 100
            threshold += 8000
            tax_rate += 2

        return {'tax': total_tax, 'percentage': round(applied_rate, 1)}

    return {'tax': 0, 'percentage': 0}
