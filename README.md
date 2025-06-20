Here's a concise README.md table summarizing your API endpoints:

```markdown
# Course Registration System API

## Authentication Endpoints

| Endpoint | Method | Description | Input | Output |
|----------|--------|-------------|-------|--------|
| `/register/` | POST | Register new user (student/faculty) | username, email, password, user_type, (student_id/faculty_id) | Redirects to dashboard |
| `/login/` | POST | User login | username, password | Redirects to dashboard |
| `/logout/` | GET/POST | User logout | - | Redirects to login |

## User Dashboard Endpoints

| Endpoint | Method | Description | Access |
|----------|--------|-------------|--------|
| `/dashboard/` | GET | Role-based dashboard redirect | All users |
| `/users/student/dashboard/` | GET | Student dashboard view | Students only |
| `/users/faculty/dashboard/` | GET | Faculty dashboard view | Faculty only |

## Course Management Endpoints

| Endpoint | Method | Description | Input (POST) | Access |
|----------|--------|-------------|--------------|--------|
| `/course/` | GET | List all courses | - | All users |
| `/course/<pk>/` | GET | Course details | - | All users |
| `/course/create/` | GET/POST | Create new course | name, code, description, credits | Faculty only |
| `/course/<pk>/update/` | GET/POST | Update course | name, code, description, credits | Faculty only |
| `/course/<pk>/delete/` | GET/POST | Delete course | - | Faculty only |

## Registration Endpoints

| Endpoint | Method | Description | Input (POST) | Access |
|----------|--------|-------------|--------------|--------|
| `/registercourse/` | GET/POST | Register for courses | Selected courses (max 2) | Students only |
| `/unregister/<pk>/` | GET/POST | Unregister from course | - | Students only |
| `/my-courses/` | GET | View registered courses | - | Students only |
```

Key Features:
- Role-based access control (Student/Faculty)
- Course registration limit (max 2 courses per student)
- Unique constraints on student/faculty IDs and course codes
- Form validation for all inputs

To set up:
1. Run migrations
2. Create superuser
3. Access `/admin/` for management
4. Register users via `/register/`