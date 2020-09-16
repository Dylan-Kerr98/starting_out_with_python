# To test more than one condition, a decision structure can be nested inside another decision structure.

#  For example, consider a program that determines whether a bank customer qualifies for a loan. To qualify, two
# conditions must exist:

# (1) - The customer must earn at lean £30,000 per year
# (2) - The customer must have been employed for at least two years

# This program determines whether a bank customer qualifies for a loan

MIN_SALARY = 30000.00   # The minimum annual salary required
MIN_YEARS = 2            # The minimum amount of years at current job

# Get the customer's annual salary
salary = float(input("Please enter your total annual salary: "))

if salary >= MIN_SALARY:
    # Get the customers time at current job
    years_on_job = int(input("Enter the number of years employed "
                             "at current job: "))
    if years_on_job >= MIN_YEARS:
        print("You qualify for the loan.")

    else:
        print("You must have been employed "
              "for at least", MIN_YEARS,
              "years to qualify")
else:
    print("You must earn at least £",
          format(MIN_SALARY, '.2f')," per year to qualify.", sep='')
