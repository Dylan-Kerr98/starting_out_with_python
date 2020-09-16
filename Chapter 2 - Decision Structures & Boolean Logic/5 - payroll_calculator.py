# This program calculates the payroll for workers included overtime

# Named constants
BASE_HOURS = 40        # Base hours worked per week
OT_MULTIPLIER = 1.5    # Overtime multiplier

# Get the hours worked and hourly rate
hours = float(input("Enter the number of hours worked: "))
pay_rate = float(input("Enter the hourly pay rate: "))

# Calculate and display gross pay
if hours > BASE_HOURS:
    # Calculate the gross pay with overtime
    overtime_hours = hours - BASE_HOURS

    # Calculate the amount of overtime pay
    overtime_pay = overtime_hours * pay_rate * OT_MULTIPLIER

    # Calculate gross pay
    gross_pay = BASE_HOURS * pay_rate + overtime_pay
else:
    gross_pay = BASE_HOURS * pay_rate
# Display the gross pay
print("The gross pay is £", format(gross_pay, ',.2f'), sep='')
