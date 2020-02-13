# Generated by Django 3.0.2 on 2020-02-13 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('semester', models.CharField(max_length=1)),
                ('academic_year', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_code', models.CharField(max_length=10)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=100)),
                ('year', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.SmallIntegerField()),
                ('weekday', models.CharField(choices=[('M', 'Monday'), ('T', 'Tuesday'), ('W', 'Wednesday'), ('TH', 'Thursday'), ('F', 'Friday'), ('S', 'Saturday'), ('Su', 'Sunday')], max_length=2)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('student_amount', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='management.Course')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='management.Room')),
                ('students', models.ManyToManyField(through='classes.StudentAttendance', to='management.Student')),
            ],
        ),
    ]
