# Generated by Django 2.2.6 on 2019-10-08 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=50)),
                ('editora', models.CharField(max_length=50)),
                ('isbn', models.IntegerField()),
                ('numeroPaginas', models.IntegerField()),
                ('titulo', models.CharField(max_length=50)),
                ('anoPublicacao', models.IntegerField()),
                ('emailEditora', models.EmailField(max_length=254)),
            ],
        ),
    ]
