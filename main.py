# Function:     This program determines if a date entered by the user is valid.  
# Input:        Interactive
# Output:       Valid date is printed or user is alerted that an invalid date was entered.

validDate = True
MIN_YEAR = 0
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1
MAX_DAY = 31

year = input('Please enter the year: ')
month = input('Please enter the month: ')
day = input('Please enter the day: ')

print(int(year) % 4)
# Get the year, then the month, then the day
# housekeeping()
def DetermineIfInvalidMonthBasedOnDays(month):
    days_of_the_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    # check for leap year
    if ((int(year) % 4) == 0):
        days_of_the_month[1] = 29

    return days_of_the_month[int(month)-1]

# Check to be sure date is valid
MAX_DAY = DetermineIfInvalidMonthBasedOnDays(month)

if int(year) <= MIN_YEAR: # invalid year
    validDate = False
elif int(month) < MIN_MONTH or int(month) > MAX_MONTH: # invalid month
    validDate = False
elif int(day) < MIN_DAY or int(day) > MAX_DAY: # invalid day
    validDate = False

# Test to see if date is valid and output date and whether it is valid or not

# endOfJob()
if validDate == True:
    # Output statement
    print(f'{month}/{day}/{year} is a valid date')
else:
    # Output statement
     print(f'{month}/{day}/{year} is an invalid date')
