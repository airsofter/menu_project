# Generated by Django 4.2.7 on 2024-02-05 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0003_remove_menuitem_menu_name_remove_menuitem_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='menu_app.menuitem'),
        ),
    ]
