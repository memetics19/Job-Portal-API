<<<<<<< HEAD
# Generated by Django 3.1.6 on 2021-02-20 19:48
=======
# Generated by Django 3.1.6 on 2021-02-19 17:35
>>>>>>> 35c1829fbf9df4fdd6efa5b2bd6f0ab4c0099cff

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_candidate_job_applied'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='job_applied',
<<<<<<< HEAD
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='api.application'),
=======
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='api.application'),
>>>>>>> 35c1829fbf9df4fdd6efa5b2bd6f0ab4c0099cff
        ),
    ]
