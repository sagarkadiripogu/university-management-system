# 🎓 University Management System (Python + MySQL)

## Overview

This project is a console-based **University Management System** built using Python and MySQL. It allows managing colleges, students, and teachers with proper validation, logging, and file storage features.

The system focuses on **data integrity, validation, and basic backend logic** rather than UI complexity.

---

## 🚀 Features

### 🏫 College Management

* Create new colleges with unique IDs
* Prevent duplicate college entries

### 👨‍🎓 Student Management

* Add students under a specific college
* Input validation using Regular Expressions
* Email verification using OTP system 
* Store student details into file 

### 👨‍🏫 Teacher Management

* Add teachers linked to a college
* Email verification system 
* Store teacher details into file 

### 🕒 Time Restriction

* System runs only during working hours (8 AM – 10 PM) 

### 📄 Logging System

* Tracks all user actions, errors, and system events 

### 💾 File Storage

* Export student and teacher data into text files

---

## 🛠️ Tech Stack

* Python
* MySQL
* PyMySQL
* Tkinter (basic GUI prototype) 
* Logging module

---

## 📂 Project Structure

* `main_1.py` → Core application logic 
* `checktime.py` → Time restriction module
* `email_verification_student.py` → Student OTP verification
* `email_verification_teacher.py` → Teacher OTP verification
* `greeting.py` → Welcome message
* `end_greeting.py` → Exit message
* `gui.py` → Basic GUI implementation
* `student-details.txt` → Stored student data
* `teachers-details.txt` → Stored teacher data
* `smslog.log` → Application logs

---

## ⚙️ How to Run

1. Install dependencies:

```bash
pip install pymysql
```

2. Setup MySQL database:

* Create database: `ums`
* Create tables: `colleges`, `students`, `teachers`

3. Run the main file:

```bash
python main_1.py
```

---

## 📌 Sample Output

### Student File Output



---

## ⚠️ Limitations

* Console-based interaction (no full UI)
* Hardcoded email credentials (not secure)
* Basic error handling (can be improved)
* No ORM or modular architecture

---

## 🧠 Key Concepts Used

* Database Connectivity (PyMySQL)
* CRUD Operations
* Input Validation (Regex)
* Logging & Debugging
* File Handling
* Email Automation (SMTP)
* Basic GUI (Tkinter)

---

## 📈 Future Improvements

* Convert to full GUI or Web App
* Use environment variables for security
* Implement proper MVC structure
* Add authentication system
* Use ORM (SQLAlchemy/Django ORM)

---

## 👨‍💻 Author

Sagar

---
