# Generated by Django 3.1.6 on 2021-02-07 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='project/')),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('icon', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('visit_number', models.PositiveIntegerField()),
                ('status', models.IntegerField(choices=[(1, 'Draft'), (2, 'Live')], default=1)),
                ('github_link', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('requirement', models.TextField()),
                ('website_link', models.CharField(max_length=255)),
                ('category', models.ManyToManyField(related_name='project_category', to='my_portfolio.Category')),
                ('image', models.ManyToManyField(related_name='project_image', to='my_portfolio.Image')),
                ('technology', models.ManyToManyField(related_name='Project_technology', to='my_portfolio.Technology')),
            ],
        ),
    ]
