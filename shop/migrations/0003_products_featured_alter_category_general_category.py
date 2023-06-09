# Generated by Django 4.2.1 on 2023-05-06 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='general_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub_categories', to='shop.generalcategory'),
        ),
    ]
