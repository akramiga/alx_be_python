from datetime import datetime 
def display_current_datetime():
    current_date = datetime.datetime.now()
    current_date_str= current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date_str}")
    return current_date
current_date = display_current_datetime()  
number_of_days = int(input("Enter the number of days to add to the current date: "))  
def calculate_future_date(current_date, number_of_days):
    future_date = current_date + datetime.timedelta(days = number_of_days)
    ans = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {ans}" )
calculate_future_date(current_date, number_of_days)    