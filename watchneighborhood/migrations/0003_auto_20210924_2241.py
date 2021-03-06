# Generated by Django 3.1.1 on 2021-09-24 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watchneighborhood', '0002_neighborhood_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='neighborhood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='members', to='watchneighborhood.neighborhood'),
        ),
        migrations.AlterField(
            model_name='neighborhood',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hood', to='watchneighborhood.profile'),
        ),
    ]
