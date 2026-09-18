from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name="Kitob nomi")
    author = models.CharField(max_length=150, verbose_name="Muallif")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Narxi")
    published_date = models.DateField(verbose_name="Nashr qilingan sana")

    class Meta:
        verbose_name = "Kitob"
        verbose_name_plural = "Kitoblar"

    def __str__(self):
        return f"{self.title} - {self.author}"
