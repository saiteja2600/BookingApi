# 🧘‍♀️ Fitness Studio Booking API

This is a simple Booking API and web interface for a fictional fitness studio. Users can view available fitness classes (like Yoga, Zumba, HIIT), book a class, and view their bookings. This project was created as part of a Python Developer assignment.

---

## 📌 Features

- View upcoming fitness classes with details
- Book a spot in a class
- Retrieve bookings by email
- Responsive frontend interface using Django templates
- Timezone-aware class scheduling (created in IST)
- Login/Logout system via session handling
- Error handling, form validations, and user messages

---

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, JavaScript (jQuery, SweetAlert2, FullCalendar)
- **Database:** SQLite (in-memory or file-based)
- **Other Tools:** Moment.js, FontAwesome

---

## 🚀 How to Run the Project

### 1. Clone the Repository 

```bash ```

https://github.com/saiteja2600/BookingApi
Create a virtual environment

python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

``` Run The Migrations```

python manage.py makemigrations
python manage.py migrate



```Run Server```
python manage.py runserver


## 📦 Functional Overview

This project implements core features for a fitness booking platform using Django. Here's a breakdown of key backend views and what they do:

---

### 🔐 Authentication & Session Management

- **Signup** (`/signup/`): Users can register using their email, username, and password. Passwords are securely hashed.
- **Login** (`/login/`): Authenticates users by checking hashed credentials. On success, stores user session.
- **Logout** (`/logout/`): Clears session data and logs out the user.
- **Session Check**: Most pages require a logged-in session (`request.session['user_email']`), redirecting unauthenticated users to login.

---

### 📅 Class Booking & Scheduling

- **Home** (`/`): Dashboard view, only accessible when logged in.
- **About** (`/about/`): A static page describing the project or fitness platform.
- **Schedule** (`/schedule/`): 
  - Displays all bookings made by the logged-in user.
  - If the request is via AJAX (XHR), it returns the bookings in JSON format for calendar display (used by FullCalendar).
- **Book Slot** (`/bookslot/`):
  - Displays a form to book a class.
  - Prevents double-booking a trainee at the same time.
  - Sends confirmation email to user after successful booking.
  - Validates all fields before booking.

---

### 🗑️ Slot Deletion

- **Delete Slot** (`/slot_delete/<client_id>/`): 
  - Allows users to cancel their previously booked class.
  - Only the user who booked the slot can delete it.
  - Deletes the record and updates the calendar view.

---

### ✉️ Email Integration

- A confirmation email is sent after a successful booking.
- Email includes slot type, trainee, date, and formatted time.
- Configured using Django’s `EmailMessage`.

---

### 📊 Technologies Used in Views

- Django Views & Templates
- Django ORM for data operations
- Django Messages Framework for user feedback
- jQuery + FullCalendar for frontend calendar rendering
- SweetAlert2 for friendly pop-up messages
- Session-based login handling

### 🎨 Frontend Overview
The frontend is built using Django Templates and enhanced with CSS, JavaScript, and third-party libraries like FullCalendar, SweetAlert2, and Font Awesome. All common structure and styling are handled in a base layout file.


🧭 Navigation Menu:
        o Home, About, and Scheduler links.
        o Login/Logout buttons are dynamically shown based on the session.
        o User Session Display:
        o Shows the logged-in user's email at the top when authenticated.



🖼️ Banner & Homepage
        ->The homepage displays a centred "Get Started" button.
        ->Clicking it scrolls smoothly to the main content.
        ->Styled using CSS and JS for responsiveness.

        
📬 Feedback & Alerts
        o Uses Django’s {% if messages %} block to display success/error messages.
                o Integrates with SweetAlert2 for clean, modern popup alerts for actions like:
                o Successful booking
                oInvalid login
                o Slot conflicts

🗓️ Schedule & Calendar Integration
        o /schedule/ page loads user's bookings and renders them using:
                o FullCalendar.js for a visual calendar.
                o AJAX (XHR) to load events dynamically as JSON from Django.
                o Booked slots are shown with client name, trainee, time, and slot type.

📝 Booking Form
        o /bookslot/ page displays a form to book new classes.
                0 Trainee dropdown updates based on slot type selected.
                o Form validation ensures:
                o No trainee double-booking
                o No duplicate user-slot combinations
        o On success:
                o Saves the slot to the database
                o Sends a confirmation email
                oShows a success alert

👣 Footer & Social Media
        o Fixed footer includes social icons:
        o Facebook, Instagram, Twitter, YouTube
        o Styled with Font Awesome icons

💡 JavaScript Enhancements
        jQuery handles UI interactivity like toggling menus.
        Custom JS Files:
                o scripts.js, schedule.js, and bookslot.js
                o Manage booking logic, alerts, and calendar rendering
                o Moment.js used for time formatting and timezone support



```Default localhost
http://127.0.0.1:8000/''' 

