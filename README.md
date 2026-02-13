

```markdown
# 🌐 NCPOR Data Management System

A full-stack web application built using **Django** for managing, storing, and accessing structured datasets.  
The platform provides an intuitive interface for users to submit records while administrators can securely manage, verify, and organize the data through the Django admin panel.

This project demonstrates practical implementation of backend development, database design, and server-side rendering.


## 🚀 Key Features

✅ Structured multi-step data entry using Django Forms  
✅ Preview functionality before final submission  
✅ Complete CRUD operations   
✅ Asynchronous updates using AJAX  
✅ Secure and powerful Django Admin interface  
✅ File / image upload & mapping with database records  
✅ Organized data storage using SQLite  
✅ Clean and modular Django project architecture  
✅ Static & media file handling  


---

## 🛠 Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python, Django |
| Database | SQLite |
| Frontend | HTML, CSS, Bootstrap  AJAX  |
| Tools | Django ORM, Admin Panel |

---

## 📂 Project Architecture

```

NCPOR/
│── manage.py
│── db.sqlite3
│
├── ncpor/ # Project configuration
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ ├── asgi.py
│ └── wsgi.py
│
├── ncpordata/ # Core application
│ ├── init.py
│ ├── models.py
│ ├── views.py
│ ├── forms.py
│ ├── admin.py
│ ├── urls.py
│ ├── apps.py
│ └── migrations/
│
├── templates/ # HTML templates
│ ├── base.html
│ ├── form.html
│ ├── preview.html
│ ├── update.html
│ └── list.html
│
├── static/ # CSS, JS, images
│
└── datasets/ # Uploaded datasets / media files

````

---

## ⚙️ How to Run Locally

### 1️⃣ Clone the repository
```bash
git clone <your-repository-link>
cd NCPOR
````

### 2️⃣ Create a virtual environment (recommended)

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```bash
pip install django
```

---

### 4️⃣ Apply database migrations

```bash
python manage.py migrate
```

---

### 5️⃣ Start the development server

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/
```

---

## 👩‍💻 Admin Setup

Create an admin account:

```bash
python manage.py createsuperuser
```

Login here:

```
http://127.0.0.1:8000/admin/
```

From the admin panel, you can:

✔ Add records
✔ Edit entries
✔ Delete data
✔ Manage uploaded files

---

## 💡 What This Project Shows

This application highlights strong understanding of:

* Django project & app structure
* Model design & database relations
* Form handling & validation
* CRUD workflows
* Admin customization
* Media & static file management
* Backend-driven web applications

---

### 📸 Application Workflow

1. User fills in the data using Django forms  
2. User can preview the entered information before final submission  
3. User can edit/update previously submitted records  
4. Data is validated on the server side  
5. Valid information is stored in the database  
6. Admin can review, modify, or delete records  
7. Files/images are mapped to database entries  
8. Data is rendered dynamically in templates  


---

## 🔮 Future Enhancements

* User authentication & authorization
* Role-based dashboards
* REST API development
* Advanced filtering & search
* Data visualization
* Cloud deployment (AWS / Azure / Render)

---

## 🎯 Ideal Use Cases

* Research data collection
* Institutional record keeping
* Dataset repositories
* Internal management systems

---

## 🤝 Contribution

Contributions, suggestions, and improvements are welcome.

---

## 📄 License

Developed for educational and demonstration purposes.

---

## 👩‍💻 Author

**Himani Chauhan**


