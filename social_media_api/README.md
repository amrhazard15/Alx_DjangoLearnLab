# 🌐 Social Media API

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Django](https://img.shields.io/badge/Django-5.2-green)
![REST](https://img.shields.io/badge/REST-API-red)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

**Social Media API** is a complete Django REST Framework project that powers a modern social media platform. Users can register, login, manage posts, follow/unfollow other users, and receive real-time notifications.

---

## 🚀 Features

- **User Authentication & Tokens** 🔐  
  - Register a new user  
  - Login with token-based authentication  

- **Social Interactions** 🤝  
  - Follow and unfollow users  
  - Create, update, and delete posts  
  - Like posts  

- **Notifications System** 🔔  
  - Receive notifications for important events  
  - Mark notifications as read  

- **API Documentation** 📚  
  - Swagger UI and Redoc integration  
  - Fully browsable API  

---

## 📂 Project Structure

social_media_api/
├── accounts/ # User management
├── posts/ # Posts management
├── notifications/ # Notifications system
├── social_media_api/ # Project settings
├── db.sqlite3 # SQLite database
├── requirements.txt # Python dependencies
└── README.md

---

## 🖥️ Installation

1. **Clone the repository**

```bash
git clone https://github.com/amrhazard15/Alx_DjangoLearnLab.git
cd social_media_api
```
---

2. **Create a virtual environment**
```bash
python -m venv venv
# Activate
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/Mac
```
---

3. **Install dependencies**
```bash
pip install -r requirements.txt
```
---

4. **Run migrations**
```bash
python manage.py migrate
```
5. **Start the development server**
```bash
python manage.py runserver
```

---

6. **Access the API**

**Base API**: http://127.0.0.1:8000/api/

**Swagger UI**: http://127.0.0.1:8000/swagger/

**Redoc**: http://127.0.0.1:8000/redoc/
  
----------------

🔗 API Endpoints
Endpoint	                      Method	              Description
/accounts/register/ 	          POST	                Register a new user
/accounts/login/	              POST	                Login and retrieve token
/accounts/follow/<id>/          POST	                Follow a user
/accounts/unfollow/<id>/	      POST	                Unfollow a user
/posts/                         GET/POST	            List or create posts
/posts/<id>/                   GET/PUT/DELETE	        Manage a specific post
/notifications/ 	             GET	                  View notifications

------------

🛠️ Technologies Used
* Python 3.11
* Django 5.2
* Django REST Framework
* drf-spectacular (Swagger/OpenAPI)
* SQLite
  
--------------

🔮 Future Improvements
Add an interactive frontend using React or Vue.js

Multimedia support for posts (images/videos)

Advanced search and filters for users and posts

Real-time notifications using WebSockets


👤 **Author**
**Amr Khaled (Hazard) – [GitHub Profile](https://github.com/amrhazard15)**
=============

📄 License
This project is licensed under the MIT License.
