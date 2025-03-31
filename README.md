# Task Manager  

A **Django-based Task Manager** that allows users to manage their tasks efficiently with categories, priorities, and due dates. The application supports authentication, a dashboard with task summaries, and REST API endpoints for task and category management.  

## Table of Contents  

- [Features](#features)  
- [Installation](#installation)  
- [Usage](#usage)  
- [API Endpoints](#api-endpoints)  
- [Project Structure](#project-structure)  
- [Technologies Used](#technologies-used)  
- [Contributing](#contributing)  
- [License](#license)  

## Features  

- User Authentication (Register, Login, Logout)  
- Task Management (Add, Edit, Delete, Mark as Completed)  
- Task Categories (Assign multiple categories to tasks)  
- Task Priorities (High, Medium, Low)  
- Due Dates & Status Filtering (Pending/Completed)  
- Dashboard with Task Summary  
- REST API for Tasks & Categories  
- Responsive UI with Bootstrap  
- Task Search & Filtering  

## Installation  

### Prerequisites  

- Python 3.8+  
- Django 5.0+  
- SQLite (default) or PostgreSQL (for production)  

### Setup  

#### Clone the Repository  
```bash
git clone https://github.com/yourusername/task-manager.git  
cd task-manager
```

#### Create a Virtual Environment  
```bash
python -m venv venv  
source venv/bin/activate  # macOS/Linux  
venv\Scripts\activate  # Windows  
```

#### Install Dependencies  
```bash
pip install -r requirements.txt  
```

#### Run Database Migrations  
```bash
python manage.py migrate  
```

#### Create a Superuser (for Admin Panel)  
```bash
python manage.py createsuperuser  
```
Follow the prompts to set up your admin credentials.  

#### Run the Development Server  
```bash
python manage.py runserver  
```

Now visit **http://127.0.0.1:8000/** in your browser!  

## Usage  

### Login & Registration  

- Register a new user at **/register/**  
- Log in at **/login/**  
- Logout at **/logout/**  

### Managing Tasks  

- View tasks on the **Dashboard (/)**  
- Add, Edit, Delete tasks  
- Assign categories & priorities  
- Mark tasks as completed  

### Admin Panel  

- Visit **/admin/** to manage users, tasks, and categories.  

## API Endpoints  

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/tasks/` | Fetch all tasks |
| POST | `/api/tasks/` | Create a new task |
| GET | `/api/tasks/<id>/` | Get task details |
| PUT | `/api/tasks/<id>/` | Update task |
| DELETE | `/api/tasks/<id>/` | Delete task |
| GET | `/api/categories/` | Fetch all categories |
| POST | `/api/categories/` | Create a new category |

Use **Postman** or `curl` to test the API.  

## Project Structure  

```
task-manager/
│── tasks/              # Task app (models, views, serializers, etc.)
│── task_manager/       # Django project settings & URLs
│── templates/          # HTML templates for frontend
│── static/             # Static files (CSS, JS)
│── db.sqlite3          # SQLite database
│── manage.py           # Django management script
│── requirements.txt    # Dependencies list
│── README.md           # Project documentation
```

## Technologies Used  

- **Backend:** Django 5.0, Django REST Framework  
- **Database:** SQLite (default), PostgreSQL (optional)  
- **Frontend:** Bootstrap 5  
- **Authentication:** Django Auth  

## Contributing  

Want to contribute? Follow these steps:  

1. Fork the repository  
2. Create a new branch:  
   ```bash
   git checkout -b feature-name
   ```  
3. Make your changes & commit:  
   ```bash
   git commit -m "Added feature X"
   ```  
4. Push to GitHub:  
   ```bash
   git push origin feature-name
   ```  
5. Open a Pull Request  

## License  

This project is licensed under the **MIT License**.  

---
