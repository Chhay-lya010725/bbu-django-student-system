"""
Django management command for populating sample Khmer student, course, and enrollment data.
"""

from contextlib import redirect_stdout

from django.core.management.base import BaseCommand, CommandError

from courses.models import Course
from enrollments.models import Enrollment
from students.models import Student


class Command(BaseCommand):
    help = 'Populates the database with sample data if it is empty.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--student-count',
            type=int,
            default=100,
            help='Number of sample students to create (default: 100)',
        )
        parser.add_argument(
            '--force',
            action='store_true',
            help='Force re-seeding sample data even if students already exist',
        )

    def handle(self, *args, **options):
        student_count = options['student_count']
        force = options['force']

        self.stdout.write(self.style.MIGRATE_HEADING('Initializing sample data...'))

        existing_students = Student.objects.count()
        existing_courses = Course.objects.count()
        if existing_students == 0 or force:
            self.stdout.write(
                self.style.NOTICE(
                    f'Populating sample data ({student_count} students, courses, and enrollments)...'
                )
            )
            try:
                from scripts.generate_khmer_data import run_seed

                with redirect_stdout(self.stdout):
                    run_seed(student_count)
            except Exception as exc:
                raise CommandError(f'Could not seed sample data: {exc}') from exc

            self.stdout.write(
                self.style.SUCCESS(
                    f'Sample data created: {Student.objects.count()} students, '
                    f'{Course.objects.count()} courses, '
                    f'{Enrollment.objects.count()} enrollments.'
                )
            )
        else:
            self.stdout.write(
                self.style.WARNING(
                    f'Database already contains {existing_students} students and '
                    f'{existing_courses} courses. Skipping seeding (pass --force to re-seed).'
                )
            )

        self.stdout.write(self.style.SUCCESS('Sample data setup completed successfully.'))
