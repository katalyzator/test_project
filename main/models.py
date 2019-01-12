from django.db import models

# Create your models here.


class Item(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    image = models.ImageField(upload_to='albums/images', verbose_name='Image')

    class Meta:
        verbose_name_plural = 'Items'
        verbose_name = 'Item'

    def __str__(self):
        return self.title
