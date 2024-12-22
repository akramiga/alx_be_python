task = input("enter task: ").upper()
priority = input("priority choose (high, medium, low): ").lower()
time_bound = input ("is is time bound (yes or no): ").lower()
match priority:
   case "high":
       if time_bound == "yes":
           print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
       else:
           print(f"Reminder: '{task}' is a high priority task that requires attention soon!")


   case "medium":
       if time_bound == "yes":
           print(f"Reminder: '{task}' is a medium priority task that requires  attention !")
       else:
           print(f"Reminder: '{task}' is a medium priority task that requires attention when u have time!")


   case "low":
       # if time_bound == "yes":
       #     print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
       # else:
       print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")

