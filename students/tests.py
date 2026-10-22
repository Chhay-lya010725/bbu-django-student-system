from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from students.models import Student
from datetime import date

class StudentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='johndoe',
            first_name='John',
            last_name='Doe',
            email='john@example.com',
            password='testpassword123'
        )
        self.student = Student.objects.create(
            user=self.user,
            student_id='STU101',
            date_of_birth=date(2001, 5, 20),
            gender='M',
            phone_number='012345678',
            address='Street 271',
            city='Phnom Penh',
            country='Cambodia'
        )

    def test_student_str(self):
        self.assertEqual(str(self.student), 'STU101 - John Doe')

    def test_student_str_with_khmer_name_as_primary(self):
        self.student.khmer_name = 'សុខ តារា'
        self.student.save()
        self.assertEqual(str(self.student), 'STU101 - សុខ តារា')
        self.assertEqual(self.student.get_primary_name(), 'សុខ តារា')

    def test_student_absolute_url(self):
        self.assertEqual(
            self.student.get_absolute_url(),
            reverse('students:student_detail', kwargs={'pk': self.student.pk})
        )


class StudentViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        # Staff teacher user
        self.user = User.objects.create_user(
            username='teacher',
            password='password123',
            is_staff=True
        )
        self.student = Student.objects.create(
            user=self.user,
            student_id='STU202',
            date_of_birth=date(2002, 1, 1),
            gender='F',
            address='Street 10',
            city='Siem Reap',
            country='Cambodia'
        )
        # Regular student user 1
        self.student_user = User.objects.create_user(
            username='student1',
            password='password123',
            is_staff=False
        )
        self.student_obj = Student.objects.create(
            user=self.student_user,
            student_id='STU801',
            khmer_name='សុខ ចាន់ដារា',
            date_of_birth=date(2003, 2, 2),
            gender='M',
            address='Street 50',
            city='Phnom Penh',
            country='Cambodia'
        )
        # Regular student user 2
        self.other_student_user = User.objects.create_user(
            username='student2',
            password='password123',
            is_staff=False
        )
        self.other_student_obj = Student.objects.create(
            user=self.other_student_user,
            student_id='STU802',
            khmer_name='គង់ សុភា',
            date_of_birth=date(2003, 3, 3),
            gender='F',
            address='Street 60',
            city='Siem Reap',
            country='Cambodia'
        )

    def test_student_list_login_required(self):
        response = self.client.get(reverse('students:student_list'))
        self.assertEqual(response.status_code, 302)

    def test_student_list_authenticated_staff(self):
        self.client.login(username='teacher', password='password123')
        self.student.khmer_name = 'ជា ពិសិដ្ឋ'
        self.student.save()
        response = self.client.get(reverse('students:student_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'STU202')
        self.assertContains(response, 'ជា ពិសិដ្ឋ')
        # Check avatar and two name columns presence
        self.assertContains(response, 'Photo')
        self.assertContains(response, 'Khmer Name')
        self.assertContains(response, 'English Name')

    def test_student_list_search_by_khmer_name(self):
        self.client.login(username='teacher', password='password123')
        self.student.khmer_name = 'ហេង មុនី'
        self.student.save()
        response = self.client.get(reverse('students:student_list') + '?q=មុនី')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'ហេង មុនី')
        self.assertContains(response, 'STU202')

    def test_regular_student_redirected_from_student_list_to_own_profile(self):
        """Regular student cannot browse directory and is redirected to own profile"""
        self.client.login(username='student1', password='password123')
        response = self.client.get(reverse('students:student_list'))
        self.assertRedirects(response, reverse('students:student_detail', kwargs={'pk': self.student_obj.pk}))

    def test_regular_student_cannot_view_other_student_detail(self):
        """Regular student accessing another student's detail receives 403 Forbidden"""
        self.client.login(username='student1', password='password123')
        response = self.client.get(reverse('students:student_detail', kwargs={'pk': self.other_student_obj.pk}))
        self.assertEqual(response.status_code, 403)

    def test_regular_student_can_view_own_detail(self):
        """Regular student can access their own profile detail"""
        self.client.login(username='student1', password='password123')
        response = self.client.get(reverse('students:student_detail', kwargs={'pk': self.student_obj.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'STU801')
        self.assertContains(response, 'សុខ ចាន់ដារា')

    def test_regular_student_cannot_update_other_student(self):
        """Regular student trying to edit another student's profile receives 403 Forbidden"""
        self.client.login(username='student1', password='password123')
        response = self.client.post(reverse('students:student_update', kwargs={'pk': self.other_student_obj.pk}), {
            'student_id': 'STU802',
            'khmer_name': 'ឈ្មោះក្លែងក្លាយ',
            'date_of_birth': '2003-03-03',
            'gender': 'F',
            'address': 'New Address',
            'city': 'Siem Reap',
            'country': 'Cambodia',
            'username': 'student2',
            'first_name': 'Hacked',
            'last_name': 'Account',
            'email': 'student2@example.com'
        })
        self.assertEqual(response.status_code, 403)
        self.other_student_obj.refresh_from_db()
        self.assertNotEqual(self.other_student_obj.khmer_name, 'ឈ្មោះក្លែងក្លាយ')

    def test_regular_student_can_update_own_profile(self):
        """Regular student can edit their own profile"""
        self.client.login(username='student1', password='password123')
        response = self.client.post(reverse('students:student_update', kwargs={'pk': self.student_obj.pk}), {
            'student_id': 'STU801',
            'khmer_name': 'សុខ ចាន់ដារា កែប្រែ',
            'date_of_birth': '2003-02-02',
            'gender': 'M',
            'phone_number': '012111222',
            'address': 'Street 50 Updated',
            'city': 'Phnom Penh',
            'country': 'Cambodia',
            'username': 'student1',
            'first_name': 'Chantara',
            'last_name': 'Sok',
            'email': 'student1@example.com'
        })
        self.assertEqual(response.status_code, 302)
        self.student_obj.refresh_from_db()
        self.assertEqual(self.student_obj.khmer_name, 'សុខ ចាន់ដារា កែប្រែ')

    def test_regular_student_cannot_delete_student(self):
        """Regular student cannot delete other student or themselves"""
        self.client.login(username='student1', password='password123')
        # Attempt to delete other student
        response_other = self.client.post(reverse('students:student_delete', kwargs={'pk': self.other_student_obj.pk}))
        self.assertEqual(response_other.status_code, 403)
        self.assertTrue(Student.objects.filter(pk=self.other_student_obj.pk).exists())

        # Attempt to delete own account
        response_own = self.client.post(reverse('students:student_delete', kwargs={'pk': self.student_obj.pk}))
        self.assertEqual(response_own.status_code, 403)
        self.assertTrue(Student.objects.filter(pk=self.student_obj.pk).exists())

    def test_staff_can_delete_student(self):
        """Staff members are authorized to delete student records"""
        self.client.login(username='teacher', password='password123')
        response = self.client.post(reverse('students:student_delete', kwargs={'pk': self.other_student_obj.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Student.objects.filter(pk=self.other_student_obj.pk).exists())

    def test_student_register_page(self):
        response = self.client.get(reverse('students:register'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Khmer Name')

    def test_student_detail_view(self):
        self.client.login(username='teacher', password='password123')
        self.student.khmer_name = 'កែវ សម្បត្តិ'
        self.student.save()
        response = self.client.get(reverse('students:student_detail', kwargs={'pk': self.student.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'STU202')
        self.assertContains(response, 'កែវ សម្បត្តិ')
        self.assertContains(response, '<strong>English Name:</strong>')
        self.assertContains(response, '<strong>Enrollment Date:</strong>')
        # Ensure no raw unparsed template tags are rendered in HTML
        self.assertNotContains(response, '{{')

    def test_student_cbv_create_and_update(self):
        self.client.login(username='teacher', password='password123')
        # Test CBV create
        response = self.client.post(reverse('students:student_create_cbv'), {
            'student_id': 'STU999',
            'khmer_name': 'សុខ វិបុល',
            'date_of_birth': '2002-04-15',
            'gender': 'M',
            'phone_number': '012999888',
            'address': 'St 123',
            'city': 'Phnom Penh',
            'country': 'Cambodia',
        })
        self.assertEqual(response.status_code, 302)
        created = Student.objects.filter(student_id='STU999').first()
        self.assertIsNotNone(created)
        self.assertEqual(created.khmer_name, 'សុខ វិបុល')

        # Test CBV update
        response_update = self.client.post(reverse('students:student_update_cbv', kwargs={'pk': created.pk}), {
            'student_id': 'STU999',
            'khmer_name': 'សុខ វិបុល រតនៈ',
            'date_of_birth': '2002-04-15',
            'gender': 'M',
            'phone_number': '012999888',
            'address': 'St 123',
            'city': 'Phnom Penh',
            'country': 'Cambodia',
        })
        self.assertEqual(response_update.status_code, 302)
        created.refresh_from_db()
        self.assertEqual(created.khmer_name, 'សុខ វិបុល រតនៈ')


class RootEndpointsTest(TestCase):
    def test_favicon_redirect(self):
        response = self.client.get('/favicon.ico')
        self.assertEqual(response.status_code, 301)
        self.assertIn('favicon.ico', response.get('Location'))

    def test_chrome_devtools_probe(self):
        response = self.client.get('/.well-known/appspecific/com.chrome.devtools.json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {})


class SetupTestDataCommandTest(TestCase):
    def test_setup_test_data_seeds_data_without_creating_admin(self):
        from io import StringIO
        from django.core.management import call_command

        out = StringIO()
        call_command('setup_test_data', student_count=5, stdout=out)
        self.assertFalse(User.objects.filter(username='admin').exists())
        self.assertGreaterEqual(Student.objects.count(), 5)
        self.assertTrue(
            all(not user.has_usable_password() for user in User.objects.all())
        )

    def test_setup_test_data_does_not_modify_existing_admin_account(self):
        from io import StringIO
        from django.core.management import call_command

        admin = User.objects.create_user(
            username='admin',
            password='existing-secure-password',
        )
        call_command('setup_test_data', student_count=5, stdout=StringIO())
        admin.refresh_from_db()

        self.assertTrue(admin.check_password('existing-secure-password'))
        self.assertFalse(admin.is_staff)
        self.assertFalse(admin.is_superuser)
