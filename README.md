🎓 University Management System (Console-Based)

A modular University Management System built using Python that supports multi-college management with secure OTP authentication, structured validation, activity logging, and persistent file storage.
⸻

🚀 Project Overview

This system allows administrators to manage multiple colleges, register students and teachers, and securely verify users using an email-based OTP authentication system.

The project is designed with modular architecture and follows structured backend workflow principles.

⸻

🔐 Key Features

🏫 Multi-College Support
	•	Create and manage multiple colleges
	•	Isolated data handling per college

👨‍🎓 Student Management
	•	Add student with validation
	•	Unique roll number check
	•	Email OTP verification (with expiry & retry limits)
	•	Store student details to file

👨‍🏫 Teacher Management
	•	Add teacher with validation
	•	Secure email verification
	•	Subject allocation
	•	Store teacher details to file

🔑 Secure OTP Authentication
	•	Email-based OTP verification
	•	OTP expiry mechanism
	•	Limited retry attempts
	•	Resend OTP functionality

📝 Activity Logging
	•	Logs INFO, WARNING, and ERROR events
	•	Tracks user actions
	•	Simulates production-style monitoring

💾 Persistent File Storage
	•	Student details stored in student-details.txt
	•	Teacher details stored in teachers-details.txt
	•	Logs stored in smslog.txt

⸻

🧠 Technical Concepts Used
	•	Python OOP (Classes & Objects)
	•	Input Validation
	•	Email SMTP Integration
	•	Logging Module
	•	File Handling
	•	Modular Project Structure
	•	Error Handling & Control Flow

⸻

📂 Project Structure
  main_1.py
  email_verification_student.py
  email_verification_teacher.py
  greeting.py
  end_greeting.py
  checktime.py
  student-details.txt
  teachers-details.txt
  smslog.txt
⸻

▶️ How To Run

1️⃣ Clone the repository:
      git clone https://github.com/sagarkadiripogu/university-management-system.git
2️⃣ Navigate to project folder:
      cd university-management-system
3️⃣ Run the main file:
      python main_1.py

⸻

🔮 Future Improvements
	•	Database integration (SQLite / MySQL)
	•	Role-based login dashboards
	•	Attendance management system
	•	Marks & grade calculation
	•	Flask-based web version
	•	JWT-based authentication

⸻

👨‍💻 Author

Sagar Kadiripogu
Aspiring Backend Developer | Python Enthusiast

⸻

⭐ Support

If you like this project, feel free to star the repository ⭐

⸻

🔥 Now your GitHub looks:
	•	Clean
	•	Structured
	•	Professional
	•	Recruiter-ready


