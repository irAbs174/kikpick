# Generated by Django 4.2.1 on 2023-06-22 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=120, null=True, unique=True, verbose_name='مشتری')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='نام')),
                ('last_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='نام خانوادگی')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='آدرس دقیق')),
                ('pelak', models.CharField(blank=True, max_length=100, null=True, verbose_name='پلاگ\\زنگ')),
                ('ostan', models.CharField(blank=True, max_length=100, null=True, verbose_name='استان محل سکونت')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='شهر محل سکونت')),
                ('zip_zode', models.CharField(blank=True, max_length=100, null=True, verbose_name='کد پستی')),
            ],
            options={
                'verbose_name': 'مشتری',
                'verbose_name_plural': 'مشتریان سایت',
            },
        ),
        migrations.CreateModel(
            name='user_accounts',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False, unique=True, verbose_name='شناسه کاربری')),
                ('email', models.CharField(db_column='email', max_length=120, null=True, unique=True, verbose_name='پست الکترونیک')),
                ('username', models.CharField(db_column='username', max_length=120, null=True, unique=True, verbose_name='نام کاربری')),
                ('WPOPass', models.CharField(db_column='WPOPass', default=False, max_length=100, null=True)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='نام')),
                ('last_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='نام خانوادگی')),
                ('phoneNumber', models.CharField(db_column='phoneNumber', max_length=20, unique=True, verbose_name='شماره تماس')),
                ('is_active', models.BooleanField(db_column='is_active', default=True, verbose_name='وضعیت کاربر')),
                ('is_staff', models.BooleanField(db_column='is_staff', default=False, verbose_name='وضعیت راهبری')),
                ('last_login', models.DateTimeField(auto_now_add=True, db_column='last_login', verbose_name='آخرین فعالیت')),
                ('has_new_password', models.BooleanField(db_column='has_new_password', default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربران سایت',
            },
        ),
    ]
