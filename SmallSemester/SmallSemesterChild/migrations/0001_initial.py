# Generated by Django 3.1 on 2020-08-17 20:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Belong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_id', models.IntegerField()),
                ('username', models.TextField()),
                ('authority', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Browse',
            fields=[
                ('browse_time', models.DateTimeField(auto_now=True)),
                ('browse_id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('username', models.TextField()),
                ('doc_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('com_content', models.TextField()),
                ('time', models.DateTimeField(auto_now=True)),
                ('com_author', models.TextField()),
                ('com_id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('doc_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Demo',
            fields=[
                ('demo_id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('demo_content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Docbelong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_id', models.IntegerField()),
                ('group_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('doc_name', models.TextField()),
                ('doc_id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('doc_content', models.TextField()),
                ('introduction', models.TextField()),
                ('time', models.DateTimeField(auto_now=True)),
                ('doc_groupid', models.IntegerField(blank=True, null=True)),
                ('doc_creater', models.TextField(null=True)),
                ('isin_recycle', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_id', models.IntegerField()),
                ('username', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('creater', models.TextField()),
                ('groupid', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('time', models.DateField(auto_now=True)),
                ('group_name', models.TextField()),
                ('introduction', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Notify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('title', models.TextField(default='通知')),
                ('notifytype', models.IntegerField()),
                ('content', models.TextField()),
                ('time', models.DateTimeField(auto_now=True)),
                ('groupid', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plainname', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Test2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Test3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(blank=True, null=True)),
                ('phonenumber', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Verifycode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verify_id', models.IntegerField()),
                ('username', models.TextField()),
                ('email', models.TextField()),
                ('verify_code', models.TextField()),
                ('verify_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('isverify', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserExtension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='暂无')),
                ('sex', models.TextField(default='不公开')),
                ('birthday', models.DateField(default=django.utils.timezone.now)),
                ('selfintro', models.TextField(default='暂无个人简介')),
                ('backgroundphoto', models.TextField(null=True)),
                ('userphoto', models.TextField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='extension', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
