# Generated by Django 5.1.7 on 2025-03-10 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='books/')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('genre', models.CharField(choices=[('Ужасы', 'Ужасы'), ('Дедективы', 'Дедективы'), ('Научная фантастика', 'Научная фантастика'), ('Романтика', 'Романтика'), ('Психология', 'Психология')], max_length=30)),
                ('time', models.TimeField()),
                ('author', models.CharField(max_length=100)),
            ],
        ),
    ]
