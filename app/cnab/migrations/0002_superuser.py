import os
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('cnab', '0001_initial'),
    ]

    def generate_superuser(apps, schema_editor):
        from django.contrib.auth.models import User
        username = os.environ.get('DJANGO_SU_NAME')
        email = os.environ.get('DJANGO_SU_EMAIL')
        password = os.environ.get('DJANGO_SU_PASSWORD')

        superuser = User.objects.create_superuser(
            username=username,
            email=email,
            password=password)

        superuser.save()

    operations = [
        migrations.RunPython(generate_superuser),
    ]
