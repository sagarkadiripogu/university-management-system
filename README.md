# 🎓 University Management System (Console-Based)

A modular University Management System built using Python that supports multi-college management with secure OTP authentication, structured validation, activity logging, and persistent file storage.

---

## 🚀 Project Overview

This system allows administrators to manage multiple colleges, register students and teachers, and securely verify users using an email-based OTP authentication system.

The project is designed with modular architecture and follows structured backend workflow principles.

---

## 🔐 Key Features

### 🏫 Multi-College Support
- Create and manage multiple colleges
- Isolated data handling per college

### 👨‍🎓 Student Management
- Add student with validation
- Unique roll number check
- Email OTP verification (with expiry & retry limits)
- Store student details to file

### 👨‍🏫 Teacher Management
- Add teacher with validation
- Secure email verification
- Subject allocation
- Store teacher details to file

### 🔑 Secure OTP Authentication
- Email-based OTP verification
- OTP expiry mechanism
- Limited retry attempts
- Resend OTP functionality

### 📝 Activity Logging
- Logs INFO, WARNING, and ERROR events
- Tracks user actions
- Helps simulate production-style monitoring

### 💾 Persistent File Storage
- Student details stored in `student-details.txt`
- Teacher details stored in `teachers-details.txt`

---

## 🧠 Technical Concepts Used

- Python OOP (Classes & Objects)
- Input Validation
- Email SMTP Integration
- Logging Module
- File Handling
- Modular Project Structure
- Error Handling & Control Flow
- Time module
- 

---

## 📂 Project Structure
