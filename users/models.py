from django.db import models
from django.contrib.auth.models import User

Gender_Choise = [
    ('Мужской', 'Мужской'),
    ('Женский', 'Женский'),
]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    register_at = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(blank=True, null=True, default='baon.jpg')
    full_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=25, choices=Gender_Choise, null=True)

    def __str__(self):
        return self.full_name

