from django.db import models
from django.contrib.auth.models import User


# Book class for keeping books of the user
class Book(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    name = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now=True)
    price = models.FloatField()
    page_count = models.IntegerField()

    def __str__(self):
        return f'{self.name} owned by {self.owner.first_name}: date_bought {self.date_added} price: {self.price} ' \
               f'page_count {self.page_count}'
