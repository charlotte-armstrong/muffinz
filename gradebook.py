#create gradebook dictionary
import csv
import subprocess

def clear_console():
    command = 'clear'
    subprocess.run(command, shell=True)

gradebook = { }

gradebook_file = "/Users/carmstrong/Documents/data-science/muffinz/gradebook.csv"

#read from csv
def read_from_csv():
    try:
        with open(gradebook_file, 'r') as file:
            data = csv.reader(file)
            for row in data:
                if row:
                    subject = row[0].title()
                    grades = row[1:]
                    gradebook[subject] = [int(grade) for grade in grades]
    except FileNotFoundError:
        menu(">>> File " + gradebook_file + " Not Found.")

#write to csv
def write_to_csv():
    try:
        with open(gradebook_file, 'w', newline="") as file:
            writer = csv.writer(file)
            for key, value in gradebook.items():
                writer.writerow([key.title()] + value)
    except FileNotFoundError:
        menu(">>> File " + gradebook_file + " Not Found.")

#print all averages
def print_all_averages():
    header()

    #tracks best and worst averages
    best_avg = 0
    best_subject = ""
    worst_avg = 100
    worst_subject = ""

    print("AVERAGES: \n")

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
        print(subject.title() + ": " + average + "%")

    print("\nYour best average is " + str(best_avg) + "%, in " + best_subject.title() + ".\nYour worst average is " + str(worst_avg) + "%, in " + worst_subject.title() + ".")
    nav_options()

#print grades for a subject
def print_grades(subject):
    subject = subject.title()
    if subject in gradebook:
        menu(">>> In " + subject + ", you scored " + ", ".join(map(str, gradebook[subject])) + ".")
    else:
        menu("No grades recorded for " + subject + ".")

#get cumulative GPA
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

#add grade to dictionary
def add_grade(subject):
    subject = subject.title()
    if subject in gradebook:
        grade = int_input(subject + " currently contains " + ", ".join(map(str, gradebook[subject])) + ". Enter new grade: ")
        gradebook[subject].append(grade)
        menu(">>> Successfully added a " + str(grade) + " in " + subject + ".\n>>> " + subject + " now contains " + ", ".join(map(str, gradebook[subject])) + ".")
    else:
        choice = smart_input("Add grade for new subject '" + subject + "'? (Y/n)")
        if choice.lower() == "y":
            grade = int_input("Enter grade: ")
            gradebook[subject] = [grade]
            menu(">>> Successfully added a " + str(grade) + " in " + subject + ".\n>>> " + subject + " now contains " + ", ".join(map(str, gradebook[subject])) + ".")
        else:
            menu(">>> No grade added.")

#remove grade from dictionary
def remove_grade(subject):
    subject = subject.title()
    if subject in gradebook:
        grade = int_input("Enter grade to remove from " + subject + " (Options: " + ", ".join(map(str, gradebook[subject])) + "): ")
        if grade in gradebook[subject]:
            gradebook[subject].remove(grade)
            menu(">>> Successfully removed a " + str(grade) + " from " + subject + ".\n>>> " + subject + " now contains " + ", ".join(map(str, gradebook[subject])) + ".")
        else:
            menu(">>> Grade not found in " + subject + ".")
    else:
        menu(">>> No grades recorded for " + subject + ".")

def visualize_grades():
    header()
    print("LEADERBOARD:\n")
    print("0." + "."*23 + "25" + "."*23 + "50" + "."*23 + "75" + "."*23 + "100")
    noodle = ""
    for subject in gradebook:
        average = round((sum(gradebook[subject])/len(gradebook[subject])))
        centerstring = ("\n| " + str(subject))
        noodle += ("\n" + "-"*(average-1) + ".")
        noodle += (centerstring + " "*len("-"*(average-len(centerstring))) + " )")
        noodle += ("\n" + "-"*(average-1) + "`")
    print(noodle)
    print("\n" + "."*103)
    nav_options()

#main menu and navigation center
def menu(message=">>>"):
    #prints menu
    header()
    print('''OPTIONS:

1. Print out classes and averages
2. Print grades for specific class
3. Print cumulative GPA
4. Add a grade for a class
5. Remove a grade from a class
6. Visualize grades
7. Exit
''')

    print(message)
    choice = int_input("\nEnter menu selection: ")

    #translates user input to corresponding function
    if choice == 1:
        print_all_averages()
    elif choice == 2:
        print("\n>>> PRINTING GRADES <<<\n")
        subject = smart_input("Enter subject (Options: " + ", ".join(gradebook.keys()) + "): ")
        print_grades(subject)
    elif choice == 3:
        menu(">>> Your cumulative GPA out of 4.0 is " + str(get_GPA()))
    elif choice == 4:
        print("\n>>> ADDING GRADE <<<\n")
        subject = smart_input("Enter subject (Options: " + ", ".join(gradebook.keys()) + "): ")
        add_grade(subject)
    elif choice == 5:
        print("\n>>> REMOVING GRADE <<<\n")
        subject = smart_input("Enter subject (Options: " + ", ".join(gradebook.keys()) + "): ")
        remove_grade(subject)
    elif choice == 6:
        visualize_grades()
    elif choice == 7:
        exit_program()
    else:
        menu(">>> Invalid Input. Try again.")

def header():
    clear_console()
    print('''
  ________  ___   ___  _______  ____  ____  __ __
 / ___/ _ \\/ _ | / _ \\/ __/ _ )/ __ \\/ __ \\/ //_/
/ (_ / , _/ __ |/ // / _// _  / /_/ / /_/ / ,<   
\\___/_/|_/_/ |_/____/___/____/\\____/\\____/_/|_|
------------------------------------------------
''')

#option to return to main menu or exit program after executing an option
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
        header()
        print("\n>>> Invalid Input. Try again.\n")
        nav_options()

#exits program
def exit_program():
    clear_console()
    print("\n>>> Exited program.\n")
    write_to_csv()
    return None

#handles invalid input
def smart_input(prompt):
    while True:
        try:
            return input(prompt)
        except (SyntaxError, ValueError, KeyboardInterrupt, EOFError, OSError, TypeError, ArithmeticError):
            print("\n>>> Invalid Input. Try again.\n")
            continue

#handles invalid input for inputs meant to be integers
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
