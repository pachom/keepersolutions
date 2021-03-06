# Generated by Django 3.2.8 on 2021-10-20 16:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookmarks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='private',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bookmark',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
