# Generated by Django 3.0.5 on 2020-09-15 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0009_auto_20200915_1452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='options',
            name='machines',
        ),
        migrations.RemoveField(
            model_name='options',
            name='water_line_compatible',
        ),
        migrations.AlterField(
            model_name='options',
            name='coffee_flavor',
            field=models.CharField(choices=[('vanela', 'vanela'), ('caramel', 'Caramel'), ('psi', 'PSI'), ('macha', 'Mocha'), ('hazelnut', 'Hazelnut')], max_length=20),
        ),
        migrations.AlterField(
            model_name='options',
            name='pack_size',
            field=models.CharField(choices=[('1 dozen', '1 dozen'), ('3 dozen', '3 dozen'), ('5 dozen', '5 dozen'), ('7 dozen', '7 dozen')], max_length=20),
        ),
        migrations.AlterField(
            model_name='options',
            name='pods',
            field=models.CharField(choices=[('large coffee pod', 'large coffee pod'), ('small coffee pod', 'small coffee pod'), ('espresso pod', 'espresso pod')], max_length=20),
        ),
        migrations.AlterField(
            model_name='options',
            name='product_name',
            field=models.CharField(max_length=200),
        ),
        migrations.CreateModel(
            name='Machines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coffee_flavor', models.CharField(choices=[('base model', 'base model'), ('premium model', 'premium model'), ('deluxe', 'deluxe')], max_length=20)),
                ('machines', models.CharField(choices=[('espresso machine', 'espresso machine'), ('large machine', 'large machine'), ('small machine', 'small machine')], max_length=20)),
                ('water_line_compatible', models.BooleanField()),
                ('product_name', models.CharField(max_length=200)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coffee.Product')),
            ],
        ),
    ]