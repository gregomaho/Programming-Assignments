# Author: Gregory Mahoy
# File Name: deans_list_honor_roll.py
# Description: Application that will check a student's GPA and determine if they made the Dean's List or Honor Roll.

print("Welcome to the GPA Checker!")

while True:
    # Get student's last name (exit if 'ZZZ')
    last_name = input("Enter student's last name (or 'ZZZ' to quit): ")
    if last_name.strip().upper() == 'ZZZ':
        print("Done checking GPAs. See you next time!")
        break

    # Get student's first name
    first_name = input("Enter student's first name: ")

    # Get GPA and make sure it's a valid number
    try:
        gpa = float(input("Enter GPA: "))
    except ValueError:
        print("Oops! That wasn't a number. Try again.\n")
        continue

    # Evaluate GPA status
    if gpa >= 3.5:
        print(f"🎉 {first_name} {last_name} made the Dean's List!\n")
    elif gpa >= 3.25:
        print(f"👏 {first_name} {last_name} made the Honor Roll!\n")
    else:
        print(f"{first_name} {last_name} did not qualify this time. Keep trying!\n")
