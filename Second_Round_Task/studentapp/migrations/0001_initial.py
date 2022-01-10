# Generated by Django 3.2.3 on 2022-01-10 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Studentinfo',
            fields=[
                ('roll_no', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Student Name')),
                ('clas', models.IntegerField(verbose_name='Class')),
                ('school', models.CharField(max_length=200, verbose_name='School Name')),
                ('mobile', models.PositiveIntegerField(verbose_name='Student Mobile Number')),
                ('address', models.TextField(verbose_name='Address')),
            ],
        ),
        migrations.CreateModel(
            name='StudentAcademics',
            fields=[
                ('stu_acad_id', models.AutoField(primary_key=True, serialize=False)),
                ('math', models.IntegerField(verbose_name='Maths Marks')),
                ('physics', models.IntegerField(verbose_name='Physics Marks')),
                ('chemistry', models.IntegerField(verbose_name='Chemistry Marks')),
                ('biology', models.IntegerField(verbose_name='Biology Marks')),
                ('english', models.IntegerField(verbose_name='English Marks')),
                ('roll_no_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentapp.studentinfo')),
            ],
        ),
    ]