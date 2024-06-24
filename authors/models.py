from django.db import models


class AuthorModel(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField()
    phone_number = models.IntegerField()
    age = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    uptaded_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


