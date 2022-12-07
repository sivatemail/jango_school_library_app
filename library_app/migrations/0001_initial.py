# Generated by Django 4.1.2 on 2022-12-07 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('book_title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=50)),
                ('total_quantity', models.IntegerField()),
                ('available_quantity', models.IntegerField()),
                ('added_on', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taken_by', models.CharField(max_length=100)),
                ('taken_on', models.DateField(auto_now_add=True)),
                ('return_date', models.DateField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_app.books')),
            ],
        ),
    ]
