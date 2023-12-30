print("\n========== Course Management Application | Firebase Realtime Database ==========\n")

# Importing the funtion packages.
import add_student as adds
import add_instructor as addi 
import add_course as addc 
import take_course as takec
import teach_course as teachc 
import find_student_courses as fsc
import find_instructor_courses as fic

header = """
----------------------------------- Welcome to -----------------------------------

╔═╗┌─┐┬ ┬┬─┐┌─┐┌─┐  ╔╦╗┌─┐┌┐┌┌─┐┌─┐┌─┐┌┬┐┌─┐┌┐┌┌┬┐  ╔═╗┌─┐┌─┐┬  ┬┌─┐┌─┐┌┬┐┬┌─┐┌┐┌
║  │ ││ │├┬┘└─┐├┤   ║║║├─┤│││├─┤│ ┬├┤ │││├┤ │││ │   ╠═╣├─┘├─┘│  ││  ├─┤ │ ││ ││││
╚═╝└─┘└─┘┴└─└─┘└─┘  ╩ ╩┴ ┴┘└┘┴ ┴└─┘└─┘┴ ┴└─┘┘└┘ ┴   ╩ ╩┴  ┴  ┴─┘┴└─┘┴ ┴ ┴ ┴└─┘┘└┘

                                       using
                           | Firebase Realtime Database |
                                 -- version 1.0.0 --
                                                               
----------------------------------------------------------------------------------
"""
print(header)

def main():
    while True:
        print("\nDatabase Actions: \n1) Add Data \n2) Associate Data \n3) Fetch Data \n")
        try:
            action_inp = input("Please input the Action number that you would like to perform: ")
            action_inp = int(action_inp)
            if action_inp == 1:
                # Add Data
                action_1()
            elif action_inp == 2:
                # Associate Data
                action_2()
            elif action_inp == 3:
                # Fetch Data
                action_3()
            else:
                print("\n========== ERROR ==========\nPlease input the number for one of the 3 options.")
                continue
        except:
            if isinstance(action_inp, str) and action_inp.lower() == "exit":
                print()
                break
            print("\n========== ERROR ==========\nPlease try again and input the number associated with the action you wish to perform.")
            continue

def action_1():
    print("\nAdd Data for entity: \n1) Students \n2) Instructors \n3) Courses \n")
    while True:
        try:
            add_inp = input("\nPlease input the entity number for which the data is to be added: ")
            add_inp = int(add_inp)
            if add_inp == 1:
                # Capturing the Student inputs.
                print("\nAdding the Student data. Please input the following information for Student:")
                student_id = input("Student ID: ")
                student_name = input("Student name: ")
                student_program = input("Student program: ")
                adds.add(student_id, student_name, student_program)
                print("\n========== SUCCESS ==========\nData Successully added for Student ID {}".format(student_id))
            elif add_inp == 2:
                # Capturing the Instructor inputs.
                print("\nAdding the Instructor data. Please input the following information for Instructor:")
                instructor_id = input("Instructor ID: ")
                instructor_name = input("Instructor name: ")
                instructor_department = input("Instructor department: ")
                addi.add(instructor_id, instructor_name, instructor_department)
                print("\n========== SUCCESS ==========\nData Successully added for Instructor ID {}".format(instructor_id))
            elif add_inp == 3:
                # Capturing the Course inputs.
                print("\nAdding the Course data. Please input the following information for Course:")
                course_number = input("Course number: ")
                course_title = input("Course title: ")
                course_semester = input("Course semester: ")
                addc.add(course_number, course_title, course_semester)
                print("\n========== SUCCESS ==========\nData Successully added for Course number {}".format(course_number))
            else:
                print("\n========== ERROR ==========\nPlease input the number for one of the 3 options.")
                continue            
            break
        except:
            if isinstance(add_inp, str) and add_inp.lower() == "exit":
                print()
                return
            print("\n========== ERROR ==========\nPlease try again and input the number associated with the entity you wish to add data for.")
            continue

def action_2():
    print("\nAssociate Data for entity: \n1) Students \n2) Instructors")
    while True:
        try:
            add_inp = input("\nPlease input the entity number for which the data is to be associated: ")
            add_inp = int(add_inp)
            if add_inp == 1:
                # Capturing the Student and Course inputs.
                print("\nAssociating the Student and Course data. Please input the following information:")
                student_id = input("Student ID: ")
                course_number = input("Course Number: ")
                course_semester = input("Course Semester: ")
                if takec.take(student_id, course_number, course_semester):
                    print("\n========== SUCCESS ==========\nData Successully associated for Student ID {} and Course number {}".format(student_id, course_number))
                else:
                    continue
            elif add_inp == 2:
                # Capturing the Instructor and Course inputs.
                print("\nAssociating the Instructor and Course data. Please input the following information:")
                instructor_id = input("Instructor ID: ")
                course_number = input("Course Number: ")
                course_semester = input("Course Semester: ")
                if teachc.teach(instructor_id, course_number, course_semester):
                    print("\n========== SUCCESS ==========\nData Successully associated for Instructor ID {} and Course number {}".format(instructor_id, course_number))
                else:
                    continue
            else:
                print("\n========== ERROR ==========\nPlease input the number for one of the 2 options.")
                continue            
            break
        except:
            if isinstance(add_inp, str) and add_inp.lower() == "exit":
                print()
                return
            print("\n========== ERROR ==========\nPlease try again and input the number associated with the entity you wish to associate data for.")
            continue

def action_3():
    print("\nFetch Data for entity: \n1) Students \n2) Instructors")
    while True:
        try:
            add_inp = input("\nPlease input the entity number for which the data is to be fetched: ")
            add_inp = int(add_inp)
            if add_inp == 1:
                # Capturing the Student inputs.
                print("\nFetching the Student data. Please input the following information:")
                student_id = input("Student ID: ")
                if fsc.fetch(student_id):
                    pass
                else:
                    continue
            elif add_inp == 2:
                # Capturing the Instructor inputs.
                print("\nFetching the Instructor data. Please input the following information:")
                instructor_id = input("Instructor ID: ")
                if fic.fetch(instructor_id):
                    pass
                else:
                    continue
            else:
                print("\n========== ERROR ==========\nPlease input the number for one of the 2 options.")
                continue            
            break
        except:
            if isinstance(add_inp, str) and add_inp.lower() == "exit":
                print()
                return
            print("\n========== ERROR ==========\nPlease try again and input the number associated with the entity you wish to fetch data for.")
            continue
    
if __name__ == "__main__":
    main()