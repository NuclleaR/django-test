import os
import django
from faker import Faker

from achievements.models import Achievement

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'appfeedback.settings')
django.setup()

fakegen = Faker()