# Generated by Django 4.2.7 on 2024-01-16 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hosteler', '0002_alter_rooms_student1_alter_rooms_student2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot', models.IntegerField(default=0)),
                ('no', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hosteler.rooms')),
            ],
        ),
    ]