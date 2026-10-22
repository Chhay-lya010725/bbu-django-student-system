from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from students.models import Student
from courses.models import Course
from enrollments.models import Enrollment
from datetime import date

class EnrollmentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='student1', password='password123')
        self.student = Student.objects.create(
            user=self.user,
            student_id='STU301',
            date_of_birth=date(2000, 3, 10),
            gender='M',
            address='Street 1',
            city='Phnom Penh',
            country='Cambodia'
        )
        self.course = Course.objects.create(
            code='CS401',
            title='Software Engineering',
            description='Software engineering principles',
            credits=3,
            level='400',
            capacity=30,
            status='ACTIVE',
            start_date=date(2024, 1, 1),
            end_date=date(2024, 6, 1),
        )

    def test_grade_calculation(self):
        enrollment = Enrollment.objects.create(
            student=self.student,
            course=self.course,
            score=92.5
        )
        self.assertEqual(enrollment.grade, 'A')

    def test_grade_recalculates_when_score_changes_including_zero(self):
        enrollment = Enrollment.objects.create(
            student=self.student,
            course=self.course,
            score=92.5
        )
        enrollment.score = 0
        enrollment.save()
        self.assertEqual(enrollment.grade, 'F')

        enrollment.score = 85
        enrollment.save()
        self.assertEqual(enrollment.grade, 'B')

    def test_enrollment_str(self):
        enrollment = Enrollment.objects.create(
            student=self.student,
            course=self.course,
            score=75
        )
        self.assertEqual(str(enrollment), 'STU301 - CS401')


class EnrollmentViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin = User.objects.create_superuser(username='admin_user', password='password123', email='admin@test.com')
        self.user = User.objects.create_user(username='student2', password='password123')
        self.student = Student.objects.create(
            user=self.user,
            student_id='STU302',
            date_of_birth=date(2000, 3, 10),
            gender='F',
            address='Street 2',
            city='Battambang',
            country='Cambodia'
        )
        self.course = Course.objects.create(
            code='CS402',
            title='Database Systems',
            description='SQL and NoSQL',
            credits=3,
            level='400',
            capacity=30,
            status='ACTIVE',
            start_date=date(2024, 1, 1),
            end_date=date(2024, 6, 1),
        )
        self.enrollment = Enrollment.objects.create(
            student=self.student,
            course=self.course,
            score=88.0,
            status='COMPLETED'
        )

    def test_enrollment_list_requires_login(self):
        response = self.client.get(reverse('enrollments:enrollment_list'))
        self.assertEqual(response.status_code, 302)

    def test_enrollment_list_authenticated(self):
        self.client.login(username='admin_user', password='password123')
        response = self.client.get(reverse('enrollments:enrollment_list'))
        self.assertEqual(response.status_code, 200)

    def test_student_transcript_view(self):
        self.client.login(username='admin_user', password='password123')
        response = self.client.get(reverse('enrollments:student_transcript', kwargs={'student_id': self.student.student_id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'CS402')

    def test_enrollment_create_view_searchable_dropdown(self):
        self.client.login(username='admin_user', password='password123')
        response = self.client.get(reverse('enrollments:enrollment_create'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'tom-select.bootstrap5.min.css')
        self.assertContains(response, 'tom-select.complete.min.js')
        self.assertContains(response, 'id_student')
        self.assertContains(response, 'id_course')

        # Test creating a new enrollment
        new_course = Course.objects.create(
            code='CS403', title='Cloud Computing', description='AWS/GCP',
            credits=3, level='400', capacity=30, status='ACTIVE',
            start_date=date(2024, 1, 1), end_date=date(2024, 6, 1)
        )
        post_response = self.client.post(reverse('enrollments:enrollment_create'), {
            'student': self.student.pk,
            'course': new_course.pk,
            'status': 'ENROLLED',
        })
        self.assertEqual(post_response.status_code, 302)
        self.assertTrue(Enrollment.objects.filter(student=self.student, course=new_course).exists())

    def test_student_can_view_own_transcript(self):
        self.client.login(username='student2', password='password123')
        response = self.client.get(reverse('enrollments:student_transcript', kwargs={'student_id': self.student.student_id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'CS402')

    def test_student_cannot_view_other_student_transcript(self):
        other_user = User.objects.create_user(username='other_student', password='password123')
        self.client.login(username='other_student', password='password123')
        response = self.client.get(reverse('enrollments:student_transcript', kwargs={'student_id': self.student.student_id}))
        self.assertEqual(response.status_code, 403)

    def test_regular_student_cannot_create_enrollment(self):
        self.client.login(username='student2', password='password123')
        response = self.client.get(reverse('enrollments:enrollment_create'))
        self.assertEqual(response.status_code, 403)

