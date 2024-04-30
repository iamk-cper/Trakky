# Generated by Django 5.0.4 on 2024-04-25 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_and_meals', '0002_alter_product_calories_per_hundred_grams'),
    ]

    operations = [
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('protein', models.IntegerField()),
                ('carbohydrates', models.IntegerField()),
                ('fat', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('daily_calory_intake', models.IntegerField()),
                ('date', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
