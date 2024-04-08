from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_product_manufactured_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'категория', 'verbose_name_plural': 'категории'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='manufactured_at',
        ),
    ]