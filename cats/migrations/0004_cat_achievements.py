# Generated by Django 3.2 on 2024-07-24 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0003_achievement_achievementcat'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='achievements',
            field=models.ManyToManyField(through='cats.AchievementCat', to='cats.Achievement'),
        ),
    ]
