from django.db import models

class Products(models.Model):
    name=models.CharField( max_length=150, unique=True
                          ,verbose_name="Названее")
    slug=models.SlugField(max_length=200,blank=True,unique=True,verbose_name="URL")
    discription=models.TextField(blank=True,null=True, verbose_name="Описание")
    price=models.DecimalField(default=0.00, max_digits=7, decimal_places=2,verbose_name="Цена")
    quantity=models.PositiveIntegerField(default=0,verbose_name="Количество")
    date_create=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = "Product"
        verbose_name="Товар"
        verbose_name_plural="Товары"
        ordering=("id",)


class Userss(models.Model):
    name=models.CharField( max_length=150, unique=True,verbose_name="Имя")
    email=models.EmailField(max_length=150,verbose_name="Email")
    phone_number=models.CharField( max_length=150, unique=True,verbose_name="Телефон")
    address=models.TextField(blank=True,null=True, verbose_name="Адрес")
    slug=models.SlugField(max_length=200,blank=True,unique=True,verbose_name="URL")
    date_create=models.DateField(auto_now_add=True)
    image=models.ImageField(upload_to="userss",blank=True,null=True, verbose_name="фото профиля")
    # date_create=models.DateField() 
    def __str__(self):
        return self.name

    class Meta:
        db_table = "Userss"
        verbose_name="Пользователь"
        verbose_name_plural="Пользователи"
        ordering=("id",)

class Orders(models.Model):
    user=models.ForeignKey(to=Userss, verbose_name=("Пользователь"), on_delete=models.CASCADE)
    product=models.ForeignKey(to=Products, verbose_name=("Товар"), on_delete=models.CASCADE)
    price=models.DecimalField(default=0.00, max_digits=7, decimal_places=2,verbose_name="Сумма заказа")
    # date_create=models.DateField(auto_now_add=True)
    date_create=models.DateField() 
    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = "Order"
        verbose_name="Заказ"
        verbose_name_plural="Заказы"
        ordering=("id",)


# Поля модели «Клиент»:
# — имя клиента
# — электронная почта клиента
# — номер телефона клиента
# — адрес клиента
# — дата регистрации клиента

# Поля модели «Товар»:
# — название товара
# — описание товара
# — цена товара
# — количество товара
# — дата добавления товара

# Поля модели «Заказ»:
# — связь с моделью «Клиент», указывает на клиента, сделавшего заказ
# — связь с моделью «Товар», указывает на товары, входящие в заказ
# — общая сумма заказа
# — дата оформления заказа