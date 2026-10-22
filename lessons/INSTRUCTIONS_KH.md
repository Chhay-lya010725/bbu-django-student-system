# 📚 ការបង្កើតប្រព័ន្ធគ្រប់គ្រងនិស្សិត Django
# (Complete Step-by-Step Guide: Building Django Student Management System from Scratch)

**សាកលវិទ្យាល័យ បៀលប្រាយ (Build Bright University - BBU)**  
**មហាវិទ្យាល័យវិទ្យាសាស្ត្រ និងបច្ចេកវិទ្យា (Faculty of Science & Technology)**  
**មុខវិជ្ជា៖ Python Project (Web Development with Django)**

---

## 🎯 សេចក្តីផ្តើម និងគោលបំណង (Project Overview)

ប្រព័ន្ធគ្រប់គ្រងនិស្សិត (**Student Management System**) នេះ គឺជាគម្រោង Full-Stack Web Application បង្កើតឡើងដោយប្រើប្រាស់ **Django Framework** (កំណែ 4.2 LTS) រួមជាមួយ **Django REST Framework**។ គម្រោងនេះត្រូវបានរចនាឡើងយ៉ាងពិសេសដើម្បីបង្រៀននិស្សិតអំពីស្ថាបត្យកម្ម **MVT (Model-View-Template)** ទំនើប ការរៀបចំទិន្នន័យជាភាសាខ្មែរ ការបញ្ចូលរូបថត Avatar ការគ្រប់គ្រងវគ្គសិក្សា និងការចុះឈ្មោះព្រមទាំងការគណនាពិន្ទុ GPA ដោយស្វ័យប្រវត្តិ។

---

## 🗺️ ផែនទីបង្ហាញផ្លូវនៃការបង្កើតគម្រោង (12-Step Implementation Roadmap)

```
[ជំហានទី ១] បង្កើត Virtual Environment & Django Project
     │
[ជំហានទី ២] កំណត់ Settings, .env, Khmer Localization & Apps
     │
[ជំហានទី ៣] បង្កើត Data Models (Students, Courses, Enrollments)
     │
[ជំហានទី ៤] ដំណើរការ Database Migrations (SQLite / PostgreSQL)
     │
[ជំហានទី ៥] បង្កើត Forms & ModelForms ជាមួយ Validation
     │
[ជំហានទី ៦] សរសេរ View Logic (FBVs និង CBVs)
     │
[ជំហានទី ៧] រៀបចំ URL Routing តាម App នីមួយៗ
     │
[ជំហានទី ៨] បង្កើត UI Templates ជាមួយ Bootstrap 5 & Inheritance
     │
[ជំហានទី ៩] រៀបចំ Static Files (CSS/JS) & Media Files (Avatar Upload)
     │
[ជំហានទី ១០] កំណត់រចនាសម្ព័ន្ធ Django Admin Panel & Auth
     │
[ជំហានទី ១១] បង្កើត REST API (Serializers, ViewSets, Routers)
     │
[ជំហានទី ១២] បង្កើត Seed Script ជាភាសាខ្មែរ & Automated Tests
```

---

## ជំហានទី ១៖ បង្កើត Virtual Environment និងគម្រោង Django

### ១.១ បង្កើត និងដំណើរការ Virtual Environment
Virtual Environment ជួយញែក Dependencies របស់គម្រោងដាច់ដោយឡែកពី Python របស់ប្រព័ន្ធកុំព្យូទ័រ៖

```bash
# ១. បង្កើតថតគម្រោង ហើយចូលទៅក្នុងថតនោះ
mkdir django_lesson
cd django_lesson

# ២. បង្កើត Virtual Environment ឈ្មោះ venv
python3 -m venv venv

# ៣. ដំណើរការ Virtual Environment
# នៅលើ macOS / Linux:
source venv/bin/activate
# នៅលើ Windows:
venv\Scripts\activate
```

### ១.២ ដំឡើង Dependencies ចាំបាច់
បង្កើតឯកសារ `requirements.txt` ដោយមានកញ្ចប់បណ្ណាល័យសំខាន់ៗ៖

```text
Django>=4.2,<5.0
djangorestframework>=3.14.0
python-decouple>=3.8
Pillow>=10.0.0
whitenoise>=6.5.0
django-filter>=23.2
```

ដំណើរការដំឡើងតាមរយៈ pip៖
```bash
pip install -r requirements.txt
```

### ១.៣ បង្កើត Django Project និង Apps ទាំង ៣
```bash
# បង្កើត Project មេ ឈ្មោះ student_system (សញ្ញាចុច '.' មានន័យថាបង្កើតក្នុងថតបច្ចុប្បន្ន)
django-admin startproject student_system .

# បង្កើត Apps ឯករាជ្យទាំង ៣
python manage.py startapp students
python manage.py startapp courses
python manage.py startapp enrollments
```

---

## ជំហានទី ២៖ ការកំណត់រចនាសម្ព័ន្ធ `student_system/settings.py`

### ២.១ បង្កើតឯកសារ `.env` សម្រាប់រក្សាសុវត្ថិភាព
កុំសរសេរ `SECRET_KEY` ឬពាក្យសម្ងាត់ Database ផ្ទាល់ក្នុងកូដ! ត្រូវប្រើ `python-decouple`៖

```ini
# .env
DEBUG=True
SECRET_KEY=bbu-super-secret-key-django-p24-lesson-2026-!@#$
ALLOWED_HOSTS=localhost,127.0.0.1,testserver

# Database Settings
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3

# Localization
LANGUAGE_CODE=km
TIME_ZONE=Asia/Phnom_Penh
```

### ២.២ កែប្រែ `student_system/settings.py`

```python
import os
from pathlib import Path
from decouple import config, Csv

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY', default='unsafe-secret-key')
DEBUG = config('DEBUG', default=True, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1,testserver', cast=Csv())

# ចុះឈ្មោះ Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third-Party Apps
    'rest_framework',
    
    # Custom Apps របស់គម្រោង
    'students',
    'courses',
    'enrollments',
]

# Database Configuration
DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE', default='django.db.backends.sqlite3'),
        'NAME': BASE_DIR / config('DB_NAME', default='db.sqlite3'),
    }
}

# ភាសាខ្មែរ និងតំបន់ម៉ោងកម្ពុជា
LANGUAGE_CODE = 'km'
TIME_ZONE = 'Asia/Phnom_Penh'
USE_I18N = True
USE_TZ = True

# Static Files
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Media Files (សម្រាប់រូបថតសិស្ស)
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
```

---

## ជំហានទី ៣៖ ការបង្កើតស្រទាប់ទិន្នន័យ (Data Models)

### ៣.១ App សិស្ស៖ `students/models.py`
Model នេះតភ្ជាប់ជាមួយ `User` តាមរយៈ `OneToOneField` មានឈ្មោះជាភាសាខ្មែរ និងរូបថត Avatar៖

```python
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

class Student(models.Model):
    """Model សម្រាប់ផ្ទុកព័ត៌មាននិស្សិត"""
    
    GENDER_CHOICES = [
        ('M', 'ប្រុស (Male)'),
        ('F', 'ស្រី (Female)'),
        ('O', 'ផ្សេងទៀត (Other)'),
    ]
    
    # One-to-One ភ្ជាប់ជាមួយ Django Built-in User Account
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    student_id = models.CharField(max_length=20, unique=True, help_text="អត្តលេខនិស្សិត (ឧ. BBU2026001)")
    
    # ឈ្មោះជាភាសាខ្មែរ (Primary Name)
    khmer_name = models.CharField(max_length=150, blank=True, default='', verbose_name="ឈ្មោះជាភាសាខ្មែរ")
    
    date_of_birth = models.DateField(verbose_name="ថ្ងៃខែឆ្នាំកំណើត")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="ភេទ")
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="លេខទូរស័ព្ទ")
    address = models.TextField(verbose_name="អាសយដ្ឋាន")
    city = models.CharField(max_length=100, verbose_name="រាជធានី/ខេត្ត")
    country = models.CharField(max_length=100, default='Cambodia', verbose_name="ប្រទេស")
    
    # រូបថតសិស្ស (Media file)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True, verbose_name="រូបថតសិស្ស")
    
    enrollment_date = models.DateField(auto_now_add=True)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, default=0.00,
                              validators=[MinValueValidator(0), MaxValueValidator(4)])
    is_active = models.BooleanField(default=True, verbose_name="ស្ថានភាពសកម្ម")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['student_id']
        verbose_name_plural = "Students"
        indexes = [
            models.Index(fields=['student_id']),
            models.Index(fields=['khmer_name']),
        ]

    def get_primary_name(self):
        """ផ្តល់អាទិភាពបង្ហាញឈ្មោះខ្មែរមុន ប្រសិនបើគ្មាន ទើបបង្ហាញឈ្មោះឡាតាំង"""
        if self.khmer_name:
            return self.khmer_name
        full_name = self.user.get_full_name()
        return full_name if full_name else self.user.username

    def __str__(self):
        return f"{self.student_id} - {self.get_primary_name()}"

    def get_absolute_url(self):
        return reverse('students:student_detail', kwargs={'pk': self.pk})
```

---

### ៣.២ App មុខវិជ្ជា៖ `courses/models.py`
មុខវិជ្ជាត្រូវបានបង្រៀនដោយគ្រូ (`ForeignKey` ទៅ `User`) និងមានកម្រិត Level (`100` ដល់ `400`)៖

```python
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Course(models.Model):
    """Model សម្រាប់ផ្ទុកព័ត៌មានវគ្គសិក្សា/មុខវិជ្ជា"""
    
    LEVEL_CHOICES = [
        ('100', 'ឆ្នាំទី ១ (Beginner)'),
        ('200', 'ឆ្នាំទី ២ (Intermediate)'),
        ('300', 'ឆ្នាំទី ៣ (Advanced)'),
        ('400', 'ឆ្នាំទី ៤ (Expert)'),
    ]
    
    STATUS_CHOICES = [
        ('ACTIVE', 'កំពុងបង្រៀន (Active)'),
        ('INACTIVE', 'ផ្អាក (Inactive)'),
        ('ARCHIVED', 'ទុកជាឯកសារ (Archived)'),
    ]
    
    code = models.CharField(max_length=20, unique=True, help_text="កូដមុខវិជ្ជា (ឧ. IT-101)")
    title = models.CharField(max_length=200, help_text="ឈ្មោះមុខវិជ្ជា")
    description = models.TextField(help_text="ការពិពណ៌នាមុខវិជ្ជា")
    instructor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='courses_taught')
    credits = models.PositiveIntegerField(default=3, help_text="ចំនួនក្រេឌីត")
    level = models.CharField(max_length=3, choices=LEVEL_CHOICES, default='100')
    capacity = models.PositiveIntegerField(default=40, help_text="ចំនួននិស្សិតអតិបរមា")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ACTIVE')
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['code']
        verbose_name_plural = "Courses"

    def __str__(self):
        return f"{self.code} - {self.title}"

    def get_absolute_url(self):
        return reverse('courses:course_detail', kwargs={'pk': self.pk})

    @property
    def is_available(self):
        return self.status == 'ACTIVE'
```

---

### ៣.៣ App ចុះឈ្មោះ៖ `enrollments/models.py`
ភ្ជាប់សិស្ស និងមុខវិជ្ជាចូលគ្នា (`Many-to-Many through Enrollment`) ព្រមទាំងគណនា Grade និង GPA ស្វ័យប្រវត្តិ៖

```python
from django.db import models
from students.models import Student
from courses.models import Course
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

class Enrollment(models.Model):
    """Model សម្រាប់កត់ត្រាការចុះឈ្មោះរៀន និងលទ្ធផលពិន្ទុ"""
    
    STATUS_CHOICES = [
        ('ENROLLED', 'កំពុងរៀន (Enrolled)'),
        ('COMPLETED', 'បានបញ្ចប់ (Completed)'),
        ('DROPPED', 'បោះបង់ (Dropped)'),
        ('SUSPENDED', 'ផ្អាកការសិក្សា (Suspended)'),
    ]
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrollment_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ENROLLED')
    
    grade = models.CharField(max_length=2, blank=True, null=True, help_text="និទ្ទេស (A, B, C, D, F)")
    score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True,
                                validators=[MinValueValidator(0), MaxValueValidator(100)])
    attendance_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0,
                                                validators=[MinValueValidator(0), MaxValueValidator(100)])
    completed_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('student', 'course') # សិស្សម្នាក់មិនអាចចុះឈ្មោះមុខវិជ្ជាដដែលលើសពីម្ដងឡើយ
        ordering = ['-enrollment_date']

    def __str__(self):
        return f"{self.student.student_id} - {self.course.code}"

    def calculate_grade(self):
        """ស្វែងរកនិទ្ទេស Letter Grade ស្វ័យប្រវត្តិផ្អែកលើពិន្ទុជាក់ស្តែង"""
        if self.score is None:
            return None
        if self.score >= 90:
            return 'A'
        elif self.score >= 80:
            return 'B'
        elif self.score >= 70:
            return 'C'
        elif self.score >= 60:
            return 'D'
        else:
            return 'F'

    def save(self, *args, **kwargs):
        """គណនា Grade មុនពេល Save ចូល Database"""
        if self.score is not None and not self.grade:
            self.grade = self.calculate_grade()
        super().save(*args, **kwargs)
```

---

## ជំហានទី ៤៖ ការអនុវត្ត Migrations បង្កើតតារាង Database

ក្រោយពីបង្កើត Models រួចរាល់ សូមដំណើរការ Migration Commands ដូចខាងក្រោម៖

```bash
# ១. បង្កើត migration files
python manage.py makemigrations students
python manage.py makemigrations courses
python manage.py makemigrations enrollments

# ២. អនុវត្តចូលទៅក្នុង Database (SQLite / Postgres)
python manage.py migrate

# ៣. បង្កើត Admin Superuser
python manage.py createsuperuser
# បញ្ចូល Username, Email, និងពាក្យសម្ងាត់ឯកជនរបស់អ្នក
```

---

## ជំហានទី ៥៖ ការបង្កើត Django Forms សម្រាប់ទទួល Input

### ៥.១ App សិស្ស៖ `students/forms.py`
យើងបង្កើត Form ចំនួន ៣៖ Form កែសម្រួលព័ត៌មានផ្ទាល់ខ្លួន, Form ព័ត៌មានគណនី User, និង Form ចុះឈ្មោះសិស្សថ្មី៖

```python
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Student

class StudentForm(forms.ModelForm):
    """Form សម្រាប់កែសម្រួល Profile សិស្ស"""
    class Meta:
        model = Student
        fields = ['student_id', 'khmer_name', 'date_of_birth', 'gender', 
                  'phone_number', 'address', 'city', 'country', 'profile_picture']
        widgets = {
            'student_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'BBU2026001'}),
            'khmer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ឈ្មោះជាភាសាខ្មែរ'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
        }

class UserForm(forms.ModelForm):
    """Form សម្រាប់កែសម្រួល First Name, Last Name, Email របស់ User"""
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class StudentRegistrationForm(UserCreationForm):
    """Form ចុះឈ្មោះសិស្សថ្មី រួមបញ្ចូលទាំង User Account និង Student Profile"""
    khmer_name = forms.CharField(max_length=150, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    student_id = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_of_birth = forms.DateField(required=True, widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    gender = forms.ChoiceField(choices=Student.GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}))
    city = forms.CharField(initial='Phnom Penh', widget=forms.TextInput(attrs={'class': 'form-control'}))
    country = forms.CharField(initial='Cambodia', widget=forms.TextInput(attrs={'class': 'form-control'}))
```

### ៥.២ App មុខវិជ្ជា៖ `courses/forms.py`
```python
from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['code', 'title', 'description', 'instructor', 'credits', 
                  'level', 'capacity', 'status', 'start_date', 'end_date']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'instructor': forms.Select(attrs={'class': 'form-control'}),
            'credits': forms.NumberInput(attrs={'class': 'form-control'}),
            'level': forms.Select(attrs={'class': 'form-control'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
```

### ៥.៣ App ចុះឈ្មោះ៖ `enrollments/forms.py`
```python
from django import forms
from .models import Enrollment

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'course', 'status']
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

class GradeForm(forms.ModelForm):
    """Form សម្រាប់សាស្រ្តាចារ្យបញ្ចូលពិន្ទុ និងវត្តមាន"""
    class Meta:
        model = Enrollment
        fields = ['score', 'attendance_percentage', 'notes']
        widgets = {
            'score': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'max': '100', 'step': '0.01'}),
            'attendance_percentage': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'max': '100'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
```

---

## ជំហានទី ៦៖ ការសរសេរ View Logic (FBVs និង CBVs)

### ៦.១ សរសេរ `students/views.py`
បង្ហាញទាំង Function-Based Views (FBV) និង Class-Based Views (CBV)៖

```python
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Student
from .forms import StudentForm, UserForm, StudentRegistrationForm

# ==================== 1. Function-Based Views ====================

@login_required
def student_list(request):
    """បង្ហាញបញ្ជីសិស្ស ជាមួយមុខងារស្វែងរកតាមឈ្មោះខ្មែរ និង Pagination"""
    search_query = request.GET.get('q', '').strip()
    students_qs = Student.objects.select_related('user').all()
    
    if search_query:
        students_qs = students_qs.filter(
            Q(student_id__icontains=search_query) |
            Q(khmer_name__icontains=search_query) |
            Q(user__first_name__icontains=search_query) |
            Q(user__last_name__icontains=search_query)
        )
    
    paginator = Paginator(students_qs.order_by('student_id'), 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'students/student_list.html', {
        'students': page_obj,
        'page_obj': page_obj,
        'search_query': search_query,
    })

@login_required
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    enrollments = student.enrollments.select_related('course').all()
    return render(request, 'students/student_detail.html', {'student': student, 'enrollments': enrollments})

@login_required
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student_form = StudentForm(request.POST, request.FILES, instance=student)
        user_form = UserForm(request.POST, instance=student.user)
        if student_form.is_valid() and user_form.is_valid():
            student_form.save()
            user_form.save()
            messages.success(request, f"បានកែប្រែទិន្នន័យ {student.student_id} ដោយជោគជ័យ!")
            return redirect('students:student_detail', pk=student.pk)
    else:
        student_form = StudentForm(instance=student)
        user_form = UserForm(instance=student.user)
    
    return render(request, 'students/student_form.html', {
        'student_form': student_form,
        'user_form': user_form,
        'student': student,
    })

def register_student(request):
    """ចុះឈ្មោះគណនីសិស្សថ្មី"""
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            student = Student.objects.create(
                user=user,
                student_id=form.cleaned_data['student_id'],
                khmer_name=form.cleaned_data.get('khmer_name', ''),
                date_of_birth=form.cleaned_data['date_of_birth'],
                gender=form.cleaned_data['gender'],
                phone_number=form.cleaned_data.get('phone_number', ''),
                address=form.cleaned_data['address'],
                city=form.cleaned_data['city'],
                country=form.cleaned_data['country'],
            )
            messages.success(request, "ការចុះឈ្មោះបានជោគជ័យ!")
            login(request, user)
            return redirect('students:student_detail', pk=student.pk)
    else:
        form = StudentRegistrationForm()
    return render(request, 'students/register.html', {'form': form})

# ==================== 2. Class-Based Views ====================

class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'students/student_list.html'
    context_object_name = 'students'
    paginate_by = 20

class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = 'students/student_detail.html'
    context_object_name = 'student'

class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('students:student_list')

    def form_valid(self, form):
        if not hasattr(self.request.user, 'student'):
            form.instance.user = self.request.user
        else:
            student_id = form.cleaned_data.get('student_id', '')
            user, _ = User.objects.get_or_create(username=f"std_{student_id.lower()}")
            form.instance.user = user
        return super().form_valid(form)
```

### ៦.២ សរសេរ Home View ក្នុង `student_system/views.py`
```python
from django.shortcuts import render
from students.models import Student
from courses.models import Course
from enrollments.models import Enrollment

def home(request):
    """ទំព័រដើម បង្ហាញស្ថិតិសរុប"""
    total_students = Student.objects.count()
    active_students = Student.objects.filter(is_active=True).count()
    total_courses = Course.objects.count()
    active_courses = Course.objects.filter(status='ACTIVE').count()
    total_enrollments = Enrollment.objects.count()
    
    return render(request, 'home.html', {
        'total_students': total_students,
        'active_students': active_students,
        'total_courses': total_courses,
        'active_courses': active_courses,
        'total_enrollments': total_enrollments,
    })
```

---

## ជំហានទី ៧៖ ការរៀបចំ URL Routing

### ៧.១ Project Root URLs: `student_system/urls.py`
```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    
    # App URLs
    path('students/', include('students.urls')),
    path('courses/', include('courses.urls')),
    path('enrollments/', include('enrollments.urls')),
    
    # REST API
    path('api/', include('student_system.api_urls')),
]

# Serve Static & Media ក្នុងពេល Development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

### ៧.២ Students URLs: `students/urls.py`
```python
from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('register/', views.register_student, name='register'),
    path('<int:pk>/', views.student_detail, name='student_detail'),
    path('<int:pk>/update/', views.student_update, name='student_update'),
    path('cbv/list/', views.StudentListView.as_view(), name='student_list_cbv'),
    path('cbv/create/', views.StudentCreateView.as_view(), name='student_create_cbv'),
]
```

---

## ជំហានទី ៨៖ ការរៀបចំ Templates និង UI Design

### ៨.១ Master Layout: `templates/base.html`
ប្រើប្រាស់ Bootstrap 5, Khmer Font, និង Static Files Tag:

```html
{% load static %}
<!DOCTYPE html>
<html lang="km">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Student Management System{% endblock %} - BBU</title>
    
    <!-- Bootstrap 5 CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    
    <!-- Custom Static CSS -->
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
    
    {% block extra_css %}{% endblock %}
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary shadow-sm">
        <div class="container">
            <a class="navbar-brand fw-bold" href="{% url 'home' %}">📚 BBU Student System</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav me-auto">
                    <li class="nav-item"><a class="nav-link" href="{% url 'students:student_list' %}">និស្សិត (Students)</a></li>
                    <li class="nav-item"><a class="nav-link" href="{% url 'courses:course_list' %}">មុខវិជ្ជា (Courses)</a></li>
                    <li class="nav-item"><a class="nav-link" href="{% url 'enrollments:enrollment_list' %}">ការចុះឈ្មោះ (Enrollments)</a></li>
                    <li class="nav-item"><a class="nav-link" href="/api/">REST API</a></li>
                </ul>
                <ul class="navbar-nav ms-auto">
                    {% if user.is_authenticated %}
                        <li class="nav-item"><span class="nav-link text-white">👤 {{ user.username }}</span></li>
                        <li class="nav-item"><a class="nav-link btn btn-outline-light btn-sm ms-2" href="{% url 'logout' %}">ចាកចេញ</a></li>
                    {% else %}
                        <li class="nav-item"><a class="nav-link" href="{% url 'login' %}">ចូលប្រើប្រាស់</a></li>
                        <li class="nav-item"><a class="nav-link btn btn-warning btn-sm text-dark ms-2" href="{% url 'students:register' %}">ចុះឈ្មោះ</a></li>
                    {% endif %}
                </ul>
            </div>
        </div>
    </nav>

    <div class="container my-4">
        {% if messages %}
            {% for message in messages %}
                <div class="alert alert-{{ message.tags }} alert-dismissible fade show">
                    {{ message }}
                    <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                </div>
            {% endfor %}
        {% endif %}

        {% block content %}{% endblock %}
    </div>

    <footer class="bg-light text-center py-4 mt-5 border-top">
        <p class="text-muted mb-0">© 2026 Build Bright University - Student Management System</p>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="{% static 'js/main.js' %}"></script>
    {% block extra_js %}{% endblock %}
</body>
</html>
```

### ៨.២ Student List Page: `templates/students/student_list.html`
រចនាតារាងដោយបំបែកជាពីរជួរឈ្មោះ (ឈ្មោះខ្មែរ + ឈ្មោះអង់គ្លេស) និងរូបថត Avatar៖

```html
{% extends 'base.html' %}
{% load static %}

{% block title %}បញ្ជីនិស្សិត{% endblock %}

{% block content %}
<div class="d-flex justify-content-between align-items-center mb-3">
    <h2>👥 បញ្ជីនិស្សិត (Student Directory)</h2>
    <a href="{% url 'students:register' %}" class="btn btn-primary">+ ចុះឈ្មោះសិស្សថ្មី</a>
</div>

<!-- របារស្វែងរក -->
<form method="get" class="row g-2 mb-4">
    <div class="col-md-5">
        <input type="text" name="q" class="form-control" placeholder="ស្វែងរកតាម ID, ឈ្មោះខ្មែរ, ឬឈ្មោះឡាតាំង..." value="{{ search_query }}">
    </div>
    <div class="col-md-2">
        <button type="submit" class="btn btn-outline-secondary w-100">ស្វែងរក</button>
    </div>
</form>

<div class="table-responsive">
    <table class="table table-hover align-middle bg-white shadow-sm rounded">
        <thead class="table-light">
            <tr>
                <th>#</th>
                <th>រូបថត</th>
                <th>Student ID</th>
                <th>ឈ្មោះជាភាសាខ្មែរ</th>
                <th>English Name</th>
                <th>GPA</th>
                <th>សកម្មភាព</th>
            </tr>
        </thead>
        <tbody>
            {% for student in students %}
            <tr>
                <td>{{ forloop.counter }}</td>
                <td>
                    {% if student.profile_picture %}
                        <img src="{{ student.profile_picture.url }}" alt="Avatar" class="rounded-circle" style="width: 42px; height: 42px; object-fit: cover;">
                    {% else %}
                        <div class="rounded-circle bg-secondary text-white d-inline-flex align-items-center justify-content-center" style="width: 42px; height: 42px;">
                            {{ student.get_primary_name|slice:":1" }}
                        </div>
                    {% endif %}
                </td>
                <td><strong>{{ student.student_id }}</strong></td>
                <td><span class="text-primary fw-bold">{{ student.khmer_name|default:"-" }}</span></td>
                <td>{{ student.user.get_full_name|default:student.user.username }}</td>
                <td><span class="badge bg-success">{{ student.gpa }}</span></td>
                <td>
                    <a href="{% url 'students:student_detail' student.pk %}" class="btn btn-sm btn-info text-white">មើល</a>
                    <a href="{% url 'students:student_update' student.pk %}" class="btn btn-sm btn-outline-primary">កែប្រែ</a>
                </td>
            </tr>
            {% empty %}
            <tr>
                <td colspan="7" class="text-center text-muted py-4">មិនមានទិន្នន័យនិស្សិតឡើយ។</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</div>
{% endblock %}
```

---

## ជំហានទី ៩៖ ការរៀបចំ Static Files & Media Files

### ៩.១ Static CSS: `static/css/style.css`
```css
/* Style សម្រាប់អក្សរខ្មែរ និង UI */
body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Kantumruy Pro", sans-serif;
    background-color: #f8fafc;
}
.navbar {
    background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%) !important;
}
```

### ៩.២ Static JS: `static/js/main.js`
```javascript
// បិទ Alert message ដោយស្វ័យប្រវត្តក្រោយ 5 វិនាទី
document.addEventListener('DOMContentLoaded', function() {
    setTimeout(function() {
        document.querySelectorAll('.alert').forEach(function(alert) {
            alert.remove();
        });
    }, 5000);
});
```

---

## ជំហានទី ១០៖ ការកំណត់ Django Admin Panel

នៅក្នុង `students/admin.py` យើងកំណត់ Display, Filter, និង Search Field ឱ្យស្វែងរកតាមឈ្មោះខ្មែរបាន៖

```python
from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'khmer_name', 'get_english_name', 'gender', 'city', 'gpa', 'is_active']
    list_filter = ['is_active', 'gender', 'city']
    search_fields = ['student_id', 'khmer_name', 'user__first_name', 'user__last_name', 'user__username']
    readonly_fields = ['created_at', 'updated_at']
    
    def get_english_name(self, obj):
        return obj.user.get_full_name()
    get_english_name.short_description = "English Name"
```

---

## ជំហានទី ១១៖ ការបង្កើត REST API ជាមួយ DRF

### ១១.១ Serializers: `student_system/serializers.py`
```python
from rest_framework import serializers
from students.models import Student
from courses.models import Course
from enrollments.models import Enrollment

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'student_id', 'khmer_name', 'date_of_birth', 'gender', 
                  'phone_number', 'city', 'country', 'profile_picture', 'gpa', 'is_active']
```

### ១១.២ API ViewSets: `student_system/api_views.py`
```python
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from students.models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['student_id', 'khmer_name', 'user__first_name', 'user__last_name']
    
    @action(detail=True, methods=['get'])
    def transcript(self, request, pk=None):
        student = self.get_object()
        enrollments = student.enrollments.filter(status='COMPLETED')
        return Response({
            'student_id': student.student_id,
            'khmer_name': student.khmer_name,
            'gpa': float(student.gpa),
            'completed_courses': enrollments.count(),
        })
```

### ១១.៣ API Routers: `student_system/api_urls.py`
```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import StudentViewSet, CourseViewSet, EnrollmentViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'enrollments', EnrollmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

---

## ជំហានទី ១២៖ ការបង្កើត Data Seeding Script និង Automated Testing

### ១២.១ Seeding 1,000+ Khmer Students: `scripts/generate_khmer_data.py`
ដំណើរការបង្កើតទិន្នន័យគំរូសិស្សកម្ពុជា ១,០០០ នាក់ មុខវិជ្ជា ២៥ មុខ និងការចុះឈ្មោះ ៣,០០០+ Records៖

```bash
# ដំណើរការតាមរយៈ Django Management Command
python manage.py seed_khmer_data --count 1000

# ឬដំណើរការ Script ផ្ទាល់
python scripts/generate_khmer_data.py
```

### ១២.២ ដំណើរការ Unit Tests
ធានាថាប្រព័ន្ធទាំងមូលដំណើរការគ្មានកំហុស (30 Unit Tests Pass):

```bash
python manage.py test
```

### ១២.៣ ដំណើរការ Development Server
```bash
python manage.py runserver 127.0.0.1:8000
```
- **Web App**: `http://127.0.0.1:8000/`
- **Admin Panel**: `http://127.0.0.1:8000/admin/`
- **REST API**: `http://127.0.0.1:8000/api/`

### ១២.៤ ការគ្រប់គ្រង Git និងការដាក់ឱ្យដំណើរការលើ Cloud (Render & Heroku)
ដើម្បីរៀនពីរបៀប Push កូដឡើង GitHub និង Deploy ទៅកាន់ Cloud (Render ឬ Heroku) ដោយប្រើ PostgreSQL Database និង WhiteNoise សូមអានមគ្គុទ្ទេសក៍ពេញលេញ៖
👉 [មគ្គុទ្ទេសក៍ការគ្រប់គ្រង Git/GitHub និងការដាក់ឱ្យដំណើរការលើ Cloud (Render & Heroku)](file:///Users/thavrakchan/Nextcloud/Work/BBU/Subject/Python/Python%20Project/Lessons_P24/django_lesson/lessons/GIT_AND_DEPLOYMENT_GUIDE_KH.md)

---

## 🌟 សេចក្តីសន្និដ្ឋាន (Conclusion)
តាមរយៈការអនុវត្តតាមជំហានទាំង ១២ នេះ និស្សិតទទួលបានបទពិសោធន៍បង្កើតប្រព័ន្ធគ្រប់គ្រងនិស្សិត **Django Full-Stack** ពិតប្រាកដមួយដែលមានលក្ខណៈសម្បត្តិស្តង់ដារឧស្សាហកម្ម រួមមាន **Database Modeling**, **Validation Forms**, **Custom Views**, **Modern Templates**, **Media Upload**, **REST API**, និង **Automated Testing**!
