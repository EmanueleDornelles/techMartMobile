# Generated by Django 5.0.4 on 2024-04-17 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NomeProduto', models.CharField(max_length=100)),
                ('Descricao', models.TextField(blank=True)),
                ('Preco', models.FloatField()),
                ('Estoque', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='Produtos',
        ),
    ]
