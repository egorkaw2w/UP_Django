from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class StoolCategory(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название категории")
    description = models.TextField(blank=True, verbose_name="Описание")

    class Meta:
        verbose_name = "Категория табуреток"
        verbose_name_plural = "Категории табуреток"

    def __str__(self):
        return self.name

class StoolManufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название производителя")
    country = models.CharField(max_length=100, blank=True, verbose_name="Страна")
    website = models.URLField(blank=True, verbose_name="Веб-сайт")

    class Meta:
        verbose_name = "Производитель табуреток"
        verbose_name_plural = "Производители табуреток"

    def __str__(self):
        return self.name

class StoolMaterial(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название материала")
    description = models.TextField(blank=True, verbose_name="Описание")

    class Meta:
        verbose_name = "Материал табуреток"
        verbose_name_plural = "Материалы табуреток"

    def __str__(self):
        return self.name

class Stool(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название табуретки")
    category = models.ForeignKey(StoolCategory, on_delete=models.CASCADE, related_name="stools", verbose_name="Категория")
    manufacturer = models.ForeignKey(StoolManufacturer, on_delete=models.SET_NULL, null=True, verbose_name="Производитель")
    materials = models.ManyToManyField(StoolMaterial, related_name="stools", verbose_name="Материалы")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    stock = models.PositiveIntegerField(default=0, verbose_name="Количество на складе")
    description = models.TextField(blank=True, verbose_name="Описание")
    dimensions = models.CharField(max_length=100, blank=True, verbose_name="Размеры (ДxШxВ)")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")
    is_available = models.BooleanField(default=True, verbose_name="В наличии")
    image = models.ImageField(upload_to='stools/', blank=True, null=True, verbose_name="Изображение")

    class Meta:
        verbose_name = "Табуретка"
        verbose_name_plural = "Табуретки"

    def __str__(self):
        return self.name

class StoolCustomer(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Телефон")
    address = models.TextField(blank=True, verbose_name="Адрес")

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class StoolOrder(models.Model):
    STATUS_CHOICES = (
        ('pending', 'В ожидании'),
        ('processing', 'В обработке'),
        ('shipped', 'Отправлен'),
        ('delivered', 'Доставлен'),
        ('canceled', 'Отменен'),
    )
    customer = models.ForeignKey(StoolCustomer, on_delete=models.CASCADE, related_name="orders", verbose_name="Клиент")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата заказа")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Статус")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Общая сумма")

    class Meta:
        verbose_name = "Заказ табуреток"
        verbose_name_plural = "Заказы табуреток"

    def __str__(self):
        return f"Заказ #{self.id} от {self.customer}"

class StoolOrderItem(models.Model):
    order = models.ForeignKey(StoolOrder, on_delete=models.CASCADE, related_name="items", verbose_name="Заказ")
    stool = models.ForeignKey(Stool, on_delete=models.CASCADE, verbose_name="Табуретка")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена за единицу")

    class Meta:
        verbose_name = "Элемент заказа табуреток"
        verbose_name_plural = "Элементы заказа табуреток"

    def __str__(self):
        return f"{self.stool.name} (x{self.quantity})"

class StoolReview(models.Model):
    stool = models.ForeignKey(Stool, on_delete=models.CASCADE, related_name="reviews", verbose_name="Табуретка")
    customer = models.ForeignKey(StoolCustomer, on_delete=models.CASCADE, related_name="reviews", verbose_name="Клиент")
    rating = models.PositiveSmallIntegerField(verbose_name="Рейтинг (1-5)", choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField(blank=True, verbose_name="Комментарий")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата отзыва")

    class Meta:
        verbose_name = "Отзыв о табуретке"
        verbose_name_plural = "Отзывы о табуретках"

    def __str__(self):
        return f"Отзыв на {self.stool.name} от {self.customer}"

from django.db import models
from django.utils import timezone

class StoolNews(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    published_at = models.DateTimeField(default=timezone.now, verbose_name="Дата публикации")

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title