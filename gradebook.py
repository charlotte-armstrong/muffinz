#create gradebook dictionary
import csv
import subprocess

def clear_console():
    command = 'clear'
    subprocess.run(command, shell=True)

clear_console()

gradebook = { }

gradebook_file = "/Users/carmstrong/Documents/data-science/muffinz/gradebook.csv"

##read from csv
def read_from_csv():
    try:
        with open(gradebook_file, 'r') as file:
            data = csv.reader(file)
            for row in data:
                if row:
                    subject = row[0].capitalize()
                    grades = row[1:]
                    gradebook[subject] = [int(grade) for grade in grades]
    except FileNotFoundError:
        print("\n>>> File " + gradebook_file + " Not Found.\n")

##write to csv
def write_to_csv():
    try:
        with open(gradebook_file, 'w', newline="") as file:
            writer = csv.writer(file)
            for key, value in gradebook.items():
                writer.writerow([key.capitalize()] + value)
    except FileNotFoundError:
        print("\n>>> File " + gradebook_file + " Not Found.\n")

#add grade to dictionary
def add_grade(subject):
    subject = subject.capitalize()
    if subject in gradebook:
        grade = int_input(subject + " currently contains " + str(gradebook[subject]) + ". Enter new grade: ")
        gradebook[subject].append(grade)
        print("\n>>> Successfully added a " + str(grade) + " in " + subject + ".\n>>> " + subject + " now contains " + str(gradebook[subject]) + ".\n")
        nav_options()
    else:
        choice = smart_input("Add grade for new subject '" + subject + "'? (Y/n)")
        if choice.lower() == "y":
            grade = int_input("Enter grade: ")
            gradebook[subject] = [grade]
            print("\n>>> Successfully added a " + str(grade) + " in " + subject + ".\n>>> " + subject + " now contains " + str(gradebook[subject]) + ".\n")
            nav_options()
        else:
            nav_options()

def remove_grade(subject):
    subject = subject.capitalize()
    if subject in gradebook:
        grade = int(int_input("Enter grade to remove from " + str(gradebook[subject]) + " (Options: " + gradebook[subject] + "): "))
        if grade in gradebook[subject]:
            gradebook[subject].remove(grade)
            print("\n>>> Successfully removed a " + str(grade) + " from " + subject + ".\n")
            print(">>> " + subject + " now contains " + str(gradebook[subject]) + ".")
        else:
            print("\n>>> Grade not found in " + subject + ".\n")
    else:
        print("No grades recorded for " + subject + ".\n")
    nav_options()

def print_average(subject):
    clear_console()
    subject = subject.capitalize()
    if subject in gradebook:
        average = sum(gradebook[subject]) / len(gradebook[subject])
        print("Your average for " + subject + " is " + str(average) + "%")
        nav_options()   
    else:
        print("No grades recorded for " + subject + ".")
        nav_options()

def print_grades(subject):
    clear_console()
    subject = subject.capitalize()
    if subject in gradebook:
        print("In " + subject + ", you scored " + str(gradebook[subject]) + ".")
        nav_options()
    else:
        print("No grades recorded for " + subject + ".")
        nav_options()

def print_all_averages():
    clear_console()

    #tracks best and worst averages
    best_avg = 0
    best_subject = ""
    worst_avg = 100
    worst_subject = ""

    print("\nAVERAGES: \n")

    for subject in gradebook:
        #calculate avg
        average = str(sum(gradebook[subject]) / len(gradebook[subject]))

        #find best and worst avg
        if float(average) > best_avg:
            best_avg = float(average)
            best_subject = subject
        if float(average) < worst_avg:
            worst_avg = float(average)
            worst_subject = subject

        #print avg for each subject 
        print(subject.capitalize() + ": " + average + "%")

    print("\nYour best average is " + str(best_avg) + "%, in " + best_subject.capitalize() + ".")
    print("Your worst average is " + str(worst_avg) + "%, in " + worst_subject.capitalize() + ".")

    nav_options()

def get_GPA():
    #store averages for each subject, used to calculate gross GPA
    averages = []
    
    for subject in gradebook:
        average = str(sum(gradebook[subject]) / len(gradebook[subject]))
        averages.append(float(average))
    
    percentGPA = sum(averages) / len(averages)

    #convert percent GPA to four-point scale
    fourpointGPA = float((percentGPA / 100) * 4.0)
    return fourpointGPA

def menu():
    #prints menu
    clear_console()
    print('''
OPTIONS:

1. Print out classes and averages
2. Print grades for specific class
3. Print cumulative GPA
4. Add a grade for a class
5. Remove a grade from a class
6. Exit
''')

    choice = int_input("Enter your choice: ")

    #translates user input to corresponding function
    if choice == 1:
        print_all_averages()
    elif choice == 2:
        subject = smart_input("Enter subject (Options: " + ", ".join(gradebook.keys()) + "): ")
        print_grades(subject)
    elif choice == 3:
        clear_console()
        print("Your cumulative GPA out of 4.0 is " + str(get_GPA()))
        nav_options()
    elif choice == 4:
        subject = smart_input("Enter subject (Options: " + ", ".join(gradebook.keys()) + "): ")
        add_grade(subject)
    elif choice == 5:
        subject = smart_input("Enter subject (Options: " + ", ".join(gradebook.keys()) + "): ")
        remove_grade(subject)
    elif choice == 6:
        exit_program()
    else:
        clear_console()
        print("\n>>> Invalid Input. Try again.\n")
        menu()

def nav_options():
    choice = int_input('''
1. Return to main menu
2. Exit program

Enter your choice: ''')
    if choice == 1:
        menu()
    elif choice == 2:
        exit_program()
    else:
        clear_console()
        print("\n>>> Invalid Input. Try again.\n")
        nav_options()

def exit_program():
    clear_console()
    print("\n>>> Exited program.\n")
    write_to_csv()
    return None

def smart_input(prompt):
    while True:
        try:
            return input(prompt)
        except (SyntaxError, ValueError, KeyboardInterrupt, EOFError, OSError, TypeError, ArithmeticError):
            print("\n>>> Invalid Input. Try again.\n")
            continue

def int_input(prompt):
    while True:
        try:
            return int(smart_input(prompt))
        except ValueError:
            print("\n>>> Input must be an integer. Try again.\n")
            continue

#main loop
if __name__ == "__main__":
    read_from_csv()
    while True:
        if menu() is None:
            break
