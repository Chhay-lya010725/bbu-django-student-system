# 📋 មគ្គុទ្ទេសក៍កិច្ចការបុគ្គល (Individual Assignment Guide)
# មុខវិជ្ជា៖ Python Project (Web Development with Django)

**សាកលវិទ្យាល័យ បៀលប្រាយ (Build Bright University - BBU)**  
**មហាវិទ្យាល័យវិទ្យាសាស្ត្រ និងបច្ចេកវិទ្យា (Faculty of Science & Technology)**  
**ថ្នាក់ / ក្រុម (Class): `A1IT-B103`**  
**ប្រធានបទកិច្ចការ (Topic): `Personal Assignment: Python Project Django Student Management System (A1IT-B103)`**  
**វេទិកាដាក់កិច្ចការ (Submission Portal): [https://bbusrithub.site/](https://bbusrithub.site/)**

---

## 📑 មាតិកា (Table of Contents)
1. [គោលបំណង និងទិដ្ឋភាពទូទៅ (Objectives & Overview)](#១-គោលបំណង-និងទិដ្ឋភាពទូទៅ-objectives--overview)
2. [ទំហំការងារ និងលក្ខខណ្ឌតម្រូវ (Scope of Work & Rules)](#២-ទំហំការងារ-និងលក្ខខណ្ឌតម្រូវ-scope-of-work)
3. [គន្លឹះ និងគំនិតកែសម្រួល Interface & Theme (UI/UX Customization)](#៣-គន្លឹះ-និងគំនិតកែសម្រួល-interface--theme)
4. [ដំណាក់កាលអនុវត្តន៍ជាជំហានៗ (Step-by-Step Instructions)](#៤-ដំណាក់កាលអនុវត្តន៍ជាជំហានៗ-step-by-step)
   - [ជំហានទី ១៖ ទាញយក និងដំណើរការគម្រោងលើ Local Machine](#ជំហានទី-១-ទាញយក-និងដំណើរការគម្រោងលើ-local-machine)
   - [ជំហានទី ២៖ កែសម្រួល Interface & Styling](#ជំហានទី-២-កែសម្រួល-interface--styling)
   - [ជំហានទី ៣៖ ដំណើរការតេស្ត និងផ្ទៀងផ្ទាត់មុខងារ](#ជំហានទី-៣-ដំណើរការតេស្ត-និងផ្ទៀងផ្ទាត់មុខងារ)
   - [ជំហានទី ៤៖ បង្កើត GitHub Repository និង Push កូដ](#ជំហានទី-៤-បង្កើត-github-repository-និង-push-កូដ)
   - [ជំហានទី ៥៖ ដាក់ឱ្យដំណើរការលើ Cloud (Deploy on Render)](#ជំហានទី-៥-ដាក់ឱ្យដំណើរការលើ-cloud-deploy-on-render)
   - [ជំហានទី ៦៖ ផ្ទៀងផ្ទាត់ Live Website & Admin Login](#ជំហានទី-៦-ផ្ទៀងផ្ទាត់-live-website--admin-login)
5. [របៀបដាក់កិច្ចការលើ Platform bbusrithub.site (Submission Guide)](#៥-របៀបដាក់កិច្ចការលើ-platform-bbusrithubsite)
6. [តារាងពិន្ទុ និងលក្ខខណ្ឌវាយតម្លៃ (Grading Rubric - 100 Marks)](#៦-តារាងពិន្ទុ-និងលក្ខខណ្ឌវាយតម្លៃ-grading-rubric)
7. [បម្រាម និងកំហុសដែលត្រូវជៀសវាង (Common Pitfalls & Warnings)](#៧-បម្រាម-និងកំហុសដែលត្រូវជៀសវាង-pitfalls--warnings)
8. [ជំនួយ និងសំណួរញឹកញាប់ (FAQ & Support)](#៨-ជំនួយ-និងសំណួរញឹកញាប់-faq--support)

---

## ១. គោលបំណង និងទិដ្ឋភាពទូទៅ (Objectives & Overview)

កិច្ចការបុគ្គលនេះត្រូវបានរៀបចំឡើងដើម្បីវាស់ស្ទង់សមត្ថភាពជាក់ស្តែងរបស់និស្សិតថ្នាក់ **A1IT-B103** ក្នុងការ៖
1. **យល់ដឹងពីស្ថាបត្យកម្ម Django MVT (Model-View-Template)** និងរចនាសម្ព័ន្ធគម្រោងស្តង់ដារវិជ្ជាជីវៈ។
2. **ការកែសម្រួល User Interface (UI/UX)** ដោយប្រើ Bootstrap 5, Custom CSS, និង Modern Aesthetics ដោយរក្សាបាននូវភាពរលូននៃប្រព័ន្ធ។
3. **ការប្រើប្រាស់ Git & GitHub** សម្រាប់ការគ្រប់គ្រង Version Control និង Repository សុវត្ថិភាពខ្ពស់។
4. **ការដាក់ពង្រាយប្រព័ន្ធលើ Cloud Platform (Render)** ដោយប្រើប្រាស់ **Gunicorn**, **WhiteNoise**, និង **PostgreSQL Database**។
5. **ការអនុវត្តវិជ្ជាជីវៈផ្នែក Software Delivery**: ការតេស្តមុនពេលបញ្ចេញ (Pre-flight testing) និងការប្រគល់លទ្ធផលការងារតាមស្តង់ដារ។

---

## ២. ទំហំការងារ និងលក្ខខណ្ឌតម្រូវ (Scope of Work)

### 📌 ក្បួនច្បាប់ស្នូល (Core Rules):
> ### 🟢 អ្វីដែលអ្នកត្រូវកែសម្រួល (Must Customize):
> - **Theme & Color Palette**: ប្តូរពណ៌ចម្បង (Primary color), Gradients, Card styles, Button hover effects។
> - **Branding & Identity**: ប្តូរឈ្មោះ Header, Logo/Favicon, Footer ដោយត្រូវ **ដាក់ឈ្មោះនិស្សិត, អត្តលេខនិស្សិត (Student ID), និងថ្នាក់ A1IT-B103** ឱ្យបានច្បាស់លាស់។
> - **Layout & Hero Section**: កែសម្រួលទំព័រដើម (`templates/home.html`) ឱ្យមានលក្ខណៈប្លែក ស្រស់ស្អាត និងឆ្លុះបញ្ចាំងពីគំនិតច្នៃប្រឌិតផ្ទាល់ខ្លួន។
>
> ### 🔴 អ្វីដែលត្រូវរក្សាទុកដដែល (Must Keep - DO NOT Break):
> - **Django Apps Structure**: ត្រូវរក្សាទុក Apps ចំនួន ៣ ដដែល (`students`, `courses`, `enrollments`)។
> - **Database Models & Relationships**: ហាមលុប Fields ស្នូលក្នុង Models ព្រោះអាចបណ្តាលឱ្យទិន្នន័យចាស់ និង Unit Tests បរាជ័យ។
> - **Core Business Logic**: មុខងារ CRUD (សិស្ស, មុខវិជ្ជា, ការចុះឈ្មោះ), Searchable Dropdown (Tom Select), Transcript Calculation, User Authentication (`/accounts/login/`), និង REST API (`/api/`) ត្រូវតែដំណើរការបានធម្មតា ១០០%។

---

## ៣. គន្លឹះ និងគំនិតកែសម្រួល Interface & Theme

និស្សិតអាចជ្រើសរើសស្ទីលរចនា (Design Theme) ណាមួយដែលខ្លួនពេញចិត្ត ដូចជា៖

### 💡 គំនិត Theme ដែលពេញនិយម៖
1. **Cyberpunk / Dark Neon Theme**:
   - ផ្ទៃខាងក្រោយងងឹត (`#0f172a`), ពណ៌ Neon Cyan (`#06b6d4`), Neon Violet (`#8b5cf6`)
2. **Emerald Modern Academic Theme**:
   - ពណ៌បៃតងត្បូងមរកត (`#059669`), មាសស្រាល (`#f59e0b`), ផ្ទៃសស្អាត (`#f8fafc`)
3. **Royal Navy / Executive University Theme**:
   - ពណ៌ខៀវចាស់កងទ័ពជើងទឹក (`#1e3a8a`), ពណ៌មាស (`#d97706`), ស្រមោលកាតបែប Soft Shadow
4. **Sunset Warm Coral Theme**:
   - ពណ៌ទឹកក្រូចស្រាល (`#f97316`), ផ្កាឈូកស្រាល (`#ec4899`), ផ្ទៃកាតបែប Frosted Glass (Glassmorphism)

### 📂 ឯកសារសំខាន់ៗដែលត្រូវកែសម្រួល UI៖
| ឯកសារ | អ្វីដែលត្រូវកែសម្រួល |
|---|---|
| [templates/base.html](file:///Users/thavrakchan/Nextcloud/Work/BBU/Subject/Python/Python%20Project/Lessons_P24/django_lesson/templates/base.html) | Navbar (Brand, ពណ៌, រូបសញ្ញា), Footer (ឈ្មោះនិស្សិត, ID, ថ្នាក់ A1IT-B103), Favicon |
| [templates/home.html](file:///Users/thavrakchan/Nextcloud/Work/BBU/Subject/Python/Python%20Project/Lessons_P24/django_lesson/templates/home.html) | Hero Banner, ស្វាគមន៍, Statistics Cards (Quick Stats), Feature Highlights |
| [static/css/style.css](file:///Users/thavrakchan/Nextcloud/Work/BBU/Subject/Python/Python%20Project/Lessons_P24/django_lesson/static/css/style.css) | Custom CSS Colors, Fonts, Transitions, Buttons, Borders, Cards |
| `static/images/favicon.ico` | ប្តូររូបតំណាង Icon នៅលើ Tab របស់ Browser តាមចំណង់ចំណូលចិត្ត |

---

## ៤. ដំណាក់កាលអនុវត្តន៍ជាជំហានៗ (Step-by-Step)

### ជំហានទី ១៖ ទាញយក និងដំណើរការគម្រោងលើ Local Machine

១. បើក Terminal លើកុំព្យូទ័ររបស់អ្នក រួចចូលទៅកាន់ Folder ការងារ៖
```bash
# Clone ឬចម្លងគម្រោងមកកាន់ម៉ាស៊ីនរបស់អ្នក
cd path/to/your/projects/django_lesson

# បង្កើត Virtual Environment និង Activate
python3 -m venv venv
source venv/bin/activate        # លើ macOS / Linux
# ឬ venv\Scripts\activate       # លើ Windows

# ដំឡើង dependencies ទាំងអស់
pip install -r requirements.txt

# បង្កើតឯកសារ .env
cp .env.example .env

# Migrate database
python manage.py migrate

# បញ្ចូលទិន្នន័យគំរូ និងបង្កើត Admin user
python manage.py setup_test_data

# សាកល្បង Run Server លើម៉ាស៊ីន
python manage.py runserver
```
បើក Browser ចូលមើល `http://127.0.0.1:8000/` ដើម្បីប្រាកដថាប្រព័ន្ធដំណើរការធម្មតា។

---

### ជំហានទី ២៖ កែសម្រួល Interface & Styling

១. **កែសម្រួល Navbar & Footer ក្នុង [templates/base.html](file:///Users/thavrakchan/Nextcloud/Work/BBU/Subject/Python/Python%20Project/Lessons_P24/django_lesson/templates/base.html)**:
   - បន្ថែមព័ត៌មានអត្តសញ្ញាណរបស់អ្នកក្នុង Footer៖
     ```html
     <footer class="mt-5 py-4 text-center text-muted border-top">
         <p class="mb-1"><strong>BBU Student Management System</strong></p>
         <p class="mb-0">
             អភិវឌ្ឍដោយ៖ <strong>[ឈ្មោះរបស់អ្នក]</strong> | 
             ID: <strong>[អត្តលេខរបស់អ្នក]</strong> | 
             ថ្នាក់៖ <strong>A1IT-B103</strong>
         </p>
         <small>© 2026 Build Bright University - Faculty of Science & Technology</small>
     </footer>
     ```
២. **កែប្រែពណ៌ និងស្ទីលក្នុង [static/css/style.css](file:///Users/thavrakchan/Nextcloud/Work/BBU/Subject/Python/Python%20Project/Lessons_P24/django_lesson/static/css/style.css)**:
   - កែសម្រួល Linear Gradients, Hover effects, និង Card border-radius តាមស្ទីលផ្ទាល់ខ្លួន។
៣. **ដំណើរការប្រមូល static files**:
   ```bash
   python manage.py collectstatic --no-input
   ```

---

### ជំហានទី ៣៖ ដំណើរការតេស្ត និងផ្ទៀងផ្ទាត់មុខងារ

មុនពេល Push ឡើង Git ត្រូវធានាថាអ្នកមិនបានធ្វើឱ្យខូចកូដចាស់ឡើយ ដោយដំណើរការ Automated Test Suite៖
```bash
python manage.py test
```
> **លទ្ធផលត្រូវតែទទួលបាន៖** `Ran 33 tests ... OK` (គ្មាន Error ឬ Failure ឡើយ)។

---

### ជំហានទី ៤៖ បង្កើត GitHub Repository និង Push កូដ

១. ចូលទៅកាន់ [https://github.com](https://github.com) រួចចុច **"New repository"**
   - **Repository name**: `bbu-django-student-system` (ឬឈ្មោះតាមចិត្ត ឧទាហរណ៍ `bbu-student-portal-yourname`)
   - **Visibility**: រើស **Public**
   - **Initialize**: មិនបាច់ធីកអ្វីទាំងអស់ (Uncheck all)
   - ចុច **Create repository**

២. ត្រឡប់មក Terminal ក្នុង Folder គម្រោងរបស់អ្នក៖
```bash
# ពិនិត្យមើល status (ប្រាកដថា .env និង db.sqlite3 មិនជាប់)
git status

# Add ឯកសារទាំងអស់
git add .

# Commit ការកែសម្រួលរបស់អ្នក
git commit -m "feat: customize UI theme and branding for class A1IT-B103"

# ប្តូរ branch ទៅ main
git branch -M main

# ភ្ជាប់ Remote Origin ទៅកាន់ Repo ថ្មីរបស់អ្នក
git remote set-url origin https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git

# Push កូដឡើង GitHub (ប្រើ Token ឬ SSH)
git push -u origin main
```

---

### ជំហានទី ៥៖ ដាក់ឱ្យដំណើរការលើ Cloud (Deploy on Render)

១. ចូលទៅកាន់ [https://dashboard.render.com](https://dashboard.render.com)
២. **បង្កើត PostgreSQL Database (ជម្រើសល្អបំផុត)**:
   - ចុច **New +** ➡️ **PostgreSQL**
   - Name: `bbu-student-db`
   - Plan: **Free** ➡️ ចុច **Create Database**
   - រង់ចាំ Database status បង្ហាញជា **Available** រួច Copy **Internal Database URL**
៣. **បង្កើត Web Service**:
   - ចុច **New +** ➡️ **Web Service**
   - Connect ទៅកាន់ GitHub Repository របស់អ្នក
   - **Name**: ដាក់ឈ្មោះ Web Service របស់អ្នក (ឧ. `bbu-student-yourname`)
   - **Runtime**: `Python 3`
   - **Build Command**: `./build.sh`
   - **Start Command**: `python manage.py migrate && python manage.py setup_test_data --student-count 100 && gunicorn student_system.wsgi:application`
   - **Instance Type**: **Free**
៤. **បញ្ចូល Environment Variables**:
   - `DEBUG`: `False`
   - `SECRET_KEY`: `(បង្កើតអក្សរចៃដន្យវែងៗ)`
   - `DATABASE_URL`: `(Paste Internal Database URL ពីជំហាន Database)`
   - `ALLOWED_HOSTS`: `localhost,127.0.0.1`
   - `CSRF_TRUSTED_ORIGINS`: `https://YOUR_APP_NAME.onrender.com`
៥. ចុច **"Create Web Service"** រួចរង់ចាំ Render ដំណើរការ Build និង Deploy (ប្រហែល ៣-៥ នាទី)។

---

### ជំហានទី ៦៖ ផ្ទៀងផ្ទាត់ Live Website & Admin Login

បន្ទាប់ពី Render បង្ហាញពាក្យ **"Live"**៖
1. ចុចលើ URL របស់ Website (e.g. `https://bbu-student-yourname.onrender.com`)
2. ពិនិត្យមើល៖
   - ទំព័រដើម និង Theme ថ្មីរបស់អ្នកដំណើរការស្អាត
   - ចុចចូល `/admin/` ហើយ Login ដោយប្រើ៖
     - ប្រើ Superuser ដែលបានបង្កើតដោយសុវត្ថិភាពសម្រាប់ Environment នេះ
   - សាកល្បងចុះឈ្មោះសិស្សថ្មី (`/students/register/`)
   - សាកល្បងចុះឈ្មោះមុខវិជ្ជា (`/enrollments/create/`) ដោយប្រើ **Searchable Select**

---

## ៥. របៀបដាក់កិច្ចការលើ Platform bbusrithub.site

នៅពេលអ្នកបានធ្វើការកែសម្រួល និង Deploy ជោគជ័យហើយ សូមចូលទៅដាក់កិច្ចការតាមការណែនាំខាងក្រោម៖

### 🌐 ព័ត៌មានលម្អិតសម្រាប់ដាក់កិច្ចការ៖
- **Website URL**: [https://bbusrithub.site/](https://bbusrithub.site/)
- **ប្រធានបទដែលត្រូវជ្រើសរើស (Topic)**:  
  **`Personal Assignment: Python Project Django Student Management System (A1IT-B103)`**

---

### 📝 គំរូទម្រង់បែបបទដាក់កិច្ចការ (Submission Template)
សូមចម្លង (Copy) ទម្រង់ខាងក្រោមនេះយកទៅបំពេញក្នុងទម្រង់ដាក់កិច្ចការលើ Website [https://bbusrithub.site/](https://bbusrithub.site/)៖

```markdown
### 🎓 ព័ត៌មាននិស្សិត (Student Information)
- ឈ្មោះនិស្សិត (Student Name): [ឈ្មោះជាភាសាខ្មែរ] ([English Full Name])
- អត្តលេខនិស្សិត (Student ID): [e.g. BBU-IT-XXXXXX]
- ថ្នាក់ / ក្រុម (Class/Section): A1IT-B103
- ជំនាញ (Major): Information Technology (IT)
- សាកលវិទ្យាល័យ (University): សាកលវិទ្យាល័យ បៀលប្រាយ (BBU)

### 🔗 តំណភ្ជាប់គម្រោង (Project Links)
- GitHub Repository URL: https://github.com/[YOUR_USERNAME]/[YOUR_REPO_NAME]
- Live Production URL (Render): https://[YOUR_APP_NAME].onrender.com
- Admin URL: https://[YOUR_APP_NAME].onrender.com/admin/
- Admin Account:
  - បង្កើត Superuser ដោយប្រើពាក្យសម្ងាត់ឯកជន មុនចូល Admin

### 🎨 ការកែសម្រួល Interface & Theme (Customization Summary)
- ស្ទីល Theme ដែលបានជ្រើសរើស: [ឧ. Emerald Modern / Dark Neon / Royal Navy]
- ពណ៌ចម្បង (Primary Colors): [ឧ. #059669, #1e3a8a, ...]
- ការកែសម្រួល Navbar & Footer: បានបញ្ចូលឈ្មោះ, អត្តលេខ, និងថ្នាក់ A1IT-B103
- ការកែសម្រួល Hero & Cards: [រៀបរាប់សង្ខេបពីអ្វីដែលអ្នកបានកែច្នៃ]

### ✅ ការផ្ទៀងផ្ទាត់មុខងារ (Self-Verification Checklist)
- [x] Django Structure & Apps (students, courses, enrollments) នៅដដែល
- [x] Searchable Dropdown (Tom Select) ដំណើរការបានរលូន
- [x] Automated Tests: 33/33 Tests Pass
- [x] Production Settings: WhiteNoise, Gunicorn, PostgreSQL
- [x] Admin Login ដំណើរការជោគជ័យ
```

---

## ៦. តារាងពិន្ទុ និងលក្ខខណ្ឌវាយតម្លៃ (Grading Rubric - 100 Marks)

| ល.រ | លក្ខណៈវិនិច្ឆ័យ (Evaluation Criteria) | ពិន្ទុអតិបរមា (Max Marks) | ការពិពណ៌នា |
|:---:|---|:---:|---|
| **១** | **UI/UX & Theme Customization** | **២៥ ពិន្ទុ** | ការកែប្រែ Theme, ពណ៌, Layout, Typography, Navbar, Footer (មានឈ្មោះ និង ID និស្សិតច្បាស់លាស់), និង Hero Section មានភាពទាក់ទាញ និងស្រស់ស្អាត |
| **២** | **Software Functionality & Integrity** | **២៥ ពិន្ទុ** | រក្សារចនាសម្ព័ន្ធ Django បានត្រឹមត្រូវ, មុខងារ CRUD សិស្ស, មុខវិជ្ជា, ការចុះឈ្មោះ, Searchable Dropdown, REST API, និង Unit Tests ដំណើរការគ្មានកំហុស |
| **៣** | **Cloud Deployment on Render** | **២៥ ពិន្ទុ** | Deploy ឡើង Render ដំណើរការបានជោគជ័យ (Live 200 OK), WhiteNoise static files ដើរស្អាត, Database តភ្ជាប់ត្រឹមត្រូវ, Login `/admin/` បាន |
| **៤** | **Git & GitHub Quality** | **១៥ ពិន្ទុ** | GitHub Repo មាន `.gitignore` ត្រឹមត្រូវ (គ្មាន `.env` ឬ `db.sqlite3`), Commit messages មានអត្ថន័យ, Readme រៀបចំបានស្អាត |
| **៥** | **Submission & Documentation** | **១០ ពិន្ទុ** | ដាក់កិច្ចការទាន់ពេលវេលាលើ `https://bbusrithub.site/` លើ Topic ត្រឹមត្រូវ ជាមួយព័ត៌មាន និង Links ពេញលេញ |
| | **ពិន្ទុសរុប (Total)** | **១០០ ពិន្ទុ** | **ពិន្ទុវាយតម្លៃកិច្ចការបុគ្គល** |

---

## ៧. បម្រាម និងកំហុសដែលត្រូវជៀសវាង (Pitfalls & Warnings)

> [!CAUTION]
> ### ⚠️ ការព្រមានសុវត្ថិភាព និងបច្ចេកទេសសំខាន់ៗ៖
> 1. **ដាច់ខាតកុំ Push ឯកសារ `.env` ឡើង GitHub**:
>    - ឯកសារ `.env` ផ្ទុកនូវលេខកូដសម្ងាត់។ ត្រូវប្រាកដថា `.gitignore` មាន `.env` ជានិច្ច!
> 2. **ដាច់ខាតកុំ Push ឯកសារ `db.sqlite3` ឡើង GitHub**:
>    - SQLite ក្នុងម៉ាស៊ីនមិនត្រូវឡើង Git ទេ ព្រោះ Render ប្រើប្រាស់ database ដាច់ដោយឡែក។
> 3. **កុំលុប ឬប្តូរឈ្មោះ Core Models Fields**:
>    - ការប្តូរឈ្មោះ Fields ដូចជា `student_id`, `khmer_name`, `credits`, `grade` អាចបណ្តាលឱ្យ Views និង Tests បរាជ័យ។
> 4. **កុំភ្លេចកំណត់ `CSRF_TRUSTED_ORIGINS` លើ Render**:
>    - ប្រសិនបើភ្លេចបញ្ចូល URL របស់ Render ក្នុង `CSRF_TRUSTED_ORIGINS` អ្នកនឹងជួប Error **403 Forbidden** ពេល Submit Form!

---

## ៨. ជំនួយ និងសំណួរញឹកញាប់ (FAQ & Support)

### សំណួរ ១៖ តើខ្ញុំអាចប្រើ Tailwind CSS ជំនួស Bootstrap 5 បានទេ?
**ចម្លើយ**: គម្រោងនេះត្រូវបានបង្កើតឡើងដោយប្រើ **Bootstrap 5**។ និស្សិតត្រូវបានលើកទឹកចិត្តឱ្យប្រើប្រាស់ **Bootstrap 5 + Custom Vanilla CSS** ក្នុង [static/css/style.css](file:///Users/thavrakchan/Nextcloud/Work/BBU/Subject/Python/Python%20Project/Lessons_P24/django_lesson/static/css/style.css) ដើម្បីកែសម្រួល Theme ជៀសវាងការខូច Format នៃ Components ស្រាប់។

### សំណួរ ២៖ បើ Render បង្ហាញ Error `DisallowedHost` តើត្រូវធ្វើដូចម្តេច?
**ចម្លើយ**: ចូលទៅកាន់ Render Dashboard ➡️ Web Service ➡️ Environment Variables រួចបន្ថែម Domain របស់អ្នកទៅក្នុង `ALLOWED_HOSTS` ឧទាហរណ៍៖ `your-app-name.onrender.com,localhost,127.0.0.1`។

### សំណួរ ៣៖ តើខ្ញុំអាចរកមើលឯកសារណែនាំបច្ចេកទេសលម្អិតបន្ថែមនៅឯណា?
**ចម្លើយ**: ក្នុងថត `lessons/` មានឯកសារមគ្គុទ្ទេសក៍ពេញលេញ៖
- [lessons/INSTRUCTIONS_KH.md](file:///Users/thavrakchan/Nextcloud/Work/BBU/Subject/Python/Python%20Project/Lessons_P24/django_lesson/lessons/INSTRUCTIONS_KH.md) — មេរៀនជំហានទាំង ១២
- [lessons/STATIC_FILES_GUIDE_KH.md](file:///Users/thavrakchan/Nextcloud/Work/BBU/Subject/Python/Python%20Project/Lessons_P24/django_lesson/lessons/STATIC_FILES_GUIDE_KH.md) — មគ្គុទ្ទេសក៍ Static Files
- [lessons/MEDIA_FILES_GUIDE_KH.md](file:///Users/thavrakchan/Nextcloud/Work/BBU/Subject/Python/Python%20Project/Lessons_P24/django_lesson/lessons/MEDIA_FILES_GUIDE_KH.md) — មគ្គុទ្ទេសក៍ Media Files
- [lessons/GIT_AND_DEPLOYMENT_GUIDE_KH.md](file:///Users/thavrakchan/Nextcloud/Work/BBU/Subject/Python/Python%20Project/Lessons_P24/django_lesson/lessons/GIT_AND_DEPLOYMENT_GUIDE_KH.md) — មគ្គុទ្ទេសក៍ Git, GitHub & Render Deployment

---

**ជូនពរនិស្សិតថ្នាក់ A1IT-B103 ទាំងអស់ទទួលបានជោគជ័យ និងទទួលបាននិទ្ទេសល្អក្នុងការអនុវត្តកិច្ចការបុគ្គលនេះ! 🚀**
