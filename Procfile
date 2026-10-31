web: gunicorn student_system.wsgi:application --bind 0.0.0.0:$PORT --log-file -
release: python manage.py migrate && python manage.py setup_test_data --student-count 100
