from greeting import greet
from end_greeting import end
import re
from email_verification_student import verify_student_email
import logging
import checktime
logging.basicConfig(level=logging.DEBUG,
                    filename="smslog.log",
                    filemode="a",
                    format="%(asctime)s : %(levelname)s - %(message)s")
colleges = []
class Person:
    def __init__(self,rollno,name,mobile,email,dob):
        self.rollno = rollno
        self.name = name
        self.mobile = mobile
        self.email = email
        self.dob = dob
class Student(Person):
    def __init__(self,rollno,name,mobile,email,dob,branch):
        super().__init__(rollno,name,mobile,email,dob)
        self.branch = branch
class Teacher(Person):
    def __init__(self,rollno,name,mobile,email,dob,subject):
        super().__init__(rollno,name,mobile,email,dob)
        self.subject = subject
class College:
    def __init__(self,clg_id,clg_name):
        self.clg_id = clg_id
        self.clg_name = clg_name
        self.students = []
        self.teachers = []
    def add_student(self,student):
        self.students.append(student)
    def add_teacher(self,teacher):
        self.teachers.append(teacher)
    def display_students(self):
        for data in self.students:
            print(f"===============> Student Details of {clg.clg_name} <===============")
            print(f"|-> Student Roll number   : {data.rollno}")
            print(f"|-> Student Name          : {data.name}")
            print(f"|-> Student Mobile        : {data.mobile}")
            print(f"|-> Student Email         : {data.email}")
            print(f"|-> Student Data of Birth : {data.dob}")
            print(f"|-> Student Branch        : {data.branch}")
            print("==============================================================")
    def display_teachers(self):
        for data in self.teachers:
            print(f"===============> Teachers Details of {clg.clg_name} <==============")
            print(f"|-> Teacher Roll number   : {data.rollno}")
            print(f"|-> Teacher Name          : {data.name}")
            print(f"|-> Teacher Mobile        : {data.mobile}")
            print(f"|-> Teacher Email         : {data.email}")
            print(f"|-> Teacher Data of Birth : {data.dob}")
            print(f"|-> Teacher Subject       : {data.subject}")
            print("==============================================================")
    def store_students(self):
        with open("student-details.txt","w") as f:
            f.write(f"====> Students Details of {clg.clg_name}\n")
            for data in self.students:
                f.write(f"-----------------------------------------------------------\n")
                f.write(f"|-> Student Roll number   : {data.rollno}\n")
                f.write(f"|-> Student Name          : {data.name}\n")
                f.write(f"|-> Student Mobile        : {data.mobile}\n")
                f.write(f"|-> Student Email         : {data.email}\n")
                f.write(f"|-> Student Data of Birth : {data.dob}\n")
                f.write(f"|-> Student Branch        : {data.branch}\n")
        print()
        print("==>  Data Stored Succesfully  <==")
        print()
    def store_teachers(self):
        with open("teachers-details.txt","w") as f:
            f.write(f"====> Teachers Details of {clg.clg_name}\n")
            for data in self.teachers:
                f.write(f"-----------------------------------------------------------\n")
                f.write(f"|-> Teacher Roll number   : {data.rollno}\n")
                f.write(f"|-> Teacher Name          : {data.name}\n")
                f.write(f"|-> Teacher Mobile        : {data.mobile}\n")
                f.write(f"|-> Teacher Email         : {data.email}\n")
                f.write(f"|-> Teacher Data of Birth : {data.dob}\n")
                f.write(f"|-> Teacher Subject        : {data.subject}\n")
        print()
        print("==>  Data Stored Succesfully  <==")
        print()
#Understanding
'''
print(colleges)
c1 = College(1001,"CBIT")
colleges.append(c1)
print(colleges)

print(colleges[0])
print(colleges[0].clg_id)
print(colleges[0].clg_name)
print(colleges[0].students)
print(colleges[0].teachers)

s11 = Student(301,"Venkat",7893570611,"saivardhan.thimmisetty@gmail.com","24-08-2025","CSE")
colleges[0].add_student(s11)

print(colleges[0])
print(colleges[0].clg_id)
print(colleges[0].clg_name)
print(colleges[0].students)
print(colleges[0].teachers)
colleges[0].display_students()


t11 = Teacher(401,"Vardhan",6302299809,"saivardhan2408@gmail.com","11-08-1994","Python")
colleges[0].add_teacher(t11)

print(colleges[0])
print(colleges[0].clg_id)
print(colleges[0].clg_name)
print(colleges[0].students)
print(colleges[0].teachers)
colleges[0].display_teachers()
'''

#Sample Data



greet()
logging.info("Portal Opened")
print()

while True:
    print("=====================================")
    print("|| Choose Your Option:             ||")
    print("|| ------------------              ||")
    print("|| 1. Create a College             ||")
    print("|| 2. Add a Student                ||")
    print("|| 3. Add a Teacher                ||")
    print("|| 4. Display Student Details      ||")
    print("|| 5. Display Teacher Details      ||")
    print("|| 6. Store Student Details - File ||")
    print("|| 7. Store Teacher Details - File ||")
    print("|| 8. Exit                         ||")
    print("=====================================")
    print()
    option = int(input("==> Enter your Option: "))
    print()
    match option:
        case 1:
            logging.warning("User Selected Option-1.Create a College")
            print("========================")
            print("||  Create a College  ||")
            print("========================")
            while True:
                cid = input("Enter College Id: ")
                logging.info(f"User Entered - College ID in Option-1.Create a College ID-That is {cid}")
                p = re.compile('\\d{5}')
                res = re.fullmatch(p,cid)
                if res is None:
                    print()
                    print("--> Invalid College ID - Give a 5 digit College ID ")
                    logging.error(f"User Entered Invalid College ID-That is {cid}")
                    print()
                else:
                    temp = False
                    for data in colleges:
                        if data.clg_id == cid:
                            clg = data
                            temp = True
                            break
                    if temp == True:
                        print()
                        print("--> College Already Exist - Try Again")
                        logging.warning(f"User Entered College ID That already existed in Data-That is {cid}")
                        print()
                    else:
                        cname = input("Enter College Name: ")
                        logging.info(f"User Entered College Name-That is{cname}")
                        clg = College(cid,cname)
                        colleges.append(clg)
                        print()
                        print("==== College Created Sucessfully ====")
                        logging.info(f"User  Created College ID Succesfully-That is\nCollege ID:{cid}\nCollege Name:{cname}")
                        print()
                        break
        case 2:
               logging.warning("User Selected - Add a student option")
               print("=====================")
               print("|| Add a Student   ||")
               print("=====================")
               while True:
                cid=input("Enter College ID: ")
                logging.info(f"User Entered - College ID in Option-2.Add a Student ID-That is {cid}")
                pattern=re.compile('\\d{5}')
                res = re.fullmatch(pattern,cid)
                if res is None:
                   print()
                   print("--> Invalid College ID - Please Enter 5 Digit Value")
                   logging.error(f"User Entered Invalid College ID-That is {cid}")
                   print()
                else:
                   temp=False
                   for data in colleges:
                       if data.clg_id==cid:
                           clg=data
                           temp=True
                   if temp==False:
                       print()
                       print("--> College not found !")
                       logging.warning(f"User Entered College ID That doesn't exist in Data-That is {cid}")
                       print()
                   else:
                       #Roll No-Student
                       while True:
                           rollno=input("Enter rollno: ")
                           logging.info(f"User entered rollno of Student that is {rollno}")
                           p = re.compile('\\d{3}')
                           r = re.fullmatch(p,rollno)
                           if r is None:
                               print()
                               print("--> Invalid ID - Please Enter 3 Digit Student ID")
                               logging.error(f"User entered invalid roll-no that is {rollno}")
                               print()
                           else:
                               temp=False
                               for data in clg.students:
                                   if data.rollno==rollno:
                                       data=clg
                                       temp=True
                                       data=clg
                                       break
                               if temp==True:
                                   print()
                                   print("--> Student already exists-Enter new roll number")
                                   logging.warning(f"User entered the Student rollno that already existed in Data {rollno}")
                                   print()
                               else:
                                   break
                       #Name-Student
                       while True:
                           name=input("Enter name: ")
                           logging.info(f"User entered Student name that is {name}")
                           p = re.compile('^[A-za-z .]+$')
                           r = re.fullmatch(p,name)
                           if r is None:
                               print()
                               print("--> Invalid Name - Please Enter in Valid Name")
                               logging.warning(f"User entered invalid Student name that is {name}")
                               print()
                           else:
                               break
                       #Mobileno-Student
                       while True:
                           mobile=input("Enter mobile no: ")
                           logging.info(f"User entered student mobile number that is {mobile}")
                           p = re.compile('^[6-9]\\d{9}$')
                           r = re.fullmatch(p,mobile)
                           if r is None:
                               print()
                               print("--> Invalid Mobile Number - Please Enter 10 Digit Phone Number")
                               logging.warning(f"User entered invalid student mobile number that is {mobile}")
                               print()
                           else:
                               break
                        #Email-student
                       while True:
                           email=input("Enter email: ")
                           logging.info(f"User entered student email that is {email}")
                           p = re.compile('^[a-z][a-z.\\d]*@gmail.com$')
                           r = re.fullmatch(p,email)
                           if r is None:
                               print()
                               print("--> Invalid Email ID - Please Enter valid mail")
                               logging.error(f"User entered invalid student email id that is {email}")
                               print()
                           else:
                               break
                        #DOB-student
                       while True:
                           dob=input("Enter date of birth: ")
                           logging.info(f"User entered student dob that is - {dob}")
                           p = re.compile('^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|[0-2])-(19|20)\\d{2}$')
                           r = re.fullmatch(p,dob)
                           if r is None:
                               print()
                               print("--> Invalid DOB-Enter Valid DOB in DD-MM-YYYY format")
                               logging.error(f"User entered invalid student dob that is-{dob}")
                               print()
                           else:
                               break
                        #Branch-Student
                       while True:
                           branch=input("Enter branch: ")
                           logging.info(f"User entered student branch that is - {branch}")
                           p = re.compile('CSE|cse|Cse|MECHANICAL|Mechanical|mechanical|EEE|eee|Eee|CIVIL|civil|Civil|ECE|ece|Ece|')
                           r = re.fullmatch(p,branch)
                           if r is None:
                               print()
                               print("--> Please Enter Valid Branch")
                               logging.error(f"User entered invalid student branch that is - {branch}")
                               print()
                           else:
                               break
                       if not verify_student_email(email):
                                   print("Student Email Verification Failed!")
                                   break
                       student=Student(rollno,name,mobile,email,dob,branch)
                       clg.add_student(student)
                       print()
                       print("=== Student Created Succesfully ===")
                       logging.info(f"User succesfully created the Student Id-{rollno} in {clg.clg_id}")
                       print()
                       temp=False
                       break
        case 3:
               logging.info("User selected 3.Add a Teacher")
               print("=====================")
               print("|| Add a Teacher   ||")
               print("=====================")
               while True:
                cid=input("Enter College ID: ")
                logging.info(f"User Entered - College ID in Option-2.Add a Student ID-That is {cid}")
                pattern=re.compile('\\d{5}')
                res = re.fullmatch(pattern,cid)
                if res is None:
                   print()
                   print("--> Invalid College ID - Please Enter 5 Digit Value")
                   logging.error(f"User Entered Invalid College ID-That is {cid}")
                   print()
                else:
                   temp=False
                   for data in colleges:
                       if data.clg_id==cid:
                           clg=data
                           temp=True
                   if temp==False:
                       print()
                       print("--> College not found !")
                       logging.warning(f"User Entered College ID That doesn't exist in Data-That is {cid}")
                       print()
                   else:
                       #Roll No-Teacher
                       while True:
                           rollno=input("Enter rollno: ")
                           logging.info(f"User entered rollno of Teacher that is {rollno}")
                           p = re.compile('\\d{4}')
                           r = re.fullmatch(p,rollno)
                           if r is None:
                               print()
                               print("--> Invalid ID - Please Enter 4 Digit Teacher ID")
                               logging.error(f"User entered invalid roll-no that is {rollno}")
                               print()
                           else:
                               temp == False
                               for data in clg.students:
                                   if data.rollno==rollno:
                                       data=clg
                                       temp=True
                                       break
                               if temp==False:
                                   print()
                                   print("--> Teacher already exists- Enter a new roll number")
                                   logging.warning(f"User entered the Teacher rollno that already existed in Data {rollno}")
                                   print()
                               else:
                                   break

                       #Name-Teacher
                       while True:
                           name=input("Enter name: ")
                           logging.info(f"User entered Teacher name that is {name}")
                           p = re.compile('^[A-za-z .]+$')
                           r = re.fullmatch(p,name)
                           if r is None:
                               print()
                               print("Invalid Name - Please Enter in Valid Name")
                               logging.warning(f"User entered invalid Teacher name that is {name}")
                               print()
                           else:
                               break
                        #Mobileno-Teacher
                       while True:
                           mobile=input("Enter mobile no: ")
                           logging.info(f"User entered Teacher mobile number that is {mobile}")
                           p = re.compile('^[6-9]\\d{9}$')
                           r = re.fullmatch(p,mobile)
                           if r is None:
                               print()
                               print("Invalid Mobile Number - Please Enter 10 Digit Phone Number")
                               logging.warning(f"User entered invalid Teacher mobile number that is {mobile}")
                               print()
                           else:
                               break
                        #Email-Teacher
                       while True:
                           email=input("Enter email: ")
                           logging.info(f"User entered Teacher email that is {email}")
                           p = re.compile('^[a-z][a-z.\\d]*@gmail.com$')
                           r = re.fullmatch(p,email)
                           if r is None:
                               print()
                               print("Invalid Email ID - Please Enter valid mail")
                               logging.error(f"User entered invalid Teacher email id that is {email}")
                               print()
                           else:
                               break
                    #DOB-Teacher
                       while True:
                           dob=input("Enter date of birth: ")
                           logging.info(f"User entered Teacher dob that is - {dob}")
                           p = re.compile('^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|[0-2])-(19|20)\\d{2}$')
                           r = re.fullmatch(p,dob)
                           if r is None:
                               print()
                               print("--> Invalid DOB-Enter Valid DOB in DD-MM-YYYY format")
                               logging.error(f"User entered invalid student dob that is-{dob}")
                               print()
                           else:
                               break
                       #Subject-Teacher
                       while True:
                           subject=input("Enter Subject: ")
                           logging.info(f"User entered Teacher's subject that is - {subject}")
                           p = re.compile('Python|Java|C++|C|C#')
                           r = re.fullmatch(p,subject)
                           if r is None:
                               print()
                               print("--> Please Enter Valid Subject")
                               logging.error(f"User entered invalid Teacher's subject that is - {subject}")
                               print()
                           else:
                               break
                       if not verify_student_email(email):
                                   print("Student Email Verification Failed!")
                                   break
                       teacher=Teacher(rollno,name,mobile,email,dob,subject)
                       clg.add_teacher(teacher)
                       print()
                       print("=== Teacher Created Succesfully ===")
                       logging.info(f"User succesfully created the Teacher's Id-{rollno} in {clg.clg_id}")
                       print()
                       temp=False
                       print()
                       break
        case 4:
            logging.info("User Selected Option 4.Display Student Details")
            print("=============================")
            print("|| Display Student Details ||")
            print("=============================")
            while True:
                cid = input("Enter College id: ")
                logging.info(f"User Entered College Id in option 4.Display Student Details{cid}")
                pattern = re.compile("\\d{5}")
                res = re.fullmatch(pattern,cid)
                if res is None:
                    print()
                    print("--> Invalid College ID - Please Enter 5 Digit College ID")
                    logging.error(f"User entered Invalid College Id in option 4-that is {cid}")
                    print()
                else:
                    temp = False
                    for data in colleges:
                        if data.clg_id == cid:
                            clg = data
                            temp = True
                            break
                    if temp == False:
                        print()
                        print("--> College Not Found !")
                        logging.warning("User entered College ID That haven't present in Data")
                        print()
                    else:
                        print()
                        clg.display_students()
                        logging.info(f"User saw the Students data in {cid}")
                        print()
                        break
        case 5:
            logging.info("User Selected Option 5.Display Teacher's Details")
            print()
            print("=== Display Teacher Details ===")
            print()
            while True:
                cid = input("Enter College id: ")
                logging.info(f"User Entered College Id in option 5.Display Teachers Details{cid}")
                pattern = re.compile('\\d{5}')
                res = re.fullmatch(pattern,cid)
                if res is None:
                    print()
                    print("--> Invalid College ID - Please enter 5 digit college ID")
                    logging.error(f"User entered Invalid College Id in option 5-that is {cid}")
                    print()
                else:
                    temp = False
                    for data in colleges:
                        if data.clg_id == cid:
                            clg = data
                            temp = True
                            break
                    if temp == False:
                        print()
                        print("--> College Not Found")
                        logging.warning("User entered College ID That haven't present in Data")
                        print()
                    else:
                        print()
                        clg.display_teachers()
                        logging.info(f"User saw the Teachers data in {cid}")
                        print()
                        break
        case 6:
            logging.info("User entered Option 6.Store Student Details")
            print("=============================")
            print("||  Store Student Details  ||")
            print("=============================")
            while True:
                cid = input("Enter College id: ")
                logging.info(f"User Entered college id in Option.6 that is {cid}")
                pattern = re.compile("\\d{5}")
                res = re.fullmatch(pattern,cid)
                if res is None:
                    print()
                    print("--> Invalid College ID - Please Enter 5 Digit College ID")
                    logging.error(f"User entered invalid college id in option.6 that is {cid}")
                    print()
                else:
                    temp = False
                    for data in colleges:
                        if data.clg_id == cid:
                            clg = data
                            temp = True
                            break
                    if temp == False:
                        print()
                        print("--> College Not Found - Please Enter Valid College ID")
                        logging.warning(f"User entered college id that haven't present in data that is {cid}")
                        print()
                    else:
                        clg.store_students()
                        logging.info("User stored the student details in (student-details.txt) file")
                        break
        case 7:
             logging.info("User entered Option 7.Store Teacher's Details")
             print("===============================")
             print("||   Store Teacher Details   ||")
             print("===============================")
             while True:
                cid = input("Enter College id: ")
                logging.info(f"User Entered college id in Option.7 that is {cid}")
                pattern = re.compile('\\d{5}')
                res = re.fullmatch(pattern,cid)
                if res is None:
                    print()
                    print("--> Invalid College ID - Please enter 5 digit college ID")
                    logging.error(f"User entered invalid college id in option.7 that is {cid}")
                    print()
                else:
                    temp = False
                    for data in colleges:
                        if data.clg_id == cid:
                            clg = data
                            temp = True
                            break
                    if temp == False:
                        print()
                        print("--> College Not Found")
                        logging.warning(f"User entered college id that haven't present in data that is {cid}")
                        print()
                    else:
                        print()
                        clg.store_teachers()
                        logging.info("User stored the student details in (teachers-details.txt) file")
                        print()
                        break
        case 8:
            logging.info("User selected option 8.Exit")
            print()
            end()
            logging.info("Portal Closed")
            print()
            break
        case _:
            print()
            print("==> Invalid Input - Try again  <==")
            logging.error(f"User entered invalid option that is {option}")
            print()
