# 🚀 មគ្គុទ្ទេសក៍ការគ្រប់គ្រង Git/GitHub និងការដាក់ឱ្យដំណើរការលើ Cloud (Render & Heroku)
# (Comprehensive Guide to Git, GitHub, and Cloud Deployment on Render & Heroku)

**សាកលវិទ្យាល័យ បៀលប្រាយ (Build Bright University - BBU)**  
**មហាវិទ្យាល័យវិទ្យាសាស្ត្រ និងបច្ចេកវិទ្យា (Faculty of Science & Technology)**  
**មុខវិជ្ជា៖ Python Project (Web Development with Django)**  
**ប្រព័ន្ធ៖ BBU Student Management System**

---

## 📑 មាតិកា (Table of Contents)
1. [ស្ថាបត្យកម្មប្រព័ន្ធ និងគោលគំនិតសំខាន់ៗ (Overview & Architecture)](#១-ស្ថាបត្យកម្មប្រព័ន្ធ-និងគោលគំនិតសំខាន់ៗ-overview--architecture)
2. [សុវត្ថិភាព និងការគ្រប់គ្រងឯកសារ .gitignore (Security & .gitignore Breakdown)](#២-សុវត្ថិភាព-និងការគ្រប់គ្រងឯកសារ-gitignore)
3. [ការរៀបចំ Git និង Push កូដទៅកាន់ GitHub (Git & GitHub Workflow)](#៣-ការរៀបចំ-git-និង-push-កូដទៅកាន់-github)
4. [ការត្រៀមរៀបចំ Django សម្រាប់ Production (Production Readiness)](#៤-ការត្រៀមរៀបចំ-django-សម្រាប់-production)
5. [ការដាក់ឱ្យដំណើរការលើ Render (Deploy to Render - Step by Step)](#៥-ការដាក់ឱ្យដំណើរការលើ-render)
6. [ការដាក់ឱ្យដំណើរការលើ Heroku (Deploy to Heroku - Step by Step)](#៦-ការដាក់ឱ្យដំណើរការលើ-heroku)
7. [ការគ្រប់គ្រង Media Files ក្នុង Production (Cloud Storage)](#៧-ការគ្រប់គ្រង-media-files-ក្នុង-production)
8. [បញ្ហាជួបញឹកញាប់ និងដំណោះស្រាយ (Troubleshooting & FAQs)](#៨-បញ្ហាជួបញឹកញាប់-និងដំណោះស្រាយ-troubleshooting)
9. [បញ្ជីត្រួតពិនិត្យចុងក្រោយ (Pre-Flight & Post-Flight Deployment Checklist)](#៩-បញ្ជីត្រួតពិនិត្យចុងក្រោយ-deployment-checklist)

---

## ១. ស្ថាបត្យកម្មប្រព័ន្ធ និងគោលគំនិតសំខាន់ៗ (Overview & Architecture)

នៅពេលយើងអភិវឌ្ឍកម្មវិធី Django នៅលើម៉ាស៊ីនផ្ទាល់ខ្លួន (Local Development) យើងដំណើរការតាមរយៈ៖
- Web Server: `python manage.py runserver` (សម្រាប់តែ Testing ប៉ុណ្ណោះ មិនអាចទ្រទ្រង់ Real Users ច្រើនបានទេ)
- Database: `SQLite` (db.sqlite3 - ឯកសារ File ក្នុងម៉ាស៊ីន)
- Static/Media Files: Django ផ្តល់ជូនដោយស្វ័យប្រវត្តិពេល `DEBUG=True`

ប៉ុន្តែនៅពេលយើងដាក់ឱ្យដំណើរការលើ **Cloud Production (Render ឬ Heroku)** យើងត្រូវរៀបចំស្ថាបត្យកម្មកម្រិតស្តង់ដារវិជ្ជាជីវៈ (Production Architecture)៖

```
+-----------------------------------------------------------------------------------+
|                                  INTERNET CLIENTS                                 |
|                         (Web Browsers / Mobile Devices)                           |
+-----------------------------------------------------------------------------------+
                                          │  (HTTPS Requests)
                                          ▼
+-----------------------------------------------------------------------------------+
|                              CLOUD PLATFORM (PaaS)                                |
|                              [Render] or [Heroku]                                 |
|                                                                                   |
|  +─────────────────────────────────────────────────────────────────────────────+  |
|  |                   GUNICORN WSGI APPLICATION SERVER                           |  |
|  |          (Multi-worker Python HTTP Server handling production traffic)      |  |
|  +─────────────────────────────────────────────────────────────────────────────+  |
|                                         │                                         |
|                 ┌───────────────────────┴───────────────────────┐                 |
|                 ▼                                               ▼                 |
|  +─────────────────────────────+                 +─────────────────────────────+  |
|  |      DJANGO APPLICATION     |                 |          WHITENOISE         |  |
|  |  - URLs, Views, Models      |                 |  - Serves CSS, JS, Fonts    |  |
|  |  - Khmer Localization       |                 |  - Brotli/Gzip Compression  |  |
|  |  - Authentication & Forms   |                 |  - Browser Cache Headers    |  |
|  +─────────────────────────────+                 +─────────────────────────────+  |
|                 │                                                                 |
+─────────────────┼─────────────────────────────────────────────────────────────────+
                  │ (Database Connection via DATABASE_URL)
                  ▼
+-----------------------------------------------------------------------------------+
|                        MANAGED POSTGRESQL DATABASE                                |
|              (Production-Grade Cloud Relational Database Service)                 |
+-----------------------------------------------------------------------------------+
```

---

## ២. សុវត្ថិភាព និងការគ្រប់គ្រងឯកសារ .gitignore

ឯកសារ `.gitignore` មានសារៈសំខាន់បំផុតសម្រាប់សុវត្ថិភាព និងទំហំរបស់ Codebase លើ Git Repository។

### ⚠️ ការព្រមានសុវត្ថិភាពកម្រិតខ្ពស់ (Critical Security Rule)
> **ដាច់ខាតមិនត្រូវ Push ឯកសារខាងក្រោមនេះចូលទៅក្នុង Git/GitHub ជាដាច់ខាត:**
> 1. 🔐 `.env` — ផ្ទុកនូវ Secret Key, Database Passwords, API Keys។ ប្រសិនបើបែកធ្លាយលើ GitHub សាធារណៈ ជនអនាមិកអាចចូលគ្រប់គ្រង Database ឬ Hack ប្រព័ន្ធរបស់អ្នកបាន!
> 2. 🗄️ `db.sqlite3` — ផ្ទុកនូវទិន្នន័យពិតរបស់អ្នកប្រើប្រាស់ ពាក្យសម្ងាត់ និងទិន្នន័យផ្ទាល់ខ្លួន។
> 3. 🐍 `venv/` — Virtual environment មានទំហំធំរាប់រយ Megabytes និងដំណើរការបានតែលើ OS ម៉ាស៊ីនផ្ទាល់ខ្លួនប៉ុណ្ណោះ។

### រចនាសម្ព័ន្ធឯកសារ `.gitignore` ពេញលេញក្នុងគម្រោងយើង៖

```gitignore
# Byte-compiled / Python cache
__pycache__/
*.py[cod]
*$py.class
*.so
.Python

# Virtual Environments (ទំហំធំ និងមិនត្រូវឡើង Git)
venv/
env/
.venv/
ENV/

# Environment Variables & Secrets (ដាច់ខាតកុំ Push!)
.env
.env.local
.env.*.local
*.env

# SQLite Database (Production ប្រើ PostgreSQL)
*.sqlite3
db.sqlite3
db.sqlite3-journal

# Collected Static Files (WhiteNoise បង្កើតពេល Build)
staticfiles/

# User Uploaded Media Files (រក្សាទុកតែ Folder តាមរយៈ .gitkeep)
media/*
!media/.gitkeep
!media/profiles/
media/profiles/*
!media/profiles/.gitkeep

# Server Logs
*.log
server.log
server_logs/

# IDEs & System Files
.vscode/
.idea/
.DS_Store
Thumbs.db
```

### ឯកសារគំរូ `.env.example` (Environment Template)
ដើម្បីឱ្យអ្នកដទៃ ឬ Server ដឹងថាត្រូវកំណត់ Variable អ្វីខ្លះ យើងបានបង្កើតឯកសារ [.env.example](file:///Users/thavrakchan/Nextcloud/Work/BBU/Subject/Python/Python%20Project/Lessons_P24/django_lesson/.env.example) ដែលគ្មានផ្ទុក Password ពិតប្រាកដឡើយ៖
```bash
# ចម្លង .env.example មកបង្កើតជា .env លើម៉ាស៊ីនផ្ទាល់ខ្លួន
cp .env.example .env
```

---

## ៣. ការរៀបចំ Git និង Push កូដទៅកាន់ GitHub

### ជំហានទី ១៖ កំណត់អត្តសញ្ញាណ Git User (ធ្វើតែម្តងគត់លើម៉ាស៊ីន)
បើអ្នកទើបតែដំឡើង Git ដំបូង សូមកំណត់ឈ្មោះ និង Email របស់អ្នក៖
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@gmail.com"
```

### ជំហានទី ២៖ ចាប់ផ្តើម Git Repository ក្នុងគម្រោង (Git Init)
បើក Terminal ក្នុង Folder គម្រោង `django_lesson/` ហើយវាយ៖
```bash
git init
```

### ជំហានទី ៣៖ ពិនិត្យស្ថានភាពឯកសារ (Git Status)
```bash
git status
```
*ចំណាំ៖ អ្នកនឹងឃើញឯកសារកូដនានា ប៉ុន្តែ **មិនឃើញ** `venv/`, `.env`, ឬ `db.sqlite3` ឡើយ ដោយសារ `.gitignore` បានការពាររួចហើយ។*

### ជំហានទី ៤៖ បន្ថែមឯកសារ និងធ្វើ Commit ដំបូង
```bash
# បន្ថែមឯកសារទាំងអស់ដែលមិនត្រូវបាន ignore
git add .

# ពិនិត្យមើលម្តងទៀត
git status

# Commit ទុកក្នុង Git History
git commit -m "feat: complete BBU student management system with searchable select and deployment readiness"
```

### ជំហានទី ៥៖ បង្កើត Repository ថ្មីនៅលើ GitHub
1. ចូលទៅកាន់ [https://github.com](https://github.com) រួច Login ចូលគណនីរបស់អ្នក
2. ចុចប៊ូតុងពណ៌បៃតង **"New"** (ឬសញ្ញា `+` នៅជ្រុងស្តាំលើ រួចរើស *New repository*)
3. បំពេញព័ត៌មាន៖
   - **Repository name**: `bbu-django-student-system`
   - **Description**: `BBU Student Management System built with Django, Bootstrap 5, and WhiteNoise`
   - **Visibility**: រើស **Public** (ឬ **Private**)
   - **Initialize this repository with**: **ដោះធីក (Uncheck)** លើ *Add a README file*, *.gitignore*, *license* ទាំងអស់ (ពីព្រោះយើងមានរួចហើយក្នុងម៉ាស៊ីន)
4. ចុចប៊ូតុង **"Create repository"**

### ជំហានទី ៦៖ ភ្ជាប់ Local Git ទៅកាន់ GitHub Remote Repository
ចម្លង URL របស់ GitHub Repository របស់អ្នក (ជ្រើសយក HTTPS ឬ SSH)៖
```bash
# ប្តូរឈ្មោះ branch ចម្បងទៅជា main
git branch -M main

# ភ្ជាប់ remote origin (សូមជំនួស username និង repo របស់អ្នក)
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/bbu-django-student-system.git
```

### ជំហានទី ៧៖ Push កូដឡើងទៅកាន់ GitHub
```bash
git push -u origin main
```
*ប្រសិនបើ GitHub សួររកពាក្យសម្ងាត់ សូមប្រើ **Personal Access Token (PAT)** ឬ **GitHub CLI** (`gh auth login`) ឧទាហរណ៍៖ `git remote set-url origin https://ghp_YOUR_TOKEN@github.com/roger-lab-01/bbu-django-student-system.git`។*


---

## ៤. ការត្រៀមរៀបចំ Django សម្រាប់ Production

គម្រោងរបស់យើងត្រូវបានរៀបចំឯកសារចាំបាច់រួចរាល់ ១០០% សម្រាប់ Deploy៖

| ឯកសារ | តួនាទី | មាតិកាសំខាន់ |
|---|---|---|
| [Procfile](file:///Users/thavrakchan/Nextcloud/Work/BBU/Subject/Python/Python%20Project/Lessons_P24/django_lesson/Procfile) | ប្រាប់ Heroku & Render ពីរបៀបដំណើរការ Web Server | `web: gunicorn student_system.wsgi:application --log-file -`<br>`release: python manage.py migrate` |
| [runtime.txt](file:///Users/thavrakchan/Nextcloud/Work/BBU/Subject/Python/Python%20Project/Lessons_P24/django_lesson/runtime.txt) | កំណត់ Python Version លើ Heroku | `python-3.11.9` |
| [build.sh](file:///Users/thavrakchan/Nextcloud/Work/BBU/Subject/Python/Python%20Project/Lessons_P24/django_lesson/build.sh) | Build Script ស្វ័យប្រវត្តសម្រាប់ Render | `pip install -r requirements.txt`<br>`python manage.py collectstatic --no-input`<br>`python manage.py migrate` |
| [render.yaml](file:///Users/thavrakchan/Nextcloud/Work/BBU/Subject/Python/Python%20Project/Lessons_P24/django_lesson/render.yaml) | Blueprint Infrastructure as Code | បង្កើត Web Service + PostgreSQL Database ស្វ័យប្រវត្តិ |
| [requirements.txt](file:///Users/thavrakchan/Nextcloud/Work/BBU/Subject/Python/Python%20Project/Lessons_P24/django_lesson/requirements.txt) | បញ្ជីបណ្ណាល័យ Python | បន្ថែម `dj-database-url` និង `psycopg2-binary` |

### ការកំណត់ក្នុង [student_system/settings.py](file:///Users/thavrakchan/Nextcloud/Work/BBU/Subject/Python/Python%20Project/Lessons_P24/django_lesson/student_system/settings.py)
យើងបានរៀបចំកូដឆ្លាតវៃ (Smart Settings) ដែលស្គាល់បរិស្ថាន Cloud ដោយស្វ័យប្រវត្តិ៖
1. **Database**: ប្រសិនបើមាន `DATABASE_URL` (ពី Render/Heroku Postgres) វានឹងភ្ជាប់ទៅ PostgreSQL ដោយស្វ័យប្រវត្តិ។ បើគ្មានទេ វានឹងដំណើរការ SQLite លើ Local ធម្មតា។
2. **Hosts**: ទទួលយក `RENDER_EXTERNAL_HOSTNAME` ដោយស្វ័យប្រវត្តិ មិនបាច់សរសេរ Hostname ចូលដោយដៃឡើយ។
3. **CSRF Protection**: បន្ថែម `CSRF_TRUSTED_ORIGINS` សម្រាប់ HTTPS Domain ជៀសវាងបញ្ហា Error 403 Forbidden ពេល Submit Form។
4. **Static Files**: ប្រើប្រាស់ `WhiteNoise` ជាមួយ `CompressedStaticFilesStorage` ដើម្បី Compress CSS/JS ឱ្យ Load លឿនបំផុត។

---

## ៥. ការដាក់ឱ្យដំណើរការលើ Render

[Render](https://render.com) គឺជា Cloud Platform ទំនើប ងាយស្រួលប្រើប្រាស់ និងមាន Free Tier ដ៏ពេញនិយមសម្រាប់ Django និង PostgreSQL។

### វិធីសាស្ត្រទី ១៖ ប្រើប្រាស់ Render Blueprint (លឿន និងងាយស្រួលបំផុត ⚡)
ដោយសារយើងបានបង្កើតឯកសារ [render.yaml](file:///Users/thavrakchan/Nextcloud/Work/BBU/Subject/Python/Python%20Project/Lessons_P24/django_lesson/render.yaml) រួចរាល់៖
1. ចូល [https://dashboard.render.com](https://dashboard.render.com)
2. ចុចប៊ូតុង **"New +"** នៅជ្រុងស្តាំលើ រួចជ្រើសរើស **"Blueprint"**
3. ភ្ជាប់គណនី GitHub របស់អ្នក ហើយជ្រើសរើស Repository `bbu-django-student-system`
4. Render នឹងអាន `render.yaml` ដោយស្វ័យប្រវត្តិ ហើយបង្ហាញ៖
   - 1 Web Service (`bbu-student-system`)
   - 1 PostgreSQL Database (`bbu-student-db`)
5. ចុច **"Apply"**។ ប្រព័ន្ធនឹងធ្វើការ Build និង Migrate Database ដោយស្វ័យប្រវត្តិ!

---

### វិធីសាស្ត្រទី ២៖ បង្កើតដោយផ្ទាល់តាម Dashboard (Manual Setup 🛠️)

#### ជំហានទី ៥.១៖ បង្កើត PostgreSQL Database
1. លើ Render Dashboard ចុច **"New +"** ➡️ **"PostgreSQL"**
2. បំពេញព័ត៌មាន៖
   - **Name**: `bbu-postgres-db`
   - **Database**: `bbu_db`
   - **User**: `bbu_admin`
   - **Region**: ជ្រើសរើសជិតបំផុត (e.g., `Singapore`)
   - **Plan**: ជ្រើសរើស **Free**
3. ចុច **"Create Database"**
4. រង់ចាំ ២ នាទីរហូតដល់ Database status បង្ហាញជា **Available**
5. ចុះក្រោមស្វែងរក **"Internal Database URL"** រួចចុច **Copy** ទុក

#### ជំហានទី ៥.២៖ បង្កើត Web Service សម្រាប់ Django
1. ចុច **"New +"** ➡️ **"Web Service"**
2. ជ្រើសរើស **"Build and deploy from a Git repository"** រួចចុច **Connect** លើ repo របស់អ្នក
3. បំពេញការកំណត់ Settings ដូចខាងក្រោម៖
   - **Name**: `bbu-student-portal` (ឬឈ្មោះតាមចិត្ត)
   - **Region**: ដូចគ្នាទៅនឹង Database (e.g., `Singapore`)
   - **Branch**: `main`
   - **Root Directory**: ទុកទទេ (Empty)
   - **Runtime**: `Python 3`
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn student_system.wsgi:application --bind 0.0.0.0:$PORT`
   - **Instance Type**: **Free**

#### ជំហានទី ៥.៣៖ បញ្ចូល Environment Variables
រំកិលចុះក្រោមត្រង់ផ្នែក **"Environment Variables"** រួចចុច **"Add Environment Variable"** បញ្ចូលទិន្នន័យដូចខាងក្រោម៖

| Key (ឈ្មោះ Variable) | Value (តម្លៃ) | ការពន្យល់ |
|---|---|---|
| `PYTHON_VERSION` | `3.11.9` | កំណត់កំណែ Python |
| `DEBUG` | `False` | បិទ Debug សម្រាប់ Production (សុវត្ថិភាពខ្ពស់) |
| `SECRET_KEY` | *(ចុច Generate ឬវាយអក្សរចៃដន្យវែង)* | Key សម្ងាត់សម្រាប់ការពារ CSRF/Sessions |
| `DATABASE_URL` | *(Paste Internal Database URL ដែលបាន Copy ពីជំហាន ៥.១)* | អាសយដ្ឋាន PostgreSQL |
| `ALLOWED_HOSTS` | `localhost,127.0.0.1` | *(Render បន្ថែម `RENDER_EXTERNAL_HOSTNAME` ស្វ័យប្រវត្តិ)* |
| `CSRF_TRUSTED_ORIGINS` | `https://your-service-name.onrender.com` | ដូរតាមឈ្មោះ Web Service របស់អ្នក |

4. ចុចប៊ូតុង **"Create Web Service"**
5. Render នឹងដំណើរការ `./build.sh` (ដំឡើង package, ប្រមូល static files, និង migrate database tables)។
6. នៅពេល build ចប់ អ្នកនឹងឃើញ URL ដូចជា `https://bbu-student-portal.onrender.com`។

#### ជំហានទី ៥.៤៖ បង្កើត Admin Superuser លើ Render
ដើម្បីអាច Login ចូល `/admin/` បាន៖
1. នៅក្នុងផ្ទាំង Web Service លើ Render ចុចលើ Tab **"Shell"**
2. ចុច Connect រួចវាយពាក្យបញ្ជា៖
   ```bash
   python manage.py createsuperuser
   ```
3. បំពេញ Username, Email, និង Password
4. បញ្ចូលទិន្នន័យគំរូ BBU (ជម្រើសបន្ថែម):
   ```bash
   python scripts/generate_khmer_data.py
   ```

---

## ៦. ការដាក់ឱ្យដំណើរការលើ Heroku

[Heroku](https://www.heroku.com) គឺជា Cloud PaaS ដ៏ល្បីល្បាញយូរអង្វែង គាំទ្រការ Deploy តាមរយៈ Git Commands យ៉ាងងាយស្រួល។

### ជំហានទី ៦.១៖ ដំឡើង Heroku CLI
- **លើ macOS**:
  ```bash
  brew tap heroku/brew && brew install heroku
  ```
- **លើ Windows**: ទាញយកកម្មវិធីតម្លើងពី [https://devcenter.heroku.com/articles/heroku-cli](https://devcenter.heroku.com/articles/heroku-cli)

### ជំហានទី ៦.២៖ ចូលគណនី Heroku តាម Terminal
```bash
heroku login
```
*ចុច Enter ដើម្បីបើក Browser និងធ្វើការផ្ទៀងផ្ទាត់ Login។*

### ជំហានទី ៦.៣៖ បង្កើត Heroku App ថ្មី
```bash
# បង្កើត app ថ្មី (ឈ្មោះត្រូវតែ unique ទូទាំងពិភពលោក)
heroku create bbu-student-management-app
```

### ជំហានទី ៦.៤៖ បន្ថែម Heroku PostgreSQL Add-on
```bash
heroku addons:create heroku-postgresql:essential-0
```
*Heroku នឹងបង្កើត PostgreSQL និងកំណត់តម្លៃ `DATABASE_URL` ក្នុង Environment Variable ដោយស្វ័យប្រវត្តិ!*

### ជំហានទី ៦.៥៖ កំណត់ Config Variables (Environment Settings)
កំណត់ Config Vars តាមរយៈ Heroku CLI៖
```bash
# បិទ Debug សម្រាប់ Production
heroku config:set DEBUG=False

# កំណត់ Secret Key
heroku config:set SECRET_KEY="bbu-super-secret-key-production-change-me"

# កំណត់ Allowed Hosts និង CSRF Trusted Origins
heroku config:set ALLOWED_HOSTS="localhost,127.0.0.1,bbu-student-management-app.herokuapp.com"
heroku config:set CSRF_TRUSTED_ORIGINS="https://bbu-student-management-app.herokuapp.com"
```

### ជំហានទី ៦.៦៖ Push កូដទៅកាន់ Heroku ដើម្បី Deploy
```bash
git push heroku main
```
Heroku នឹងអាន [runtime.txt](file:///Users/thavrakchan/Nextcloud/Work/BBU/Subject/Python/Python%20Project/Lessons_P24/django_lesson/runtime.txt) និង [Procfile](file:///Users/thavrakchan/Nextcloud/Work/BBU/Subject/Python/Python%20Project/Lessons_P24/django_lesson/Procfile) រួចដំណើរការ `collectstatic` និង `release: python manage.py migrate` ដោយស្វ័យប្រវត្តិ!

### ជំហានទី ៦.៧៖ បង្កើត Superuser លើ Heroku
```bash
heroku run python manage.py createsuperuser
```

### ជំហានទី ៦.៨៖ បើកមើល Website
```bash
heroku open
```

---

## ៧. ការគ្រប់គ្រង Media Files ក្នុង Production

### ⚠️ ការយល់ដឹងពី Ephemeral Filesystem
ទាំង Render និង Heroku ប្រើប្រាស់ប្រព័ន្ធ **Ephemeral Storage** (ឬ Stateless Containers)។ មានន័យថា៖
- រាល់ពេលដែល Server Restart, Deploy សារជាថ្មី, ឬដេក (Sleep) រាល់ File ដែល User Upload ចូលក្នុង `media/` នឹងត្រូវបាត់បង់!
- ចំណែកឯ **Static Files** (CSS, JS) មិនបាត់បង់ទេ ពីព្រោះវាស្ថិតក្នុង Git Repo និងត្រូវបានបង្កើតឡើងវិញដោយ WhiteNoise។

### ដំណោះស្រាយសម្រាប់ Production ពិតប្រាកដ (Persistent Media Storage)
សម្រាប់រូបភាព Profile របស់និស្សិត និងឯកសារ Upload ដំណោះស្រាយល្អបំផុតគឺការតភ្ជាប់ទៅកាន់ **Cloud Object Storage**:
1. **Cloudinary** (ងាយស្រួលបំផុត មាន Free Tier 25GB): ប្រើ Package `django-cloudinary-storage`
2. **AWS S3** (Amazon Web Services Simple Storage Service): ប្រើ `django-storages` និង `boto3`
3. **Supabase Storage** (Postgres + S3-compatible bucket)

---

## ៨. បញ្ហាជួបញឹកញាប់ និងដំណោះស្រាយ (Troubleshooting & FAQs)

### ❌ បញ្ហាទី ១៖ `DisallowedHost at /`
- **មូលហេតុ**: Domain របស់ Render ឬ Heroku មិនទាន់បានបញ្ចូលក្នុង `ALLOWED_HOSTS`។
- **ដំណោះស្រាយ**: បន្ថែម Domain របស់អ្នកទៅក្នុង Environment Variable `ALLOWED_HOSTS`:
  ```bash
  # លើ Heroku:
  heroku config:set ALLOWED_HOSTS="your-app.herokuapp.com,localhost,127.0.0.1"
  # លើ Render: បន្ថែម your-app.onrender.com ក្នុង Dashboard -> Environment
  ```

### ❌ បញ្ហាទី ២៖ `CSRF verification failed. Request aborted.` (Error 403)
- **មូលហេតុ**: ចាប់ពី Django 4.0 ឡើងទៅ រាល់ Form Submission តាម HTTPS តម្រូវឱ្យមាន `CSRF_TRUSTED_ORIGINS` ត្រូវគ្នាជាមួយ Domain។
- **ដំណោះស្រាយ**: កំណត់ Origin ដែលមាន `https://`:
  ```bash
  CSRF_TRUSTED_ORIGINS=https://your-app.onrender.com,https://your-app.herokuapp.com
  ```

### ❌ បញ្ហាទី ៣៖ Static Files (CSS, JS) បាត់រូបរាង (Broken Design)
- **មូលហេតុ**: មិនទាន់បានដំណើរការ `collectstatic` ឬមិនទាន់ដាក់ `WhiteNoiseMiddleware`។
- **ដំណោះស្រាយ**:
  1. ពិនិត្យមើល [student_system/settings.py](file:///Users/thavrakchan/Nextcloud/Work/BBU/Subject/Python/Python%20Project/Lessons_P24/django_lesson/student_system/settings.py) ថាមាន `'whitenoise.middleware.WhiteNoiseMiddleware'` បន្ទាប់ពី `SecurityMiddleware`។
  2. ពិនិត្យមើលថា `STATIC_ROOT = BASE_DIR / 'staticfiles'` ត្រូវបានកំណត់ត្រឹមត្រូវ។

### ❌ បញ្ហាទី ៤៖ `django.db.utils.OperationalError: no such table`
- **មូលហេតុ**: Database Tables មិនទាន់បាន Migrate លើ PostgreSQL។
- **ដំណោះស្រាយ**:
  - លើ Render: ចូលទៅ Shell រួចរត់ `python manage.py migrate`
  - លើ Heroku: រត់ `heroku run python manage.py migrate`

### ❌ បញ្ហាទី ៥៖ Heroku Application Error (H10 Crash)
- **មូលហេតុ**: Web dyno បរាជ័យក្នុងការ Start ឬមានបញ្ហា Syntax ក្នុង settings/Procfile។
- **ដំណោះស្រាយ**: ពិនិត្យ Logs ភ្លាមៗដើម្បីដឹងពីមូលហេតុពិតប្រាកដ៖
  ```bash
  heroku logs --tail
  ```

### ❌ បញ្ហាទី ៦៖ `ModuleNotFoundError: No module named 'pkg_resources'` (លើ Render)
- **មូលហេតុ**: លើ Python 3.12+ (ឬ Default Linux container លើ Render) កញ្ចប់ `setuptools` មិនត្រូវបានដាក់មកជាមួយតាមលំនាំដើមឡើយ ហើយកំណែចាស់របស់ `gunicorn` (e.g. 20.1.0) ព្យាយាម `import pkg_resources`។
- **ដំណោះស្រាយ**:
  1. ធ្វើបច្ចុប្បន្នភាព [requirements.txt](file:///Users/thavrakchan/Nextcloud/Work/BBU/Subject/Python/Python%20Project/Lessons_P24/django_lesson/requirements.txt) ដោយដំឡើង `gunicorn>=21.2.0` និងបន្ថែម `setuptools>=68.0.0`
  2. ក្នុង [build.sh](file:///Users/thavrakchan/Nextcloud/Work/BBU/Subject/Python/Python%20Project/Lessons_P24/django_lesson/build.sh) បន្ថែមបន្ទាត់៖
     ```bash
     pip install --upgrade pip setuptools
     ```

### ❌ បញ្ហាទី ៧៖ `ModuleNotFoundError: No module named 'app'` (លើ Render)
- **មូលហេតុ**: Render Web Service កំណត់ Start Command លំនាំដើមជា `gunicorn app:app` ដែលស្វែងរកឯកសារឈ្មោះ `app.py` ជំនួសឱ្យ Django WSGI (`student_system.wsgi:application`)។
- **ដំណោះស្រាយ**:
  - **វិធីទី ១ (កែក្នុង Dashboard)**: ចូលទៅកាន់ Render Dashboard ➡️ Web Service ➡️ Settings ➡️ Start Command ប្តូរទៅជា៖
    ```bash
    gunicorn student_system.wsgi:application --bind 0.0.0.0:$PORT
    ```
  - **វិធីទី ២ (ស្វ័យប្រវត្តិ)**: គម្រោងយើងមានឯកសារ [app.py](file:///Users/thavrakchan/Nextcloud/Work/BBU/Subject/Python/Python%20Project/Lessons_P24/django_lesson/app.py) រួចជាស្រេចដែលហៅ `from student_system.wsgi import application as app` ដូច្នេះទោះបី Render រត់ `gunicorn app:app` ឬ `gunicorn student_system.wsgi:application` ក៏ដើរដោយជោគជ័យទាំងពីរ។

---

## ៩. បញ្ជីត្រួតពិនិត្យចុងក្រោយ (Deployment Checklist)

### ✅ Checklist មុនពេល Push ទៅកាន់ GitHub (Pre-Push)
- [x] ឯកសារ [.gitignore](file:///Users/thavrakchan/Nextcloud/Work/BBU/Subject/Python/Python%20Project/Lessons_P24/django_lesson/.gitignore) ត្រូវបានបង្កើត និងមាន `.env`, `db.sqlite3`, `venv/`, `staticfiles/` ត្រឹមត្រូវ
- [x] ឯកសារ [.env.example](file:///Users/thavrakchan/Nextcloud/Work/BBU/Subject/Python/Python%20Project/Lessons_P24/django_lesson/.env.example) មាន Template ពេញលេញ
- [x] ឯកសារ [Procfile](file:///Users/thavrakchan/Nextcloud/Work/BBU/Subject/Python/Python%20Project/Lessons_P24/django_lesson/Procfile) មាន web និង release commands
- [x] ឯកសារ [runtime.txt](file:///Users/thavrakchan/Nextcloud/Work/BBU/Subject/Python/Python%20Project/Lessons_P24/django_lesson/runtime.txt) កំណត់ Python 3.11.9
- [x] ឯកសារ [build.sh](file:///Users/thavrakchan/Nextcloud/Work/BBU/Subject/Python/Python%20Project/Lessons_P24/django_lesson/build.sh) មានសិទ្ធិ Executable (`chmod +x build.sh`)
- [x] ឯកសារ [requirements.txt](file:///Users/thavrakchan/Nextcloud/Work/BBU/Subject/Python/Python%20Project/Lessons_P24/django_lesson/requirements.txt) មាន `gunicorn`, `whitenoise`, `dj-database-url`, `psycopg2-binary`
- [x] រត់ `python manage.py check` និង `python manage.py test` ឃើញ **0 errors, 30 tests OK**

### ✅ Checklist បន្ទាប់ពី Deploy រួចរាល់ (Post-Deployment)
- [ ] ចូលទំព័រដើម Website ពិនិត្យមើល CSS Styling និង Fonts ដំណើរការស្អាត
- [ ] ចូល `/admin/` Login ដោយប្រើ Superuser
- [ ] សាកល្បងចុះឈ្មោះសិស្សថ្មី (`/students/register/`)
- [ ] សាកល្បងបង្កើត Enrollment ថ្មី (`/enrollments/create/`) និងតេស្ត Searchable Dropdown លើ Tom Select
- [ ] ពិនិត្យមើល Response Status 200 ក្នុង Server Logs
