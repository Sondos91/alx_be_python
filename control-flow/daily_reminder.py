# daily_reminder.py

# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Process the Task Based on Priority and Time Sensitivity
match priority:
    case "high":
        reminder = f"Reminder: High priority task: {task}"
    case "medium":
        reminder = f"Reminder: Medium priority task: {task}"
    case "low":
        reminder = f"Note: Low priority task: {task}"
    case _:
        reminder = f"Unknown priority task: {task}"

if time_bound== "yes":
    reminder += " that requires immediate attention today!"

# Provide a Customized Reminder
print(reminder)