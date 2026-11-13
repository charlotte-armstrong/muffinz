#create gradebook dictionary
from operator import sub
import csv

dict = { }
filepath = "gradebook.csv"

##READ FROM CSV
try:
    with open(filepath, 'r') as file:
        data = csv.reader(file)

    for row in data:
        if row:
            key = row[0]
            values = row[1:]
            dict[key] = values
    print(dict)
except FileNotFoundError:
    print("File Not Found")

##WRITE TO CSV
try:
    with open(filepath, 'w', newline="") as file:
        writer = csv.writer(file)

        for key, value in data.items():
            writer.writerow([key] + value)
except FileNotFoundError:
    print("File Not Found")


gradebook = {
    "Math": [67,68,69,70],
    "Science": [75,84,90,79],
    "English": [96,98,99,100],
    "History": [88,85,91,87],
    "Art": [100,99,95,100],
    "Sex Ed": [50, 45, 32, 64]
}

#add grade to dictionary
def add_grade(subject, grade):
    if subject in gradebook:
        gradebook[subject].append(grade)
    else:
        gradebook[subject] = [grade]

def print_average(subject):
    subject = subject.capitalize()
    if subject in gradebook:
        average = sum(gradebook[subject]) / len(gradebook[subject])
        print("Your average for " + subject + " is " + str(average) + "%")
    else:
        print("No grades recorded for " + subject + ".")

def print_grades(subject):
    subject = subject.capitalize()
    if subject in gradebook:
        print("In " + subject + ", you scored " + str(gradebook[subject]) + ".")
    else:
        print("No grades recorded for " + subject + ".")

def print_all_averages():

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
        print(subject + ": " + average + "%")

    print("\nYour best average is " + str(best_avg) + "%, in " + best_subject)
    print("Your worst average is " + str(worst_avg) + "%, in " + worst_subject + "\n")

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
    print('''
OPTIONS:

    1. Print out classes and averages
    2. Print grades for specific class
    3. Pring cumulative GPA
    4. Add a grade for a class
    ''')

    choice = input("Enter your choice: ")

    #translates user input to corresponding function
    if choice == "1":
        print_all_averages()
    elif choice == "2":
        subject = input("Enter the subject: ")
        print_grades(subject)
    elif choice == "3":
        print("Your cumulative GPA out of 4.0 is " + str(get_GPA()))
    elif choice == "4":
        subject = input("Enter subject: ")
        grade = int(input("Enter grade: "))
        add_grade(subject, grade)
    else:
        print("Invalid Input. Try again.")

#main loop
if __name__ == "__main__":
    menu()