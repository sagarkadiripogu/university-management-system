from greeting import greet
from end_greeting import end
import re
from email_verification_student import verify_student_email
from email_verification_teacher import verify_teacher_email
import logging
import checktime
import pymysql


logging.basicConfig(level=logging.DEBUG,
                    filename="smslog.log",
                    filemode="a",
                    format="%(asctime)s : %(levelname)s - %(message)s")
conn = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "ums"
)
x = conn.cursor()
print("Connection With Database Created")
logging.info("Connection with database is Started")
class College:
    def store_students():
        x = conn.cursor()
        x.execute("select * from students where college_id = %s",(cid))
        data = list(x.fetchall())
        with open("student-details.txt","w") as f:
            f.write(f"====> Students Details of {cid}\n")
            for i in range(len(data)):
                f.write(f"-----------------------------------------------------------\n")
                f.write(f"|-> Student Roll number   : {data[i][0]}\n")
                f.write(f"|-> Student Name          : {data[i][1]}\n")
                f.write(f"|-> Student Mobile        : {data[i][2]}\n")
                f.write(f"|-> Student Email         : {data[i][3]}\n")
                f.write(f"|-> Student Data of Birth : {data[i][4]}\n")
                f.write(f"|-> Student Branch        : {data[i][5]}\n")
        print()
        print("==>  Data Printed Succesfully  <==")
        print()
    def store_teachers():
        x = conn.cursor()
        x.execute("SELECT * FROM teachers WHERE college_id = %s", (cid,))
        data = x.fetchall()

        if not data:
            print("No teacher records found")
            return

        with open("teachers-details.txt", "w") as f:
            f.write(f"====> Teachers Details of {cid}\n")

            for i in range(len(data)):
                f.write("-----------------------------------------------------------\n")
                f.write(f"|-> Teacher Roll number   : {data[i][0]}\n")
                f.write(f"|-> Teacher Name          : {data[i][1]}\n")
                f.write(f"|-> Teacher Mobile        : {data[i][2]}\n")
                f.write(f"|-> Teacher Email         : {data[i][3]}\n")
                f.write(f"|-> Teacher Date of Birth : {data[i][4]}\n")
                f.write(f"|-> Teacher Subject       : {data[i][5]}\n")

        print("\n==> Teacher Data Printed Successfully <==\n")


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
    print("|| 6. Print Student Details - File ||")
    print("|| 7. Print Teacher Details - File ||")
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
                    x = conn.cursor()
                    x.execute("select college_id from colleges where college_id =%s",(cid))
                    data = x.fetchone()
                    if data is not None:
                        print()
                        print("--> College Already Exist - Try Again")
                        logging.warning(f"User Entered College ID That already existed in Data-That is {cid}")
                        print()
                    else:
                        cname = input("Enter College Name: ")
                        logging.info(f"User Entered College Name-That is{cname}")
                        x = conn.cursor()
                        x.execute("INSERT INTO colleges (college_id, college_name) VALUES (%s, %s)",(cid, cname))
                        conn.commit()
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
                    x = conn.cursor()
                    x.execute("select college_id from colleges where college_id =%s",(cid))
                    data = x.fetchone()
                    if data is None:
                        print()
                        print("--> College not found !")
                        print()
                        logging.warning(f"User Entered College ID That doesn't exist in Data-That is {cid}")
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
                               x = conn.cursor()
                               x.execute("select roll_no from students where roll_no=%s",(rollno))
                               data = x.fetchone()
                               if data is not None:
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
                       x = conn.cursor()
                       x.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(rollno,name,mobile,email,dob,branch,cid))
                       conn.commit()
                       print()
                       print("=== Student Created Succesfully ===")
                       logging.info(f"User succesfully created the Student Id-{rollno} in {cid}")
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
                   x = conn.cursor()
                   x.execute("select college_id from colleges where college_id=%s",(cid))
                   data = x.fetchone()
                   if data is None:
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
                               x = conn.cursor()
                               x.execute("select roll_no from teachers where roll_no = %s",(rollno))
                               data = x.fetchone()
                               if data is not None:
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
                       if not verify_teacher_email(email):
                                   print("Student Email Verification Failed!")
                                   break
                       x = conn.cursor()
                       x.execute("insert into teachers values (%s,%s,%s,%s,%s,%s,%s)",(rollno,name,mobile,email,dob,subject,cid))
                       conn.commit()
                       print()
                       print("=== Teacher Created Succesfully ===")
                       logging.info(f"User succesfully created the Teacher's Id-{rollno} in {cid}")
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
                    x = conn.cursor()
                    x.execute("select college_id from colleges where college_id=(%s)",(cid))
                    data = x.fetchone()
                    if data is None:
                        print()
                        print("--> College Not Found !")
                        logging.warning("User entered College ID That haven't present in Data")
                        print()
                    else:
                        print()
                        x = conn.cursor()
                        x.execute("select * from students where college_id=(%s)",(cid))
                        details = x.fetchall()

                        y = conn.cursor()
                        y.execute("select * from colleges where college_id = %s",(cid))
                        college_details = y.fetchone()
                        for i in details:
                            high = f"Student Details of {college_details[1]}"
                            print(high)
                            print("-"*len(high))
                            print(f"Student Rollno:    {i[0]}")
                            print(f"Student Name:      {i[1]}")
                            print(f"Student Number:    {i[2]}")
                            print(f"Student Email:     {i[3]}")
                            print(f"Student DOB:       {i[4]}")
                            print(f"Student Branch:    {i[5]}")
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
                    x = conn.cursor()
                    x.execute("select college_id from colleges where college_id=(%s)",(cid))
                    data = x.fetchone()
                    if data is None:
                        print()
                        print("--> College Not Found !")
                        logging.warning("User entered College ID That haven't present in Data")
                        print()
                    else:
                        print()
                        x = conn.cursor()
                        x.execute("select * from teachers where college_id=(%s)",(cid))
                        details = x.fetchall()

                        y = conn.cursor()
                        y.execute("select * from colleges where college_id = %s",(cid))
                        college_details = y.fetchone()
                        for i in details:
                            high = f"Teachers Details of {college_details[1]}"
                            print(high)
                            print("-"*len(high))
                            print(f"Teacher Rollno:    {i[0]}")
                            print(f"Teacher Name:      {i[1]}")
                            print(f"Teacher Number:    {i[2]}")
                            print(f"Teacher Email:     {i[3]}")
                            print(f"Teacher DOB:       {i[4]}")
                            print(f"Teacher Branch:    {i[5]}")
                        logging.info(f"User saw the Students data in {cid}")
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
                    x = conn.cursor()
                    x.execute("select college_id from students where college_id = %s",(cid))
                    data = x.fetchone()
                    if data is None:
                        print()
                        print("--> College Not Found - Please Enter Valid College ID")
                        logging.warning(f"User entered college id that haven't present in data that is {cid}")
                        print()
                    else:
                        College.store_students()
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
                    x = conn.cursor()
                    x.execute("select college_id from teachers where college_id = %s",(cid))
                    data = x.fetchone()
                    if data is None:
                        print()
                        print("--> College Not Found - Please Enter Valid College ID")
                        logging.warning(f"User entered college id that haven't present in data that is {cid}")
                        print()
                    else:
                        College.store_students()
                        logging.info("User stored the teachers details in (student-details.txt) file")
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
