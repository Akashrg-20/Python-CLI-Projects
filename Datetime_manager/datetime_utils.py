from datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta

def verify_date(data):
    try:
        datetime.strptime(data, "%d-%m-%Y")
        return True

    except ValueError:
        return False
    


def show_current_dateTime():
    current = datetime.today()
    print("\n",current.strftime("%d-%m-%Y %I:%M %p"),"\n")


def format_dates(input_date):

    input_date = datetime.strptime(input_date,"%d-%m-%Y")

    format1 = input_date.strftime("%d-%m-%Y")
    format2 = input_date.strftime("%Y-%m-%d")
    format3 = input_date.strftime("%m-%d-%Y")

    
    print("\nFormat 1 (DD-MM-YYYY) : ",format1)
    print("Format 2 (YYYY-MM-DD) : ",format2)
    print("Format 3 (MM-DD-YYYY) : ",format3,"\n")


# dob : Date of Birth

def calculate_age(dob):

    today = datetime.today().date()
    dob = datetime.strptime(dob,"%d-%m-%Y").date()

    if dob > today:
        print("\nDate of birth cannot be in the future!\n")
        return

    diff = relativedelta(today,dob)

    print(f"\nYour age is: {diff.years}")
    print(f"You're {diff.years} years, {diff.months} months, {diff.days} days old\n")


def days_between(first_date,second_date):
    first_date = datetime.strptime(first_date,"%d-%m-%Y").date()
    second_date = datetime.strptime(second_date,"%d-%m-%Y").date()

    print("\nDifference: ",(second_date - first_date).days," days")
    print("\n")


def future_date_calculator(choice,input_date,number_of_days):
    if number_of_days < 0:
        print("\nPlease enter a positive number of days\n")
        return

    future_date = None
    input_date = datetime.strptime(input_date,"%d-%m-%Y").date()

    if choice not in (1, 2):
        print("Invalid choice")
        return


    if choice == 1:
        future_date = input_date + timedelta(number_of_days)
        print("\nCalculated Date: ",future_date.strftime("%d-%m-%Y"))

    else:
        future_date=input_date - timedelta(number_of_days)
        print("\nCalculated Date: ",future_date.strftime("%d-%m-%Y"))


    print("\n")


    
def deadline_countdown(deadline):
    today = datetime.today().date()
    deadline = datetime.strptime(deadline,"%d-%m-%Y").date()


    if today < deadline:
        print("\nRemaining days: ",(deadline-today).days,"\n")

    elif today == deadline:
        print("\nDeadline is today!\n")
    
    else:
        print("\nDeadline expired\n")


