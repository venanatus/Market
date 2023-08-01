from django.contrib.auth.models import User
from django.db.models import *


class Category(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name


class SubCategory(Model):
    category = ForeignKey(Category, on_delete=CASCADE, null=True)
    name = CharField(max_length=255)

    def __str__(self):
        return f'{self.name} / {self.category}'


Gender_Choise = [
    ('Мужской', 'Мужской'),
    ('Женский', 'Женский')
]
Sleeve_Choise = [
    ('Длинные', 'Длинные'),
    ('Короткие', 'Короткие')
]

Vozrast_Choise = [
    ('Детская', 'Детская'),
    ('Для новорожденных', 'Для новорожденных'),
    ('Женская', 'Женская'),
    ('Мужская', 'Мужская'),

]


class Product(Model):
    name = CharField(max_length=255)
    price = IntegerField(blank=True, null=True)
    description = TextField()
    preview = ImageField(null=True)
    category = ForeignKey(Category, on_delete=CASCADE, null=True)
    subcategory = ForeignKey(SubCategory, on_delete=CASCADE, null=True)
    package_length = IntegerField()
    packing_width = IntegerField()
    packing_height = IntegerField(null=True)
    made_country = CharField(max_length=255)
    equipment = CharField(max_length=255)
    seller = ForeignKey(User, on_delete=CASCADE, null=True)

    def __str__(self):
        return self.name[:30]

    def snippet(self):
        return self.name[:23]

    def desc(self):
        return self.description[:100]


class Image(Model):
    product = ForeignKey(Product, on_delete=CASCADE, related_name='product')
    image1 = ImageField(null=True)
    image2 = ImageField(null=True)
    image3 = ImageField(null=True)
    image4 = ImageField(blank=True)
    image5 = ImageField(blank=True)
    image6 = ImageField(blank=True)
    image7 = ImageField(blank=True)
    image8 = ImageField(blank=True)
    image9 = ImageField(blank=True)
    image10 = ImageField(blank=True)

    def str(self):
        return str(self.product)


class CartItem(Model):
    customer = ForeignKey(User, on_delete=SET_NULL, null=True, blank=True)
    product = ForeignKey(Product, on_delete=CASCADE)
    quantity = IntegerField()

    def __str__(self):
        return self.product.name

    def total_price(self):
        return self.quantity * self.product.price


class Order(Model):
    customer = ForeignKey(User, on_delete=CASCADE)
    address = CharField(max_length=255)
    phone = IntegerField()
    total_price = IntegerField()

    def __str__(self):
        return f"{self.pk} - заказ"


class OrderProduct(Model):
    order = ForeignKey(Order, on_delete=CASCADE, related_name='order_products')
    product = ForeignKey(Product, on_delete=CASCADE)
    amount = IntegerField()
    total = IntegerField()

    def __str__(self):
        return f"{self.product} x{self.amount} - {self.order.customer.username}"

