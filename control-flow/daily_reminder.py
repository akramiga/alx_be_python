task = input("Enter your task: ").upper()
priority = input("Priority (high/medium/low): ").lower()
time_bound = input ("Is is time bound? (yes/no): ").lower()
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
