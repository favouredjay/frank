# Generated by Django 3.2.7 on 2021-09-28 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cohorts', '0002_native'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cohort',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]