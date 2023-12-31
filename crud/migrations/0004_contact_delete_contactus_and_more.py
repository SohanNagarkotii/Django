# Generated by Django 4.2.3 on 2023-07-31 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_blog_subheading'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.BigIntegerField()),
                ('message', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='contactus',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='description',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='subheading',
        ),
        migrations.AddField(
            model_name='blog',
            name='date',
            field=models.DateField(default='aiwhrwuiabfdkjarh iuserfhkje esrhewuhf seughfiusehfegfhrugtuirh ruith rbdkjgb'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='sub_heading',
            field=models.CharField(default='Subheading', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='user_name',
            field=models.CharField(default='ramukaka', max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]
