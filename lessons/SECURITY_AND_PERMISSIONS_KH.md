# 🛡️ ការគ្រប់គ្រងសិទ្ធិ និងសុវត្ថិភាពប្រព័ន្ធ (Security & Role-Based Access Control)
## Build Bright University (BBU) - Django Student Management System

---

## 📋 មាតិកា (Table of Contents)
1. [បញ្ហា និងមូលហេតុដើម (Root Cause Analysis)](#១-បញ្ហា-និងមូលហេតុដើម-root-cause-analysis)
2. [ស្ថាបត្យកម្មសិទ្ធិ និងតួនាទី (Role-Based Access Control Architecture)](#២-ស្ថាបត្យកម្មសិទ្ធិ-និងតួនាទី-role-based-access-control-architecture)
3. [ដំណោះស្រាយ និងការកែលម្អ (Implemented Solutions)](#៣-ដំណោះស្រាយ-និងការកែលម្អ-implemented-solutions)
4. [ការការពារតាមស្រទាប់ (Layered Protection Details)](#៤-ការការពារតាមស្រទាប់-layered-protection-details)
5. [ការធ្វើតេស្តផ្ទៀងផ្ទាត់ (Automated Test Verification)](#៥-ការធ្វើតេស្តផ្ទៀងផ្ទាត់-automated-test-verification)

---

## ១. បញ្ហា និងមូលហេតុដើម (Root Cause Analysis)

### ❓ សំណួរ៖ ហេតុអ្វីបានជាគណនីនិស្សិតអាចមើល ផ្លាស់ប្ដូរ កែប្រែ ឬលុបនិស្សិតដទៃបាន?
*(Why could student accounts view, edit, or delete other students?)*

### 🔍 មូលហេតុបច្ចេកទេស៖
1. **ការភាន់ច្រឡំរវាង Authentication និង Authorization:**
   - កូដពីមុនប្រើប្រាស់ត្រឹមតែ `@login_required` ឬ `LoginRequiredMixin`។
   - ក្នុង Django `@login_required` គ្រាន់តែបញ្ជាក់ថាអ្នកប្រើប្រាស់បាន **Log in** ចូលក្នុងប្រព័ន្ធប៉ុណ្ណោះ (`request.user.is_authenticated == True`) ប៉ុន្តែ **មិនបានត្រួតពិនិត្យសិទ្ធិ (Permissions)** ថាតើអ្នកនោះជា **Admin/Staff** ឬជា **Student** ធម្មតានោះទេ។
2. **កង្វះខាត Object-Level Permission Check:**
   - ក្នុង `student_detail(request, pk)` `student_update(request, pk)` និង `student_delete(request, pk)` កូដបានទាញយក `get_object_or_404(Student, pk=pk)` ដោយមិនបានផ្ទៀងផ្ទាត់ថា `request.user == student.user` ឬ `request.user.is_staff` នោះឡើយ។
   - ហេតុដូចនេះ និស្សិតណាក៏ដោយអាចចូលទៅកាន់ URL `/students/<pk>/update/` ឬ `/students/<pk>/delete/` ដើម្បីកែប្រែ ឬលុបទិន្នន័យនិស្សិតដទៃបាន (Insecure Direct Object Reference - IDOR)។
3. **Template UI បង្ហាញប៊ូតុងសកម្មភាពដល់អ្នកប្រើប្រាស់ទាំងអស់:**
   - ក្នុង `student_list.html` និង `student_detail.html` ប៊ូតុង **Edit** និង **Delete** ត្រូវបាន render បង្ហាញដោយគ្មានលក្ខខណ្ឌ `{% if user.is_staff or user == student.user %}`។

---

## ២. ស្ថាបត្យកម្មសិទ្ធិ និងតួនាទី (Role-Based Access Control Architecture)

ប្រព័ន្ធត្រូវបានរៀបចំឡើងវិញដោយបែងចែកតួនាទីជាពីរយ៉ាងច្បាស់លាស់៖

| សកម្មភាព (Action) | សាស្ត្រាចារ្យ/រដ្ឋបាល (Staff/Admin: `is_staff=True`) | និស្សិតធម្មតា (Student: `is_staff=False`) |
| :--- | :--- | :--- |
| **មើលបញ្ជីនិស្សិតទាំងអស់ (`student_list`)** | ✅ មើលបានទាំងអស់ ស្វែងរកបានទូទាំងសាកលវិទ្យាល័យ | ❌ ត្រូវបាន Redirect ទៅកាន់ប្រវត្តិរូបផ្ទាល់ខ្លួនភ្លាមៗ |
| **មើលប្រវត្តិរូបនិស្សិត (`student_detail`)** | ✅ មើលប្រវត្តិរូបនិស្សិតទាំងអស់បាន | 🔒 មើលបានតែប្រវត្តិរូបផ្ទាល់ខ្លួន (អ្នកដទៃ: 403 Forbidden) |
| **កែប្រែព័ត៌មាននិស្សិត (`student_update`)** | ✅ កែប្រែបាននិស្សិតទាំងអស់ | 🔒 កែប្រែបានតែព័ត៌មានខ្លួនឯង (`student_id` ត្រូវបានចាក់សោ) |
| **លុបនិស្សិត (`student_delete`)** | ✅ មានសិទ្ធិលុប | ⛔ ហាមឃាត់ដាច់ខាត (403 Forbidden) |
| **បង្កើតនិស្សិតថ្មី (`cbv/create/`)** | ✅ មានសិទ្ធិបង្កើត | ⛔ ហាមឃាត់ដាច់ខាត (403 Forbidden) |
| **មើល Transcript (`student_transcript`)** | ✅ មើល transcript សិស្សទាំងអស់បាន | 🔒 មើលបានតែ transcript ផ្ទាល់ខ្លួនរបស់ខ្លួនឯង |
| **បង្កើត/កែប្រែ/លុប វគ្គសិក្សា (`courses`)** | ✅ បង្កើត កែប្រែ និងលុបបានតាមតម្រូវការ | ⛔ ហាមឃាត់ដាច់ខាត (403 Forbidden; ប៊ូតុងត្រូវបានលាក់) |
| **មើលបញ្ជីសិស្សក្នុងថ្នាក់ (`course_detail`)** | ✅ មើលឃើញបញ្ជី ឈ្មោះ និងពិន្ទុសិស្សទាំងអស់ | 🔒 ត្រូវបានលាក់ដើម្បីការពារទិន្នន័យផ្ទាល់ខ្លួនរបស់សិស្ស |
| **ដាក់ពិន្ទុ & ចុះឈ្មោះ (`enrollments`)** | ✅ មានសិទ្ធិគ្រប់គ្រង | 🔒 មើលបានតែការចុះឈ្មោះរបស់ខ្លួន (ហាមដាក់ពិន្ទុ/លុប) |

### 🔑 ការបង្កើតគណនីដោយសុវត្ថិភាព

កុំប្រើគណនី ឬពាក្យសម្ងាត់សាកល្បងដែលបានចែករំលែកជាសាធារណៈ។ ពាក្យបញ្ជា `setup_test_data`
បង្កើតតែទិន្នន័យគំរូប៉ុណ្ណោះ ហើយមិនបង្កើត ឬកែប្រែគណនីអ្នកប្រើទេ។ បង្កើត Superuser ផ្ទាល់ខ្លួន៖

```bash
python manage.py createsuperuser
```

---

## ៣. ដំណោះស្រាយ និងការកែលម្អ (Implemented Solutions)

### ក. ការពារ Backend Views (`students/views.py`)
```python
from django.core.exceptions import PermissionDenied

# ១. បញ្ជីឈ្មោះនិស្សិត: បើជានិស្សិតធម្មតា បញ្ជូនទៅកាន់ profile របស់ខ្លួនឯង
@login_required
def student_list(request):
    if not request.user.is_staff:
        if hasattr(request.user, 'student'):
            messages.info(request, "Students can only access their own profile.")
            return redirect('students:student_detail', pk=request.user.student.pk)
        raise PermissionDenied("Only staff members can view the student directory.")
    ...

# ២. មើលលម្អិត: អនុញ្ញាតតែ Staff ឬម្ចាស់គណនីផ្ទាល់
@login_required
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if not request.user.is_staff and student.user != request.user:
        raise PermissionDenied("You are not authorized to view other students' profiles.")
    ...

# ៣. កែប្រែ: អនុញ្ញាតតែ Staff ឬម្ចាស់គណនីផ្ទាល់
@login_required
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if not request.user.is_staff and student.user != request.user:
        raise PermissionDenied("You are not authorized to edit this student profile.")
    ...

# ៤. លុប: អនុញ្ញាតតែ Staff ប៉ុណ្ណោះ
@login_required
def student_delete(request, pk):
    if not request.user.is_staff:
        raise PermissionDenied("Only staff and administrators can delete student records.")
    ...
```

### ខ. ការពារទម្រង់កែប្រែ (`students/forms.py`)
និស្សិតធម្មតាមិនអាចកែប្រែ `student_id` ដោយខ្លួនឯងបានឡើយ៖
```python
class StudentForm(forms.ModelForm):
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user and not user.is_staff and 'student_id' in self.fields:
            self.fields['student_id'].disabled = True
```

### គ. ការពារលើ Class-Based Views (CBV)
ប្រើប្រាស់ `UserPassesTestMixin` លើគ្រប់ CBVs:
```python
class StudentListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    def test_func(self):
        return self.request.user.is_staff

class StudentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    def test_func(self):
        student = self.get_object()
        return self.request.user.is_staff or student.user == self.request.user
```

---

## ៤. ការការពារតាមស្រទាប់ (Layered Protection Details)

### ១. ស្រទាប់ Navigation & Base Template (`templates/base.html`)
- ប្រសិនបើអ្នកប្រើប្រាស់ជានិស្សិត Navbar នឹងបង្ហាញប៊ូតុង **"My Profile"** (ភ្ជាប់ទៅប្រវត្តិរូបផ្ទាល់ខ្លួន) ជំនួសឱ្យ "Students"។
- ប៊ូតុង **"Admin Panel"** បង្ហាញសម្រាប់តែ Staff (`{% if user.is_staff %}`) ប៉ុណ្ណោះ។
- User dropdown មាន shortcuts ទៅកាន់ "👤 My Profile" និង "📄 My Transcript"។

### ២. ស្រទាប់ទំព័រលម្អិត និងតារាង (`student_list.html` & `student_detail.html`)
- ប៊ូតុង **Edit** បង្ហាញតែក្នុងករណី `{% if user.is_staff or user == student.user %}`។
- ប៊ូតុង **Delete** បង្ហាញតែក្នុងករណី `{% if user.is_staff %}`។
- ប៊ូតុង **Add New Student** បង្ហាញតែក្នុងករណី `{% if user.is_staff %}`។

### ៣. ទំព័រ 403 Forbidden ស្អាតស្អំ (`templates/403.html`)
នៅពេលអ្នកប្រើប្រាស់គ្មានសិទ្ធិត្រូវបានបដិសេធ ប្រព័ន្ធនឹងបង្ហាញទំព័រ 403 យ៉ាងស្រស់ស្អាតជាភាសាខ្មែរ និងអង់គ្លេស រួមជាមួយប៊ូតុងត្រឡប់ទៅកាន់ Profile ផ្ទាល់ខ្លួន ឬទំព័រដើម។

---

## ៥. ការធ្វើតេស្តផ្ទៀងផ្ទាត់ (Automated Test Verification)

គ្រប់លក្ខខណ្ឌទាំងអស់ត្រូវបានសរសេរ និងផ្ទៀងផ្ទាត់តាមរយៈ Django Test Suite (`students/tests.py` & `enrollments/tests.py`)៖

```bash
./venv/bin/python manage.py test
```

### លទ្ធផលតេស្ត (Test Cases Verified):
- ✅ `test_regular_student_redirected_from_student_list_to_own_profile`: និស្សិតចូលទៅ `student_list` ត្រូវបាន redirect ទៅកាន់ profile ខ្លួនឯងដោយសុវត្ថិភាព។
- ✅ `test_regular_student_cannot_view_other_student_detail`: និស្សិតចូលមើល profile អ្នកដទៃ ទទួលបាន **HTTP 403 Forbidden**។
- ✅ `test_regular_student_can_view_own_detail`: និស្សិតអាចមើល profile ខ្លួនឯងបានជោគជ័យ (**HTTP 200**)。
- ✅ `test_regular_student_cannot_update_other_student`: និស្សិតកែប្រែ profile អ្នកដទៃ ទទួលបាន **HTTP 403 Forbidden**។
- ✅ `test_regular_student_can_update_own_profile`: និស្សិតអាចកែប្រែ profile ខ្លួនឯងបានជោគជ័យ (**HTTP 302**)。
- ✅ `test_regular_student_cannot_delete_student`: និស្សិតមិនអាចលុប profile អ្នកដទៃ ឬខ្លួនឯងបានឡើយ (**HTTP 403 Forbidden** ទាំងសងខាង)។
- ✅ `test_staff_can_delete_student`: Staff មានសិទ្ធិគ្រប់គ្រាន់ក្នុងការលុបទិន្នន័យ។
- ✅ `test_student_cannot_view_other_student_transcript`: និស្សិតមិនអាចលួចមើល Transcript អ្នកដទៃបានឡើយ (**HTTP 403 Forbidden**)។
