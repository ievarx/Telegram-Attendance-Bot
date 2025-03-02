
### **📌 Telegram Attendance Bot - University Database Task (2023-2024) ✅**  

This repository contains the **Telegram Attendance Bot**, a **university database task** designed to manage student attendance. The bot retrieves student names from a **MySQL** database and provides interactive buttons for marking attendance. Attendance records are stored with the date in the database.  

📌 **This project was developed as a mandatory university assignment for the 2023-2024 academic year.**  

#### **📂 Project Files:**  
- **`Query.txt`** → Contains SQL queries to create the student attendance database.  
- **`install.txt`** → Instructions for setting up and installing dependencies.  
- **`attendance.py`** → The main script for running the Telegram attendance bot.  

#### **🚀 Features:**  
- Developed as a **mandatory university assignment**.  
- Retrieves student names from a **MySQL** database.  
- Provides interactive buttons (**Present / Absent**) for each student.  
- Saves attendance records with timestamps in the database.  

#### **⚙️ How to Install & Run:**  
1. **Clone the repository:**  
   ```bash
   git clone https://github.com/yourusername/Telegram-Attendance-Bot.git
   ```  
2. **Install dependencies:**  
   Run the following commands:  
   ```bash
   pip install python-telegram-bot==13.7.0  
   pip install mysql-connector-python  
   ```  
3. **Create the database:**  
   - Open **MySQL** and execute the queries from **`query.txt`**.  
4. **Run the bot:**  
   ```bash
   python attendance.py  
   ```  

💡 **Notes:**  
- Ensure that your **Telegram bot token** is correctly configured inside `attendance.py`.  
- The bot must have permission to send and receive messages.  
- Feel free to contribute or suggest improvements! 😊  

---
