# 🧘‍♀️ Fitness Studio Booking API

A full-featured fitness studio management system built using Django. It includes both RESTful APIs and user-friendly interfaces for admins and clients to manage and book fitness classes like Yoga, Zumba, and HIIT.

---

## 📦 Features

### ✅ API Features

- View available fitness classes
- Book a class with client details
- Retrieve bookings by client email
- Timezone-aware scheduling (default: IST)
- Input validation, error handling, and overbooking prevention

### 🧑‍💼 Admin Panel

The admin panel is designed for fitness studio staff to manage operations efficiently.

**Features:**

- 🧑‍🏫 **Trainer Management**: Add/update/remove trainers.
- 📅 **Schedule Management**: Manage class slots and instructor assignments.
- 📊 **Dashboard**: Access summarized metrics and quick navigation.
- 🔐 **Secure Login/Logout**
- 🖥️ **Responsive UI** using Bootstrap 5, SweetAlert, FullCalendar.

> Access via `/admin/login/`

---

### 🙋‍♂️ User Panel

The client-facing panel allows users to explore, book, and manage their fitness class interactions.

**Features:**

- 📚 **Class Listings**: View and filter available classes.
- 🗓️ **Book Classes**: Reserve available slots for sessions.
- 📆 **Calendar View**: Full interactive calendar for upcoming sessions.
- 🔐 **User Authentication**
- 🎨 **Modern UI** using Bootstrap, SweetAlert, FullCalendar.

> Access via `/login/` (User Login)

---

### 🌐 Global Landing Page

The main entry point for the platform.

**Features:**

- Clean, modern homepage
- Dropdown selector for User or Admin login
- Centralized navigation

> Access via `/`

---

## 🚀 Technologies Used

- **Backend**: Python, Django
- **Database**: SQLite (in-memory or file-based)
- **Frontend**: Django Templates, Bootstrap 5, jQuery
- **Calendar**: FullCalendar.js
- **Alerts**: SweetAlert2
- **Icons**: FontAwesome

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash```
https://github.com/saiteja2600/Fitnees_Booking.git
cd fitness-booking-api

### 2. Create Virtual Environment and Install Dependencies```

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt


### 3. Run Migrations and Load Sample Data```
python manage.py makemigrations
python manage.py migrate

🧪 API Endpoints

GET /classes/

curl http://localhost:8000/Fitnees-Studio/classes/


POST /book/

curl -X POST http://localhost:8000/Fitnees-Studio/book/ \
-H "Content-Type: application/json" \
-d '{"class_id": 1, "client_name": "John Doe", "client_email": "john@example.com"}'

GET /bookings/?email=john@example.com
curl "http://localhost:8000/Fitnees-Studio/bookings/?email=john@example.com"







