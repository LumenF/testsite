from django.db import models


class Group(models.Model):
    name = models.CharField(
        verbose_name='Товарная группа',
        max_length=90,
        help_text='Макс. длинна 90 символов'
    )

    class Meta:
        verbose_name = 'Товарная группа'
        verbose_name_plural = 'Товарная группа'

    def __str__(self):
        return self.name


class Category(models.Model):
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='media_default/'
    )
    group = models.ForeignKey(
        verbose_name='Товарная группа',
        to=Group,
        on_delete=models.CASCADE,

    )
    name = models.CharField(
        verbose_name='Категория',
        max_length=90,
        help_text='Макс. длинна 90 символов'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Series(models.Model):
    name = models.CharField(
        verbose_name='Серия',
        max_length=90,
        help_text='Макс. длинна 90 символов'
    )
    category = models.ForeignKey(
        verbose_name='Категория',
        to=Category,
        on_delete=models.CASCADE,

    )

    class Meta:
        verbose_name = 'Серия'
        verbose_name_plural = 'Серии'

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(
        verbose_name='Цвета',
        max_length=90,
        help_text='Макс. длинна 90 символов'
    )
    name_eng = models.CharField(
        verbose_name='Цвет на английском',
        max_length=90,
        help_text='Макс. длинна 90 символов'
    )

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    def __str__(self):
        return self.name


class Product(models.Model):
    image_1 = models.ImageField(
        verbose_name='Картинка 1',
        upload_to=''
    )

    image_2 = models.ImageField(
        verbose_name='Картинка 2',
        upload_to=''
    )

    name = models.CharField(
        verbose_name='Название',
        max_length=90,
        help_text='Макс. длинна 90 символов',
    )

    category = models.ForeignKey(
        verbose_name='Категория',
        to=Category,
        on_delete=models.CASCADE,

    )
    series = models.ForeignKey(
        verbose_name='Серия',
        to=Series,
        on_delete=models.CASCADE,

    )

    description = models.TextField(
        verbose_name='Описание'
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class Variable(models.Model):
    product = models.ForeignKey(
        verbose_name='Базовый товар',
        to=Product,
        on_delete=models.CASCADE,
    )
    color = models.ForeignKey(
        verbose_name='Цвет',
        to=Color,
        on_delete=models.CASCADE,
    )
    cost = models.IntegerField(
        verbose_name='Цена'
    )

    cost_sale = models.IntegerField(
        verbose_name='Цена со скидкой'
    )

    class Meta:
        verbose_name = 'Вариация'
        verbose_name_plural = 'Вариации'

    def __str__(self):
        return self.product.name
