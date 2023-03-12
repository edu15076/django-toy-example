from django.db import migrations
from django.core.management import call_command


def load_persons(apps, schema_editor):
    Person = apps.get_model('toy', 'Person')
    Person.objects.test_create_from_csv('../../../data/tests/person2.csv')


class Migration(migrations.Migration):

    dependencies = [
        ('toy', '0004_alter_person_birth_date'),
    ]

    operations = [
        migrations.RunPython(load_persons),
    ]
