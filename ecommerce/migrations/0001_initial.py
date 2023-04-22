# Generated by Django 4.2 on 2023-04-20 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('M', 'MALE'), ('W', 'WOMEN'), ('G', 'GENERAL')], max_length=2)),
                ('image', models.ImageField(default='default.jpg', upload_to='product_images')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]