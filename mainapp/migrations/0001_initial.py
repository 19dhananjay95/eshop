# Generated by Django 4.1.2 on 2022-10-17 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('addressline1', models.CharField(max_length=150)),
                ('addressline2', models.CharField(max_length=150)),
                ('addressline3', models.CharField(max_length=150)),
                ('pin', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('pic4', models.FileField(blank=True, default='', null=True, upload_to='uploads')),
            ],
        ),
        migrations.CreateModel(
            name='Maincategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=20)),
                ('stock', models.CharField(blank=True, default='In Stock', max_length=20, null=True)),
                ('description', models.TextField()),
                ('baseprice', models.IntegerField()),
                ('discount', models.IntegerField(blank=True, default=0, null=True)),
                ('finalprice', models.IntegerField()),
                ('pic1', models.FileField(blank=True, default='', null=True, upload_to='uploads')),
                ('pic2', models.FileField(blank=True, default='', null=True, upload_to='uploads')),
                ('pic3', models.FileField(blank=True, default='', null=True, upload_to='uploads')),
                ('pic4', models.FileField(blank=True, default='', null=True, upload_to='uploads')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.brand')),
                ('maincategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.maincategory')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.subcategory')),
            ],
        ),
    ]
