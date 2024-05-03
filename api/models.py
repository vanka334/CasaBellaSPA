from django.db import models


# Таблицы с данными на каждый сезон и тип блюда в дальнейшем будем считывать нынешний сезон и подключать нужную таблицу(мб через апи)
class  Menu(models.Model):
    name = models.CharField(max_length=15, verbose_name="Меню")
    isActive = models.BooleanField(default=True, verbose_name="Активен")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"
class Type(models.Model):
    name = models.CharField(max_length=30, verbose_name="Тип блюда")
    season = models.ForeignKey(Menu,max_length=2, verbose_name="Сезон", on_delete=models.CASCADE, null=False, blank=False)
    queue_view = models.IntegerField(verbose_name="Очередь показа на странице", null=False, blank=False,default=0)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Раздел"
        verbose_name_plural = "Разделы"

class MenuItem(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название блюда")
    img = models.ImageField(upload_to='img/%Y/%m/%d/', verbose_name="Изображение блюда", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places= 2, verbose_name="Цена")
    description = models.TextField(verbose_name="Описание блюда")
    type = models.ForeignKey(Type, verbose_name="Тип блюда",on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, verbose_name="Меню", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Блюдо  меню"
        verbose_name_plural = "Блюда  меню"





