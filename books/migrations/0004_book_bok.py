# Generated by Django 3.2 on 2021-06-02 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20210602_0955'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='bok',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bok', to='books.category'),
        ),
    ]
