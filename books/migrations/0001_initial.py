# Generated by Django 4.0.5 on 2023-04-03 10:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('author', models.CharField(max_length=100, verbose_name='نویسنده')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='قیمت')),
                ('cover', models.ImageField(blank=True, upload_to='covers/', verbose_name='عکس جلد')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='متن پیام')),
                ('datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('recommend', models.BooleanField(default=True, verbose_name='پیشنهاد می شود')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='books.book', verbose_name='نام کتاب')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
        ),
    ]
