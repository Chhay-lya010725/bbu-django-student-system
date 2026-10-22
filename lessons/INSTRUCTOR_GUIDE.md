# 👨‍🏫 ឧបករណ៍ដែលកាលត្របាក់ សម្រាប់គ្រូ
# 👨‍🏫 Quick Instructor's Guide

## 🎯 គោលបំណង (Purpose)
ឧបករណ៍នេះគឺដើម្បីដែលកាលត្របាក់ដោះស្រាយប្រព័ន្ធគ្រប់គ្រងនិស្សិតក្នុងថ្នាក់របស់អ្នក។

---

## ⚡ Quick Setup (រៀបចំលឿន - 5 min)

```bash
# 1. Open terminal in project folder
cd django_lesson

# 2. Activate environment
source venv/bin/activate

# 3. Run server
python manage.py runserver

# 4. Admin login: http://127.0.0.1:8000/admin/
#    Create a superuser first with: python manage.py createsuperuser
```

---

## 📚 How to Teach (ដូចម្តេច រៀនបង្រៀន)

### Session 1: Architecture & Setup (ផ្នែកទី១)
**Time**: 45 min | **Location**: INSTRUCTIONS_KH.md Part 1

```bash
# Show the project structure
ls -la
tree django_lesson/ -L 2

# Explain settings.py
cat student_system/settings.py | head -50

# Demo: Create new Django project from scratch (live coding)
django-admin startproject demo
cd demo
python manage.py startapp demo_app
```

**Key Teaching Points**:
- ✅ Virtual Environment (why we use it)
- ✅ Django project vs apps
- ✅ settings.py configuration
- ✅ INSTALLED_APPS
- ✅ Database configuration

### Session 2: Models & Database (ផ្នែកទី២)
**Time**: 45 min | **Location**: INSTRUCTIONS_KH.md Part 2

```bash
# Show models
cat students/models.py
cat courses/models.py
cat enrollments/models.py

# Explain relationships
# Open Django Shell
python manage.py shell

# Try ORM commands:
>>> from students.models import Student
>>> from django.contrib.auth.models import User
>>> User.objects.all()
>>> Student.objects.all()
>>> student = Student.objects.first()
>>> student.user.username
```

**Key Teaching Points**:
- ✅ Field types (CharField, IntegerField, etc.)
- ✅ OneToOne vs ForeignKey vs ManyToMany
- ✅ Migrations (makemigrations vs migrate)
- ✅ Django ORM (CREATE, READ, UPDATE, DELETE)
- ✅ Query filtering

### Session 3: Views & URL Routing (ផ្នែកទី៣)
**Time**: 45 min | **Location**: INSTRUCTIONS_KH.md Part 3

```bash
# Show URLs
cat student_system/urls.py
cat students/urls.py

# Show FBV
cat students/views.py | grep "def " | head -10

# Show CBV
cat students/views.py | grep "class " | head -10

# Test URLs
# Visit: http://127.0.0.1:8000/students/
# Visit: http://127.0.0.1:8000/api/students/
```

**Key Teaching Points**:
- ✅ URL routing (path, re_path)
- ✅ FBV (Function-Based Views)
- ✅ CBV (Class-Based Views)
- ✅ URL parameters (<int:pk>, <str:name>)
- ✅ View logic

### Session 4: Templates & Forms (ផ្នែកទី៤)
**Time**: 45 min | **Location**: INSTRUCTIONS_KH.md Part 4

```bash
# Show templates
ls -la templates/
cat templates/base.html
cat templates/home.html

# Show forms
cat students/forms.py
cat courses/forms.py

# Demonstrate form rendering
# Visit: http://127.0.0.1:8000/admin/
# Create new Student via form
```

**Key Teaching Points**:
- ✅ Template tags ({% %}, {{ }})
- ✅ Template inheritance (extends, block)
- ✅ ModelForm
- ✅ Form validation
- ✅ CSRF protection

### Session 5: Admin & Authentication (ផ្នែកទី៥)
**Time**: 45 min | **Location**: INSTRUCTIONS_KH.md Part 5

```bash
# Show admin configuration
cat students/admin.py
cat courses/admin.py

# Visit: http://127.0.0.1:8000/admin/
# - Add new student
# - Edit course
# - Check permissions

# Show auth in views
grep -n "login_required\|LoginRequiredMixin" students/views.py
```

**Key Teaching Points**:
- ✅ Django Admin Panel
- ✅ admin.register() decorator
- ✅ list_display, list_filter, search_fields
- ✅ Authentication (login_required, LoginRequiredMixin)
- ✅ Permissions and Groups

### Session 6: REST API & Deployment (ផ្នែកទី៦)
**Time**: 45 min | **Location**: INSTRUCTIONS_KH.md Part 6

```bash
# Show serializers
cat student_system/serializers.py | head -30

# Show ViewSets
cat student_system/api_views.py | head -30

# Test API endpoints
# Visit: http://127.0.0.1:8000/api/
# Click on different endpoints
# Try curl:
curl http://127.0.0.1:8000/api/students/
curl http://127.0.0.1:8000/api/courses/
```

**Key Teaching Points**:
- ✅ REST API principles
- ✅ Serializers (convert Model to JSON)
- ✅ ViewSets
- ✅ API Authentication
- ✅ Deployment concepts

---

## 🎯 Demo Workflow (ផ្លូវលម្អិតដែលបង្ហាញ)

### 5-Minute Live Demo
```
1. Show home page: http://127.0.0.1:8000/
   → Show statistics (students, courses, enrollments)

2. Show admin: http://127.0.0.1:8000/admin/
   → Sign in with the superuser configured for this environment
   → Create a student
   → Show list, filter, search

3. Show API: http://127.0.0.1:8000/api/
   → Show student list (JSON)
   → Show course data
   → Explain REST concepts

4. Show code: In IDE/Editor
   → models.py structure
   → views.py logic
   → urls.py routing
```

---

## 📋 Assignment Ideas (គំនិតលម្អិត)

### Easy Assignments
1. Add new student via admin
2. Create new course via admin
3. View API endpoints
4. Explore code structure

### Medium Assignments
1. Complete exercises 1-10 from PRACTICE_EXERCISES_KH.md
2. Create student via HTML form
3. Modify template HTML
4. Add CSS styling

### Advanced Assignments
1. Extend models with new fields
2. Create new API endpoint
3. Add custom admin filters
4. Deploy to Render.com

---

## 🔍 Troubleshooting (ដោះស្រាយបញ្ហា)

### Error: "Port already in use"
```bash
# Kill existing process
lsof -ti:8000 | xargs kill -9
# Or use different port:
python manage.py runserver 8001
```

### Error: "ModuleNotFoundError"
```bash
# Ensure venv is activated
source venv/bin/activate
# Reinstall requirements
pip install -r requirements.txt
```

### Error: "Database locked"
```bash
# Remove lock file and restart
rm db.sqlite3
python manage.py migrate
```

### Admin login not working
```bash
# Create superuser again
python manage.py createsuperuser
# Follow prompts
```

---

## 📊 Demo Data Ideas

### Create Sample Data via Admin
1. Add 5-10 students
   - Names: Sophea, Dara, Thandi, etc.
   - Different genders, cities
   - Varying GPA (2.5 to 4.0)

2. Add 3-5 courses
   - CS101, CS102, CS201
   - Different levels (100, 200)
   - Assign instructors

3. Enroll students
   - Each student in 2-3 courses
   - Vary enrollment status
   - Add grades (A, B, C, etc.)

---

## 🎓 Learning Progression for Students

### Week 1
- Read: INSTRUCTIONS_KH.md Part 1-2
- Do: PRACTICE_EXERCISES_KH.md #1-10

### Week 2
- Read: INSTRUCTIONS_KH.md Part 3
- Do: PRACTICE_EXERCISES_KH.md #11-20

### Week 3
- Read: INSTRUCTIONS_KH.md Part 4
- Do: PRACTICE_EXERCISES_KH.md #21-30

### Week 4
- Read: INSTRUCTIONS_KH.md Part 5
- Do: PRACTICE_EXERCISES_KH.md #31-40

### Week 5
- Read: INSTRUCTIONS_KH.md Part 6
- Do: PRACTICE_EXERCISES_KH.md #41-60
- Final project: Extend system

---

## 💡 Pro Tips (ដំបូះប្រឹក្សា)

1. **Show don't tell**: Live coding demos are more engaging than slides
2. **Make mistakes**: Intentionally make errors to show debugging
3. **Interactive**: Let students try typing commands
4. **Real-world**: Relate to actual student management systems
5. **Celebrate success**: Show when students complete exercises

---

## 📞 Support Resources

- **Django Docs**: https://docs.djangoproject.com/
- **DRF Docs**: https://www.django-rest-framework.org/
- **Bootstrap**: https://getbootstrap.com/
- **BBU Course Materials**: INSTRUCTIONS_KH.md + PRACTICE_EXERCISES_KH.md

---

## ✅ Checklist Before Teaching

- [ ] Virtual environment activated
- [ ] Server running without errors
- [ ] Admin user created
- [ ] Can access http://127.0.0.1:8000/
- [ ] Can access http://127.0.0.1:8000/admin/
- [ ] Can access http://127.0.0.1:8000/api/
- [ ] Read INSTRUCTIONS_KH.md
- [ ] Review PRACTICE_EXERCISES_KH.md
- [ ] Test database (add sample data)

---

## 🎬 Sample Lesson Plan (45 min)

**Duration**: 45 minutes  
**Topic**: Introduction to Django Models

```
0-5 min:  Welcome & Overview
          "Today we learn Django Models"

5-15 min: Explain Model Concept
          - Database tables
          - Fields and types
          - Relationships

15-25 min: Live Demo
          - Show Student model code
          - Show in Django Admin
          - Add new student
          - Query in shell

25-35 min: Code Along
          - Students follow
          - Create course together
          - Add fields
          - Run migrations

35-42 min: Practice
          - Students try exercises 1-3
          - Instructor circulates

42-45 min: Summary & Homework
          - Recap key points
          - Assign exercises 4-10
```

---

## 🚀 Ready to Teach!

Everything is set up and ready to use. Start with Session 1 and progress through the 6 sessions. Students will learn Django comprehensively through this complete system.

**Happy Teaching!** 🎓

---

Created by: Build Bright University (BBU)  
Date: October 1, 2024  
Project: Student Management System - Django Full-Stack
