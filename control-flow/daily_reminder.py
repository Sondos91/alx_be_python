# daily_reminder.py

# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Process the Task Based on Priority and Time Sensitivity
match priority:
    case "high":
        print(f"Reminder: High priority task: {task}")
    case "medium":
        print(f"Reminder: Medium priority task: {task}")
    case "low":
        print(f"Note: Low priority task: {task}")
    case _:
        print(f"Unknown priority task: {task}")

if time_bound== "yes":
    print(" that requires immediate attention today!")