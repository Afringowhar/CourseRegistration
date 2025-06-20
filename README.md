


# Course Registration System

A Django-based web application for managing course registrations with separate interfaces for students and faculty.

## Table of Contents
1. [Cloning the Repository](#cloning-the-repository)
2. [Local Setup](#local-setup)
3. [Application Models](#application-models)
4. [File Structure](#file-structure)
5. [Tech Stack](#tech-stack)
6. [Views and Functionalities](#views-and-functionalities)

---

## Cloning the Repository

```bash
git clone https://github.com/Afringowhar/CourseRegistration.git
cd course_registration
```

## Local Setup

### Prerequisites
- Python 3.12+
- PostgreSQL
- pip

### Installation
1. Create and activate virtual environment:
```bash
python3 -m venv env
source env/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up PostgreSQL database:
```sql
CREATE DATABASE course_registration;
CREATE USER crs_user WITH PASSWORD 'password123';
GRANT ALL PRIVILEGES ON DATABASE course_registration TO crs_user;
```

4. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your credentials
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create superuser:
```bash
python manage.py createsuperuser
```

7. Run development server:
```bash
python manage.py runserver
```

Access the application at: http://localhost:8000

## Application Models

### User Models (`users/models.py`)
| Model | Fields | Description |
|-------|--------|-------------|
| User | username, email, password, user_type (student/faculty) | Base user model |
| Student | user (OneToOne), student_id | Extends User |
| Faculty | user (OneToOne), faculty_id | Extends User |

### Course Models (`courses/models.py`)
| Model | Fields | Description |
|-------|--------|-------------|
| Course | name, code, faculty (FK), credits| Course offerings |
| Registration | student (FK), course (FK), registration_date | Enrollment records |

## File Structure

```
course_registration/
├── course_registration/          # Project config
│   ├── __pycache__/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py               # Django settings
│   ├── urls.py                   # Main URLs
│   └── wsgi.py
├── users/                        # Auth app
│   ├── __pycache__/
│   ├── migrations/
│   ├── templates/
│   │   └── users/
│   │       ├── faculty_dashboard.html
│   │       ├── login_register.html
│   │       └── student_dashboard.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── decorators.py
│   ├── forms.py
│   ├── models.py                 # User models
│   ├── tests.py
│   ├── urls.py                   # User URLs
│   └── views.py                  # Auth views
├── courses/                      # Courses app
│   ├── __pycache__/
│   ├── migrations/
│   ├── templates/
│   │   └── courses/
│   │       ├── course_confirm_delete.html
│   │       ├── course_detail.html
│   │       ├── course_form.html
│   │       ├── course_list.html
│   │       ├── my_courses.html
│   │       ├── registration_form.html
│   │       └── unregister_confirm.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py                 # Course models
│   ├── tests.py
│   ├── urls.py                   # Course URLs
│   └── views.py                  # Course views
├── templates/                    # Base templates
│   └── base.html
├── static/                       # Static files
├── env/                          # Virtual environment
├── .gitignore
├── manage.py                     # Django CLI
├── README.md
└── requirements.txt              # Dependencies
```

## Tech Stack

| Component | Technology |
|-----------|------------|
| Backend | Django 5.0 |
| Database | PostgreSQL |
| Frontend | Bootstrap 5 |
| Authentication | Django Auth |

## Views and Functionalities

### Authentication Views
| URL Route | View | Description | Access |
|-----------|------|-------------|--------|
| `/login/` | `user_login` | Login page | Public |
| `/register/` | `register` | Registration page | Public |
| `/logout/` | `LogoutView` | Logout handler | Authenticated |

### Student Views
| URL Route | View | Description |
|-----------|------|-------------|
| `/student/dashboard/` | `student_dashboard` | Student homepage |
| `/courses/` | `course_list` | Browse all courses |
| `/courses/register/` | `register_courses` | Course registration |
| `/courses/my-courses/` | `my_courses` | Registered courses |
| `/courses/unregister/<pk>/` | `unregister_course` | Drop a course |

### Faculty Views
| URL Route | View | Description |
|-----------|------|-------------|
| `/faculty/dashboard/` | `faculty_dashboard` | Faculty homepage |
| `/courses/create/` | `create_course` | Add new course |
| `/courses/<pk>/update/` | `update_course` | Edit course |
| `/courses/<pk>/delete/` | `delete_course` | Remove course |

### Common Views
| URL Route | View | Description |
|-----------|------|-------------|
| `/courses/<pk>/` | `course_detail` | Course details page |
| `/dashboard/` | `dashboard` | Role-based redirect |

---