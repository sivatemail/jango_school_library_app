# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils.timezone import localdate


def return_date():
    return localdate()+timedelta(30)

class Books(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    total_quantity = models.IntegerField()
    available_quantity = models.IntegerField()
    added_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.book_title} by ({self.author})"


class BookStatus(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    taken_by = models.ForeignKey(User, on_delete=models.RESTRICT)
    taken_on = models.DateField(auto_now_add=True)
    return_date = models.DateField()
    renewal_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.book} return by --{self.return_date}"


    def save(self, *args, **kwargs):
        self.return_date = return_date()
        super(BookStatus, self).save(*args, **kwargs)


class user_books(models.Model):
    user = models.OneToOneField(User, on_delete=models.RESTRICT)
    books_count = models.IntegerField(default=0)


