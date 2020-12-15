# Generated by Django 3.1.4 on 2020-12-15 22:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('intra', '0003_forfait_rdv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forfait',
            name='name',
            field=models.CharField(choices=[('Conduite Basic', 'Conduite Basic'), ('Conduite Premium', 'Conduite Premium')], max_length=200),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('Student', 'Student'), ('Instructor', 'Instructor'), ('Secretary', 'Secretary'), ('Admin', 'Admin')], default='Student', max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]