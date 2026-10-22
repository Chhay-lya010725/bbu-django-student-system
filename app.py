"""
Application entry-point alias for Cloud platforms (such as Render)
that default to `gunicorn app:app` or `app.py`.
"""
from student_system.wsgi import application

# Expose WSGI application callable as `app`
app = application
