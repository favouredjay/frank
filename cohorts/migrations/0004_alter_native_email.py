# Generated by Django 3.2.7 on 2021-09-28 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cohorts', '0003_alter_cohort_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='native',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
