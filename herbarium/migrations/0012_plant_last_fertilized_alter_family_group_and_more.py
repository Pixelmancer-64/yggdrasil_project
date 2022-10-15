# Generated by Django 4.1 on 2022-10-08 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('herbarium', '0011_alter_plant_complementary_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='last_fertilized',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='family',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='herbarium.group'),
        ),
        migrations.AlterField(
            model_name='family',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='genus',
            name='family',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='herbarium.family'),
        ),
        migrations.AlterField(
            model_name='genus',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='species',
            name='genus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='herbarium.genus'),
        ),
    ]