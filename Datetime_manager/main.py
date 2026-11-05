import datetime_utils as dtu

while True:
    print("=================================")
    print("\tDATE-TIME MANAGER")
    print("=================================")

    print("1. Show Current Date & Time")
    print("2. Date Formatter")
    print("3. Age Calculator")
    print("4. Days Between Two Dates")
    print("5. Future Date Calculator")
    print("6. Deadline Countdown")
    print("7. Exit")

    print("=================================")

    try:
        user_input = int(input("Enter your choice: "))
        match user_input:

            case 1:
                dtu.show_current_dateTime()

            case 2:
                input_date = input("Enter date (DD-MM-YYYY): ")

                dtu.format_dates(input_date) if dtu.verify_date(input_date) else print("\nInvalid date or Invalid input\n")

                
            case 3:
                dob = input("Enter Date of Birth (DD-MM-YYYY): ")

                dtu.calculate_age(dob) if dtu.verify_date(dob) else print("\nInvalid date or Invalid input\n")

            case 4:
                first_date = input("Enter first date: ")
                second_date = input("Enter second date: ")

                if dtu.verify_date(first_date) and dtu.verify_date(second_date):
                    dtu.days_between(first_date,second_date) 
                
                else: 
                    print("\nInvalid date or Invalid input\n")

            case 5:
                print("Enter number of days: ")

                print("1. Add days")
                print("2. Subtract days\n")
                
                choice = int(input("Choice: "))

                input_date = input("Enter date (DD-MM-YYYY): ")
                number_of_days = int(input("Enter number of days: "))

                dtu.future_date_calculator(choice,input_date,number_of_days) if dtu.verify_date(input_date) else print("\nInvalid date or Invalid input\n")
                
            
            case 6:
                deadline = input("Enter deadline (DD-MM-YYYY): ")
                dtu.deadline_countdown(deadline) if dtu.verify_date(deadline) else print("\nInvalid date or Invalid input\n")

            case 7:
                print("\nThank you for using Datetime Manager!\n")
                break
                
            case _:
                print("\nInvalid choice. Try again.\n")

    
    except ValueError:
        print("Invalid input")