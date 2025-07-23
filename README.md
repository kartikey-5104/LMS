# 📚 Library Management System (LMS) 🚀

Welcome to the **Library Management System** — a powerful web application built with **Django** 🐍 to help manage books, users, borrowing, and more!

---

## 🧠 Key Features

✅ **User Authentication** – Login/Register with secure sessions  
📖 **Book Catalog** – Add, edit, delete, and browse books  
👥 **Role-Based Dashboards** – Separate views for Admins and Members  
📅 **Borrow & Return System** – Track lending & due dates  
🔍 **Search & Filter** – Quickly find any book  
📊 **Admin Panel** – Manage everything with ease  
📦 **SQLite Database** – Lightweight and fast by default  
🎨 **Responsive UI** – Clean and intuitive frontend

---

## 🛠️ Tech Stack

| Layer       | Tech Used                  |
|-------------|----------------------------|
| 💻 Backend  | Django, Python             |
| 🗂️ Database | SQLite (default), can upgrade to PostgreSQL |
| 🎨 Frontend | HTML, CSS, Bootstrap       |
| 🔐 Auth     | Django Auth System         |
| 🌐 Hosting  | GitHub + (Optional: Render, Heroku, etc.) |

---

## ⚙️ Setup Instructions

```bash
# 1️⃣ Clone the repo
git clone git@github.com:kartikey-5104/LMS.git
cd LMS

# 2️⃣ Setup virtual environment
python3 -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run migrations
python manage.py makemigrations
python manage.py migrate

# 5️⃣ Create a superuser (for admin panel)
python manage.py createsuperuser

# 6️⃣ Start the server 🚀
python manage.py runserver
