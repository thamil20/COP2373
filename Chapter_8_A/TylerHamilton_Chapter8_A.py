import os
import csv

def get_info():
    num_students = int(input("How many students' grades need storing? "))
    student_grades = []
    if type(num_students) == int:
        for i in range(num_students):
            names = input(f"Please enter student number {i + 1}'s first and last name (as strings): ").split(sep=' ')
            scores = input("Please enter each student's scores for exams 1, 2, and 3 (as integers), "
                            "separate the values with commas followed by spaces: ").split(sep=', ')
            
            student_grades.append({"First Name": names[0], "Last Name": names[1],
                                   "Exam 1": scores[0], "Exam 2": scores[1], "Exam 3": scores[2]})
        
        return student_grades
    
    
def store_grades():    
    fields = ['First Name','Last Name','Exam 1','Exam 2','Exam 3']
    
    if not os.path.isfile('grades.csv'):
        student_grades = get_info()
        
        with open('grades.csv', 'w') as grades:
            writer = csv.DictWriter(grades, lineterminator='\n',  fieldnames=fields)
            writer.writeheader()
            writer.writerows(student_grades)
        
    else:
        print("File already exists.")
        append_grades()

        

def append_grades():
    student_grades = get_info()
    
    fields = ['First Name','Last Name','Exam 1','Exam 2','Exam 3']
    
    with open('grades.csv', 'a') as grades:
        writer = csv.DictWriter(grades, fieldnames=fields)
        writer.writerows(student_grades)
        
def read_grades():
    try:
        with open("grades.csv", 'r') as grades:
            reader = csv.reader(grades)
            
            header = next(reader, None)          
              
            if header:
                print(' | '.join(header))
            else:
                store_grades()
            
            for row in reader:
                print(' | '.join(row))
    
    except FileNotFoundError:
        print("File not found, please input the necessary data.")
        store_grades()



if __name__ == "__main__":
    if not os.path.isfile('grades.csv'):
        store_grades()

    read_grades()